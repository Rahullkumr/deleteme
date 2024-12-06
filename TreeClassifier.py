
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv('salarydata.csv')

# Assume that the last column is the target variable (adjust according to your dataset)
X = data.iloc[:, :-1]  
y = data.iloc[:, -1]   

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf_entropy = DecisionTreeClassifier(criterion='entropy', random_state=42)

clf_entropy.fit(X_train, y_train)

y_pred_entropy = clf_entropy.predict(X_test)

accuracy_entropy = accuracy_score(y_test, y_pred_entropy)
print(f"Accuracy of Decision Tree Classifier (entropy): {accuracy_entropy * 100:.2f}%")

# Initialize the Decision Tree Classifier with 'gini' as the criterion
clf_gini = DecisionTreeClassifier(criterion='gini', random_state=42)

clf_gini.fit(X_train, y_train)

y_pred_gini = clf_gini.predict(X_test)

accuracy_gini = accuracy_score(y_test, y_pred_gini)
print(f"Accuracy of Decision Tree Classifier (gini index): {accuracy_gini * 100:.2f}%")
