library(tidyverse)
library(stringr)

setwd("~/Dropbox/KI/ICW/werkgroep/code/CWI/data/demo")
datafolder <- "~/Dropbox/KI/ICW/werkgroep/code/CWI/data/demo/"
# readfolder function
ReadFolder <- function(infolder) {
  data_frame(file = dir(infolder, full.names = TRUE)) 
}
# read all datafiles, filter csv
datafiles <- ReadFolder('.') %>%
  filter(str_detect(file, ".csv"))
# select 4-tests met oplopende snelheid voor 4 balletjes
tests4 <- datafiles %>%
  filter(str_detect(file, "4tests")) %>%
  filter(!str_detect(file, "trials"))

# maak dataframe door alle csv te combineren voor 4test
m <- data_frame()
for (x in (1:dim(tests4)[1])) {
  m <- rbind(m, read_csv(toString(tests4[x,1])))
}

# selecteer alle demografie van participanten
demog <- m %>%
  select(rating_2.response, date, participant) %>%
  filter(is.na(rating_2.response) == FALSE )
age <- m %>%
  select(rating.response, date) %>%
  filter(is.na(rating.response) == FALSE )
participants <- left_join(demog, age, by = "date")

trial <- m %>%
  mutate(corrCount = obj4_1Count + obj4_2Count + obj4_3Count + obj4_4Count) %>%
  select(imgName, corrAns, ratingMV_2.response, 
         corrCount, rating2_2.response, rating_3.response, date) %>%
  filter(is.na(imgName) == FALSE )

data <- left_join(trial, participants, by = "date") %>%
  mutate(errorcount = (rating2_2.response-corrCount)/corrCount) %>%
  cbind(seq = 1:8)

data$errorMV <- ifelse(
  ((data$corrAns == 'v') & (data$ratingMV_2.response == "'vrouw'")) |
    ((data$corrAns == 'm') & (data$ratingMV_2.response == "'man'"))
  , 1, 0)

a <- as.tibble(rep(seq(0.5, 1.2, 0.1),6))
datas <- bind_cols(data, a)
ggplot(datas) +
  geom_boxplot(mapping = aes(x = value, y = rating_3.response, group = seq))


MinMeanSEMMax <- function(x) {
  v <- c(min(x), mean(x) - sd(x)/sqrt(length(x)), mean(x), mean(x) + sd(x)/sqrt(length(x)), max(x))
  names(v) <- c("ymin", "lower", "middle", "upper", "ymax")
  v
}
pdf(file = "boxplot-snelheidstest.pdf")
ggplot(datas, mapping = aes(x = value, y = rating_3.response, group = seq)) +
  stat_summary(fun.data=MinMeanSEMMax, geom="boxplot") +
  labs(title = "Snelheidstest", 
       subtitle = "Waardering van snelheden met 4 objecten",
       x = 'relatieve snelheid objecten',
       y = 'beoordeling snelheid op vijfpunts-likertscale')
dev.off()
ggplot(data = data) +
  geom_smooth(method = "glm", aes(x = seq, y = errorcount, color = "lineaire regressie")) +
  geom_point(mapping = aes(x = seq, y = errorcount, color = date))


ggplot(data = data) +
  geom_jitter(mapping = aes(x = seq, y = errorMV, color = date)) + 
  geom_smooth(method = "glm", aes(x = seq, y = errorMV))
  
ggplot(data = data) +
  geom_smooth(method = "glm", aes(x = seq, y = errorcount, color = "lineaire regressie")) +
  geom_smooth(method = "glm", aes(x = seq, y = errorMV))

