import argparse
import datetime

def arg_parser():
    year = datetime.date.today().year
    parser = argparse.ArgumentParser(description = "life recorder")

    # file_creator
    parser.add_argument("-y", "--year", type=int,
                        default=year,
                        metavar="y", nargs=1, help="year of the csv file")

    parser.add_argument("-p", "--path", type=str,
                        default="/Users/sbridge/Program/time_spend/data",
                        metavar="p", nargs=1, help="path of csv file")

    # date
    parser.add_argument("-di", "--date_indicator", type=str,
                        default="===",
                        metavar="di", nargs=1, help="date indicator to distinguish date")

    # time
    parser.add_argument("-ti", "--time_indicator", type=str,
                        default="-",
                        metavar="ti", nargs=1, help="time indicator to distinguish date")

    # cost
    parser.add_argument("-ci", "--cost_indicator", type=str,
                        default="cost,",
                        metavar="ci", nargs=1, help="cost indicator to distinguish date")

    # meal
    parser.add_argument("-mi", "--meal_indicator", type=str,
                        default="meal,",
                        metavar="mi", nargs=1, help="meal indicator to distinguish date")



    # time_calculator
    parser.add_argument("-ds", "--date_split", type=str,
                        default="/",
                        metavar="ds", nargs=1, help="symbol that split date, month and year")

    parser.add_argument("-pdp", "--pro_data_path", type=str,
                        default=f"/Users/sbridge/Program/time_spend/pro_data/",
                        metavar="ds", nargs=1, help="pro data path")

    parser.add_argument("-pdtn", "--pro_data_time_name", type=str,
                        default="/time.csv",
                        metavar="ds", nargs=1, help="pro data time file name")








    return parser.parse_args()
