library(tidyverse)
setwd("/Users/rgrouls/Dropbox/KI/ICW/werkgroep/code/CWI/data/")
trial_2 <- read_csv('./001_movingDots-demo_2017_Oct_15_2317.csv')
trialSel <- trial_2 %>%
  mutate(corrCount = obj4_1Count + obj4_2Count + obj4_3Count + obj4_4Count) %>%
  select(imgName, corrAns, 
         ratingMV.response, ratingMV_2.response, ratingMV_4.response, 
         corrCount, rating2.response, rating2_4.response, rating2_2.response) %>%
  filter(!is.na(imgName))
View(trialSel)

