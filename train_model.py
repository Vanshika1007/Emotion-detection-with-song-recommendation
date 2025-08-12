import pandas as pd
import matplotlib.pyplot as plt

# ✅ Load the file with correct separator and quotechar
df = pd.read_csv("test.csv", sep=';', quotechar='"')

# ✅ Print raw data and shape
print("📁 Raw DataFrame:")
print(df.head())
print("\n📏 Shape of DataFrame:", df.shape)

# ✅ Clean column names
df.columns = df.columns.str.strip().str.replace('"', '').str.lower()
print("🧼 Cleaned column names:", df.columns.tolist())

# ✅ Drop rows with missing values
df.dropna(subset=['text', 'emotion'], inplace=True)

# ✅ Check if data is still empty
if df.empty:
    print("🚨 DataFrame is empty after cleaning! Check CSV formatting.")
else:
    print("\n📊 Emotion Distribution:")
    print(df['emotion'].value_counts())

    # ✅ Plot only if data is present
    plt.figure(figsize=(10,6))
    df['emotion'].value_counts().plot(kind='bar', color='skyblue')
    plt.title('Emotion Distribution')
    plt.xlabel('Emotions')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
