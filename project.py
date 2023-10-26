import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def select_operation(data):
    print("stats: for Statistical Analysis")
    print("modify: for Modification in Data Using Pandas")
    print("info: for info on Data using Pandas")
    print("visuals: for Data Visualization and Graphs")
    type_analysis = input("Enter your Analysis Type: ")
    if type_analysis == "stats":
        numpy_analysis(data)
    elif type_analysis == "modify":
        pandas_modification(data)
    elif type_analysis == "info":
        pandas_analysis(data)
    elif type_analysis == "visuals":
        matplot_visuals(data)
    else:
        print("No Valid Operation selected, Terminating the Program, restart the code to try again")

def numpy_analysis(data):
    operation = input("Select the Operation {mean, median, mode, standard deviation, describe}: ")
    if operation == "mean":
        result = np.mean(data["Attendance"])
        print(result)
    elif operation == "median":
        result = np.median(data["Attendance"])
        print(result)
    elif operation == "standard deviation":
        result = np.std(data["Attendance"])
        print(result)
    elif operation == "describe":
        print(data.describe())
    else:
        print("No Valid Operation selected, Terminating the Program, restart the code to try again")

def pandas_modification(data):
    operation = input("Modification needed: ")
    if operation == "fill missing values with zero":
        data1 = data.fillna(0)
        data1.to_csv('file1.csv')
        print("Modified Data Frame is successfully saved as a CSV File")
    elif operation == "fill missing values with forward values":
        data1 = data.fillna(method='ffill')
        data1.to_csv('file1.csv')
        print("Modified Data Fame is successfully saved as a CSV File")
    elif operation == "fill missing values with average":
        data1 = data.interpolate(method='linear', limit=1)
        data1.to_csv('file1.csv')
        print("Modified Data Fame is successfully saved as a CSV File")
    elif operation == "drop missing values":
        data1 = data.dropna()
        data1.to_csv('file1.csv')
        print("Modified Data Fame is successfully saved as a CSV File")
    else:
        print("No Valid Operation selected, Terminating the Program, restart the code to try again")

def pandas_analysis(data):
    operation = input("Enter the required Statistical Information {info, count values, unique values}: ")
    if operation == "info":
        print(data.info())
    elif operation == "count values":
        result = data["Attendance"].value_counts()
        print(result)
    elif operation == "unique values":
        result = data["Attendance"].nunique()
        print(result)
    else:
        print("No Valid Operation selected, Terminating the Program, restart the code to try again")

def matplot_visuals(data):
    operation = input("Enter the Visualization Type {bar plot, box plot}: ")
    if operation == "bar plot":
        x_axis = input("Enter X-Axis: ")
        x = data[x_axis]
        y_axis = input("Enter Y-Axis: ")
        y = data[y_axis]
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.bar(x, y)
        plt.savefig("Bar_Plot.png")
        plt.show()
    elif operation == "box plot":
        axis = input("Enter Column Name for Box Plot: ")
        axis_data = data[axis]
        plt.boxplot(axis_data)
        plt.savefig("Box_Plot.png")
        plt.show()
    else:
        print("No Valid Operation selected, Terminating the Program, restart the code to try again")

if __name__ == "__main__":
    user_input = input("Enter the name of your CSV file: ")
    data = pd.read_csv(user_input)
    select_operation(data)