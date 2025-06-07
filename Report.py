from customtkinter import *

import DatabaseConnector

class Report:
    def __init__(self, root, type):
        orders = DatabaseConnector.viewOrder()
        print(orders)
        if(type == "Annual"):
            frame = CTkFrame(master= root, width=1000, height=680, fg_color="#A09E9E")
            frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        elif(type == "Monthly"):
            frame = CTkFrame(master= root, width=1000, height=680, fg_color="#A09E9E")
            frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        else:
            frame = CTkFrame(master= root, width=1000, height=680, fg_color="#A09E9E")
            frame.place(relx=0.5, rely=0.5, anchor=CENTER)