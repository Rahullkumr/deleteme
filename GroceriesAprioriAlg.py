import pandas as pd
from apyori import apriori

# Read the dataset
data = pd.read_csv("groceries - groceries.csv", header=None)

# Convert data into a list of lists for Apriori algorithm
transactions = []
for index, row in data.iterrows():
    transaction = [str(item) for item in row if str(item) != 'nan']  # Filter out 'nan' values
    transactions.append(transaction)

# Apply Apriori algorithm with the given min_support, min_confidence
rules = apriori(transactions, min_support=0.0040, min_confidence=0.2)

# Filter and display rules with min_lift=3 and min_length=2
print("Association Rules:")
for rule in rules:
    items = list(rule.items)
    if len(items) >= 2:  # Minimum length
        for result in rule.ordered_statistics:
            if result.lift >= 3:  # Minimum lift
                print(f"Rule: {', '.join(items)} -> {', '.join(result.items_add)}")
                print(f"Support: {rule.support:.4f}")
                print(f"Confidence: {result.confidence:.4f}")
                print(f"Lift: {result.lift:.2f}")
                print("-" * 20)
