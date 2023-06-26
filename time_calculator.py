# coding=utf-8
from utils import csv_file_creator, getEveryDay
from opts import arg_parser


class Event():
    def __init__(self, start_time, end_time, event_length, event_type, detail):
        self.start_time = start_time
        self.end_time = end_time
        self.event_length = event_length
        self.event_type = event_type
        self.detail = detail

        self.event_length_hours = minutes_to_hours(event_length)

    def __str__(self):
        return f"{self.start_time:5} {self.end_time:5} {str(self.event_length):3} {self.event_type:5} {self.detail}"

    def csv(self):
        return self.start_time + "," + self.end_time + "," + \
               str(self.event_length) + "," + self.event_type + "," + \
               self.detail + "\n"


class Summary():
    def __init__(self, getup_time, sleep_time, type_dict):
        self.getup_time = getup_time
        self.sleep_time = sleep_time
        self.type_dict = type_dict

        self.whole = 0
        for i in type_dict:
            self.whole += self.type_dict[i][0]

        # [type_time_sum, type_event_list, type_time_percentage]
        for i in self.type_dict:
            self.type_dict[i].append(percentage_calculator(self.type_dict[i][0], self.whole))

    def __str__(self):
        return_string = "getup_time: " + self.getup_time + "\n" + \
                        "sleep_time: " + self.sleep_time + "\n"

        for i in self.type_dict:
            return_string += f"{i:10}: {str(self.type_dict[i][0]):5} {str(self.type_dict[i][2])}%\n"

        return return_string

    def detail(self):
        detail = ""
        for i in self.type_dict:
            for j in self.type_dict[i][1]:
                detail += "{:6}".format(str(percentage_calculator(j.event_length, self.type_dict[i][0]))) + "% "
                detail += j.__str__() + "\n"
        return detail


def time_format_reformer(time):
    """
    把时间从 xx:yy 转换成 [xx,yy]
    """
    time = time.split(":")
    return [int(i) for i in time]


def minutes_to_hours(time):
    try:
        time = int(time)
        return "{:>02}".format(str(time // 60)) + ":" + "{:>02}".format(str(time % 60))
    except:
        return time


def percentage_calculator(length, whole):
    return round(int(length) / int(whole) * 100, 1)


def time_interval_calculator(previous_time, time):
    """
    返回两个时间之间的间隔
    """
    previous_time = time_format_reformer(previous_time)
    time = time_format_reformer(time)

    # 熬夜超过12点了
    if time[0] < previous_time[0]:
        time[0] += 24

    hour = time[0] - previous_time[0]
    minute = time[1] - previous_time[1]

    return hour * 60 + minute


def summary(final_list):
    summary_list = []
    type_dict = {}
    for i in final_list:
        for j in i:
            event_type = j.event_type
            if event_type not in type_dict:
                type_dict[event_type] = [0,[]]
            type_dict[event_type][0] += int(j.event_length)
            type_dict[event_type][1].append(j)

        if len(i) != 0:
            summary_list.append(Summary(i[0].start_time, i[-1].end_time, type_dict))
        else:
            summary_list.append(None)

    return summary_list


def event_list_creator(day_time_list):
    """
    !!!此方法只适合给原始数据使用!!!
    TODO:放回pro_data_writer里面去
    day_time_list就是time_list中的元素
    创建一个全是Event对象的list
    """
    event_list = []
    for i in range(1, len(day_time_list)):
        previous_event = day_time_list[i - 1].split(",")
        current_event = day_time_list[i].split(",")
        event_length = time_interval_calculator(previous_event[0],
                                                current_event[0])
        event_list.append(Event(previous_event[0], current_event[0],
                                event_length, current_event[1], ";".join(current_event[2:])))
    return event_list


def pro_data_writer(args, time_list, date_list):
    for i in range(len(time_list)):
        date = date_list[i].split(args.date_split)
        date = "{:>02}".format(date[0]) + args.date_split + "{:>02}".format(date[1])
        pro_data_list = [j.csv() for j in event_list_creator(time_list[i])]
        csv_file_creator(f"{args.pro_data_path}{args.year}/{date}",
                         args.pro_data_time_name, pro_data_list)


def pro_data_reader(args, start_date, end_date, detail=False):
    """
    start_date =  year/month/day
    end_date = year/month/day
    """

    # [
    #     [
    #         Event
    #         .
    #         .
    #         .
    #     ],
    #     .
    #     .
    #     .
    # ]
    final_list = []
    date_list = getEveryDay(start_date, end_date)

    # print(date_list)

    for date in date_list:
        with open(args.pro_data_path + date + args.pro_data_time_name, "r") as f:
            day_time_list = [i.rstrip("\n").split(",") for i in f.readlines()]
        event_list = [Event(i[0], i[1], i[2], i[3], i[4]) for i in day_time_list]
        final_list.append(event_list)

    # [
    #     [
    #         Summary
    #     ],
    #     .
    #     .
    #     .
    # ]
    summary_list = summary(final_list)

    # print(summary_list)

    return_string = ""

    if not detail:
        # length in minutes
        for i in range(len(final_list)):
            return_string += date_list[i]
            return_string += "\n"
            if summary_list[i] is None:
                continue
            return_string += summary_list[i].__str__()
            return_string += "\n"
            i = final_list[i]
            for j in i:
                return_string += j.__str__()
                return_string += "\n"

        # length in hours
        # for i in range(len(final_list)):
        #     print(date_list[i])
        #     print(summary_list[i])
        #     i = final_list[i]
        #     for j in i:
        #         print(j)

    else:
        # summary detail
        for i in range(len(final_list)):
            return_string += date_list[i] + "\n"
            if summary_list[i] is None:
                continue
            return_string += summary_list[i].__str__()
            if summary_list[i] is not None:
                return_string += summary_list[i].detail() + "\n"

    print(return_string)
    return return_string


def main():
    parser_args = arg_parser()
    pro_data_reader(parser_args, "2023/5/2", "2023/5/3", True)
    # pass


if __name__ == '__main__':
    main()
