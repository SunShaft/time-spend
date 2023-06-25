from opts import arg_parser
from utils import csv_file_creator
import cost_calculator
import time_calculator
import os

# TODO: 换成arg形式
date_list = []

time_list = []
cost_list = []
meal_list = []

def top_label_collector():
    pass

def date_collector(date):
    date_list.append(date)

    time_list.append([])
    cost_list.append([])
    meal_list.append([])

def time_collector(line):
    time_list[-1].append(line)

def cost_collector(line):
    cost_list[-1].append(line)

def meal_collector(line):
    meal_list[-1].append(line)

def file_iterator(args, line):
    # TODO: check top label
    # TODO: strip换成arg
    if args.date_indicator in line:
        line = line.strip(args.date_indicator)
        date_collector(line)
    else:
        if args.time_indicator in line:
            line = line.replace(args.time_indicator, "*").strip("*")
            time_collector(line)
        elif args.cost_indicator in line:
            line = line.replace(args.cost_indicator, "*").strip("*")
            cost_collector(line)
        elif args.meal_indicator in line:
            line = line.replace(args.meal_indicator, "*").strip("*")
            meal_collector(line)
        else:
            raise Exception(f"indicator not found in row: [{line}]")
    return

def main():
    args = arg_parser()
 
    with open("temp_file.csv") as f:
        file_list = f.readlines()
        file_list_copy = file_list[:]

    while len(file_list) != 0:
        line = file_list.pop(0).rstrip("\n")
        file_iterator(args, line)


    path = os.path.join(args.path,
        str(args.year) + "_" + date_list[0].replace("/", "_"))
    csv_file_creator(path, "/original_file.csv", file_list_copy)

    # print(date_list)
    # print(time_list)
    # print(cost_list)
    # print(meal_list)

    cost_calculator.main(cost_list, date_list)
    time_calculator.pro_data_writer(args, time_list, date_list)






 



if __name__ == '__main__':
    main()
