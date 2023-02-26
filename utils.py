import os
import datetime 

def row_iterator(row, item_interval = 2):
    '''
    exchange row into a final_list include serval lists and return
    the length of the list in the final_list equal to item_interval
    '''
    current_interval = 0
    current_index = 0
    final_list = []
    while current_index < len(row):
        if current_interval == 0:
            item_list = [row[current_index]]
            current_interval += 1
            current_index += 1
        elif current_interval < item_interval:
            item_list.append(row[current_index])
            current_interval += 1
            current_index += 1
            if current_interval == item_interval:
                final_list.append(item_list)
                current_interval = 0
        # print(item_list)
        # print(item_interval)
    return final_list



def csv_file_creator(path, file_name, file_content, operate_type = "w"):
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + file_name, operate_type) as f:
        f.writelines(file_content)



def getEveryDay(start_date,end_date):
    date_list = [] 
    start_date = datetime.datetime.strptime(start_date, "%Y/%m/%d") 
    end_date = datetime.datetime.strptime(end_date,"%Y/%m/%d")
    while start_date <= end_date: 
        date_str = start_date.strftime("%Y/%m/%d") 
        date_list.append(date_str) 
        start_date += datetime.timedelta(days=1) 
    return date_list 






