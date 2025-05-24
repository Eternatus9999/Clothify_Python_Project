from customtkinter import *
class Chashier:
    def __init__(self):

        def back():
            root.destroy()
            import Main_Page
            Main_Page.MainPage()
        
        def clicked():
            frame.configure(fg_color="#FF0000")

        def clicked2():
            frame.configure(fg_color="#00FF00")

        root = CTk()
        root.title("Clothify")

        root.geometry("1400x800")

        root.resizable(False, False)

        root.config(bg="#000000")

        frame = CTkFrame(master= root, width=1000, height=680, fg_color="#FFFFFF")

        title = CTkLabel(master=root, text="CLOTHIFY", font=("Luckiest Guy", 80, "bold"), fg_color="#000000", text_color="#00FFFF", bg_color="#000000")

        back_button = CTkButton(master=root,width=20, height=30, text="←", font=("Arial", 40, 'bold'), fg_color="#000000", text_color="#00FFFF", corner_radius=40, bg_color="#000000",  hover_color="gray", command=back)

        test_button = CTkButton(master=root,width=20, height=30, text="Test", font=("Arial", 40, 'bold'), fg_color="#000000", text_color="#00FFFF", corner_radius=40, bg_color="#000000",  hover_color="gray", command=clicked)
        test1_button = CTkButton(master=root,width=20, height=30, text="Test", font=("Arial", 40, 'bold'), fg_color="#000000", text_color="#00FFFF", corner_radius=40, bg_color="#000000",  hover_color="gray", command=clicked2)

        title.place(relx=0.5, rely=0.05, anchor=CENTER)
        back_button.place(relx=0.1, rely=0.05, anchor=CENTER)
        frame.place(relx=0.63, rely=0.55, anchor=CENTER)
        test_button.place(relx=0.5, rely=0.5, anchor=CENTER)
        test1_button.place(relx=0.5, rely=0.7, anchor=CENTER)

        root.mainloop()

