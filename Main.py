from customtkinter import *

root = CTk()

root.geometry("600X500")

root.config(bg="#000000")

register_button = CTkButton(master=root, text="Register", fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000")
login_button = CTkButton(master=root, text="Login", fg_color="#FFFFFF", text_color="#000000", corner_radius=40, bg_color="#000000")
title = CTkLabel(master=root, text="CLOTHIFY", font=("Arial", 50), fg_color="#000000", text_color="#00FFFF", bg_color="#000000")
register_button.place(relx=0.5, rely=0.5, anchor=CENTER)
title.place(relx=0.5, rely=0.3, anchor=CENTER)
login_button.place(relx=0.5, rely=0.6, anchor=CENTER)
root.mainloop()