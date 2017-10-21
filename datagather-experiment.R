library(tidyverse)
library(stringr)
setwd("data/")
# readfolder function
readFolder <- function(infolder) {
  data_frame(file = dir(infolder, full.names = TRUE)) # geef namen files in dir
}
# read all datafilenames, filter juiste csv
datafiles <- readFolder(".") %>%
  filter(str_detect(file, ".csv")) %>%
  filter(!str_detect(file, "trials"))

# workaround voor missende info in twee experimenten
a <- read_csv(toString(datafiles[2, 1]))
a <- a %>%
  mutate(leeftijd.response = as.integer(NA)) %>%
  mutate(manvrouw.response = as.integer(NA))
a[1, 19] <- 10 # dummyleeftijd
a[3, 22] <- 0
datafiles <- datafiles[-2,]

b <- read_csv(toString(datafiles[5, 1]))
b <- b %>%
  mutate(leeftijd.response = as.integer(NA)) %>%
  mutate(manvrouw.response = as.integer(NA))
b[1, 19] <- 10 # dummyleeftijd
b[3, 22] <- 0
datafiles <- datafiles[-5,]

# verwerking van overige experimenten
matrix <- data_frame() # gebruik alle filenames voor csv import
for (x in (1:dim(datafiles)[1])){
  matrix <- bind_rows(matrix, read_csv(toString(datafiles[x, 1])))
}
matrix <- matrix %>% # combineer met workarounds
  bind_rows(a, b)

# selecteer demografische info, verwijder NA
names <- matrix %>%
  select(leeftijd.response, manvrouw.response, participant) %>%
  gather("var", "val", -participant) %>%
  filter(is.na(val) == FALSE) %>%
  spread(key = "var", value = "val")

# maak matrix van alle bruikbare observaties
matrixObservations <- matrix %>%
  select(imgName, corrAns, trials.thisRepN,
         obj2_1Count, obj2_2Count, ratingMV2_.response, rating2_.response,
         obj3_1Count, obj3_2Count, obj3_3Count,
         ratingMV3_.response, rating3_.response,
         obj4_1Count, obj4_2Count, obj4_3Count, obj4_4Count,
         ratingMV4_.response, rating4_.response,
         date, participant) %>%
  mutate(cond = # voeg conditie toe (2,3,4 objecten)
           (is.na(obj2_1Count) == FALSE) * 2 +
           (is.na(obj3_1Count) == FALSE) * 3 +
           (is.na(obj4_1Count) == FALSE) * 4
  ) %>%
  filter(cond != 0)

# replace NA with 0
matrixObservations[is.na(matrixObservations)] <- 0

# bewerk data zodat matrix geschikt wordt voor plotting
matrixProcessed <- matrixObservations %>%
  mutate(MVResp = # beoordeel input
           ( (corrAns == "v") & (ratingMV2_.response == "'vrouw'")) * 1 +
           ( (corrAns == "m") & (ratingMV2_.response == "'man'")) * 1 +
           ( (corrAns == "v") & (ratingMV3_.response == "'vrouw'")) * 1 +
           ( (corrAns == "m") & (ratingMV3_.response == "'man'")) * 1 +
           ( (corrAns == "v") & (ratingMV4_.response == "'vrouw'")) * 1 +
           ( (corrAns == "m") & (ratingMV4_.response == "'man'")) * 1
  ) %>%
  mutate(noConsc = # no consciousness
           (ratingMV2_.response == "'geen foto gezien'") * 1 +
           (ratingMV3_.response == "'geen foto gezien'") * 1 +
           (ratingMV4_.response == "'geen foto gezien'") * 1) %>%
  mutate(ObjCorr = # correct aantal objecten
           obj4_1Count + obj4_2Count + obj4_3Count + obj4_4Count +
           obj3_1Count + obj3_2Count + obj3_3Count +
           obj2_1Count + obj2_2Count) %>%
  transmute(imgName, MVCorr = corrAns, MVResp, noConsc, ObjCorr, ObjResp =
           rating2_.response + rating3_.response + rating4_.response,
           repN = trials.thisRepN, cond, participant) %>% # verwijder noise
  mutate(ObjError = 1- abs((ObjResp - ObjCorr) / ObjCorr )) %>%
  left_join(names, by = "participant") # voeg demografie toe

# groepeer op conditie
matrixProcessed$cond <- as.integer(matrixProcessed$cond)
matrixStat <- matrixProcessed %>%
  group_by(participant) %>%
  arrange(cond) # arrange by condition

write_excel_csv(matrixProcessed, '/Users/rgrouls/Dropbox/KI/ICW/werkgroep/code/CWI/data.csv')

# summarise complete matrix
matrixSum <-  matrixStat %>%
  group_by(participant, cond) %>%
  summarise(gistError = mean(MVResp),
            ObjError = mean(ObjError))

# voeg summarise toe aan matrix
matrixStatEr <- matrixStat %>%
  group_by(participant, cond) %>%
  mutate(gistError = mean(MVResp), ObjError = mean(ObjError))

# t.test
t.test(matrixSum$cond, matrixSum$gistError)

# lineaire regressie
fit <- lm(gistError ~ cond, data = matrixSum)
coefficients(fit)
summary(fit)
anova(fit)

# jitterpoint van gemiddeldes plus lm
ggplot(data = matrixSum, aes(x = cond, y = gistError)) +
  geom_jitter(position = position_jitter(width = 0.01, height = 0), alpha = 0.5) +
  stat_smooth(method = "lm", fullrange = TRUE)

# jitterpoint van gemiddeldes plus lm met facet van participant
ggplot(data = matrixSum, aes(x = cond, y = gistError)) +
  geom_jitter(position = position_jitter(width = 0.01, height = 0), alpha = 0.5) +
  stat_smooth(method = "lm", fullrange = TRUE) +
  facet_wrap(~participant)

ggplot(data = matrixSum) +
  stat_summary(
    mapping = aes(x = cond, y = gistError),
    fun.ymin = min,
    fun.ymax = max,
    fun.y = median
  )

ggplot(data = matrixSum) +
  geom_boxplot(mapping = aes(x = cond, y = gistError, group = cond))

# facet wrap met lm voor elke participant
ggplot(data = matrixSum, aes(x = cond, y = gistError)) +
  stat_smooth(method = "auto", fullrange = TRUE) +
  facet_wrap(~ participant)

ggplot(data = matrixSum, aes(x = cond, y = gistError)) +
  stat_smooth(method = "auto", fullrange = TRUE)

# alle lm over elkaar geplot
ggplot(data = matrixSum, aes(x = cond, y = gistError, color = participant)) +
  stat_smooth(method = "lm", fullrange = TRUE)

# object error in tijd (trainingseffect)
ggplot(data = matrixProcessed, aes(x = repN, y = ObjError)) +
  geom_point() +
  facet_grid(cond ~ participant)

ggplot(data = matrixProcessed, aes(x = repN, y = ObjError)) +
  geom_point() +
  facet_wrap(~cond)

ggplot(data = matrixStat) +
  geom_jitter(mapping = aes(x = repN, y = ObjError, color = cond, alpha = 0.1))

ggplot(data = matrixSum, aes(x = cond, y = gistError, color = participant)) +
  geom_smooth() +
  facet_wrap(~ participant)


