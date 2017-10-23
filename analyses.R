############ ANALYSES ###############
### trainingseffect bij complete dataset
setwd('../plots')
pdf(file = "training-conditie.pdf")
ggplot(data = matrixProcessed20, mapping = aes(x = repN, y = ObjError)) +
  geom_jitter(alpha = 0.1) +
  geom_smooth(aes(colour="lineaire regressie")) +
  facet_wrap(~ condition) +
  labs(title = "Trainings- en vermoeidheidseffect", 
       subtitle = "Verloop prestatie gistherkenning in de tijd, per conditie",
       x = 'Volgorde van experimenten (experimentnummer)',
       y = 'prestatie gist (percentage correct)') +
  scale_colour_manual(name="legenda", values="blue")
dev.off()
# mv verschil
matrixProcessed20mv <- matrixProcessed20 %>%
  mutate(gender = ifelse(manvrouw.response == 0, "vrouw", "man"))
formula = y ~ x
pdf(file = "training-mv.pdf")
ggplot(data = matrixProcessed20mv, mapping = aes(x = repN, y = ObjError)) +
  geom_jitter(alpha = 0.1) +
  geom_smooth(formula = formula, fullrange = TRUE, aes(colour="lineaire regressie")) +
  stat_fit_glance(method.args = list(formula = formula),
                  geom = 'text',
                  aes(label = paste("P-value = ", signif(..p.value.., digits = 2), sep = "")),
                  label.x.npc = 'right', label.y.npc = 0.35, size = 3) +
  facet_wrap(~gender) +
  labs(title = "Trainings- en vermoeidheidseffect", 
       subtitle = "Verloop prestatie gistherkenning in de tijd, per geslacht",
       x = 'Volgorde van experimenten (experimentnummer)',
       y = 'prestatie gist (percentage correct)') +
  scale_colour_manual(name="legenda", values="blue")
dev.off()
# p-waardes
matrixProcessed20mvM <- matrixProcessed20mv %>%
  filter(manvrouw.response == 1) %>%
  rename(y = ObjError, x = repN)
modelM <- lm(formula = formula, matrixProcessed20mvM)
summary(modelM)
matrixProcessed20mvV <- matrixProcessed20mv %>%
  filter(manvrouw.response == 0) %>%
  rename(y = ObjError, x = repN)
modelV <- lm(formula = formula, matrixProcessed20mvV)
summary(modelV)

# leeftijdsverschil
pdf(file = "spredingLeeftijden.pdf")
ggplot(data = names, aes(leeftijd.response)) +
  geom_histogram()
dev.off()
# toevoegen categorieen
matrixProcessed20age <- matrixProcessed20 %>%
  mutate(gender = ifelse(manvrouw.response == 0, "vrouw", "man")) %>%
  mutate(agegroup = ifelse(leeftijd.response <= 30, "17-30", "30+"))
formula = y ~ x
pdf(file = "training-leeftijd.pdf")
ggplot(data = matrixProcessed20age, mapping = aes(x = repN, y = ObjError)) +
  geom_jitter(alpha = 0.1) +
  geom_smooth(formula = formula, fullrange = TRUE, aes(colour="lineaire regressie")) +
  stat_fit_glance(method.args = list(formula = formula),
                  geom = 'text',
                  aes(label = paste("P-value = ", signif(..p.value.., digits = 2), sep = "")),
                  label.x.npc = 'right', label.y.npc = 0.35, size = 3) +
  facet_wrap(~agegroup) +
  labs(title = "Trainings- en vermoeidheidseffect", 
       subtitle = "Verloop van prestatie op gist in de tijd per leeftijdsgroep",
       x = 'Volgorde van experimenten (experimentnummer)',
       y = 'prestatie gist (percentage correct)') +
  scale_colour_manual(name="legenda", values="blue")
dev.off()
# grid leeftijdsgroep en gender
pdf(file = "training-grid-jitter.pdf")
ggplot(data = matrixProcessed20age, mapping = aes(x = repN, y = ObjError)) +
  geom_jitter(alpha = 0.1, color = "blue") +
  stat_smooth(formula = formula, fullrange = TRUE) +
  stat_fit_glance(method.args = list(formula = formula),
                  geom = 'text',
                  aes(label = paste("P-value = ", signif(..p.value.., digits = 2), sep = "")),
                  label.x.npc = 'right', label.y.npc = 0.35, size = 3) +
  facet_grid(gender~agegroup) +
  labs(title = "Trainings- en vermoeidheidseffect", 
       subtitle = "Verloop van prestatie op gist in de tijd, per leeftijdgroep en geslacht",
       x = 'Volgorde van experimenten (experimentnummer)',
       y = 'prestatie gist (percentage correct)') +
  scale_colour_manual(name="legenda", values="blue")
dev.off()
pdf(file = "training-grid.pdf")
ggplot(data = matrixProcessed20age, mapping = aes(x = repN, y = ObjError)) +
  stat_smooth(formula = formula, fullrange = TRUE) +
  stat_fit_glance(method.args = list(formula = formula),
                  geom = 'text',
                  aes(label = paste("P-value = ", signif(..p.value.., digits = 2), sep = "")),
                  label.x.npc = 'right', label.y.npc = 0.35, size = 3) +
  facet_grid(gender~agegroup) +
  labs(title = "Trainings- en vermoeidheidseffect", 
       subtitle = "Verloop van prestatie op gist in de tijd, per leeftijdgroep en geslacht",
       x = 'Volgorde van experimenten (experimentnummer)',
       y = 'prestatie gist (percentage correct)') +
  scale_colour_manual(name="legenda", values="blue")
dev.off()

ggplot(data = matrixSum, mapping = aes(x = cond, y = ObjError, color = participant)) +
  geom_line() +
  labs(title = "Trainings- en vermoeidheidseffect", 
       subtitle = "Verloop van prestatie op gist in de tijd, per leeftijdgroep en geslacht",
       x = 'Volgorde van experimenten (experimentnummer)',
       y = 'prestatie gist (percentage correct)')

  
# poging tot modelering van functie  
# ggplot(data.frame(x=c(0,2)), aes(x)) +
#   stat_function(fun=function(x)0.5+(1/(x-2.3)), geom="line", aes(colour="training")) +
#   stat_function(fun=function(x) x, geom="line", aes(colour="vermoeidheid")) +
#   stat_function(fun=function(x) x+0.5+(1/(x-2.5)), geom="line", aes(colour="combi"))

#  p-waardes
pValue <- list()
coef <- list()
for (x in 1:20) {
  pv <- matrixProcessed20 %>%
    filter(repN <= x) %>%
    group_by(participant, cond) %>%
    summarise(gistError = mean(MVResp))
  fit <- lm(gistError ~ cond, data = pv)
  pValue[x] <- anova(fit)$`Pr(>F)`
  coef[x] <- coefficients(fit)[2]
}
# met 2e orde formule
pValue2 <- list()
coef21 <- list()
coef22 <- list()
coef23 <- list()
formula = y ~ poly(x, 2)
for (x in 1:20) {
  pv <- matrixProcessed20 %>%
    filter(repN <= x) %>%
    group_by(participant, cond) %>%
    summarise(gistError = mean(MVResp)) %>%
    rename(y = gistError, x = cond)
  fit <- lm(formula = formula, data = pv)
  pValue2[x] <- anova(fit)$`Pr(>F)`[1]
  coef21[x] <- coefficients(fit)[1]
  coef22[x] <- coefficients(fit)[2]
  coef23[x] <- coefficients(fit)[3]
}
pvaluePlot <- as_tibble(cbind(p = unlist(pValue), 
                              c2 = unlist(coef),
                              afkap = 1:20))
pvaluePlot2 <- as_tibble(cbind(p = unlist(pValue2), 
                               c1 = unlist(coef21), 
                               c2 = unlist(coef22), 
                               c3 = unlist(coef23), 
                               afkap =1:20))
# LaTeX export
library(knitr)
pvaluePlot[,1:2] <- round(pvaluePlot[,1:2],2)
pposter <- pvaluePlot[c(5, 8, 9, 10, 15, 17, 20),]
kable(pposter, format = "latex")

demo <- names %>%
  summarize(leeftijd = median(leeftijd.response),
            sdleeftijd = sd(leeftijd.response),
            minleeftijd = min(leeftijd.response),
            maxleeftijd = max(leeftijd.response),
            geslacht = mean(manvrouw.response),
            aantal = n())
kable(demo, format = "latex")
# plot van p-waardes 
pdf(file = "pwaardes.pdf")
ggplot(data = pvaluePlot, mapping = aes(x = afkap, y = p)) +
  geom_smooth() +
  labs(title = "Relatie tussen afkappunt en p-waarde", 
       subtitle = "Optimaal afkappunt voor modelvorming",
       x = 'Afkappunt (experimentnummer)',
       y = 'p-waarde van model')
dev.off()
# lineaire regressie plot met p waarde
formula = y ~ x
pdf(file = "lineaireRegressie.pdf")
ggplot(data = matrixSum, aes(x = cond, y = gistError)) +
  stat_smooth(method = 'lm', formula = formula, fullrange = TRUE) +
  stat_fit_glance(method = 'lm',
                  method.args = list(formula = formula),
                  geom = 'text',
                  aes(label = paste("P-value = ", signif(..p.value.., digits = 2), sep = "")),
                  label.x.npc = 'right', label.y.npc = 0.35, size = 3) +
  labs(title = "Inloed aandachtstaak op gistwaarneming", 
       subtitle = "Toenemende intensiteit van aandachtstaak veroorzaakt minder gistwaarneming",
       x = 'Conditie (aantal objecten)',
       y = 'Prestatie gistwaarneming (percentage correct)')
dev.off()

# met mv facets
# NIET RELEVANT ??
ggplot(data = matrixSum, aes(x = cond, y = gistError)) +
  stat_smooth(method = 'lm', formula = formula, fullrange = TRUE) +
  stat_fit_glance(method = 'lm',
                  method.args = list(formula = formula),
                  geom = 'text',
                  aes(label = paste("P-value = ", signif(..p.value.., digits = 2), sep = "")),
                  label.x.npc = 'right', label.y.npc = 0.35, size = 3) +
  labs(title = "lineare regressie van prestatie gist ~ conditie", 
       subtitle = "Relatie tussen intensiteit van aandachtstaak en gistwaarneming",
       x = 'conditie (aantal objecten)',
       y = 'prestatie gist (percentage correct)') +
  facet_wrap(~manvrouw.response)


# boxplot spreiding gist per conditie
MinMeanSEMMax <- function(x) {
  v <- c(min(x), mean(x) - sd(x)/sqrt(length(x)), mean(x), mean(x) + sd(x)/sqrt(length(x)), max(x))
  names(v) <- c("ymin", "lower", "middle", "upper", "ymax")
  v
}
pdf(file = "boxplotGist-conditie.pdf")
ggplot(data = matrixSum, mapping = aes(x = cond, y = gistError, group = cond)) +
  stat_summary(fun.data=MinMeanSEMMax, geom="boxplot") +
  labs(title = "Variatie in prestatie gistwaarneming", 
       subtitle = "Prestatie in gistwaarneming per conditie",
       x = 'conditie (aantal objecten)',
       y = 'prestatie gist (percentage correct)')
dev.off()
summary(names)
