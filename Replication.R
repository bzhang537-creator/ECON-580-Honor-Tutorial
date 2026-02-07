#Instruction 2
# Table 1 & 2 and Figure 1 Replication

getwd()   # should end with wu2018_replication
setwd("lasso")
getwd() # should end with wu2018_replication/lasso
install.packages(c(
  "ggplot2",
  "data.table",
  "dplyr",
  "tidyr",
  "stringr",
  "readr"
))
source("../tables-figures.R")
rm(list = ls())
graphics.off()
source("../tables-figures.R", echo = TRUE)
write.csv(tab1, "table1_replication.csv", row.names = FALSE)
write.csv(tab2, "table2_replication.csv", row.names = FALSE)
print(tab1)
print(tab2)
