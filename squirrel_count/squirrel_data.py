import pandas

data = pandas.read_csv("228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

color = "Primary Fur Color"
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, red_count, black_count]
}

count_data = pandas.DataFrame(data_dict)
count_data.to_csv("squirrel_count.csv")

