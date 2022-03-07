import csv

# with open("226 weather-data.csv") as file:
#     data = file.readlines()
#     stripped_data = []
#     for entry in data:
#         stripped_entry = entry.strip("\n")
#         stripped_data.append(stripped_entry)
#     print(stripped_data)

with open("226 weather-data.csv") as data_file:
    data = csv.reader(data_file)
    print(data)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

print(type(temperatures[1]))

# Wow that was so long to do. If only there was an easier way to do it. Let's go install a new module, pandas.

import pandas

data = pandas.read_csv("226 weather-data.csv")
print(data["temp"])


