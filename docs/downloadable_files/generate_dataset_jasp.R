# Script to generate dataset in wide format for JASP

library(tidyverse)

# Stroop data
# # ---------------------------------------------------------------------
# read in & filter data
d_stroop <- read.csv("dataset_stroop_clean.csv") |>
    filter(rt > 0.1 & rt < 6) |>
    mutate(condition = case_when(congruent == 1 ~ "congruent",
                                 congruent == 0 ~ "incongruent"))

# change format to wide (by conditions)
d_stroop_wide <- d_stroop |>
    pivot_wider(id_cols = c(id),
                names_from = condition,
                values_from = rt,
                values_fn = mean) # take mean for id/conditions

# save new file
write.csv(d_stroop_wide, "data_stroop_wide.csv", row.names = FALSE)



# Random Dot data
# ---------------------------------------------------------------------
# read in & filter data
d_rdk<- read.csv("dataset_rdk_clean.csv") |>
    filter(rt > 0.1 & rt < 6)


# change format to wide (by conditions)
d_rdk_wide_condition <- d_rdk |>
    pivot_wider(id_cols = c(id),
                names_from = condition,
                values_from = c(rt, corr),
                values_fn = mean) # take mean for id/conditions

# change format to wide (by conditions and directions)
d_rdk_wide_direction <- d_rdk |>
    pivot_wider(id_cols = c(id),
                names_from = c(condition, direction),
                values_from = c(rt, corr),
                values_fn = mean) # take mean for id/conditions

# merge dataframes
d_rdk_wide <- merge(d_rdk_wide_condition, d_rdk_wide_direction,
                       by = "id")

# save new file
write.csv(d_rdk_wide, "data_rdk_wide.csv", row.names = FALSE)
