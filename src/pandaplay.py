import pandas as pd


# Read Excel spreadsheet
df = pd.read_excel("../data/Cyclanthaceae.xlsx")

type(df)
df.head()
print(df)
print(" Shape is " + str(df.shape))

# Select Collector column
print(df["Collector"])

# Select rows containing Hjalmar Jensen. in Collector
print(df["Collector"] == "Hjalmar Jensen.")
limited_dataframe = df[df["Collector"] == "Hjalmar Jensen."]
print(limited_dataframe)

# Save to disk
limited_dataframe.to_excel("../data/Hjalmar_only.xlsx", index=True)
limited_dataframe.to_csv("../data/Hjalmar_only.csv", index=False)


# Select all rows wit Glaziou in either Collector or Locality
limited_dataframe2 = df[(df["Collector"] == "Glaziou") | (df["Locality"] == "Glaziou")]
print(limited_dataframe2)


# Find occurrences of Warming in the Other Remarks column
df["Other Remarks"].str.contains("Warming")
# But there are some NaN among the rows!
df["Other Remarks"].str.contains("Warming").notna()

limited_dataframe3 = df[df["Other Remarks"].str.contains("Warming").notna()]
print(limited_dataframe3)


# Creating a new table
agents = pd.DataFrame(
    { # A dictionay with column names as keys and lists as values
        "Name": [
            "Hjalmar Jensen",
            "Dr. A. Glaziou"
            ],
        "Short name": [
            "Hj. Jensen",
            "Glaziou"
            ]
    
    }
)




# Join tables together
df2 = pd.merge(df, agents, how='left', left_on='Collector', right_on='Short name')
