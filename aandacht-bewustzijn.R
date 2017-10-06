library(tidyverse)
gistType <- rep(c(rep('Gender', 500), rep('Nature', 500)), 3)
taak <- c(rep('A', 1000), rep('B', 1000), rep('C', 1000))

resAG1 <- replicate(1000, mean(sample(0:1, 200, rep = T, prob = c(0.1, 0.9))))
resAG2 <- replicate(1000, mean(sample(0:1, 200, rep = T, prob = c(0.2, 0.8))))
resAG3 <- replicate(1000, mean(sample(0:1, 200, rep = T, prob = c(0.3, 0.7))))

resT1 <- replicate(1000, mean(sample(0:1, 200, rep = T, prob = c(0.1, 0.9))))
resT2 <- replicate(1000, mean(sample(0:1, 200, rep = T, prob = c(0.2, 0.8))))
resT3 <- replicate(1000, mean(sample(0:1, 200, rep = T, prob = c(0.3, 0.7))))

resBG <- replicate(3000, mean(sample(0:1, 200, rep = T, prob = c(0.1, 0.9))))

M <- tibble(resAG = c(resAG1, resAG2, resAG3),
            resBG, 
            resT = c(resT1, resT2, resT3),
            taak,
            gistType
)

ggplot(data = M) +
  geom_jitter(mapping = aes(x = resT, y = resAG, shape = taak, color = taak)) +
  scale_shape(solid = F) +
  labs(title = "gist en intensiteit van aandacht", 
       subtitle = "Hypothese : geen bewustzijn zonder aandacht",
       x = 'prestatie op aandachtstaak',
       y = 'prestatie op gist')

ggplot(data = M) +
  geom_jitter(mapping = aes(x = resT, y = resBG, shape = taak, color = taak)) +
  scale_shape(solid = F) +
  labs(title = "gist en intensiteit van aandacht", 
       subtitle = "Hypothese : wel bewustzijn zonder aandacht",
       x = 'prestatie op aandachtstaak',
       y = 'prestatie op gist')

resAG1 <- replicate(100, mean(sample(0:1, 200, rep = T, prob = c(0.1, 0.9))))
resAG2 <- replicate(100, mean(sample(0:1, 200, rep = T, prob = c(0.2, 0.8))))
resAG3 <- replicate(100, mean(sample(0:1, 200, rep = T, prob = c(0.3, 0.7))))

resT1 <- replicate(100, mean(sample(0:1, 20, rep = T, prob = c(0.1, 0.9))))
resT2 <- replicate(100, mean(sample(0:1, 20, rep = T, prob = c(0.2, 0.8))))
resT3 <- replicate(100, mean(sample(0:1, 20, rep = T, prob = c(0.3, 0.7))))

resBG <- replicate(300, mean(sample(0:1, 20, rep = T, prob = c(0.1, 0.9))))
taak <- c(rep('A', 100), rep('B', 100), rep('C', 100))
M <- tibble(resAG = c(resAG1, resAG2, resAG3),
            resBG, 
            resT = c(resT1, resT2, resT3),
            taak
)
ggplot(data = M) +
  geom_smooth(method = "lm", mapping = aes(x = resT, y = resAG, color = taak)) +
  labs(title = "gist en intensiteit van aandacht", 
       subtitle = "Hypothese : geen bewustzijn zonder aandacht",
       x = 'prestatie op aandachtstaak',
       y = 'prestatie op gist')

ggplot(data = M) +
  geom_smooth(method = "glm", mapping = aes(x = resT, y = resBG)) +
  labs(title = "gist en intensiteit van aandacht", 
       subtitle = "Hypothese : wel bewustzijn zonder aandacht",
       x = 'prestatie op aandachtstaak',
       y = 'prestatie op gist') +
  scale_x_continuous(limits = c(0,1)) +
  scale_y_continuous(limits = c(0,1))

ggplot(data = M) +
  geom_jitter(mapping = aes(x = resT, y = resBG, shape = taak, color = taak)) +
  scale_shape(solid = F) +
  labs(title = "gist en intensiteit van aandacht", 
       subtitle = "Hypothese : wel bewustzijn zonder aandacht",
       x = 'prestatie op aandachtstaak',
       y = 'prestatie op gist')