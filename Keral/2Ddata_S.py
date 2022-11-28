import matplotlib.pyplot as plt
import pandas as pd

index_name = ["IndexA", "Loss", "ARG"]
data = pd.read_csv(r"csv_data.csv", delimiter=",", names=index_name )
data_loss = data["Loss"]
data_ARG = data["ARG"]

# data[["Index", "Loss", "ARG"]].plot(x="Index", kind="bar")
data.plot(x="IndexA", y=["Loss", "ARG"], kind="bar", figsize=(20, 10), title="Index for the loss and ARG")
plt.show()