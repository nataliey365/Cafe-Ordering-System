from os import name
from tkinter import*
import tkinter as ttk
import tkinter as tk
from tkinter import Entry

#Class
class Pocafe:
    def __init__(self,parent):

        px = 30
        py = 10
        
        self.account_dict = {"Name":[], "Age":[], "Email":["hi"], "Password":["hi"]}
        self.item_cart = []
        self.price_cart = []
        self.add_button_index = 0
        

        self.beverage_menu = ["Hot Chocolate", "Flat White", "Macchiato", "Mocha", "Milk Tea", "Cappuccino", "Americano", "Juice", 
        "Iced Chocolate", "Iced Tea", "Iced Coffee"]
        self.beverage_price = [5, 4, 4, 4, 5, 4, 4, 5, 6, 5, 6]
        self.breakfast_menu = ["French Toast", "Pancakes","Waffles", "Bacon and Eggs","English Breakfast", "Avocado Toast (VG, DF)", "Vegan Pancakes(VG, GF)"]
        self.breakfast_price = [15, 15.50, 16, 17.50, 19.50, 14, 15.50]
        self.lunch_menu = ["Green Salad (VE, GF, DF)", "Mushroom Burger (V, VG, GF,DF)", "Chicken Burger and Chips", "Veggie Burger and Chips (VE, DF)",
         "Fish Burger (V)", "Veggie Sandwich (VE, DF)", "Chicken Tenders and Chips", "Veggie Quiche (V,GF)", "Bacon Quiche"]
        self.lunch_price = [15, 16, 16, 16, 16, 15.50, 13, 14, 14]

        self.full_menu = self.beverage_menu + self.breakfast_menu + self.lunch_menu
        self.full_price = self.beverage_price + self.breakfast_price + self.lunch_price
    
#Homepage Frame
        self.welcome = tk.Frame(parent, bg = "white")
        self.welcome.grid(row = 0, column = 0)
        

        self.titleLabel = Label(self.welcome, text = "Welcome to Pocafe",
         bg = "light blue", fg = "white", width = 20, padx = px, pady = py, font = ("Time", "24", "bold"))
        self.titleLabel.grid(columnspan = 2)
        self.online = Label(self.welcome, text = "Online", bg = "light blue", fg = "white", width = 42, padx = px, pady = 5, font = ("Time", "12"))
        self.online.grid(columnspan = 2)

        self.description = Label(self.welcome, text = "Welcome to Pocafe Online! Fresh, tasty food available for pickup at your convinience. We have gluten free, dairy free, vegetarian and vegan options available too!.",
        fg = "#78517c", bg = "white", wraplength = 390, padx = 10, pady = 30, font = ("Time", "12"))
        self.description.grid(columnspan = 2)

    #Homepage buttons for signup/login
        self.signup_label = Label(self.welcome, text = "Don't have an account yet?", fg = "#f17950", bg = "white", font = ("Time", "12", "italic"))
        self.signup_label.grid(row = 4, columnspan = 2)

        self.signup_button = Button(self.welcome, text = "Sign Up", bg = "white", fg = "#78517c", height = "2", width = "30", command = self.show_signup)
        self.signup_button.grid(row = 5, columnspan = 2, pady = (0, 20))

        
        self.login_label = Label(self.welcome, text = "Already have an account?", fg = "#f17950", bg = "white", font = ("Time", "12", "italic"))
        self.login_label.grid(row = 6, columnspan = 2)

        self.login_button = Button(self.welcome, text = "Log In", bg = "white", fg = "#78517c", width = "30", height = "2", command = self.show_login)
        self.login_button.grid(row = 7, columnspan = 2, pady = (0, 35))

    #Sign up Frame 
        self.sign_up = tk.Frame(parent, bg = "white")
        self.sign_up.grid(row = 0, column = 1)
        self.sign_up.grid_remove()

        self.title_label = Label(self.sign_up, text = "Welcome to Pocafe",
         bg = "light blue", fg = "white", width = 20, padx = px, pady = py, font = ("Time", "24", "bold"))
        self.title_label.grid(columnspan = 2)
        self.online = Label(self.sign_up, text = "Sign Up", bg = "light blue", fg = "white", width = 45, padx = 30, pady = 5, font = ("Time", "12"))
        self.online.grid(columnspan = 10)

        self.signup_description = Label(self.sign_up, text = "Signing up to Pocafe online enables you to order delivery or pick up meals at your own convinience!",
        fg = "#78517c", bg = "white", wraplength = 390, padx = 10, pady = 20, font = ("Time", "12"))
        self.signup_description.grid(columnspan = 2)


    #Entry/Labels for Sign Up
        self.name = Label(self.sign_up, text = "Name", bg = "white", fg = "#f17950", width = 5, font = ("Time", "10"))
        self.name.grid(columnspan = 1, row = 4, padx = (0,20), sticky = W, pady = 5)

        self.name_entry = Entry(self.sign_up, bd = "2", width = "30")
        self.name_entry.grid(columnspan = 2, row = 4, pady = 5)

        self.age = Label(self.sign_up, text = "Age", bg = "white", fg = "#f17950", width = 4, font = ("Time", "10"))
        self.age.grid(columnspan = 1, row = 5, padx = (0,20), sticky = W, pady = 5)

        self.age_entry = Entry(self.sign_up, bd = "2", width = "30")
        self.age_entry.grid(columnspan = 2, row = 5, pady = 5)

        self.email = Label(self.sign_up, text = "Email", bg = "white", fg = "#f17950", width = 5, font = ("Time", "10"))
        self.email.grid(columnspan = 1, row = 6, padx = (0,20), sticky = W, pady = 5)

        self.email_entry = Entry(self.sign_up, bd = "2", width = "30")
        self.email_entry.grid(columnspan = 2, row = 6, pady = 5)

        self.password = Label(self.sign_up, text = "Password", bg = "white", fg = "#f17950", width = 8, font = ("Time", "10"))
        self.password.grid(columnspan = 1, row = 7, sticky = W, padx = (0,10))

        self.password_entry = Entry(self.sign_up, show = "*", bd = "2", width = "30")
        self.password_entry.grid(columnspan = 2, row = 7, pady = 5)

        self.confirm = Label(self.sign_up, text = "Confirm Password",  bg = "white", fg = "#f17950", width = 14, font = ("Time", "10"))
        self.confirm.grid(columnspan = 1, row = 8, padx = (0,10), sticky = W, pady = 5)

        self.confirm_entry = Entry(self.sign_up, bd = "2", show = "*",width = "30")
        self.confirm_entry.grid(columnspan = 2, row = 8, pady = 5)

    #Error Label
        self.error_label = Label(self.sign_up, text = "", anchor = W, bg = "white", fg = "red", width = "50")
        self.error_label.grid(row = 9)

    #Return and Sign Up Buttons
        self.signup_button = Button(self.sign_up, text = "Sign Up", bg = "white", fg = "#78517c", width = "10", height = "2", command = self.check_sign_up)
        self.signup_button.grid(row = 10, columnspan = 2,  pady = (0,5), padx = 10, sticky = E)
        self.signup_button.bind("<Return>", lambda event: self.check_sign_up())
        root.bind("<Return>", lambda event:self.check_sign_up())
    
        self.return_button = Button(self.sign_up, text = "Return", bg = "white", fg = "#78517c", width = "10", height = "2", command = self.show_home)
        self.return_button.grid(row = 10, columnspan = 2, pady = (0,5), padx = 10, sticky = W)

#Log In Screen
        self.log_in = tk.Frame(parent, bg = "white")
        self.log_in.grid(row = 0, column = 1)
        self.log_in.grid_remove()

        self.title_label = Label(self.log_in, text = "Welcome to Pocafe",
         bg = "light blue", fg = "white", width = 20, padx = px, pady = py, font = ("Time", "24", "bold"))
        self.title_label.grid(columnspan = 2)
        self.sub_title = Label(self.log_in, text = "Log In", bg = "light blue", fg = "white", width = 42, padx = px, pady = 5, font = ("Time", "12"))
        self.sub_title.grid(columnspan = 2)

        self.login_description = Label(self.log_in, text = "Log in to your Pocafe account to create an order with us!",
        fg = "#78517c", bg = "white", wraplength = 390, padx = 10, pady = 20, font = ("Time", "12"))
        self.login_description.grid(columnspan = 2, pady = (0,30))

        self.email_label = Label(self.log_in, text = "Email", bg = "white", fg = "#f17950", width = 10, font = ("Time", "12"))
        self.email_label.grid(columnspan = 1, row = 10, padx = 10, pady = 10, sticky = W)

        self.login_email_entry = Entry(self.log_in, bd = "2", width = "30")
        self.login_email_entry.grid(columnspan = 2, row = 10, padx = 10, pady = 10)

        self.login_password = Label(self.log_in, text = "Password", bg = "white", fg = "#f17950", width = 15, font = ("Time","12"))
        self.login_password.grid(columnspan = 1, row = 12, padx = (0,10), pady = 10, sticky = W)

        self.login_password_entry = Entry(self.log_in, show = "*", bd = "2", width = "30")
        self.login_password_entry.grid(columnspan = 2, row = 12, padx = 10, pady = 10)

        self.login_button = Button(self.log_in, text = "Log In", bg = "white", fg = "#78517c", width = "10", height = "2", command = self.check_log_in)
        self.login_button.grid(row = 15, columnspan = 2, pady = (30,5), padx = 10, sticky = E)
        

        self.home_button = Button(self.log_in, text = "Home", bg = "white", fg = "#78517c", width = "10", height = "2", command = self.show_home)
        self.home_button.grid(row = 15, columnspan = 2, pady = (30,5), padx = 10, sticky = W)

        
    #Error Label
        self.login_error_label = Label(self.log_in, text = "", anchor = W, bg = "white", fg = "red", width = "55", height = "3")
        self.login_error_label.grid(row = 13)

#Menu frame
        self.menu = tk.Frame(parent, bg = "white")
        self.menu.grid(row = 0, column = 1)
        self.menu.grid_remove()

        self.title_label = Label(self.menu, text = "Pocafe Menu",
         bg = "light blue", fg = "white", width = 20, padx = px, pady = py, font = ("Time", "24", "bold"))
        self.title_label.grid(columnspan = 2)
        self.sub_title = Label(self.menu, text = "Menu Options", bg = "light blue", fg = "white", width = 42, padx = px, pady = 5, font = ("Time", "12"))
        self.sub_title.grid(columnspan = 2)

        self.menu_description = Label(self.menu, text = "Press any menu item and the add button to add to your cart!",
        fg = "#78517c", bg = "white", wraplength = 420, padx = 10, pady = 5, font = ("Time", "12"))
        self.menu_description.grid(columnspan = 2)
        self.usermax = Label(self.menu, text = "Please note that you can order a max of 6 items.",
        fg = "#78517c", bg = "white", wraplength = 390, padx = 10, pady = 2, font = ("Time", "10"))
        self.usermax.grid(columnspan = 2)

        #Listbox for the menu which shows all the menu items, the price and a number
        self.items = Listbox(self.menu, bg ="white", width = 40, height = 8, fg = "#f17950", font = ("Time", "10"))
        for idx, (item, price) in enumerate(zip(self.full_menu, self.full_price)):
              self.items.insert(END, str(idx + 1) + ". " + str(item) + "      $" + str(price))
        self.items.grid(sticky = S, row = 4, pady = 10, padx = (30,10))
        self.scrollbar = Scrollbar(self.menu,command = self.items.yview)
        self.scrollbar.grid(sticky = N+S, row = 4, column = 1)
        self.items.config(yscrollcommand = self.scrollbar.set)

        #Success Label showing that it was successfully added to their cart
        self.success_label = Label(self.menu, text = "", bg = "white", fg = "red", width = "50", height = "2")
        self.success_label.grid(row = 9)

        
        self.home_button = Button(self.menu, text = "Home", bg = "white", fg = "#78517c", width = "10", height = "2", command = self.show_home)
        self.home_button.grid(row = 11, columnspan = 2, pady = (10,5), padx = 10, sticky = S+W)
        self.add_button = Button(self.menu, text = "Add", bg = "white", fg = "#78517c", width = "10", height = "2", command = self.add_cart)
        self.add_button.grid(row = 11, columnspan = 2, pady = (10,5), padx = 10, sticky = S)
        self.next_button = Button(self.menu, text = "Next", bg = "white", fg = "#78517c", width = "10", height = "2", command = self.show_receipt)
        self.next_button.grid(row = 11, columnspan = 2, pady = (10,5), padx = 10, sticky = S+E)

#Receipt Screen
        self.receipt = tk.Frame(parent, bg = "white")
        self.receipt.grid(row = 0, column = 1)
        self.receipt.grid_remove()

        self.title_label = Label(self.receipt, text = "Pocafe Menu",
         bg = "light blue", fg = "white", width = 20, padx = px, pady = py, font = ("Time", "24", "bold"))
        self.title_label.grid(columnspan = 2)
        self.sub_title = Label(self.receipt, text = "Receipt", bg = "light blue", fg = "white", width = 42, padx = px, pady = 5, font = ("Time", "12"))
        self.sub_title.grid(columnspan = 2)

        self.home_button = Button(self.receipt, text = "Exit", bg = "white", fg = "#78517c", width = "10", height = "2", command = quit)
        self.home_button.grid(row = 15, columnspan = 2, pady = (70,10), padx = 10, sticky = E)
       
#Log In Requirements and Check
    def check_log_in(self):

        
        try:
            #Checks for empty and non text entries in Email/Password
            if self.login_email_entry.get() == "":
                self.login_error_label.configure(text = " Please enter Email")
                self.login_email_entry.focus()
                self.login_email_entry.delete(0, END)
                self.login_email_entry.focus()
            elif self.login_password_entry.get() == "":
                self.login_error_label.configure(text = "Please enter a password")
                self.login_password_entry.focus()
            elif self.login_email_entry.get() in self.account_dict["Email"] and self.login_password_entry.get() in self.account_dict["Password"]:
                self.show_menu()
            else:
                self.login_error_label.configure(text = "Your username or password is wrong. If you don't have an account please go back to home and press sign up. If your username and password is wrong, please re-enter it.", 
                wraplength = 400)         
        except ValueError:
            self.login_error_label.configure(text = "Please enter a number")
        
#Sign Up Requirements and check
    def check_sign_up(self):


        saved_password = self.password_entry.get()
        attempt_password = self.confirm_entry.get()

       

        try:
            #Checks for empty and non text entries for Name
            if self.name_entry.get() == "":
                self.error_label.configure(text = " Please enter name")
                self.name_entry.focus()
            elif self.name_entry.get().isalpha() == False:
                self.error_label.configure(text = "Please enter text")
                self.name_entry.delete(0, END)
                self.name_entry.focus()
            #Checks age is over 16
            elif self.age_entry.get() == "":
                self.error_label.configure(text = "Please enter age")
                self.age_entry.focus()
            elif int(self.age_entry.get()) < 16:
                self.error_label.configure(text = "You are too young")
                self.age_entry.delete(0, END)
                self.age_entry.focus()
            elif self.email_entry.get() == "":
                self.error_label.configure(text = "Please enter an email")
                self.email_entry.focus()
            elif self.password_entry.get() == "":
                self.error_label.configure(text = "Please enter a password")
                self.password_entry.focus()
            elif self.confirm_entry.get() == "":
                self.error_label.configure(text = "Please confirm your password")
                self.password_entry.focus()
            elif saved_password != attempt_password:
                self.error_label.configure(text = "Your passwords do not match")
                self.password_entry.focus()
            else: 
                self.account_dict["Name"].append(self.name_entry.get())
                self.name_entry.delete(0,END)
                self.account_dict["Age"].append(self.age_entry.get())
                self.age_entry.delete(0,END)
                self.account_dict["Email"].append(self.email_entry.get())
                self.email_entry.delete(0,END)
                self.account_dict["Password"].append(self.password_entry.get())
                self.password_entry.delete(0,END)
                self.confirm_entry.delete(0,END)
                self.signup_button.unbind("<Return>")
                self.login_button.bind("<Return>", lambda event: self.show_login())
                root.bind("<Return>", lambda event:self.show_login())
                self.show_login()
        except ValueError:
            self.error_label.configure(text = "Please enter a number")
            self.age_entry.delete(0,END)
            self.age_entry.focus()

#Add to cart
    def add_cart(self):
        selected_item = self.items.curselection()
        try:
            item_index = int(selected_item[0])
            self.add_button_index += 1
            for idx, (item, price) in enumerate(zip(self.full_menu, self.full_price)):
                if self.add_button_index >= 6:
                    self.success_label.configure(wraplength = 300, text = "You have reached your max number of items in cart. Please press next to proceed to your receipt")
                    self.add_button["state"] = "disabled"
                elif int(item_index) == idx:
                    self.item_cart.append(item)
                    self.price_cart.append(price)
                    self.success_label.configure(text = "Successfully Added to Cart!")
        except:        
                    self.success_label.configure(text = "Please choose an item!")
                
class Frames(Pocafe):        
#Show home function
    def show_home(self):
        self.sign_up.grid_remove()
        self.welcome.grid()
        self.log_in.grid_remove()
        self.menu.grid_remove()  
        self.receipt.grid_remove()    
#Show sign up function
    def show_signup(self):
        self.welcome.grid_remove()
        self.log_in.grid_remove()
        self.menu.grid_remove()
        self.sign_up.grid()
        self.receipt.grid_remove()
        self.login_button.unbind("<Return>")
        self.signup_button.bind("<Return>", lambda event: self.check_sign_up())
        root.bind("<Return>", lambda event:self.check_sign_up())
#Show login function
    def show_login(self):
        self.welcome.grid_remove()
        self.sign_up.grid_remove()
        self.menu.grid_remove()
        self.log_in.grid()
        self.receipt.grid_remove()
        self.signup_button.unbind("<Return>")
        self.login_button.bind("<Return>", lambda event: self.check_log_in())
        root.bind("<Return>", lambda event:self.check_log_in())
#Show menu function
    def show_menu(self):
        self.welcome.grid_remove()
        self.log_in.grid_remove()
        self.sign_up.grid_remove()
        self.menu.grid()
        self.receipt.grid_remove()

#Show Menu funtion for the Recipt Page
    def back_menu(self):
        self.welcome.grid_remove()
        self.log_in.grid_remove()
        self.sign_up.grid_remove()
        self.menu.grid()
        self.receipt.grid_remove()
        self.order_label.destroy()
        self.return_button.destroy()
#Show receipt funtion as well as print completed receipt

    def show_receipt(self):
        self.welcome.grid_remove()
        self.log_in.grid_remove()
        self.sign_up.grid_remove()
        self.menu.grid_remove()
        self.receipt.grid()

        if not self.item_cart:
            self.order_label = Label(self.receipt, text = ("You have not ordered anything. If you would like to go back to the menu press the return button."), wraplength = 300, height = 8, bg = "white", fg = "#f17950", width = 40, font = ("Time", "12"))
            self.order_label.grid(columnspan = 2, row = 5, pady = 20)
            self.return_button = Button(self.receipt, text = "Return", bg = "white", fg = "#78517c", width = "10", height = "2", command = self.back_menu)
            self.return_button.grid(row = 15, columnspan = 2, pady = (60,1) , padx = 10, sticky = W)
        else:
            self.total_price = sum(self.price_cart) 
            self.order_label = Label(self.receipt, text = ("Your order items are \n {}".format(self.item_cart)), height = 5, wraplength = 300, bg = "white", fg = "#f17950", width = 40, font = ("Time", "12"))
            self.order_label.grid(columnspan = 2, row = 5, pady = 5)
            self.order_price = Label(self.receipt, text = ("Your total price is ${}".format(self.total_price)), height = 1, wraplength = 300, bg = "white", fg = "#f17950", width = 20, font = ("Time", "12"))
            self.order_price.grid(columnspan = 2, row = 6, pady = 5)
            self.order_finish = Label(self.receipt, text = ("We will let you know when your order is ready! Have a great day!"), height = 3, width = 40, wraplength = 300, bg = "white", fg = "#f17950", font = ("Time", "12"))
            self.order_finish.grid(columnspan = 2, row = 7)
        
        
        self.complete_order = ("Order items are {} \n".format(self.item_cart))

        with open('Receipts.txt', 'w') as f:
                f.write(self.complete_order)
                f.write('\n')
                
            



if __name__ == "__main__":
    root = Tk()
    frames = Frames(root)
    root.geometry("440x400+500+200")
    root.title("Pocafe Online")
    root.mainloop()