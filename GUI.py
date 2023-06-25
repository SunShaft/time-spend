from tkinter import *
from tkinter import ttk

from opts import arg_parser
import time_calculator


# def search(*args):
#     start_date = start_year.get() + "/" + start_month.get() + "/" + start_day.get()
#     end_date = end_year.get() + "/" + end_month.get() + "/" + end_day.get()
#     for i in time_calculator.pro_data_reader(start_date,end_date).split("\n"):
#         l.insert('end',i)

def search(*args):
    choices = []
    for i in time_calculator.pro_data_reader(parser_args, 
        start_date.get(),end_date.get(),
        time_detail.get()).split("\n"):
        choices.append(i)
    choicesvar.set(choices)

parser_args = arg_parser()

root = Tk()
root.title("management")

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# start_year = StringVar()
# ttk.Entry(mainframe, width=4, textvariable=start_year).grid(column=1, row=2, sticky=(W, E))
# start_month = StringVar()
# ttk.Entry(mainframe, width=2, textvariable=start_month).grid(column=3, row=2, sticky=(W, E))
# start_day = StringVar()
# ttk.Entry(mainframe, width=2, textvariable=start_day).grid(column=5, row=2, sticky=(W, E))

# end_year = StringVar()
# ttk.Entry(mainframe, width=4, textvariable=end_year).grid(column=7, row=2, sticky=(W, E))
# end_month = StringVar()
# ttk.Entry(mainframe, width=2, textvariable=end_month).grid(column=9, row=2, sticky=(W, E))
# end_day = StringVar()
# ttk.Entry(mainframe, width=2, textvariable=end_day).grid(column=11, row=2, sticky=(W, E))




# ttk.Label(mainframe, text="START").grid(column=1, row=0, sticky=W)
# ttk.Label(mainframe, text="END").grid(column=7, row=0, sticky=W)

# ttk.Label(mainframe, text="YEAR").grid(column=1, row=1, sticky=W)
# ttk.Label(mainframe, text="/").grid(column=2, row=1, sticky=W)
# ttk.Label(mainframe, text="MONTH").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="/").grid(column=4, row=1, sticky=W)
# ttk.Label(mainframe, text="DAY").grid(column=5, row=1, sticky=W)

# ttk.Label(mainframe, text="——").grid(column=6, row=1, sticky=W)

# ttk.Label(mainframe, text="YEAR").grid(column=7, row=1, sticky=W)
# ttk.Label(mainframe, text="/").grid(column=8, row=1, sticky=W)
# ttk.Label(mainframe, text="MONTH").grid(column=9, row=1, sticky=W)
# ttk.Label(mainframe, text="/").grid(column=10, row=1, sticky=W)
# ttk.Label(mainframe, text="DAY").grid(column=11, row=1, sticky=W)

# ttk.Label(mainframe, text="/").grid(column=2, row=2, sticky=W)
# ttk.Label(mainframe, text="/").grid(column=4, row=2, sticky=W)
# ttk.Label(mainframe, text="——").grid(column=6, row=2, sticky=W)
# ttk.Label(mainframe, text="/").grid(column=8, row=2, sticky=W)
# ttk.Label(mainframe, text="/").grid(column=10, row=2, sticky=W)

# ttk.Button(mainframe, text="SEARCH", command=search).grid(column=12, row=2, sticky=W)

start_date = StringVar()
ttk.Entry(mainframe, width = 11, textvariable=start_date).grid(column=0, row=2, sticky=(W, E))

end_date = StringVar()
ttk.Entry(mainframe, width = 11, textvariable=end_date).grid(column=2, row=2, sticky=(W, E))

time_detail = BooleanVar(value=False)
ttk.Checkbutton(mainframe, text="detail", variable=time_detail, onvalue=True).grid(column=3, row=1, sticky=(W, E))


ttk.Label(mainframe, text="START DATE").grid(column=0, row=0, sticky=W)
ttk.Label(mainframe, text="END DATE").grid(column=2, row=0, sticky=W)

ttk.Label(mainframe, text="YYYY/MM/DD").grid(column=0, row=1, sticky=W)
ttk.Label(mainframe, text="——").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="YYYY/MM/DD").grid(column=2, row=1, sticky=W)

ttk.Label(mainframe, text="——").grid(column=1, row=2, sticky=W)

ttk.Button(mainframe, text="SEARCH", command=search).grid(column=3, row=2, sticky=W)



choices = []
choicesvar = StringVar(value=choices)
l = Listbox(root, listvariable=choicesvar)
l.grid(column=0, row=5, sticky=(N,W,E,S))
s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
s.grid(column=1, row=5, sticky=(N,S))
l['yscrollcommand'] = s.set



for child in mainframe.winfo_children(): 
    child.grid_configure(padx=1, pady=1)

root.mainloop()

