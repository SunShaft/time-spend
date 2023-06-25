# coding=utf-8
from utils import csv_file_creator, getEveryDay


class Event():
    def __init__(self, start_time, end_time, event_length, event_type, detail):
        self.start_time = start_time
        self.end_time = end_time
        self.event_length = event_length
        self.event_type = event_type
        self.detail = detail

        self.event_length_hours = minutes_to_hours(event_length)

    def __str__(self):
        return self.start_time + " " + self.end_time + " " + \
               str(self.event_length) + " " + self.event_type + " " + self.detail

    def csv(self):
        return self.start_time + "," + self.end_time + "," + \
               str(self.event_length) + "," + self.event_type + "," + \
               self.detail + "\n"


class Summary():
    def __init__(self, getup_time, sleep_time, A, B, C, D, E,
                 A_list, B_list, C_list, D_list, E_list):
        self.getup_time = getup_time
        self.sleep_time = sleep_time
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.E = E

        self.A_list = A_list
        self.B_list = B_list
        self.C_list = C_list
        self.D_list = D_list
        self.E_list = E_list

        self.A_hours = minutes_to_hours(A)
        self.B_hours = minutes_to_hours(B)
        self.C_hours = minutes_to_hours(C)
        self.D_hours = minutes_to_hours(D)
        self.E_hours = minutes_to_hours(E)

    def __str__(self):
        whole = self.A + self.B + self.C + self.D + self.E
        A_per = percentage_calculator(self.A, whole)
        B_per = percentage_calculator(self.B, whole)
        C_per = percentage_calculator(self.C, whole)
        D_per = percentage_calculator(self.D, whole)
        E_per = percentage_calculator(self.E, whole)

        return "getup_time: " + self.getup_time + "\n" + \
               "sleep_time: " + self.sleep_time + "\n" + \
               "A: " + "{:4}".format(str(self.A)) + " " + str(A_per) + "%\n" + \
               "B: " + "{:4}".format(str(self.B)) + " " + str(B_per) + "%\n" + \
               "C: " + "{:4}".format(str(self.C)) + " " + str(C_per) + "%\n" + \
               "D: " + "{:4}".format(str(self.D)) + " " + str(D_per) + "%\n" + \
               "E: " + "{:4}".format(str(self.E)) + " " + str(E_per) + "%"

    def detail(self):
        detail = ""
        for i in self.A_list:
            detail += "{:6}".format(str(percentage_calculator(i.event_length, self.A))) + "% "
            detail += i.__str__() + "\n"
        for i in self.B_list:
            detail += "{:6}".format(str(percentage_calculator(i.event_length, self.B))) + "% "
            detail += i.__str__() + "\n"
        for i in self.C_list:
            detail += "{:6}".format(str(percentage_calculator(i.event_length, self.C))) + "% "
            detail += i.__str__() + "\n"
        for i in self.D_list:
            detail += "{:6}".format(str(percentage_calculator(i.event_length, self.D))) + "% "
            detail += i.__str__() + "\n"
        for i in self.E_list:
            detail += "{:6}".format(str(percentage_calculator(i.event_length, self.E))) + "% "
            detail += i.__str__() + "\n"
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
    return round(int(length) / int(whole) * 100, 2)


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
    for i in final_list:
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        a_list = []
        b_list = []
        c_list = []
        d_list = []
        e_list = []
        for j in i:
            if j.event_type == "A":
                a += int(j.event_length)
                a_list.append(j)
            elif j.event_type == "B":
                b += int(j.event_length)
                b_list.append(j)
            elif j.event_type[0] == "C":
                c += int(j.event_length)
                c_list.append(j)
            elif j.event_type == "D":
                d += int(j.event_length)
                d_list.append(j)
            elif j.event_type == "E":
                e += int(j.event_length)
                e_list.append(j)
            else:
                raise Exception(f"unknown type in row {j}: {j.event_type}")
        if len(i) != 0:
            summary_list.append(Summary(i[0].start_time, i[-1].end_time,
                                        a, b, c, d, e, a_list, b_list, c_list, d_list, e_list))
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

    print(date_list)

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

    print(summary_list)

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
            return_string += summary_list[i].__str__() + "\n"
            if summary_list[i] is not None:
                return_string += summary_list[i].detail() + "\n"

    return return_string


def main():
    pass


if __name__ == '__main__':
    main()
