############ ANALYSES ###############
##########
# geschreven voor onderzoek cognitiewetenschappen
# alle code beschikbaar onder de creative commons licentie
# https://creativecommons.org/licenses/by-nc-sa/4.0/
# meer informatie op https://github.com/raoulg/CWI
# refereer aan de github-url en R.Grouls wanneer je dit werk gebruikt.
##########
library(knitr) # voor latex export
setwd('../plots')
# manvrouw verschil
mpnm <- matrixProcessed %>% # filter man (1) of vrouw (0) icm leeftijdsgroep
  filter((manvrouw.response == 0)|(leeftijd.response <=30))
formula = y ~ x # formule voor lineaire regressie
o <-   labs(title = "Trainings- en vermoeidheidseffect",  # plot-titels
            subtitle = "Verloop prestatie objecttelling in de tijd, per leeftijdsgroep",
            x = 'Volgorde van experimenten (experimentnummer)',
            y = 'Objecttelling (percentage correct)')
# training-grid plot
pdf(file = "training-grid-conditie.pdf")
ggplot(data = matrixProcessed, mapping = aes(x = repN, y = ObjError)) +
  geom_jitter(alpha = 0.1) +
  geom_smooth(method='auto') + # pas aan naar lm, loess of gam voor specifieke methodes
  stat_fit_glance(geom = 'text',
                  aes(label = paste("p = ", signif(..p.value.., digits = 2), sep = "")),
                  label.x.npc = 'right', label.y.npc = 0.05, size = 3) +
  o +
  facet_wrap(~condition) # wrap voor conditie
dev.off()
# wrap voor agegroup
pdf(file = "training-grid.pdf")
ggplot(data = matrixProcessed, mapping = aes(x = repN, y = ObjError)) +
  geom_jitter(alpha = 0.1) +
  geom_smooth(method='auto') +
  stat_fit_glance(geom = 'text',
                  aes(label = paste("p = ", signif(..p.value.., digits = 2), sep = "")),
                  label.x.npc = 'right', label.y.npc = 0.05, size = 3) +
  o +
  facet_wrap(~agegroup)
dev.off()

# fit
fitmp <- matrixProcessed %>%
  select(x = repN, y = ObjError)
fit <- lm(y~x,fitmp)
coefficients(fit)
summary(fit)
t.test(x~y, as.matrix(fitmp))
# p-waardes
matrixProcessed20mvM <- matrixProcessed %>%
  filter(manvrouw.response == 1) %>%  # filter voor man/vrouw
  rename(y = ObjError, x = repN)
modelM <- lm(formula = formula, matrixProcessed20mvM)  # model met alleen mannen
summary(modelM)

matrixProcessed20mvV <- matrixProcessed %>%
  filter(manvrouw.response == 0) %>%  # filter voor man/vrouw
  rename(y = ObjError, x = repN)
modelV <- lm(formula = formula, matrixProcessed20mvV)  # model met alleen vrouwen
summary(modelV)

# leeftijdsverschil histogram
pdf(file = "spreidingLeeftijden.pdf")
ggplot(data = names, aes(leeftijd.response)) +
  geom_histogram()
dev.off()
# toevoegen categorieen in tekst
matrixProcessed20age <- matrixProcessed %>%
  mutate(gender = ifelse(manvrouw.response == 0, "vrouw", "man")) %>%
  mutate(agegroup = ifelse(leeftijd.response <= 30, "17-30", "30+"))
formula = y ~ x # formule voor lin. reg.
ggplot(data = matrixProcessed, mapping = aes(x = repN, y = ObjError)) +
  geom_jitter(alpha = 0.1) +
  geom_smooth(formula = formula, fullrange = TRUE, aes(colour="lineaire regressie")) +
  stat_fit_glance(method.args = list(formula = formula),
                  geom = 'text',
                  aes(label = paste("P-value = ", signif(..p.value.., digits = 2), sep = "")),
                  label.x.npc = 'right', label.y.npc = 0.35, size = 3) +
  facet_wrap(~agegroup) +
  o +
  scale_colour_manual(name="legenda", values="blue")

# complete dataset, individuele lijnen
ggplot(data = matrixSum, mapping = aes(x = cond, y = ObjError, color = participant)) +
  geom_line() +
  labs(title = "Trainings- en vermoeidheidseffect", 
       subtitle = "Verloop van prestatie op gist in de tijd, per leeftijdgroep en geslacht",
       x = 'Volgorde van experimenten (experimentnummer)',
       y = 'prestatie gist (percentage correct)')

#  p-waardes voor alle afkappunten
pValue <- list()
coef <- list()
for (x in 1:20) {
  pv <- matrixProcessed %>%
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
formula = y ~ poly(x, 2) # tweede orde formule
for (x in 1:20) {
  pv <- matrixProcessed %>%
    filter(repN <= x) %>%
    group_by(participant, cond) %>%
    summarise(gistError = mean(MVResp)) %>%
    rename(y = gistError, x = cond)
  fit <- lm(formula = formula, data = pv)  # gebruik 2e orde ipv default 1e orde
  pValue2[x] <- anova(fit)$`Pr(>F)`[1]
  coef21[x] <- coefficients(fit)[1]
  coef22[x] <- coefficients(fit)[2]
  coef23[x] <- coefficients(fit)[3]
}

# bewerk voor plotten
pvaluePlot <- as_tibble(cbind(p = unlist(pValue), 
                              c2 = unlist(coef),
                              afkap = 1:20))
pvaluePlot2 <- as_tibble(cbind(p = unlist(pValue2), 
                               c1 = unlist(coef21), 
                               c2 = unlist(coef22), 
                               c3 = unlist(coef23), 
                               afkap =1:20))
# LaTeX export van p-waardes

pvaluePlot[,1:2] <- round(pvaluePlot[,1:2],3)
pposter <- pvaluePlot[c(8, 9, 10, 15, 17, 20),]
kable(pposter, format = "latex")
 # demografie overzicht
demo <- names %>%
  summarize(leeftijd = median(leeftijd.response),
            sdleeftijd = sd(leeftijd.response),
            minleeftijd = min(leeftijd.response),
            maxleeftijd = max(leeftijd.response),
            geslacht = mean(manvrouw.response),
            aantal = n())
kable(demo, format = "latex") # latex export tabel

# summaries
matrixSumSum <- matrixSum %>%
  group_by(cond) %>%
  summarise(GE = mean(gistError),
            ObjErSd = sd(gistError)/sqrt(n()),
            Objmin = min(gistError),
            ObjMax = max(gistError))

matrixSumSum <- round(matrixSumSum, 2)
kable(matrixSumSum, format = "latex")

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
formula = y ~ x # gebruik weer 1e orde
g <-  labs(title = "Invloed aandachtstaak op bewustzijn", 
           subtitle = "Lineaire regressie van gistwaarneming en aantal objecten in aandachtstaak",
           x = 'Conditie (aantal objecten)',
           y = 'Gistwaarneming (percentage correct)')
pdf(file = "lineaireRegressie.pdf")
ggplot(data = matrixSum, aes(x = cond, y = gistError)) +
  stat_smooth(method = 'lm', formula = formula, fullrange = TRUE) +
  stat_fit_glance(method = 'lm',
                  method.args = list(formula = formula),
                  geom = 'text',
                  aes(label = paste("p = ", signif(..p.value.., digits = 2), sep = "")),
                  label.x.npc = 'right', label.y.npc = 0.05, size = 5) +
  g
dev.off()

# plot facet grid gender - leeftijd
ggplot(data = matrixSum, aes(x = cond, y = gistError)) +
  stat_smooth(method = 'lm', formula = formula, fullrange = TRUE) +
  stat_fit_glance(method = 'lm',
                  method.args = list(formula = formula),
                  geom = 'text',
                  aes(label = paste("p = ", signif(..p.value.., digits = 2), sep = "")),
                  label.x.npc = 'right', label.y.npc = 0.05, size = 3) +
  g +
  facet_grid(manvrouw.response~agegroup)
# met mv facets
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
MinMeanSEMMax <- function(x) { # pas standaard errorbars aan naar SDM
  v <- c(min(x), mean(x) - sd(x)/sqrt(length(x)), mean(x), mean(x) + sd(x)/sqrt(length(x)), max(x))
  names(v) <- c("ymin", "lower", "middle", "upper", "ymax")
  v
}
pdf(file = "boxplotGist-conditie.pdf") 
# boxplot met y = gistError
ggplot(data = matrixSum, mapping = aes(x = cond, y = gistError, group = cond)) +
  stat_summary(fun.data=MinMeanSEMMax, geom="boxplot") +
  labs(title = "Invloed aandachtstaak op bewustzijn", 
       subtitle = "Spreiding van gistwaarneming per conditie",
       x = 'Conditie (aantal objecten)',
       y = 'Gistwaarneming (percentage correct)')
dev.off()
# boxplot met y = ObjError
ggplot(matrixSum, mapping = aes(x = cond, y = ObjError, group = cond)) +
  stat_summary(fun.data=MinMeanSEMMax, geom="boxplot") +
  labs(title = "Invloed aandachtstaak op bewustzijn", 
       subtitle = "Spreiding van gistwaarneming per conditie",
       x = 'Conditie (aantal objecten)',
       y = 'Gistwaarneming (percentage correct)')

# nog wat summaries van de demografie
matrixSum %>%
  group_by(cond, ObjError) %>%
  summarise(ObjE = mean(ObjError))

summary(names)
names %>% 
  ungroup() %>%
  group_by(manvrouw.response) %>%
  summarise(agegromean = mean(agecount))

names %>%
  filter(manvrouw.response == 0) %>%