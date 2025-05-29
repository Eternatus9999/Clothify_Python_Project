from customtkinter import *
from tkinter import ttk

class ViewSupplier:
    def __init__(self,root):

        def delete():
            selected_item = table.selection()
            for item in selected_item:
                table.delete(item)

        suppliers = []

        frame = CTkFrame(master= root, width=1000, height=680, fg_color="#A09E9E")

        title = CTkLabel(master=frame, text="View Supplier", font=("Arial", 80, 'bold'), fg_color="#A09E9E", text_color="#000000")

        delete_button = CTkButton(master=frame, width=20, height=30, text="DELETE", font=("Arial", 30, 'bold'), fg_color="#FF0000", text_color="#000000", corner_radius=40, command=delete)

        table = ttk.Treeview(frame, height=20, columns=("ID", "Name", "Company", "Contact"), show="headings")

        table.heading("ID", text="ID")
        table.heading("Name", text="Name")
        table.heading("Company", text="Email")
        table.heading("Contact", text="Contact")

        for supplier in suppliers:
            table.insert("", "end", values=supplier)
        
        table.place(relx=0.5, rely=0.5, anchor=CENTER)

        title.place(relx=0.5, rely=0.1, anchor=CENTER)

        delete_button.place(relx=0.8, rely=0.9, anchor=CENTER)

        frame.place(relx=0.5, rely=0.5, anchor=CENTER)


root = CTk()
root.geometry("1000x680")
root.title("View Supplier")
ViewSupplier(root)
root.mainloop()