library(tidyverse)
library(stringr)
setwd("~/Dropbox/KI/ICW/werkgroep/code/CWI/data/")
# readfolder function
ReadFolder <- function(infolder) {
  data_frame(file = dir(infolder, full.names = TRUE)) # geef namen files in dir
}
# read all datafilenames, filter juiste csv
datafiles <- ReadFolder('.') %>% 
  filter(str_detect(file, ".csv")) %>%
  filter(!str_detect(file, "trials"))

matrix <- data_frame() # gebruik alle filenames voor csv import
for (x in (1:dim(datafiles)[1])){
  matrix <- rbind(matrix, read_csv(toString(datafiles[x,1])))
}

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
           (is.na(obj2_1Count) == FALSE)*2 + 
           (is.na(obj3_1Count) == FALSE)*3 +
           (is.na(obj4_1Count) == FALSE)*4
  ) %>%
  filter(cond != 0)

# replace NA with 0
matrixObservations[is.na(matrixObservations)] <- 0

# bewerk data zodat matrix geschikt wordt voor plotting
matrixProcessed <- matrixObservations %>%
  mutate(MVResp = # beoordeel input
           ((corrAns == "v") & (ratingMV2_.response == "'vrouw'"))*1 +
           ((corrAns == "m") & (ratingMV2_.response == "'man'"))*1 +
           ((corrAns == "v") & (ratingMV3_.response == "'vrouw'"))*1 +
           ((corrAns == "m") & (ratingMV3_.response == "'man'"))*1 +
           ((corrAns == "v") & (ratingMV4_.response == "'vrouw'"))*1 +
           ((corrAns == "m") & (ratingMV4_.response == "'man'"))*1 
  ) %>%
  mutate(noConsc = # no consciousness
           (ratingMV2_.response == "'geen foto gezien'")*1 +
           (ratingMV3_.response == "'geen foto gezien'")*1 +
           (ratingMV4_.response == "'geen foto gezien'")*1) %>%
  mutate(ObjCorr = # correct aantal objecten
           obj4_1Count + obj4_2Count + obj4_3Count + obj4_4Count +
           obj3_1Count + obj3_2Count + obj3_3Count +
           obj2_1Count + obj2_2Count) %>%
  transmute(imgName, MVCorr = corrAns, MVResp, noConsc, ObjCorr, ObjResp = 
           rating2_.response + rating3_.response + rating4_.response, 
           repN = trials.thisRepN, cond, participant) %>% # verwijder onnodige info
  mutate(ObjError = (ObjResp-ObjCorr)/ObjCorr ) %>%
  left_join(names, by = "participant") # voeg demografie toe

matrixProcessed$cond <- as.factor(matrixProcessed$cond)
matrixStat <- matrixProcessed %>%
  group_by(participant) %>% 
  arrange(cond)

ggplot(data = matrixStat) +
  geom_jitter(mapping = aes(x = repN, y = ObjError, color = cond, alpha = 0.1)) 

ggplot(data = matrixStat) +
#######

#######
ggplot(data = data) +
  geom_smooth(method = "glm", aes(x = seq, y = errorcount, color = "lineaire regressie")) +
  geom_point(mapping = aes(x = seq, y = errorcount, color = date))


ggplot(data = data) +
  geom_jitter(mapping = aes(x = seq, y = errorMV, color = date)) + 
  geom_smooth(method = "glm", aes(x = seq, y = errorMV))

ggplot(data = data) +
  geom_smooth(method = "glm", aes(x = seq, y = errorcount, color = "lineaire regressie")) +
  geom_smooth(method = "glm", aes(x = seq, y = errorMV))


