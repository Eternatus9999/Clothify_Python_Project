from customtkinter import *

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import DatabaseConnector

class Report:
    def __init__(self, root, type):
        self.frame = CTkFrame(master= root, width=1000, height=680, fg_color="#A09E9E")
        fig, ax = plt.subplots()
        if(type == "Product"):
            orders = DatabaseConnector.viewProduct()
            category = self.organizeCategory(orders)
            title = CTkLabel(master=self.frame, text="Product Report", font=("Arial", 80, 'bold'), fg_color="#A09E9E", text_color="#000000")
            title.place(relx=0.5, rely=0.1, anchor=CENTER)
            ax.pie(category, labels=["Gents","Ladies","Kids"], autopct='%1.1f%%', radius=1.25, startangle=90, textprops={'fontsize': 20, 'color': 'black'})
        elif(type == "Supplier"):
            suppliers = DatabaseConnector.viewSupplier()
            amount = self.organizeSuppliersAmount(suppliers)
            ids = self.organizeSuppliers(suppliers)
            ax.pie(amount, labels = ids, autopct='%1.1f%%', radius=1.25, startangle=90, textprops={'fontsize': 20, 'color': 'black'})
            title = CTkLabel(master=self.frame, text="Supplier Report", font=("Arial", 80, 'bold'), fg_color="#A09E9E", text_color="#000000")
            title.place(relx=0.5, rely=0.1, anchor=CENTER)
        fig.patch.set_facecolor('#A09E9E')
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.5, rely=0.6, anchor=CENTER)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def organizeCategory(self, orders):
        category = [0,0,0]
        for order in orders:
            if(order[5] =="Gents"):
                category[0] = category[0] + (order[3])
            elif(order[5] == "Ladies"):
                category[1] = category[1] + (order[3])   
            else:
                category[2] = category[2] + (order[3])
        return category

    def organizeSuppliersAmount(self, suppliers):
        amount = []
        for supplier in suppliers:
            amount.append(supplier[3])
        return amount

    def organizeSuppliers(self, suppliers):
        ids = []
        for supplier in suppliers:
            ids.append(supplier[0])
        return ids