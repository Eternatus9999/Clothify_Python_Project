from customtkinter import *
class Cashier:
    def __init__(self):

        self.root = CTk()
        self.root.title("Clothify")

        self.root.geometry("1300x800+300+100")

        self.root.resizable(False, False)

        self.root.config(bg="#000000")

        self.frame = CTkFrame(master= self.root, width=1000, height=680, fg_color="#FFFFFF")

        self.addOrder()

        title = CTkLabel(master=self.root, text="CLOTHIFY", font=("Luckiest Guy", 80, "bold"), fg_color="#000000", text_color="#00FFFF", bg_color="#000000")

        back_button = CTkButton(master=self.root,width=20, height=30, text="←", font=("Arial", 40, 'bold'), fg_color="#000000", text_color="#00FFFF", corner_radius=40, bg_color="#000000",  hover_color="gray", command= self.back)

        add_order_button = CTkButton(master=self.root, width=225, height=30, text="Add Order", font=("Arial", 26, 'bold'), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000", command = self.addOrder)
        view_order_button = CTkButton(master=self.root, width=225, height=30, text="View Order", font=("Arial", 26, 'bold'), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000", command= self.viewOrder)
        
        add_product_button = CTkButton(master=self.root, width=225, height=30, text="Add Product", font=("Arial", 26, 'bold'), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000", command = self.addProduct)
        update_product_button = CTkButton(master=self.root, width=20, height=30, text="Update Product", font=("Arial", 26, 'bold'), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000", command= self.updateProduct)
        view_product_button = CTkButton(master=self.root, width=225, height=30, text="View Product", font=("Arial", 26, 'bold'), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000", command= self.viewProduct)
        
        add_supplier_button = CTkButton(master=self.root, width=225, height=30, text="Add Supplier", font=("Arial", 26, 'bold'), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000", command= self.addSupplier)
        update_supplier_button = CTkButton(master=self.root, width=225, height=30, text="Update Supplier", font=("Arial", 26, 'bold'), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000", command= self.updateSupplier)
        view_supplier_button = CTkButton(master=self.root, width=225, height=30, text="View Supplier", font=("Arial", 26, 'bold'), fg_color="#00FFFF", text_color="#000000", corner_radius=40, bg_color="#000000", command= self.viewSupplier)

        title.place(relx=0.5, rely=0.06, anchor=CENTER)
        back_button.place(relx=0.1, rely=0.05, anchor=CENTER)
        self.frame.place(relx=0.6, rely=0.55, anchor=CENTER)

        add_order_button.place(relx=0.1, rely=0.2, anchor=CENTER)
        view_order_button.place(relx=0.1, rely=0.26, anchor=CENTER)

        add_product_button.place(relx=0.1, rely=0.34, anchor=CENTER)
        update_product_button.place(relx=0.1, rely=0.4, anchor=CENTER)
        view_product_button.place(relx=0.1, rely=0.46, anchor=CENTER)

        add_supplier_button.place(relx=0.1, rely=0.54, anchor=CENTER)
        update_supplier_button.place(relx=0.1, rely=0.6, anchor=CENTER)
        view_supplier_button.place(relx=0.1, rely=0.66, anchor=CENTER)

        self.root.mainloop()

    def back(self):
        self.root.destroy()
        import Main_Page
        Main_Page.MainPage()

    def addOrder(self):
        import Add_Order
        Add_Order.AddOrder(self.frame)

    def addProduct(self):
        import Add_Product
        Add_Product.AddProduct(self.frame)

    def addSupplier(self):
        import Add_Supplier
        Add_Supplier.AddSupplier(self.frame)

    def updateProduct(self):
        import Update_Product
        Update_Product.UpdateProduct(self.frame)

    def updateSupplier(self):
        import Update_Supplier
        Update_Supplier.UpdateSupplier(self.frame)
        
    def viewProduct(self):
        import View_Product
        View_Product.ViewProduct(self.frame)

    def viewSupplier(self):
        import View_Supplier
        View_Supplier.ViewSupplier(self.frame)

    def viewOrder(self):
        import View_Order
        View_Order.ViewOrder(self.frame)
