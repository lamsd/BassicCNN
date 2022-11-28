import matplotlib.pyplot as plt
import pandas as pd

index_name = ["X", "Y", "Z", "Class"]
data = pd.read_csv(r"output\train_data.csv", delimiter=",", names=index_name )

data_1 = data[data["Class"] > 0.5].iloc[:, 0:3]
data_0 = data[data["Class"] < 0.5].iloc[:, 0:3]

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(projection='3d')

ax.scatter(data_1["X"], data_1["Y"], data_1["Z"], c="red", marker='x', label="1")
ax.scatter(data_0["X"], data_0["Y"], data_0["Z"], c="blue", marker='o', label="0")
plt.legend(loc="upper left")
plt.show()