import pandas as pd

# Sample dataset
data = {
    "Name": ["Aman", "Riya", "Rahul", None],
    "Age": [20, 21, None, 22],
    "Marks": [85, 90, 88, None]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Handling missing values
df["Name"] = df["Name"].fillna("Unknown")
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nCleaned Dataset:")
print(df)

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("\nPreprocessing Completed!")
