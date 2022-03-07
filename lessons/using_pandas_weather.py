import pandas

data = pandas.read_csv("226 weather-data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
#
# average_temperature = sum(temp_list)/len(temp_list)
# print(average_temperature)
#
# print(data["temp"].max())
#
# # Get Data in columns
# print(data["condition"])
# print(data.condition)
#
# # return row
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(data[data.day == "Monday"]["condition"])
print(data[data.day == "Monday"].condition)

monday_temp_F = 9/5*int(monday.temp) + 32
print(monday_temp_F)