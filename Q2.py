

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Iris.csv")

print(data)

plt.figure(figsize = (10,8))
sns.countplot(x = 'Species', data = data)
plt.xlabel("Species")
plt.ylabel("Frequency")
plt.title("Frequency Distribution of Iris Species")
plt.show()

# Plot histograms of SepalLengthCm for each species
plt.hist(data[data['Species'] == 'Iris-setosa']['SepalLengthCm'], bins=15, color='blue', alpha=0.5)
plt.hist(data[data['Species'] == 'Iris-versicolor']['SepalLengthCm'], bins=15, color='green', alpha=0.5)
plt.hist(data[data['Species'] == 'Iris-virginica']['SepalLengthCm'], bins=15, color='red', alpha=0.5)

plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.title('Distribution of Sepal Length for Different Iris Species')

plt.legend(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])

plt.show()