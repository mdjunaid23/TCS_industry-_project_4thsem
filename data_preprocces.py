import pandas as pd

# Step 1: Load Dataset
df = pd.read_csv("Retail_Sales_Dataset.csv")

# Step 2: Preview Data
print("Initial Data:")
print(df.head())

# Step 3: Data Cleaning

# Remove duplicate rows
df = df.drop_duplicates()

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values (if any)
df = df.fillna(method='ffill')

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Step 4: Add Month Column
df['Month'] = df['Date'].dt.strftime('%b')

# Step 5: Add Age Group Column
def age_group(age):
    if age <= 25:
        return "18-25"
    elif age <= 35:
        return "26-35"
    elif age <= 50:
        return "36-50"
    else:
        return "50+"

df['Age Group'] = df['Age'].apply(age_group)

# Step 6: Verify Changes
print("\nUpdated Data:")
print(df[['Age', 'Age Group', 'Month']].head())

# Step 7: Save Cleaned Dataset
df.to_csv("_Retail_Sales_Dataset(1).csv", index=False)

print("\n✅ Data cleaning and transformation completed successfully!")