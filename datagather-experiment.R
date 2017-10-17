library(tidyverse)
library(stringr)
setwd("~/Dropbox/KI/ICW/werkgroep/code/CWI/data/")
# readfolder function
ReadFolder <- function(infolder) {
  data_frame(file = dir(infolder, full.names = TRUE)) 
}
# read all datafiles, filter conditie 2
datafiles_2 <- ReadFolder('.') %>% # read filenames
  filter(str_detect(file, "2.csv")) 

frame_2 <- data_frame() # import csv
for (x in (1:dim(datafiles_2)[1])){
  frame_2 <- rbind(frame_2, read_csv(toString(datafiles_2[x,1])))
}

names <- frame_2 %>%
  filter(imgName == 'participant') %>%
  select(name = corrAns)

frame_2_select <- frame_2 %>% # select usefull data
  filter((corrAns == 'v') | (corrAns == 'm')) %>% # strip noise
  select(imgName, corrAns, obj2_1Count_raw, obj2_2Count_raw,
         rating2_.response_raw, ratingMV2_.response_raw) %>%
  cbind(names) # bind names

# selecteer alle demografie van participanten
demog <- md %>%
  select(manvrouw.response, date, participant) %>%
  filter(is.na(manvrouw.response) == FALSE )
age <- md %>%
  select(leeftijd.response, date) %>%
  filter(is.na(leeftijd.response) == FALSE )
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

ggplot(data = data) +
  geom_smooth(method = "glm", aes(x = seq, y = errorcount, color = "lineaire regressie")) +
  geom_point(mapping = aes(x = seq, y = errorcount, color = date))


ggplot(data = data) +
  geom_jitter(mapping = aes(x = seq, y = errorMV, color = date)) + 
  geom_smooth(method = "glm", aes(x = seq, y = errorMV))

ggplot(data = data) +
  geom_smooth(method = "glm", aes(x = seq, y = errorcount, color = "lineaire regressie")) +
  geom_smooth(method = "glm", aes(x = seq, y = errorMV))
