


import pandas as pd

data = {
    'Name' : ['a', 'b', None, 'a', 'e', 'f', 'g', 'h', 'i', 'j'],
    'Salary' : [50000, 60000, 55000, 65000, None, 30000, 35000, 50000, 40000, 45000],
    'Department' : ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', None, 'IT', 'IT', 'IT']
}

df = pd.DataFrame(data)
print(df)


print("\n\n")

df1 = df.dropna()
print(df1)


#3Q

import pandas as pd
import matplotlib.pyplot as plt


iris_data = pd.read_csv("Iris.csv")

print(iris_data)

print("\nNames of columns:", iris_data.columns.tolist())

species_count = iris_data["Species"].value_counts()

plt.hist(iris_data[iris_data['Species'] == 'Iris-setosa']['SepalLengthCm'], bins=15, color='red', alpha=0.5, label='Iris-setosa')
plt.hist(iris_data[iris_data['Species'] == 'Iris-versicolor']['SepalLengthCm'], bins=15, color='green', alpha=0.5, label='Iris-versicolor')
plt.hist(iris_data[iris_data['Species'] == 'Iris-virginica']['SepalLengthCm'], bins=15, color='yellow', alpha=0.5, label='Iris-virginica')

plt.suptitle('Histogram of Sepal Length by Species', y=1.02)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')

plt.legend()

plt.show()