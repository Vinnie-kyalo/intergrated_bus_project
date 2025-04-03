# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
titanic_df = pd.read_csv(url)

# Handle missing values
titanic_df['Age'].fillna(titanic_df['Age'].median(), inplace=True)
titanic_df['Embarked'].fillna(titanic_df['Embarked'].mode()[0], inplace=True)

# Drop columns that won't be used in the analysis
titanic_df.drop(columns=['Cabin', 'Ticket', 'Name'], inplace=True)

# Create new features
titanic_df['FamilySize'] = titanic_df['SibSp'] + titanic_df['Parch']
titanic_df['IsAlone'] = (titanic_df['FamilySize'] == 0).astype(int)

# Encode categorical variables
titanic_df = pd.get_dummies(titanic_df, columns=['Sex', 'Embarked'], drop_first=True)

# Display the first few rows of the cleaned dataset
print(titanic_df.head())

# Display basic information about the cleaned dataset
print(titanic_df.info())

# Display summary statistics of the cleaned dataset
print(titanic_df.describe())

# Visualize the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(titanic_df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()