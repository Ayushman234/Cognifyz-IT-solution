import pandas as pd
import matplotlib.pyplot as plt

try:
    data = pd.read_csv("Level3/Task2/students.csv")

    print(data)

    plt.figure(figsize=(8, 5))
    plt.bar(data["Name"], data["Marks"])

    plt.title("Student Marks")
    plt.xlabel("Students")
    plt.ylabel("Marks")

    plt.show()

except FileNotFoundError:
    print("students.csv not found.")