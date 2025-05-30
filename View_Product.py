from customtkinter import *
from tkinter import ttk

class ViewProduct:
    def __init__(self,root):

        def delete():
            selected_item = table.selection()
            for item in selected_item:
                table.delete(item)

        products = []

        frame = CTkFrame(master= root, width=1000, height=680, fg_color="#A09E9E")

        title = CTkLabel(master=frame, text="View Product", font=("Arial", 80, 'bold'), fg_color="#A09E9E", text_color="#000000")

        delete_button = CTkButton(master=frame, width=20, height=30, text="DELETE", font=("Arial", 30, 'bold'), fg_color="#FF0000", text_color="#000000", corner_radius=40, command=delete)

        table = ttk.Treeview(frame, height=20, columns=("ID", "Name", "Size", "Quantity", "Price", "Category", "Supplier"), show="headings")

        table.heading("ID", text="ID")
        table.heading("Name", text="Name")
        table.heading("Size", text="Size")
        table.heading("Quantity", text="Quantity")
        table.heading("Price", text="Price")
        table.heading("Category", text="Category")
        table.heading("Supplier", text="Supplier")

        for product in products:
            table.insert("", "end", values=product)
        
        table.place(relx=0.5, rely=0.5, anchor=CENTER)

        title.place(relx=0.5, rely=0.1, anchor=CENTER)

        delete_button.place(relx=0.8, rely=0.9, anchor=CENTER)

        frame.place(relx=0.5, rely=0.5, anchor=CENTER)


root = CTk()
root.geometry("1000x680")
root.title("View Supplier")
ViewProduct(root)
root.mainloop()