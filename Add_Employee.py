from customtkinter import *
from tkinter import messagebox

import DatabaseConnector
import Encryptor

class AddEmployee:
    def __init__(self,root):

        self.employee_id = StringVar(value = "EM"+str(DatabaseConnector.getEmployeeId()+1))

        frame = CTkFrame(master= root, width=1000, height=680, fg_color="#A09E9E")

        title = CTkLabel(master=frame, text="Add Employee", font=("Arial", 80, 'bold'), fg_color="#A09E9E", text_color="#000000")

        self.employeeId = CTkEntry(master = frame, textvariable = self.employee_id, width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40, state = "readonly")
        self.employeeName = CTkEntry(master = frame, placeholder_text="Name", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        self.employeeEmail = CTkEntry(master = frame, placeholder_text="Email", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        self.employeeAddress = CTkEntry(master = frame, placeholder_text="Address", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        self.employeeContact = CTkEntry(master = frame, placeholder_text="Contact", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        self.employeePassword = CTkEntry(master = frame, placeholder_text="Password", show='*', width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        self.employeeRePassword = CTkEntry(master = frame, placeholder_text="Re-Password", show='*', width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        
        add_employee_button = CTkButton(master=frame, width=20, height=30, text="ADD", font=("Arial", 40, 'bold'), fg_color="#2ED573", text_color="#000000", corner_radius=40, command=self.addEmployee)

        title.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.employeeId.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.employeeName.place(relx=0.5, rely=0.38, anchor=CENTER)
        self.employeeEmail.place(relx=0.5, rely=0.46, anchor=CENTER)
        self.employeeAddress.place(relx=0.5, rely=0.54, anchor=CENTER)
        self.employeeContact.place(relx=0.5, rely=0.62, anchor=CENTER)
        self.employeePassword.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.employeeRePassword.place(relx=0.5, rely=0.78, anchor=CENTER)

        add_employee_button.place(relx=0.5, rely=0.9, anchor=CENTER)

        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def addEmployee(self):
        if(self.employeeName.get() == "" or self.employeeEmail.get() == "" or self.employeeAddress.get() == "" or self.employeeContact.get() == "" or self.employeePassword.get() == "" or self.employeeRePassword.get() == ""):
            messagebox.showerror("Error", "All fields are required")
        elif(self.employeePassword.get() == self.employeeRePassword.get()):
            DatabaseConnector.insertEmployee(self.employeeId.get(), self.employeeName.get(), self.employeeEmail.get(), self.employeeAddress.get(), self.employeeContact.get(), Encryptor.encrypt(self.employeePassword.get()))
            messagebox.showinfo("Success", "Employee added successfully")
            self.employeeName.delete(0, END)
            self.employeeEmail.delete(0, END)
            self.employeeAddress.delete(0, END)
            self.employeeContact.delete(0, END)
            self.employeePassword.delete(0, END)
            self.employeeRePassword.delete(0, END)
            self.employeeId.configure(textvariable = StringVar(value = "EM"+str(DatabaseConnector.getEmployeeId()+1)))
        else:
            messagebox.showerror("Error", "Password does not match")

    
