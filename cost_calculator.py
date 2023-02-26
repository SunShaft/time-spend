import time_calculator
from utils import row_iterator
#########################FORMAT###########################
# top_labels_1,value_1,top_labels_2,value_2,...
# ===MM/DD===
# cost_labal,item_name_1,cost_1,item_name_2,cost_2,...
# ===MM/DD===
# cost_labal,item_name_1,cost_1,item_name_2,cost_2,...
# .
# .
# .
##########################################################

# [ 
#     [top_labels_1, value_1], 
#     [top_labels_2, value_2], ... 
# ]
top_label_list = []

# [ "MM/DD", "MM/DD", ... ]
date_list = []

# [ 
#     [ 
#         [item_name_1, cost_1],
#         [item_name_2, cost_2], ... 
#     ],
#     [ 
#         [item_name_1, cost_1], 
#         [item_name_2, cost_2], ... 
#     ], ...
# ]
cost_list = []

# [daliy_sum_1, daily_sum_2, ...]
daily_cost_sum_list = []

# [
#     [
#         [time_1, thing_1],
#         [time_2, thing_2], ...
#     ],
#     [
#         [time_1, thing_1],
#         [time_2, thing_2], ...
#     ], ...
# ]
time_list = []



def main(cost_list, date_list):

    for i in range(len(cost_list)):
        if len(cost_list[i]) != 0:
            cost_list[i] = row_iterator(cost_list[i][0].split(","))

    for i in cost_list:
        daily_cost_sum = 0
        for j in i:
            daily_cost_sum += float(j[1])
        daily_cost_sum_list.append(round(daily_cost_sum,2))

    print('''############################################################
# COST SIMPLE
############################################################''')
    for i in range(len(date_list)):
        print("{:5}".format(str(date_list[i])) + " : " + str(daily_cost_sum_list[i]))

    total_cost_sum = sum(daily_cost_sum_list)
    print(f"total   : {round(total_cost_sum,2)}")
    print(f"average : {round(total_cost_sum/len(daily_cost_sum_list),2)}")

    for i in top_label_list:
        for j in range(len(i)):
            if i[j] == income_label:
                income = float(i[j+1])
                
    # print(f"balance : {income-total_cost_sum}")

    print('''############################################################
# COST COMPLEX
############################################################''')
    for i in range(len(date_list)):
        print(date_list[i] + " : " + str(daily_cost_sum_list[i]))
        print(cost_list[i])


    print('''############################################################
# COST DETAL
############################################################''')
    # print("##########top_label_list##########")
    # print(top_label_list)
    print("##########date_list##########")
    print(date_list)
    print("##########cost_list##########")
    print(cost_list)
    print("#####daily_cost_sum_list#####")
    print(daily_cost_sum_list)
    




if __name__ == '__main__':
    main()