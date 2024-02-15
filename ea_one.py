import seaborn as sns
import pandas
from matplotlib import pyplot as plt
import math

fileName = input("Enter the CSV name: ")

try:
    dataset = pandas.read_csv(fileName)
    plot = sns.lineplot(data=dataset, x="Month", y="Max Temp (°C)")
    title = "Max Temperature Recorded At " + dataset["Station Name"][0] + " Station Per Month"
    plot.set_title(title)
    plot.set_xlabel("Months In Number Form")
    plt.show() #Only needed if you're not using Jupyter to run this program.
except:
    print("An error occured")