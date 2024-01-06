import pandas as pd 

df = pd.read_csv("file.csv")

print(df.head())

print(df)

print(df.shape)

# Find all null value in the dataset. If there is any column, then fill it with the mean of that column.
print(df.isnull().sum())

df["Cylinders"] = df["Cylinders"].fillna(df["Cylinders"].mean())

print(df["Cylinders"])

df.dropna()

print(df.isna().sum())

# Check what are the diffirent types of make are there in our dataset. And what is the count (occurence) of each make in data

print(df.head(2))

print(df["Make"].value_counts())

# Show all the records where origin is Asia or Europe

df.head(2)

print(df[df["Origin"].isin(["Asia", "Europe"])])

# Remove all the records (rows) where Weight is above 4000.

print(df.head(2))

print(df[df["Weight"] > 4000])

# Increase all the values of 'MPG_City' column by 3.

df["MPG_City"] = df["MPG_City"].apply(lambda x:x+3)
