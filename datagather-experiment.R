##########
# geschreven voor onderzoek cognitiewetenschappen
# alle code beschikbaar onder de creative commons licentie
# https://creativecommons.org/licenses/by-nc-sa/4.0/
# meer informatie op https://github.com/raoulg/CWI
# refereer aan de github-url en R.Grouls wanneer je dit werk gebruikt.
##########
library(tidyverse)
library(stringr)
library(ggpmisc)
setwd("~/path/to/data/files")
# readfolder function
readFolder <- function(infolder) {
  data_frame(file = dir(infolder, full.names = TRUE)) # geef namen files in dir
}
# read all datafilenames, filter juiste csv
datafiles <- readFolder(".") %>%
  filter(str_detect(file, ".csv")) %>%
  filter(!str_detect(file, "trials"))

# gebruik alle filenames voor csv import
matrix <- data_frame() 
for (x in (1:dim(datafiles)[1])){
  matrix <- bind_rows(matrix, read_csv(toString(datafiles[x, 1])))
  print(x) # print voor eventuele debug
}
# gebruikt voor debugging:
# b <- read_csv(toString(datafiles[3, 1]))

# selecteer demografische info, verwijder NA
names <- matrix %>%
  select(leeftijd.response, manvrouw.response, participant = date) %>%
  gather("var", "val", -participant) %>%
  filter(is.na(val) == FALSE) %>%
  spread(key = "var", value = "val") %>%
  mutate(agegroup = ifelse(leeftijd.response <= 30, "17-30", "30+")) %>%
  mutate(agecount = ifelse(leeftijd.response <= 30, 0, 1))

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
  mutate(noConsc = # geen bewustzijn van de foto
           (ratingMV2_.response == "'geen foto gezien'") * 1 +
           (ratingMV3_.response == "'geen foto gezien'") * 1 +
           (ratingMV4_.response == "'geen foto gezien'") * 1) %>%
  mutate(ObjCorr = # correct aantal objecten
           obj4_1Count + obj4_2Count + obj4_3Count + obj4_4Count +
           obj3_1Count + obj3_2Count + obj3_3Count +
           obj2_1Count + obj2_2Count) %>%
  transmute(imgName, MVCorr = corrAns, MVResp, noConsc, ObjCorr, ObjResp =
           rating2_.response + rating3_.response + rating4_.response,
           repN = trials.thisRepN, cond, participant = date) %>% # verwijder noise
  mutate(ObjError = 1- abs((ObjResp - ObjCorr) / ObjCorr )) %>%
  left_join(names, by = "participant") # voeg demografie toe

# condition als integer voor modeleren
matrixProcessed$cond <- as.integer(matrixProcessed$cond)
# diverse afkappunten voor vermoeidheidseffect
matrixProcessed15 <- matrixProcessed %>%
  filter(repN <= 15)
matrixProcessed10 <- matrixProcessed %>%
  filter(repN <= 10)

# summarise complete matrix
matrixSum <-  matrixProcessed %>%
  group_by(participant, cond, manvrouw.response, leeftijd.response) %>%
  summarise(gistError = mean(MVResp)*100,
            ObjError = mean(ObjError)*100)

matrixSum <- matrixSum %>% # voeg tekst toe voor leeftijdscategorie
  mutate(agegroup = ifelse(leeftijd.response <= 30, "17-30 jaar", "30+ jaar"))

# bewerkingen voor afkappunt 10 rondes
matrixSum10 <-  matrixProcessed10 %>%
  group_by(participant, cond, manvrouw.response, leeftijd.response) %>%
  summarise(gistError = mean(MVResp)*100,
            ObjError = mean(ObjError)*100)
matrixSum10 <- matrixSum10 %>%
  mutate(agegroup = ifelse(leeftijd.response <= 30, "17-30 jaar", "30+ jaar"))

# toevoegen kolommen voor titels van facets
matrixProcessed <- matrixProcessed %>%
  mutate(condition = ifelse((cond == 2), "2 objecten", 
                            ifelse((cond == 3), "3 objecten", 
                                   "4 objecten"))) %>%
  mutate(ObjError = ObjError*100) %>%
  mutate(gender = ifelse(manvrouw.response == 0, "vrouw", "man")) %>%
  mutate(agegroup = ifelse(leeftijd.response <= 30, "17-30 jaar", "30+ jaar"))

# export naar csv
write_csv(matrixProcessed, '~/Dropbox/KI/ICW/werkgroep/code/CWI/data.csv')