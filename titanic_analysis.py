# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
titanic_df = pd.read_csv(url)

# Display the first few rows of the dataset
print(titanic_df.head())

# Display basic information about the dataset
print(titanic_df.info())

# Display summary statistics of the dataset
print(titanic_df.describe())

# Check for missing values
print(titanic_df.isnull().sum())

# Visualize the distribution of numerical features
titanic_df.hist(bins=30, figsize=(10, 8))
plt.show()

# Visualize the distribution of categorical features
sns.countplot(x='Survived', data=titanic_df)
plt.show()

sns.countplot(x='Pclass', data=titanic_df)
plt.show()

sns.countplot(x='Sex', data=titanic_df)
plt.show()