

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('income.csv')

print(df.head())  
print()
print(df.info()) 
print("-------------------------------------------------\n\n")

X = df[['Income($)', 'Age']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

plt.figure(figsize=(10, 6))

# Plot data points with cluster colors
sns.scatterplot(x=df['Income($)'], y=df['Age'], hue=df['Cluster'], palette='Set1', s=100)

# Calculate centroids in original scale and plot them
centroids_original_scale = scaler.inverse_transform(kmeans.cluster_centers_)
plt.scatter(centroids_original_scale[:, 0], centroids_original_scale[:, 1], 
            s=300, c='black', marker='*', label='Centroids')

# Add titles and labels
plt.title('K-means Clustering (Income vs Age)')
plt.xlabel('Income')
plt.ylabel('Age')
plt.legend()
plt.show()

print("Cluster centers (after scaling):", kmeans.cluster_centers_)
print("Cluster centers (in original scale):", centroids_original_scale)
