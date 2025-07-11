from customtkinter import *
from tkinter import messagebox

import DatabaseConnector

class UpdateEmployee:
    def __init__(self,root):

        frame = CTkFrame(master= root, width=1000, height=680, fg_color="#A09E9E")

        title = CTkLabel(master=frame, text="Update Employee", font=("Arial", 80, 'bold'), fg_color="#A09E9E", text_color="#000000")

        self.employees = self.Convert(DatabaseConnector.getEmployeeIds())

        self.employeeId = CTkComboBox(master = frame, values = self.employees, width=300, height=50, fg_color="#FFFFFF", text_color="#000000", button_color= "#00FFFF", font=("Arial", 20), corner_radius=40)
        self.employeeName = CTkEntry(master = frame, placeholder_text="Name", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        self.employeeEmail = CTkEntry(master = frame, placeholder_text="Email", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        self.employeeAddress = CTkEntry(master = frame, placeholder_text="Address", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        self.employeeContact = CTkEntry(master = frame, placeholder_text="Contact", width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        self.employeePassword = CTkEntry(master = frame, placeholder_text="Password", show='*', width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        self.employeeRePassword = CTkEntry(master = frame, placeholder_text="Re-Password", show='*', width=300, height=50, fg_color="#FFFFFF", text_color="#000000", font=("Arial", 20), corner_radius=40)
        
        update_employee_button = CTkButton(master=frame, width=20, height=30, text="Update", font=("Arial", 40, 'bold'), fg_color="#FFA502", text_color="#000000", corner_radius=40, command = self.updateEmployee)
        
        search = CTkButton(master=frame, width=100, text="Search", font=("Arial", 30, 'bold'), fg_color="#3742FA", text_color="#000000", corner_radius=40, command=self.search)

        title.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.employeeId.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.employeeName.place(relx=0.5, rely=0.38, anchor=CENTER)
        self.employeeEmail.place(relx=0.5, rely=0.46, anchor=CENTER)
        self.employeeAddress.place(relx=0.5, rely=0.54, anchor=CENTER)
        self.employeeContact.place(relx=0.5, rely=0.62, anchor=CENTER)
        self.employeePassword.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.employeeRePassword.place(relx=0.5, rely=0.78, anchor=CENTER)

        update_employee_button.place(relx=0.5, rely=0.9, anchor=CENTER)
        search.place(relx=0.75, rely=0.3, anchor=CENTER)

        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def search(self):
        employee = DatabaseConnector.getEmployee(self.employeeId.get())

        self.employeeName.delete(0, END)
        self.employeeEmail.delete(0, END)
        self.employeeAddress.delete(0, END)
        self.employeeContact.delete(0, END)
        self.employeePassword.delete(0, END)
        self.employeeRePassword.delete(0, END)

        self.employeeName.insert(0, employee[1])
        self.employeeEmail.insert(0, employee[2])
        self.employeeAddress.insert(0, employee[3])
        self.employeeContact.insert(0, employee[4])
        self.employeePassword.insert(0, employee[5])
        self.employeeRePassword.insert(0, employee[5])

    def updateEmployee(self):
        if(self.employeePassword.get() == self.employeeRePassword.get()):
            DatabaseConnector.updateEmployee(self.employeeId.get(),self.employeeName.get(),self.employeeEmail.get(),self.employeeAddress.get(),self.employeeContact.get(),self.employeePassword.get())
            messagebox.showinfo("Success", "Employee updated successfully")
            self.employeeName.delete(0, END)
            self.employeeEmail.delete(0, END)
            self.employeeAddress.delete(0, END)
            self.employeeContact.delete(0, END)
            self.employeePassword.delete(0, END)
            self.employeeRePassword.delete(0, END)
        else:
            messagebox.showerror("Error", "Password does not match")

    def Convert(self, list1): 
        list2 = [] 
        for x in list1: 
            list2.append(x[0]) 
        return list2
