# ------------------------------------------------------
# Copyright (c) 2026 Antonis Koukoumelas. All rights reserved.
# Αυτό το project δημιουργήθηκε από Antonis Koukoumelas.
# ------------------------------------------------------

# data_analysis.py
import pandas as pd
import matplotlib.pyplot as plt

# Παράδειγμα CSV: data.csv
# Name,Score1,Score2,Score3
# Maria,18,19,20
# John,15,17,16

df = pd.read_csv("data.csv")
df["Average"] = df[["Score1","Score2","Score3"]].mean(axis=1)
print(df)

# Γράφημα
plt.bar(df["Name"], df["Average"])
plt.ylabel("Average Score")
plt.title("Student Average Scores")
plt.show()
