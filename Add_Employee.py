from customtkinter import *

class AddEmployee:
    def __init__(self,root):

        frame = CTkFrame(master= root, width=1000, height=680, fg_color="#A09E9E")

        title = CTkLabel(master=frame, text="Add Employee", font=("Arial", 80, 'bold'), fg_color="#A09E9E", text_color="#000000")

        employeeId = CTkEntry(master = frame, placeholder_text="ID", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        employeeName = CTkEntry(master = frame, placeholder_text="Name", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        employeeEmail = CTkEntry(master = frame, placeholder_text="Email", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        employeeAddress = CTkEntry(master = frame, placeholder_text="Address", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        employeeContact = CTkEntry(master = frame, placeholder_text="Contact", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        employeePassword = CTkEntry(master = frame, placeholder_text="Password", show='*', width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        employeeRePassword = CTkEntry(master = frame, placeholder_text="Re-Password", show='*', width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        
        add_order_button = CTkButton(master=frame, width=20, height=30, text="ADD", font=("Arial", 40, 'bold'), fg_color="#2ED573", text_color="#000000", corner_radius=40)

        title.place(relx=0.5, rely=0.1, anchor=CENTER)

        employeeId.place(relx=0.5, rely=0.3, anchor=CENTER)
        employeeName.place(relx=0.5, rely=0.38, anchor=CENTER)
        employeeEmail.place(relx=0.5, rely=0.46, anchor=CENTER)
        employeeAddress.place(relx=0.5, rely=0.54, anchor=CENTER)
        employeeContact.place(relx=0.5, rely=0.62, anchor=CENTER)
        employeePassword.place(relx=0.5, rely=0.7, anchor=CENTER)
        employeeRePassword.place(relx=0.5, rely=0.78, anchor=CENTER)

        add_order_button.place(relx=0.5, rely=0.9, anchor=CENTER)

        frame.place(relx=0.5, rely=0.5, anchor=CENTER)
