
#############################
# obsolete plots 
write_excel_csv(matrixProcessed, '/Users/rgrouls/Dropbox/KI/ICW/werkgroep/code/CWI/data.csv')

# method = auto
ggplot(data = matrixSum, aes(x = cond, y = gistError)) +
  stat_smooth(method = "auto", fullrange = TRUE)

ggplot(data = matrixSum20, aes(x = cond, y = gistError)) +
  geom_boxplot(mapping = aes(x = cond, y = gistError, group = cond)) +
  stat_smooth(fullrange = TRUE) +
  stat_fit_glance(geom = 'text',
                  aes(label = paste("P-value = ", signif(..p.value.., digits = 4), sep = "")),
                  label.x.npc = 'right', label.y.npc = 0.35, size = 3) +
  labs(title = "lineare regressie van prestatie gist ~ conditie", 
       subtitle = "Relatie tussen intensiteit van aandachtstaak en gistwaarneming",
       x = 'conditie (aantal objecten)',
       y = 'prestatie gist (percentage correct)')

ggplot(data = matrixSum, aes(x = cond, y = gistError)) +
  geom_point(alpha = 0.5) +
  geom_line() +
  facet_wrap(~participant)

# facet wrap met lm voor elke participant
ggplot(data = matrixSum, aes(x = cond, y = gistError)) +
  stat_smooth(method = "auto", fullrange = TRUE) +
  facet_wrap(~ participant)

# tweede orde formule
formula = y ~ poly(x, 2)
ggplot(data = matrixSum, aes(x = cond, y = gistError)) +
  stat_smooth(method = 'lm', formula = formula, fullrange = TRUE, level = 0.95) +
  stat_fit_glance(method = 'lm',
                  method.args = list(formula = formula),
                  geom = 'text',
                  aes(label = paste("P-value = ", signif(..p.value.., digits = 2), sep = "")),
                  label.x.npc = 'right', label.y.npc = 0.35, size = 3) +
  labs(title = "lineare regressie van prestatie gist ~ conditie", 
       subtitle = "Relatie tussen intensiteit van aandachtstaak en gistwaarneming",
       x = 'conditie (aantal objecten)',
       y = 'prestatie gist (percentage correct)')

formula = y ~ poly(x, 2)
ggplot(data = matrixSum, aes(x = cond, y = gistError)) +
  stat_smooth(fullrange = TRUE) +
  stat_fit_glance(geom = 'text',
                  aes(label = paste("P-value = ", signif(..p.value.., digits = 2), sep = "")),
                  label.x.npc = 'right', label.y.npc = 0.35, size = 3) +
  labs(title = "lineare regressie van prestatie gist ~ conditie", 
       subtitle = "Relatie tussen intensiteit van aandachtstaak en gistwaarneming",
       x = 'conditie (aantal objecten)',
       y = 'prestatie gist (percentage correct)')

ggplot(data = pvaluePlot2, mapping = aes(x = afkap, y = p)) +
  geom_smooth() +
  labs(title = "Relatie tussen afkappunt en p-waarde", 
       subtitle = "Optimaal afkappunt voor modelvorming",
       x = 'Afkappunt (experimentnummer)',
       y = 'p-waarde van model')
######### met weglating van conditie met 3 objecten
m <- matrixSum %>%
  filter(cond != 3)

formula = y ~ x
ggplot(data = m, aes(x = cond, y = gistError)) +
  stat_smooth(method = 'lm', formula = formula, fullrange = TRUE) +
  stat_fit_glance(method = 'lm',
                  method.args = list(formula = formula),
                  geom = 'text',
                  aes(label = paste("P-value = ", signif(..p.value.., digits = 4), sep = "")),
                  label.x.npc = 'right', label.y.npc = 0.35, size = 3)

ggplot(data = m) +
  geom_boxplot(mapping = aes(x = cond, y = gistError, group = cond))

ggplot(data = m) +
  geom_line(mapping = aes(x = cond, y = gistError, color = participant))

formula = y ~ x
ggplot(data = m, aes(x = cond, y = gistError)) +
  stat_smooth(method = 'lm', formula = formula, fullrange = TRUE) +
  stat_fit_glance(method = 'lm',
                  method.args = list(formula = formula),
                  geom = 'text',
                  aes(label = paste("P-value = ", signif(..p.value.., digits = 4), sep = "")),
                  label.x.npc = 'right', label.y.npc = 0.35, size = 3)

# verwijder mogelijk foute fotos
imgFail <- matrixProcessed %>%
  arrange(imgName) %>%
  group_by(imgName) %>%
  summarise(total = mean(MVResp)) %>%
  arrange(total)
imgDrop <- imgFail[1:10,]  

matrixDropped <- data_frame()
for (x in 1:10) {
  matrixDropped <- bind_rows(matrixDropped, 
                             filter(matrixProcessed, 
                                    imgName != imgDrop$imgName[x]))
}
matrixDropped$cond <- as.integer(matrixDropped$cond)
matrixStat <- matrixDropped %>%
  group_by(participant) %>%
  arrange(cond) # arrange by condition

# groepeer op conditie
matrixStat <- matrixProcessed %>%
  group_by(participant) %>%
  arrange(cond) # arrange by condition

# voeg summarise toe aan matrix
matrixStatEr <- matrixStat %>%
  group_by(participant, cond) %>%
  mutate(gistError = mean(MVResp), ObjError = mean(ObjError))

matrixStat <- matrixStat %>%
  ungroup() %>%
  arrange(ObjError)