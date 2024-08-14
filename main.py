# with open("weather_data.csv") as date_file:
#     date = date_file.readlines()
#     print(date)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(data["temp"])
# data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
# # moyenne = sum(temp_list) / len(temp_list)
# # print(round(moyenne, 2))
# print(data["temp"].mean())
# print(data["temp"].max())
#
# #Get date in the colmun
# print(data["condition"])
# print(data.condition)

#Get date in the row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# temp_monday = monday.temp[0]
# temp_monday_F = temp_monday * 9/5 + 32
# print(temp_monday_F)
#Create datframe from scratch
# data_dict = {
#     "students": ["Inncent", "David", "Underson"],
#     "Score": [74, 69, 65]
# }
# date = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240813.csv")
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrel_count)
print(cinnamon_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, black_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")