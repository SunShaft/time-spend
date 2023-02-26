import argparse
import datetime

def arg_parser():
    parser = argparse.ArgumentParser(description = "life recorder")

    # file_creator
    parser.add_argument("-y", "--year", type=int,
                        default=datetime.date.today().year,
                        metavar="y", nargs=1, help="year of the csv file")

    parser.add_argument("-p", "--path", type=str,
                        default="/Users/sbridge/Program/time_spend/data",
                        metavar="p", nargs=1, help="path of csv file")

    # date
    parser.add_argument("-di", "--date_indicator", type=str,
                        default="===",
                        metavar="d", nargs=1, help="date indicator to distinguish date")

    # time
    parser.add_argument("-ti", "--time_indicator", type=str,
                        default="-",
                        metavar="d", nargs=1, help="time indicator to distinguish date")

    # cost
    parser.add_argument("-ci", "--cost_indicator", type=str,
                        default="cost,",
                        metavar="d", nargs=1, help="cost indicator to distinguish date")

    # meal
    parser.add_argument("-mi", "--meal_indicator", type=str,
                        default="meal,",
                        metavar="d", nargs=1, help="meal indicator to distinguish date")










    return parser.parse_args()
