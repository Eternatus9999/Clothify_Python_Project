from customtkinter import *
class Cashier:
    def __init__(self):
        def back():
            root.destroy()
            import Main_Page
            Main_Page.MainPage()

        def addOrder():
            import Add_Order
            Add_Order.AddOrder(frame)

        def addProduct():
            import Add_Product
            Add_Product.AddProduct(frame)

        def addSupplier():
            import Add_Supplier
            Add_Supplier.AddSupplier(frame)

        def updateProduct():
            import Update_Product
            Update_Product.UpdateProduct(frame)

        root = CTk()
        root.title("Clothify")

        root.geometry("1300x800+300+100")

        root.resizable(False, False)

        root.config(bg="#000000")

        frame = CTkFrame(master= root, width=1000, height=680, fg_color="#FFFFFF")

        addOrder()

        title = CTkLabel(master=root, text="CLOTHIFY", font=("Luckiest Guy", 80, "bold"), fg_color="#000000", text_color="#00FFFF", bg_color="#000000")

        back_button = CTkButton(master=root,width=20, height=30, text="←", font=("Arial", 40, 'bold'), fg_color="#000000", text_color="#00FFFF", corner_radius=40, bg_color="#000000",  hover_color="gray", command=back)

        add_order_button = CTkButton(master=root, width=225, height=30, text="Add Order", font=("Arial", 26, 'bold'), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000", command = addOrder)
        update_order_button = CTkButton(master=root, width=225, height=30, text="Update Order", font=("Arial", 26, 'bold'), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000")
        view_order_button = CTkButton(master=root, width=225, height=30, text="View Order", font=("Arial", 26, 'bold'), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000")
        
        add_product_button = CTkButton(master=root, width=225, height=30, text="Add Product", font=("Arial", 26, 'bold'), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000", command = addProduct)
        update_product_button = CTkButton(master=root, width=20, height=30, text="Update Product", font=("Arial", 26, 'bold'), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000", command= updateProduct)
        view_product_button = CTkButton(master=root, width=225, height=30, text="View Product", font=("Arial", 26, 'bold'), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000")
        
        add_supplier_button = CTkButton(master=root, width=225, height=30, text="Add Supplier", font=("Arial", 26, 'bold'), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000", command= addSupplier)
        update_supplier_button = CTkButton(master=root, width=225, height=30, text="Update Supplier", font=("Arial", 26, 'bold'), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000")
        view_supplier_button = CTkButton(master=root, width=225, height=30, text="View Supplier", font=("Arial", 26, 'bold'), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000")

        annual_report_button = CTkButton(master=root, width=225, height=30, text="Annual Report", font=("Arial", 26, 'bold'), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000")
        monthly_report_button = CTkButton(master=root, width=225, height=30, text="Monthly Report", font=("Arial", 26, 'bold'), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000")
        daily_report_button = CTkButton(master=root, width=225, height=30, text="Daily Report", font=("Arial", 26, 'bold'), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000")

        title.place(relx=0.5, rely=0.06, anchor=CENTER)
        back_button.place(relx=0.1, rely=0.05, anchor=CENTER)
        frame.place(relx=0.6, rely=0.55, anchor=CENTER)

        add_order_button.place(relx=0.1, rely=0.2, anchor=CENTER)
        update_order_button.place(relx=0.1, rely=0.26, anchor=CENTER)
        view_order_button.place(relx=0.1, rely=0.32, anchor=CENTER)

        add_product_button.place(relx=0.1, rely=0.4, anchor=CENTER)
        update_product_button.place(relx=0.1, rely=0.46, anchor=CENTER)
        view_product_button.place(relx=0.1, rely=0.52, anchor=CENTER)

        add_supplier_button.place(relx=0.1, rely=0.6, anchor=CENTER)
        update_supplier_button.place(relx=0.1, rely=0.66, anchor=CENTER)
        view_supplier_button.place(relx=0.1, rely=0.72, anchor=CENTER)

        annual_report_button.place(relx=0.1, rely=0.8, anchor=CENTER)
        monthly_report_button.place(relx=0.1, rely=0.86, anchor=CENTER)
        daily_report_button.place(relx=0.1, rely=0.92, anchor=CENTER)

        root.mainloop()
