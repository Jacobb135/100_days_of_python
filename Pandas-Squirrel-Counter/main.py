# # weather = open("weather_data.csv")
# #
# # data = weather.readlines()
# # print(data)
#
# # import csv
# #
# # data_file = open("weather_data.csv")
# # data = csv.reader(data_file)
# # temperatures = []
# # for row in data:
# #     if row[1] != "temp":
# #         temperatures.append(int(row[1]))
# # print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# #
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# # print(temp_list)
# #
# # print(data["temp"].mean())
# # # print(data["temp"].max())
#
# # print(data[data.day == "Monday"])
# # highest = data["temp"].max()
# # print(data[data.temp == highest])
#
# # monday = data[data.day == "Monday"]
# # monday_temp = int(monday.temp)
# # monday_temp_f = monday_temp * 9 / 5 + 32
# # print(monday_temp_f)
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_dict = {}
squirrel_color = data["Primary Fur Color"]
for squirrel in squirrel_color:
    data_dict[squirrel] = data_dict.get(squirrel, 0) + 1

gray = data_dict["Gray"]
red = data_dict["Cinnamon"]
black = data_dict["Black"]
new_data = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, red, black]
}

df = pandas.DataFrame([data_dict])
df.to_csv("squirrel_count.csv")



