from customtkinter import *
class Chashier:
    def __init__(self):
        # self.master = master

        root = CTk()
        root.title("Clothify")

        root.geometry("1400x800")

        root.resizable(False, False)

        root.config(bg="#000000")

        def back():
            root.destroy()
            import Main_Page
            Main_Page.MainPage()

        frame = CTkFrame(master= root, width=1000, height=680, fg_color="#FFFFFF")

        title = CTkLabel(master=root, text="CLOTHIFY", font=("Luckiest Guy", 80, "bold"), fg_color="#000000", text_color="#00FFFF", bg_color="#000000")

        back_button = CTkButton(master=root,width=20, height=30, text="←", font=("Arial", 40, 'bold'), fg_color="#000000", text_color="#00FFFF", corner_radius=40, bg_color="#000000",  hover_color="gray", command=back)

        title.place(relx=0.5, rely=0.05, anchor=CENTER)
        back_button.place(relx=0.1, rely=0.05, anchor=CENTER)
        frame.place(relx=0.63, rely=0.55, anchor=CENTER)

        root.mainloop()


