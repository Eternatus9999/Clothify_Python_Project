from customtkinter import *
class Cashier:
    def __init__(self):
        def back():
            root.destroy()
            import Main_Page
            Main_Page.MainPage()

        def add():
            import Add_Order
            Add_Order.AddOrder(frame)

        root = CTk()
        root.title("Clothify")

        root.geometry("1300x800")

        root.resizable(False, False)

        root.config(bg="#000000")

        frame = CTkFrame(master= root, width=1000, height=680, fg_color="#FFFFFF")

        add()

        title = CTkLabel(master=root, text="CLOTHIFY", font=("Luckiest Guy", 80, "bold"), fg_color="#000000", text_color="#00FFFF", bg_color="#000000")

        back_button = CTkButton(master=root,width=20, height=30, text="←", font=("Arial", 40, 'bold'), fg_color="#000000", text_color="#00FFFF", corner_radius=40, bg_color="#000000",  hover_color="gray", command=back)

        add_order_button = CTkButton(master=root, width=20, height=30, text="Add Order", font=("Arial", 28, 'bold'), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000", command = add)
        update_order_button = CTkButton(master=root, width=20, height=30, text="Update Order", font=("Arial", 22, 'bold'), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000")
        view_order_button = CTkButton(master=root, width=20, height=30, text="View Order", font=("Arial", 26, 'bold'), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000")

        title.place(relx=0.5, rely=0.05, anchor=CENTER)
        back_button.place(relx=0.1, rely=0.05, anchor=CENTER)
        frame.place(relx=0.6, rely=0.55, anchor=CENTER)

        add_order_button.place(relx=0.1, rely=0.2, anchor=CENTER)
        update_order_button.place(relx=0.1, rely=0.26, anchor=CENTER)
        view_order_button.place(relx=0.1, rely=0.32, anchor=CENTER)

        root.mainloop()

Cashier()