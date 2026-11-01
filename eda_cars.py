import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("cars_dataset.csv", low_memory=False)
print("Shape:", df.shape)
print(df[["make", "body_type", "fuel_type", "vehicle_age", "msrp", "final_sale_price"]].describe(include="all"))

df = df.drop_duplicates()
df = df.dropna(subset=["final_sale_price"])
df = df[df["final_sale_price"] > 0]
df = df.loc[:, df.isna().mean() < 0.5]

num_cols = df.select_dtypes(include="number").columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())
cat_cols = df.select_dtypes(exclude="number").columns
df[cat_cols] = df[cat_cols].fillna("Unknown")

low, high = df["final_sale_price"].quantile([0.01, 0.99])
df = df[df["final_sale_price"].between(low, high)].copy()

df["discount_percent_msrp"] = np.where(df["msrp"] > 0, (df["msrp"] - df["final_sale_price"]) / df["msrp"] * 100, 0)

print("Clean shape:", df.shape)

sns.histplot(df["final_sale_price"], bins=50, kde=True)
plt.title("Distribution of final sale price")
plt.xlabel("Final sale price")
plt.show()

top_body_types = df["body_type"].value_counts().head(8).index
sns.boxplot(data=df[df["body_type"].isin(top_body_types)], x="body_type", y="final_sale_price")
plt.title("Final sale price by body type")
plt.xlabel("Body type")
plt.ylabel("Final sale price")
plt.show()
