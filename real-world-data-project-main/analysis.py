import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/retail_sales.csv")

# Display first rows
print(df.head())

# Dataset info
print(df.info())

# Total sales
print("Total Sales:", df["Sales"].sum())

# Total profit
print("Total Profit:", df["Profit"].sum())

# Sales by category
category_sales = df.groupby("Category")["Sales"].sum()
print(category_sales)

# Visualization
plt.figure(figsize=(8,5))
sns.barplot(x=category_sales.index, y=category_sales.values)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.savefig("outputs/charts/sales_by_category.png")
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Features and target
X = df[["Quantity", "Profit"]]
y = df["Sales"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Accuracy
score = model.score(X_test, y_test)
print("Model Accuracy:", score)

# Prediction
prediction = model.predict([[5, 2000]])
print("Predicted Sales:", prediction[0])