"""
    This Program is used to make bar graph from file CSV.
    This graph is All internet usage desktop in 2558
"""
import csv
import pygal
import cairo
with open('2558_usage_mobile.csv', newline='') as csvfile:
    a = csv.reader(csvfile)
    list_types = []
    list_male = []
    list_female = []
    for types, male, female in a:
        list_types.append(types)
        list_male.append(male)
        list_female.append(female)
    line_chart = pygal.Bar()
    line_chart.title = 'All internet usage mobile 2558 (in %)'
    line_chart.x_labels = list_types[1:]
    line_chart.add('Male', [float(i) for i in list_male[1:]])
    line_chart.add('Female',  [float(i)  for i in list_female[1:]])
    line_chart.render_to_file('line_chart2.svg')                          # Save the svg to a file