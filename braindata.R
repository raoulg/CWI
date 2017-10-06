library(tidyverse)
require(stats)
braindata <- read_tsv("http://wps.aw.com/wps/media/objects/14/15269/projects/ch6_iq/brain.txt")

brainplot <- braindata %>% 
  select(FSIQ, MRICount)
  
linearModel <- lm(brainplot$MRICount ~ brainplot$FSIQ)
a <- linearModel$coefficients[1]
b <- linearModel$coefficients[2]
plot(brainplot, main = "pixelcount in MRI versus IQ")
abline(a, b)
cor(brainplot)

brainF <- braindata %>% 
  select(FSIQ, MRICount, Gender) %>%
  filter(Gender == "Female")
  

brainFplot <- brainF %>%
  select(FSIQ, MRICount)

linearModelf <- lm(brainF$MRICount ~ brainF$FSIQ)
aF <- linearModelF$coefficients[1]
bF <- linearModelF$coefficients[2]
plot(brainFplot)
abline(af, bf)
cor(brainFplot)

ggplot(data = braindata) +
  geom_point(mapping =aes(x = FSIQ, y = MRICount, color = Gender))

ggplot(data = braindata, aes(FSIQ, MRICount)) + 
  geom_smooth(method = 'lm', formula = y~x) +
  geom_point(mapping =aes(x = FSIQ, y = MRICount, color = Gender)) +
  labs(title = "MRI pixelcount vs IQ", subtitle = "blauwe lijn : lineare regressie y~x")

ggplot(data = braindata, mapping =aes(x = Gender, y = MRICount, color = Gender)) +
  geom_boxplot() +
  labs(title = "MRI pixelcount per Gender")


  
ggplot(data = braindata, mapping =aes(x = Gender, y = FSIQ, color = Gender)) +
  geom_boxplot() +
  labs(title = "FSIQ per Gender")
  
p <- ggplot(mpg, aes(class, hwy))
p + geom_boxplot()
p + geom_boxplot() + geom_jitter(width = 0.2)
p + geom_boxplot() + coord_flip()
