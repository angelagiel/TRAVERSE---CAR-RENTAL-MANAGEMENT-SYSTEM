from tkinter import *
from tkinter import messagebox
import tkinter as tk 
import database_handler
from tkinter import ttk
import models
import random
from database_handler import DBHandler
import re 
from datetime import datetime, timedelta
from PIL import Image, ImageTk

class LoginPage(tk.Frame): 
    def __init__(self, master): 
        tk.Frame.__init__(self, master)
        self.parent = master
        self.configure(bg='white')
        self.failed_login_attempts = {}
        self.locked_accounts = {}
        
         #----- TRAVERSE LOGO
        logo = Image.open("3traverse logo.png")
        logo = logo.resize((250, 250))
        self.logo = ImageTk.PhotoImage(logo)
        
        tk.Label(self, image=self.logo, bg='white').grid(row=0, column=0, sticky='nsew', padx=(450,0), pady=(0,0))
        
        #----- HEADING PAGE TITLE
        self.heading = tk.Label(self, text='Log in', fg='#4caf50', font=('Inter', 40, ''), bg='white')
        self.heading.grid(row=1, column=0, padx=(470,0), pady=(0,0))
        
        #----- ACCOUNT TYPE
        self.account_type = tk.StringVar()
        self.account_type.set("Admin")
        
        self.admin_radio = tk.Radiobutton(self, text="Admin", variable=self.account_type, value="admin", width=6, bg='white', command=self.hide_customer_widgets)
        self.admin_radio.grid(row=2, column=0, padx=(370,0))
        
        self.customer_radio = tk.Radiobutton(self, text="Customer", variable=self.account_type, value="customer", width=6, bg='white', command=self.toggle_customer_widgets)
        self.customer_radio.grid(row=2, column=0, padx=(520,0))
        #----- NAME FIELDS
        self.name_field = tk.Entry(self, width=45, fg='black', border=0, font=('Inter', 11))
        self.name_field.grid(row=3, column=0, padx=(500, 0), pady=(0,0))
        self.name_field.insert(0, 'Name')
        tk.Frame(self, width=350, height=2, bg='black').grid(row=3, column=0, pady=(40, 0), padx=(470,0))
        self.name_field.bind('<FocusIn>', self.on_enter)
        self.name_field.bind('<FocusOut>', self.on_leave)

        #----- PASSWORD FIELDS
        self.code_field = tk.Entry(self, width=45, fg='black', border=0, font=('Inter', 11))
        self.code_field.grid(row=4, column=0, padx=(500, 0), pady=(0,0))
        self.code_field.insert(0, "Password")
        tk.Frame(self, width=350, height=2, bg='black').grid(row=4, column=0, pady=(40, 0), padx=(470,0))
        self.code_field.bind('<FocusIn>', self.on_enter)
        self.code_field.bind('<FocusOut>', self.on_leave)

        #----- SIGNIN BUTTON
        self.signin_button = tk.Button(self, width=47, pady=7, text='Sign in', bg='#4caf50', fg='white', border=0, command=self.login_clicked)
        self.signin_button.grid(row=5, column=0, pady=(20,0), padx=(480,0))
        
        #------- For Customer Widgets
        self.label = tk.Label(self, text="New to our services?", fg='black', bg='white', font=('Inter', 9))

        #-----SIGNUP BUTTON 
        self.signup_btn = tk.Button(self, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#4caf50', command=self.go_to_signup_page)
        
        #----- CAPTCHA SECTION
        
        self.captcha = tk.Label(self, width=25, height=4, fg='#4caf50', font=('Roboto', 15, 'italic'), border=1)
        self.label_captcha = tk.Label(self, text='To continue, type the characters you see in the picture.', bg='white')
        self.entry_captcha = tk.Entry(self, width=53, fg='black', border=1)
        self.button_captcha = tk.Button(self, text="Submit", width=12, cursor='hand2', bg='#4caf50', command=self.login)
        
        self.hide_customer_widgets()
        self.hide_captcha_section()

    def hide_customer_widgets(self): 
        self.label.grid_forget()
        self.signup_btn.grid_forget()

    def show_customer_widgets(self): 
        self.label.grid(row=6,column=0, padx=(400, 0), pady=(10,0))
        self.signup_btn.grid(row=6, column=0, padx=(580,0), pady=(10, 0))
        
    def toggle_customer_widgets(self): 
        self.hide_captcha_section()
        if self.account_type.get() == "customer": 
            self.on_return()
            self.show_customer_widgets()
        else: 
            self.hide_customer_widgets()
            self.on_return()
    
    def login_clicked(self): 
        self.hide_customer_widgets()
        if self.name_field.get() != '' and self.code_field.get() != '': 
            self.toggle_captcha_section()
        elif self.name_field.get() == '' or self.code_field.get() == '': 
            messagebox.showerror("Error", "Name and Password are Required")
    
    def show_captcha_section(self): 
        self.captcha.grid(row=7, column=0, padx=(470,0), pady=(10,0))
        self.label_captcha.grid(row=8, column=0, padx=(470,0), pady=(10,0))
        self.entry_captcha.grid(row=9, column=0, padx=(470,0), pady=(10,0))
        self.button_captcha.grid(row=10, column=0, padx=(470,0), pady=(10,0))

    def hide_captcha_section(self): 
        self.captcha.grid_forget()
        self.label_captcha.grid_forget()
        self.entry_captcha.grid_forget()
        self.button_captcha.grid_forget()
    
    def toggle_captcha_section(self): 
        self.show_captcha_section()
        self.generate_captcha()
        
    def generate_captcha(self): 
        self.entry_captcha.delete(0, 'end')
        captcha_text = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=6))
        self.captcha.config(text=captcha_text)
        
    def check_captcha(self):
        entered_captcha = self.entry_captcha.get()
        captcha_text = self.captcha.cget("text")
        if entered_captcha == captcha_text:
            return True
        else:
            messagebox.showerror("Error", "Captcha didn't match!")
            self.entry_captcha.delete(0, 'end')
            self.generate_captcha()
            return False
    
    def on_enter(self, e): 
        widget = e.widget
        widget.delete(0, 'end')
        
    def on_leave(self, e):
        widget = e.widget
        name = widget.get()
        if name == '':
            widget.insert(0, 'Name' if widget == self.name_field else 'Password')
    
    def on_return(self):
        self.name_field.delete(0, tk.END)
        self.code_field.delete(0, tk.END)

        self.name_field.insert(0, 'Name')
        self.code_field.insert(0, 'Password')
    
    def login(self): 
        name = self.name_field.get()
        password = self.code_field.get()
        account_type = self.account_type.get()
        
        if self.is_account_locked(name): 
            messagebox.showerror('Account Locked', "Your account is locked. Please try again later.")
            return

        db_handler = DBHandler()
        accounts = db_handler.read_accounts()

        for account in accounts:
            if account.name == name and account.password == password:
                if self.check_captcha():  # Corrected the function call
                    if account_type == 'admin':
                        messagebox.showinfo("Welcome!", "Login Successful. Hello, admin!")
                        self.go_to_admin_dashboard()
                    elif account_type == 'customer':
                        messagebox.showinfo("Welcome!", "Login Successful. Hello, customer!")
                        customer_id = account.id  # Fetch the ID of the logged-in customer
                        self.reset_failed_attempts(name)
                        self.go_to_customer_window(customer_id)  # Pass customer ID to CustomerWindow
                        
                    self.hide_captcha_section()
                    self.hide_customer_widgets()
                    self.account_type.set("None")
                    db_handler.close()
                    # self.on_return()
                    return
           
                else: 
                    self.record_failed_attempt(name)
                    return
        messagebox.showerror('Invalid', 'Invalid name or password')
       
        
    def record_failed_attempt(self, name): 
        if name in self.failed_login_attempts: 
            self.failed_login_attempts[name] += 1
        else: 
            self.failed_login_attempts[name] = 1
            
        if self.failed_login_attempts[name] >= 3: 
            self.lock_account(name)

    def lock_account(self, name):
        self.failed_login_attempts[name] = -1
        self.locked_accounts[name] = datetime.now() + timedelta(minutes=1)
        messagebox.showerror('Account Locked', 'Your account is locked. Please try again later.')  
        self.on_return()
        self.hide_captcha_section()
        self.account_type.set("None")
        
    
    def is_account_locked(self, name):
        if name in self.failed_login_attempts and self.failed_login_attempts[name] == -1:
            if name in self.locked_accounts:
                if datetime.now() < self.locked_accounts[name]:  # Check if it's still within the lock time
                    # self.on_return()
                    self.hide_captcha_section()
                    self.hide_customer_widgets()
                    self.account_type.set("None")
                    return True
                else:
                    del self.failed_login_attempts[name]  # Unlock the account
                    del self.locked_accounts[name]  # Remove from locked accounts
                    messagebox.showinfo('Account Unlocked', 'Your account has been automatically unlocked.')
                    
        return False
    
    def reset_failed_attempts(self, name):
        if name in self.failed_login_attempts:
            del self.failed_login_attempts[name]
    
    def go_to_signup_page(self): 
        self.parent.change_window('Signup_Page')
    
    def go_to_admin_dashboard(self):
        self.parent.change_window('Admin_Dashboard')
    
    def go_to_customer_window(self, customer_id): 
        self.parent.change_window('Customer_Window', customer_id=customer_id)
    

class SignupPage(tk.Frame): 
    def __init__(self, master): 
        tk.Frame.__init__(self, master)
        self.parent = master
        self.configure(bg='white')
        
         #----- TRAVERSE LOGO
        logo = Image.open("3traverse logo.png")
        logo = logo.resize((250, 250))
        self.logo = ImageTk.PhotoImage(logo)
        
        tk.Label(self, image=self.logo, bg='white').grid(row=0, column=0, sticky='nsew', padx=(340,20), pady=(0,0))
        
        #----- HEADING PAGE TITLE
        self.heading = tk.Label(self, text='Sign up', fg='#4caf50', font=('Inter', 40, ''), bg='white')
        self.heading.grid(row=1, column=0, padx=(470,150), pady=(0,50))
        
          # Name
        self.name_field = Entry(self, width=20, border=0, fg='black', bg='white', font=('Microsoft yahei UI Light', 11))
        self.name_field.grid(row=3, column=0,pady=(0, 40), padx=(0, 60))
        self.name_field.insert(0, 'Name')
        self.name_field.bind('<FocusIn>', self.on_enter)
        self.name_field.bind('<FocusOut>', self.on_leave)
        Frame(self, width=250, height=2, bg='black').grid(row=3, column=0)

        # License Number
        self.license_field = Entry(self, width=20, border=0, fg='black', bg='white', font=('Microsoft yahei UI Light', 11))
        self.license_field.grid(row=3, column=0, pady=(0, 40), padx=(600, 60))
        self.license_field.insert(0, "Driver's License Number")
        self.license_field.bind('<FocusIn>', self.on_enter)
        self.license_field.bind('<FocusOut>', self.on_leave)
        Frame(self, width=250, height=2, bg='black').grid(row=3, column=0, padx=(600,0))

        # Contact Number
        self.contact_field = Entry(self, width=20, border=0, fg='black', bg='white', font=('Microsoft Yahei UI Light', 11))
        self.contact_field.grid(row=4, column=0,pady=(0, 40), padx=(0, 60))
        self.contact_field.insert(0, 'Contact Number')
        self.contact_field.bind('<FocusIn>', self.on_enter)
        self.contact_field.bind('<FocusOut>', self.on_leave)
        Frame(self, width=250, height=2, bg='black').grid(row=4, column=0)

        # Email
        self.email_field = Entry(self, width=20, border=0, fg='black', bg='white', font=('Microsoft Yahei UI Light', 11))
        self.email_field.grid(row=4, column=0, pady=(0, 40), padx=(600, 60))
        self.email_field.insert(0, 'Email Address')
        self.email_field.bind('<FocusIn>', self.on_enter)
        self.email_field.bind('<FocusOut>', self.on_leave)
        Frame(self, width=250, height=2, bg='black').grid(row=4, column=0, padx=(600,0))

        # Password
        self.code_field = Entry(self, width=20, border=0, fg='black', bg='white', font=('Microsoft Yahei UI Light', 11))
        self.code_field.grid(row=6, column=0,pady=(0, 40), padx=(0, 60))
        self.code_field.insert(0, 'Password')
        self.code_field.bind('<FocusIn>', self.on_enter)
        self.code_field.bind('<FocusOut>', self.on_leave)
        Frame(self, width=250, height=2, bg='black').grid(row=6, column=0)

        # Confirm Password
        self.confirm_field = Entry(self, width=15, border=0, fg='black', bg='white', font=('Microsoft Yahei UI Light', 11))
        self.confirm_field.grid(row=6, column=0, pady=(0, 40), padx=(580, 80))
        self.confirm_field.insert(0, 'Confirm Password')
        self.confirm_field.bind('<FocusIn>', self.on_enter)
        self.confirm_field.bind('<FocusOut>', self.on_leave)
        Frame(self, width=250, height=2, bg='black').grid(row=6, column=0, padx=(600,0))

        # Button 
        self.signup_button = Button(self, width=45, pady=7, text='Sign Up', 
        bg='#4caf50', fg='#fff', border=0, command=self.signup)
        self.signup_button.grid(row=8, column=0, padx=(350,0))

        self.label = tk.Label(self, text='Already a member?', fg='black', bg='white', font=('Inter', 9))
        self.label.grid(row=9, column=0, pady=(40,0), padx=(300,50))

        self.signin_button = Button(self, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#4caf50', command=self.go_to_login_page)
        self.signin_button.grid(row=9, column=0, pady=(40,0), padx=(500, 50))

#------ FUNCTIONS
    def on_enter(self, e):
        widget = e.widget
        widget.delete(0, 'end')

    def on_leave(self, e):
        widget = e.widget
        if widget.get() == '':
            if widget == self.name_field:
                widget.insert(0, 'Name')
            elif widget == self.license_field:
                widget.insert(0, "Driver's License Number")
            elif widget == self.contact_field:
                widget.insert(0, 'Contact Number')
            elif widget == self.email_field:
                widget.insert(0, 'Email Address')
            elif widget == self.code_field:
                widget.insert(0, 'Password')
            elif widget == self.confirm_field:
                widget.insert(0, 'Confirm Password')
                
    def validate_name(self, name): 
        if len(name) >= 6: 
            return True
    
    def validate_email(self, email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))
           
    def validate_license(self, license_number):
        pattern = r'^[A-Z]{2}\d{1}-\d{2}-\d{6}$'
        return bool(re.match(pattern, license_number))
    
    def validate_password(self, password):
        if not 8 <= len(password) <= 12: # >8 characters and <=12
            return False

        if not re.search(r'[A-Z]', password): #1 uppercase letter
            return False

        if not re.search(r'[a-z]', password): #  1 lowercase letter
            return False

        if not re.search(r'[0-9]', password): #1 number
            return False

        if not re.search(r'[!@#$%^&*()-+=]', password): # 1 special character
            return False

        return True     # All conditions passed

    def validate_contact_number(self, contact_number):
        pattern = r'^09\d{9}$'
        return bool(re.match(pattern, contact_number))

    def signup(self):
        name = self.name_field.get()
        email = self.email_field.get()
        license_number = self.license_field.get()
        contact_number = self.contact_field.get()
        password = self.code_field.get()
        confirm_password = self.confirm_field.get()
        
        if not name or not email or not password or not confirm_password or not contact_number or not license_number:
            messagebox.showerror("Empty Fields", "Please fill in all the required fields.")
            return
        
        if not self.validate_name(name): 
            messagebox.showerror("Invalid Name", "Name must containe atleast 6 characters.")
            return
        
        if not self.validate_license(license_number):
            messagebox.showerror("Invalid Driver's License Number", "Traverse Car Rental does not permit the use of invalid driver's license numbers.")
            return
        
        if not self.validate_contact_number(contact_number):
            messagebox.showerror("Invalid Contact Number", "Invalid Contact Number. Please try again.")
            return
        
        if not self.validate_email(email):
            messagebox.showerror("Invalid Email Address", "Invalid email format. Please use a valid email address")
            return
        
        if not self.validate_password(password):
            messagebox.showerror("Invalid Password", "Must contain at least 8 characters.\nAt least 1 uppercase letter.\nAt least 1 lowercase letter.\nAt least 1 number.\nAt least 1 special character.")
            return
        
        if password != confirm_password:
            messagebox.showerror("Passwords Do Not Match", "Password and Confirm Password fields do not match.")
            return
        
        try:
            new_customer = models.Accounts()
            new_customer.account_type = 'customer'
            new_customer.name = name
            new_customer.email = email
            new_customer.contact = int(contact_number)
            new_customer.password = password
            new_customer.license_number = license_number

            db_conn = database_handler.DBHandler()
            db_conn.add_customer(new_customer)
            db_conn.close()
            
            messagebox.showinfo("Congratulations!", "You are now registered in the system. Please Sign in.")
            
            self.on_return()
            self.go_to_login_page()
            
        except ValueError:
            pass
                     
    def on_return(self):
        self.name_field.delete(0, tk.END)
        self.email_field.delete(0, tk.END)
        self.contact_field.delete(0, tk.END)
        self.code_field.delete(0, tk.END)
        self.confirm_field.delete(0, tk.END)
        self.license_field.delete(0, tk.END)
        
        self.name_field.insert(0, 'Name')
        self.email_field.insert(0, 'Email')
        self.contact_field.insert(0, 'Contact Number')
        self.code_field.insert(0, 'Password')
        self.confirm_field.insert(0,'Confirm Password')
        self.license_field.insert(0, 'License Number')       

    def go_to_login_page(self): 
        self.parent.change_window('Login_Page')

             
class AdminDashboard(tk.Frame): 
    def __init__(self, master): 
        tk.Frame.__init__(self, master)
        self.parent = master
        self.configure(bg='white')
        
        #------ MENU LOGO 
        self.logo = tk.PhotoImage(file='3traverse logo.png')
        tk.Label(self, image=self.logo, bg='white').grid(row=0, column=0, sticky='nsew', pady=(0, 0))
        
        #----- ADMIN MENU 
        self.heading = tk.Label(self, text='Admin Menu', fg='#4caf50', font=('Roboto', 50, 'bold'), bg='white')
        self.heading.grid(row=0, column=0, padx=(450, 450), sticky='n', pady=(270,0))

        #----- FLEET MANAGEMENT 
        self.fleet_button = tk.Button(self, text='Car Fleet Management', fg='white', font=('Inter', 18), bg='#4caf50', width=35, command=self.go_to_fleet_page)
        self.fleet_button.grid(row=1, column=0, pady=(30, 10))
        
        #----- MEMBER MANAGEMENT
        self.revenue_button = tk.Button(self, text='Customer Management', fg='white', bg='#4caf50', font=('Inter', 18), width=35, command=self.go_to_members_page)
        self.revenue_button.grid(row=2, column=0, pady=(10,10))
        
        #----- RENT REVENUE
        self.members_button = tk.Button(self, text='Rent Car', fg='white', bg='#4caf50', font=('Inter', 18), width=35, command=self.go_to_revenue_page)
        # self.members_button.grid(row=3, column=0, pady=(10,10))
        
        #----- LOGOUT 
        
        self.logout_button = tk.Button(self, text='Logout', fg='white', bg='#4caf50', font=('Inter', 18), width=35, command=self.go_to_login_page)
        self.logout_button.grid(row=4, column=0, pady=(10,10))
        
        
        
    
    def on_return(self, **kwargs): 
        pass
        
    def go_to_login_page(self): 
        self.parent.change_window('Login_Page')

    def go_to_fleet_page(self): 
        self.parent.change_window('Fleet_Page')
        
    def go_to_members_page(self): 
        self.parent.change_window('Members_Page')
    
    def go_to_revenue_page(self): 
        self.parent.change_window('Revenue_Page')
        
    
class MembersPage(tk.Frame): 
    def __init__(self, master): 
        tk.Frame.__init__(self, master)
        self.parent = master
        self.configure(bg='white')
        
        self.logo = tk.PhotoImage(file='250traverse logo.png')
        tk.Label(self, image=self.logo, bg='white').grid(row=0, column=0, padx=(100,100))
        
        #----- HEADING PAGE TITLE
        self.heading = tk.Label(self, text='Members Information', fg='#4caf50', font=('Roboto', 40, 'bold'), bg='white')
        self.heading.grid(row=1, column=0, padx=(150,100), pady=(0, 50), sticky='n')
        
        #----- SEARCH FIELD
        
        tk.Label(self, text="Search by Name: ", font=('Inter', 13), bg='white').grid(row=1, column=0, sticky='w', pady=(70,0), padx=(100,0))
        
        self.search_field = tk.Entry(self, width=140)
        self.search_field.grid(row=1, column=0, pady=(70, 0), padx=(120, 0))
        self.search_field.bind('<KeyRelease>', self.update_table)
        
        #----- TABLE 
        columns = ('id', 'name', 'email', 'contact', 'license_number', 'rental status', 'rented model', 'plate number', 'rental period', 'rent date-time')
        
        self.table = ttk.Treeview(self, columns=columns, show='headings')
        
        self.table.heading('id', text='ID')
        self.table.heading('name', text='Name')
        self.table.heading('email', text='Email')
        self.table.heading('contact', text='Contact No.')
        self.table.heading('license_number', text='License Number')
        self.table.heading('rental status', text='Status')
        self.table.heading('rented model', text='Model')
        self.table.heading('plate number', text='Plate Number')
        self.table.heading('rental period', text='Days')
        self.table.heading('rent date-time', text='Rented Date-Time')
        
        self.table.grid(row=2, column=0, padx=(100, 100))

        # Set the width of each column
        self.table.column('id', width=30)
        self.table.column('name', width=120)
        self.table.column('email', width=120)
        self.table.column('contact', width=100)
        self.table.column('license_number', width=95)
        self.table.column('rental status', width=70)
        self.table.column('rented model', width=70)
        self.table.column('plate number', width=95)
        self.table.column('rental period', width=70)
        self.table.column('rent date-time', width=150)
        self.table.tag_configure("center", anchor="center")
        self.update_table()
        
        #------ MENU BUTTON
        self.menu_button = tk.Button(self, text='Menu', width=15, fg='#4caf50', bg='white', border=0, font=('Inter', 15, 'underline'), command=self.go_to_admin_dashboard)
        self.menu_button.grid(row=3, column=0, padx=(300,0), sticky='w',pady=(20,0))
        
        #------ UPDATE MEMBER INFO
        self.update_button = tk.Button(self, text='Update', width=15, fg='#4caf50', bg='white', border=0, font=('Inter', 15, 'underline'), command=self.go_to_update_form)
        self.update_button.grid(row=3, column=0, padx=(100, 100), pady=(20,0))
        
        #------ DELETE MEMBER
        self.delete_button = tk.Button(self, text='Delete', width=15, fg='#4caf50', bg='white', border=0, font=('Inter', 15, 'underline'), command=self.delete_customer)
        self.delete_button.grid(row=3, column=0, padx=(400, 100), pady=(20,0))
        
    def update_table(self, event=None):
            self.get_employee_list()
            rental_data = self.get_rental_data()  # Retrieve rental data

            self.table.delete(*self.table.get_children())

            for account in self.employee_list:
                if account.account_type == 'customer':
                    account_data = (account.id, account.name, account.email, account.contact, account.license_number)
                    # Check if rental data exists for this account
                    if account.id in rental_data:
                        rental_info = rental_data[account.id]
                        row = account_data + rental_info  # Merge account and rental data
                    else:
                        # If no rental data found, fill empty values
                        row = account_data + ('---', '---', '---', '---', '----')  # Fill empty rental data
                    self.table.insert('', tk.END, values=row)

    def get_rental_data(self):
        db_conn = database_handler.DBHandler()
        rentals = db_conn.search_rental()
        db_conn.close()

        rental_data = {}  # Dictionary to store rental data for each customer
        for rental in rentals:
            if rental.customer_id not in rental_data:
                if rental.rental_status == "UNAVAILABLE": 
                    rental.rental_status = "ACTIVE"
                    rental_data[rental.customer_id] = (
                        rental.rental_status,
                        rental.rented_model,
                        rental.rent_plateNo,
                        rental.rental_period,
                        rental.rent_datetime
                )
        return rental_data

    
    def get_employee_list(self):
        key = self.search_field.get()
        db_conn = database_handler.DBHandler()
        self.employee_list = db_conn.search_employee(key)
        db_conn.close()
        
    
    def delete_customer(self): 
        selected_items = self.table.selection()

        if len(selected_items) == 0: 
            messagebox.showwarning('Delete Customer', 'Please Select a Customer to Delete')
            return
        
        proceed = messagebox.askyesno('Delete Customer', 'Are you sure you want to delete?')
        
        if not proceed: 
            return
        
        for item in selected_items: 
            id = self.table.item(item)['values'][0]

            db_conn = database_handler.DBHandler()
            db_conn.delete_customer(id)
            db_conn.close()
            
            self.update_table()
    
    def go_to_admin_dashboard(self): 
        self.parent.change_window('Admin_Dashboard')
        
    def go_to_update_form(self):
        selected_items = self.table.selection()
        if len(selected_items) == 0:
            messagebox.showwarning("Update Customer", "Select a customer to update.")
            return

        for item in selected_items:
            id = self.table.item(item)['values'][0]
            self.parent.change_window('Update_Form', customer_id=id)
    
    def on_return(self): 
        self.update_table()
        
        
class UpdateForm(tk.Frame): 
    def __init__(self, master): 
        tk.Frame.__init__(self, master)
        self.parent = master
        self.configure(bg='white')
        
        self.logo = tk.PhotoImage(file='250traverse logo.png')
        tk.Label(self, image=self.logo, bg='white').grid(row=0, column=0, padx=(100,100))
        
        #----- HEADING PAGE TITLE
        self.heading = tk.Label(self, text='Update Information', fg='#4caf50', font=('Roboto', 40, 'bold'), bg='white')
        self.heading.grid(row=1, column=0, padx=(150,100), pady=(0, 50), sticky='n')
        
        #----- ID FIELDS
        tk.Label(self, text='Customer ID', font=('Inter', 13), fg='black', bg='white').grid(row=2, column=0, padx=(0, 300), sticky='we')
        
        self.id_field = Label(self, text='xx', width=60, border=1, fg='black', bg='white', font=('Microsoft yahei UI Light', 11))
        self.id_field.grid(row=2, column=0, padx=(500, 100), sticky='w')
        # self.id_field.insert(0, 'ID')
        self.id_field.bind('<FocusIn>', self.on_enter)
        self.id_field.bind('<FocusOut>', self.on_leave)
        #----- NAME FIELDS
        tk.Label(self, text='Customer Name', font=('Inter', 13), fg='black', bg='white').grid(row=3, column=0, padx=(0, 300), sticky='we')
        
        self.name_field = Entry(self, width=60, border=1, fg='black', bg='white', font=('Microsoft yahei UI Light', 11))
        self.name_field.grid(row=3, column=0, padx=(500, 100))
        self.name_field.insert(0, 'Name')
        self.name_field.bind('<FocusIn>', self.on_enter)
        self.name_field.bind('<FocusOut>', self.on_leave)
        
        #----- EMAIL FIELDS
        tk.Label(self, text='Email Address', font=('Inter', 13), fg='black', bg='white').grid(row=4, column=0, padx=(0, 300), sticky='we')
        self.email_field = Entry(self, width=60, border=1, fg='black', bg='white', font=('Microsoft Yahei UI Light', 11))
        self.email_field.grid(row=4, column=0, padx=(500, 100))
        self.email_field.insert(0, 'Email Address')
        self.email_field.bind('<FocusIn>', self.on_enter)
        self.email_field.bind('<FocusOut>', self.on_leave)
        #----- CONTACT NUMBER FIELDS
        tk.Label(self, text='Contact Number', font=('Inter', 13), fg='black', bg='white').grid(row=5, column=0, padx=(0, 300), sticky='we')
        self.contact_field = Entry(self, width=60, border=1, fg='black', bg='white', font=('Microsoft Yahei UI Light', 11))
        self.contact_field.grid(row=5, column=0, padx=(500, 100))
        self.contact_field.insert(0, 'Contact Number')
        self.contact_field.bind('<FocusIn>', self.on_enter)
        self.contact_field.bind('<FocusOut>', self.on_leave)
        #----- LICENSE NUMBER FIELDS
        tk.Label(self, text='License Number', font=('Inter', 13), fg='black', bg='white').grid(row=6, column=0, padx=(0, 300), sticky='we')
        self.license_field = Entry(self, width=60, border=1, fg='black', bg='white', font=('Microsoft yahei UI Light', 11))
        self.license_field.grid(row=6, column=0, padx=(500, 100))
        self.license_field.insert(0, "Driver's License Number")
        self.license_field.bind('<FocusIn>', self.on_enter)
        self.license_field.bind('<FocusOut>', self.on_leave)
        #----- PASSWORD FIELDS
        tk.Label(self, text='Password', font=('Inter', 13), fg='black', bg='white').grid(row=7, column=0, padx=(0, 300), sticky='we')
        self.code_field = Entry(self, width=60, border=1, fg='black', bg='white', font=('Microsoft Yahei UI Light', 11))
        self.code_field.grid(row=7, column=0, padx=(500, 100))
        self.code_field.insert(0, 'Password')
        self.code_field.bind('<FocusIn>', self.on_enter)
        self.code_field.bind('<FocusOut>', self.on_leave)
        #----- CONFIRM PASSWORD
        tk.Label(self, text='Confirm Password', font=('Inter', 13), fg='black', bg='white').grid(row=8, column=0, padx=(0, 300), sticky='we')
        self.confirm_field = Entry(self, width=60, border=1, fg='black', bg='white', font=('Microsoft Yahei UI Light', 11))
        self.confirm_field.grid(row=8, column=0, padx=(500, 100))
        self.confirm_field.insert(0, 'Confirm Password')
        self.confirm_field.bind('<FocusIn>', self.on_enter)
        self.confirm_field.bind('<FocusOut>', self.on_leave)

        #------ UPDATE BUTTON 
        self.update_button = Button(self, width=68, pady=7, text='Save Changes', bg='#4caf50', fg='#fff', border=0, command=self.update_customer)
        self.update_button.grid(row=9, column=0, padx=(390, 0), pady=(20, 20))

        
        
    #----- FUNCTIONS
    
    
    def on_return(self, **kwargs):
        # self.id = kwargs['customer_id']
        
        print("Received kwargs:", kwargs)
        self.id = kwargs.get('customer_id', None)
        if self.id is None:
            print("Error: 'customer_id' not found in kwargs")
            return
        
        self.id = kwargs['customer_id']
        self.id_field.config(text=self.id)

        db_conn = database_handler.DBHandler()
        customer_data = db_conn.read_one_customer(self.id)
        db_conn.close

        self.clear_fields()

        self.name_field.insert(0, customer_data.name)
        self.email_field.insert(0, customer_data.email)
        self.contact_field.insert(0, customer_data.contact)
        self.license_field.insert(0, customer_data.license_number)
        self.code_field.insert(0, customer_data.password)
        self.confirm_field.insert(0, 'Confirm Password')
        

    def clear_fields(self):
        self.name_field.delete(0, tk.END)
        self.email_field.delete(0, tk.END)
        self.contact_field.delete(0, tk.END)
        self.license_field.delete(0, tk.END)
        self.code_field.delete(0, tk.END)
        self.confirm_field.delete(0, tk.END)

    def validate_date(self):
        #Input validation
        return True
    
    def update_customer(self):
        if not self.validate_date():
            return
        try:
            new_customer = models.Accounts()
            new_customer.id = self.id
            new_customer.name = self.name_field.get()
            new_customer.email = self.email_field.get()
            new_customer.contact = int(self.contact_field.get())
            new_customer.license_number = self.license_field.get()
            new_customer.password = (self.code_field.get())

            proceed = messagebox.askyesno("Update Employee", "Do you want to commit changes to the selected data?")

            if not proceed:
                return

            db_conn = database_handler.DBHandler()
            db_conn.update_customer(new_customer)
            db_conn.close()
            
            self.go_to_members_page()
        except ValueError:
            messagebox.showerror("Update Customer", "Value Error")
    
    def go_to_members_page(self):
        self.parent.change_window('Members_Page')
    
    def on_enter(self, e):
        widget = e.widget
        widget.delete(0, 'end')

    def on_leave(self, e):
        widget = e.widget
        if widget.get() == '':
            if widget == self.name_field:
                widget.insert(0, 'Name')
            elif widget == self.license_field:
                widget.insert(0, "Driver's License Number")
            elif widget == self.contact_field:
                widget.insert(0, 'Contact Number')
            elif widget == self.email_field:
                widget.insert(0, 'Email Address')
            elif widget == self.code_field:
                widget.insert(0, 'Password')
            elif widget == self.confirm_field:
                widget.insert(0, 'Confirm Password')
                            
                
class FleetPage(tk.Frame): 
    def __init__(self, master): 
        tk.Frame.__init__(self, master)
        self.parent = master
        self.configure(bg='white')
        
        #----- TRAVERSE LOGO
        logo = Image.open("250traverse logo.png")
        logo = logo.resize((150, 150))
        self.logo = ImageTk.PhotoImage(logo)
        
        tk.Label(self, image=self.logo, bg='white').grid(row=0, column=0, padx=(100,100))
        
        #----- HEADING PAGE TITLE
        self.heading = tk.Label(self, text='Car Fleet Management', fg='#4caf50', font=('Roboto', 40, 'bold'), bg='white')
        self.heading.grid(row=1, column=0, padx=(150,100), pady=(0, 50), sticky='n')
        
        #----- SEARCH FIELD
        
        tk.Label(self, text="Search by Brand: ", font=('Inter', 13), bg='white').grid(row=1, column=0, sticky='w', pady=(70,0), padx=(100,0))
        
        self.search_field = tk.Entry(self, width=140)
        self.search_field.grid(row=1, column=0, pady=(70, 0), padx=(120, 0))
        self.search_field.bind('<KeyRelease>', self.update_table)
        
        #----- TABLE 
        columns = ('id', 'brand', 'model', 'plate#', 'fuel', 'cost', 'seating capacity', 'location', 'status')
        
        self.table = ttk.Treeview(self, columns=columns, show='headings')
        
        self.table.heading('id', text='ID')
        # self.table.heading('img', text='Car Image')
        self.table.heading('brand', text='Brand')
        self.table.heading('model', text='Model')
        self.table.heading('plate#', text='Plate Number')
        self.table.heading('fuel', text='Fuel Type')
        self.table.heading('cost', text='Cost/Day')
        self.table.heading('seating capacity', text='Seaters')
        self.table.heading('location', text='Location')
        self.table.heading('status', text='Status')
        
        self.table.grid(row=2, column=0, padx=(100, 100))

        # Set the width of each column
        self.table.column('id', width=30)
        # self.table.column('img', width=200)
        self.table.column('brand', width=150)
        self.table.column('model', width=100)
        self.table.column('plate#', width=120)
        self.table.column('fuel', width=100)
        self.table.column('cost', width=120)
        self.table.column('seating capacity', width=90)
        self.table.column('location', width=145)
        self.table.column('status', width=145)
        # self.table.tag_configure("center", anchor="center")
        self.update_table()
        
        #------ MENU BUTTON
        self.menu_button = tk.Button(self, text='Menu', width=15, fg='#4caf50', bg='white', border=0, font=('Inter', 15, 'underline'), command=self.go_to_admin_dashboard)
        self.menu_button.grid(row=3, column=0, padx=(300,0), sticky='w',pady=(20,0))
        
        #------ DELETE CAR
        self.delete_button = tk.Button(self, text='Delete', width=15, fg='#4caf50', bg='white', border=0, font=('Inter', 15, 'underline'), command=self.delete_car)
        self.delete_button.grid(row=3, column=0, padx=(400, 100), pady=(20,0))
        #-----  UPDATE CAR
        self.view_car = tk.Button(self, text='Update', width=15, fg='#4caf50', bg='white', border=0, font=('Inter', 15, 'underline'), command=self.go_to_car_page)
        self.view_car.grid(row=3, column=0, padx=(60, 100), pady=(20,0))
        
    def update_table(self, event=None):
        self.get_car_list()
        rental_data = self.get_rental_data()
        
        self.table.delete(*self.table.get_children())

        for car in self.car_list:
            car_data = (car.id, car.brand, car.model, car.plate_number, car.fuel_type, car.cost_per_day, car.seating_capacity, car.location)
            
            if car.id in rental_data: 
                rental_info = rental_data[car.id]
                row = car_data + (rental_info,)
            else: 
                 row = car_data + ('----',)
                
            self.table.insert('', tk.END, values=row)


    def get_car_list(self):
        key = self.search_field.get()
        db_conn = database_handler.DBHandler()
        self.car_list = db_conn.search_car(key)
        
        self.rental_statuses = db_conn.get_rental_statuses()
        db_conn.close()
    
    def get_rental_data(self):
        db_conn = database_handler.DBHandler()
        rentals = db_conn.search_rental()
        db_conn.close()

        rental_data = {}  # Dictionary to store rental data for each customer
        for rental in rentals:
            if rental.car_id not in rental_data:
                if rental.rental_status == "UNAVAILABLE": 
                    rental.rental_status = "CURRENTLY RENTED"
                    rental_data[rental.car_id] = (
                        rental.rental_status

                )
        return rental_data

    
    
    def delete_car(self): 
        selected_items = self.table.selection()

        if len(selected_items) == 0: 
            messagebox.showwarning('Delete a Car', 'Please Select a Car to Delete')
            return
        
        proceed = messagebox.askyesno('Delete a Car', 'Are you sure you want to delete?')
        
        if not proceed: 
            return
        
        for item in selected_items: 
            id = self.table.item(item)['values'][0]

            db_conn = database_handler.DBHandler()
            db_conn.delete_car(id)
            db_conn.close()
            
            self.update_table()
    
    def on_return(self): 
        self.update_table()
        
    def go_to_admin_dashboard(self): 
        self.parent.change_window('Admin_Dashboard')
        
    def go_to_car_page(self): 
        selected_items = self.table.selection()
        if len(selected_items) == 0:
            messagebox.showwarning("Update Car", "Select a car to update.")
            return

        for item in selected_items:
            id = self.table.item(item)['values'][0]
            self.parent.change_window('View_Car', car_id=id)
        
        
class CarPage(tk.Frame): 
    def __init__(self, master): 
        tk.Frame.__init__(self, master)
        self.parent = master
        self.configure(bg='white')
        
         #----- TRAVERSE LOGO
        logo = Image.open("3traverse logo.png")
        logo = logo.resize((200, 200))
        self.logo = ImageTk.PhotoImage(logo)
        
        tk.Label(self, image=self.logo, bg='white').grid(row=0, column=0, sticky='w', padx=(250, 0))
        
        #----- HEADING PAGE TITLE
        self.heading = tk.Label(self, text='Car Details & Information', fg='#4caf50', font=('Roboto', 40, 'bold'), bg='white')
        self.heading.grid(row=0, column=0, columnspan=5, pady=(0, 0), padx=(450, 0), sticky='w')
        #----- CAR IMAGE 
        car = Image.open('toyota.png')
        # car = car.resize((500, 200))
        self.car = ImageTk.PhotoImage(car)
        tk.Label(self, image=self.car, bg='white', borderwidth=1).grid(row=2, column=0, padx=(100, 0), sticky='nws')
        
        #----- ID FIELDS
        tk.Label(self, text='CAR ID', font=('Inter', 13), fg='black', bg='white', width=20).grid(row=2, column=0, padx=(600, 0), sticky='n')
        self.id_field = Label(self, text='xx', width=35, border=2, fg='black', bg='white', font=('Microsoft yahei UI Light', 11))
        self.id_field.grid(row=2, column=1, sticky='n')
        # self.id_field.insert(0, 'ID')
        self.id_field.bind('<FocusIn>', self.on_enter)
        self.id_field.bind('<FocusOut>', self.on_leave)
        
        #----- BRAND FIELDS
        tk.Label(self, text='BRAND', font=('Inter', 13), fg='black', bg='white', width=20).grid(row=2, column=0, padx=(600, 0), pady=(50,0), sticky='n')
        self.brand_field = Entry(self, width=40, border=2, fg='black', bg='white', font=('Microsoft yahei UI Light', 11))
        self.brand_field.grid(row=2, column=1, pady=(50, 0), sticky='n')
        self.brand_field.insert(0, 'Car Brand')
        self.brand_field.bind('<FocusIn>', self.on_enter)
        self.brand_field.bind('<FocusOut>', self.on_leave)
        #----- MODEL FIELDS
        tk.Label(self, text='MODEL', font=('Inter', 13), fg='black', bg='white', width=20).grid(row=2, column=0, padx=(600, 0), pady=(100,0), sticky='n')
        self.model_field = Entry(self, width=40, border=2, fg='black', bg='white', font=('Microsoft yahei UI Light', 11))
        self.model_field.grid(row=2, column=1, pady=(100, 0), sticky='n')
        self.model_field.insert(0, 'Car Model')
        self.model_field.bind('<FocusIn>', self.on_enter)
        self.model_field.bind('<FocusOut>', self.on_leave)
        #----- PLATE NUMBER FIELDS
        tk.Label(self, text='PLATE NUMBER', font=('Inter', 13), fg='black', bg='white', width=20).grid(row=2, column=0, padx=(600, 0), pady=(150,0), sticky='n')
        self.plate_field = Entry(self, width=40, border=2, fg='black', bg='white', font=('Microsoft yahei UI Light', 11))
        self.plate_field.grid(row=2, column=1, pady=(150, 0), sticky='n')
        self.plate_field.insert(0, 'Plate Number')
        self.plate_field.bind('<FocusIn>', self.on_enter)
        self.plate_field.bind('<FocusOut>', self.on_leave)
        #----- FUEL TYPE FIELDS
        tk.Label(self, text='FUEL TYPE', font=('Inter', 13), fg='black', bg='white', width=20).grid(row=2, column=0, padx=(600, 0), pady=(200,0), sticky='n')
        self.fuel_field = Entry(self, width=40, border=2, fg='black', bg='white', font=('Microsoft yahei UI Light', 11))
        self.fuel_field.grid(row=2, column=1, pady=(200, 0), sticky='n')
        self.fuel_field.insert(0, 'Fuel Type')
        self.fuel_field.bind('<FocusIn>', self.on_enter)
        self.fuel_field.bind('<FocusOut>', self.on_leave)
        #----- COST PER DAY FIELDS
        tk.Label(self, text='COST PER DAY', font=('Inter', 13), fg='black', bg='white', width=20).grid(row=2, column=0, padx=(600, 0), pady=(250,0), sticky='n')
        self.cost_field = Entry(self, width=40, border=2, fg='black', bg='white', font=('Microsoft yahei UI Light', 11))
        self.cost_field.grid(row=2, column=1, pady=(250, 0), sticky='n')
        self.cost_field.insert(0, 'Cost Per Day')
        self.cost_field.bind('<FocusIn>', self.on_enter)
        self.cost_field.bind('<FocusOut>', self.on_leave)
        #----- SEATING CAPACITY FIELDS
        tk.Label(self, text='SEATING CAPACITY', font=('Inter', 13), fg='black', bg='white', width=20).grid(row=2, column=0, padx=(600, 0), pady=(300,0), sticky='n')
        self.seater_field = Entry(self, width=40, border=2, fg='black', bg='white', font=('Microsoft yahei UI Light', 11))
        self.seater_field.grid(row=2, column=1, pady=(300, 0), sticky='n')
        self.seater_field.insert(0, 'Seating Capacity')
        self.seater_field.bind('<FocusIn>', self.on_enter)
        self.seater_field.bind('<FocusOut>', self.on_leave)
        #----- LOCATION FIELDS
        tk.Label(self, text='PICKUP LOCATION', font=('Inter', 13), fg='black', bg='white', width=20).grid(row=2, column=0, padx=(600, 0), pady=(350, 0), sticky='n')
        self.picupLoc_field = Entry(self, width=40, border=2, fg='black', bg='white', font=('Microsoft yahei UI Light', 11))
        self.picupLoc_field.grid(row=2, column=1, pady=(350, 0), sticky='n')
        self.picupLoc_field.insert(0, 'PICKUP LOCATION')
        self.picupLoc_field.bind('<FocusIn>', self.on_enter)
        self.picupLoc_field.bind('<FocusOut>', self.on_leave)
        #----- STATUS FIELDS
        tk.Label(self, text='STATUS', font=('Inter', 13), fg='black', bg='white', width=20).grid(row=2, column=0, padx=(600, 0), pady=(400, 0), sticky='n')
        self.status_field = Entry(self, width=40, border=2, fg='black', bg='white', font=('Microsoft yahei UI Light', 11))
        self.status_field.grid(row=2, column=1, pady=(400, 0), sticky='n')
        self.status_field.insert(0, 'STATUS')
        self.status_field.bind('<FocusIn>', self.on_enter)
        self.status_field.bind('<FocusOut>', self.on_leave)
        #------ UPDATE BUTTON 
        self.update_button = Button(self, width=20, pady=7, text='Save Changes', bg='#4caf50', fg='#fff', border=0, command=self.update_car)
        self.update_button.grid(row=2, column=1, pady=(450,0), sticky='n')
    
    
#----- FUNCTIONS 
    def on_return(self, **kwargs):        
        print("Received kwargs:", kwargs)
        self.id = kwargs.get('car_id', None)
        if self.id is None:
            print("Error: 'customer_id' not found in kwargs")
            return
        
        self.id = kwargs['car_id']
        self.id_field.config(text=self.id)

        db_conn = database_handler.DBHandler()
        car_data = db_conn.read_one_car(self.id)
        db_conn.close

        self.clear_fields()
        
        self.brand_field.insert(0, car_data.brand)
        self.model_field.insert(0, car_data.model)
        self.plate_field.insert(0, car_data.plate_number)
        self.fuel_field.insert(0, car_data.fuel_type)
        self.status_field.insert(0, car_data.availability)
        self.cost_field.insert(0, car_data.cost_per_day)
        self.seater_field.insert(0, car_data.seating_capacity)
        self.picupLoc_field.insert(0, car_data.location)
        
    def clear_fields(self):
        self.brand_field.delete(0, tk.END)
        self.model_field.delete(0, tk.END)
        self.plate_field.delete(0, tk.END)
        self.fuel_field.delete(0, tk.END)
        self.status_field.delete(0, tk.END)
        self.cost_field.delete(0, tk.END)
        self.seater_field.delete(0, tk.END)
        self.picupLoc_field.delete(0, tk.END)

    def validate_date(self):
        return True
    
    def update_car(self):
        if not self.validate_date():
            return
        try:
            new_car = models.Cars()
            new_car.id = self.id
            new_car.brand = self.brand_field.get()
            new_car.model = self.model_field.get()
            new_car.plate_number = self.plate_field.get()
            new_car.fuel_type = self.fuel_field.get()
            new_car.availability = self.status_field.get()
            new_car.cost_per_day = int(self.cost_field.get())
            new_car.seating_capacity = int(self.seater_field.get())
            new_car.location = self.picupLoc_field.get()

            proceed = messagebox.askyesno("Update Car", "Do you want to commit changes to the selected data?")

            if not proceed:
                return

            db_conn = database_handler.DBHandler()
            db_conn.update_car(new_car)
            db_conn.close()
            
            self.go_to_fleet_page()
            
        except ValueError:
            messagebox.showerror("Update Car", "Value Error")
    
    def on_enter(self, e): 
        widget = e.widget
        widget.delete(0, 'end')
        
    def on_leave(self, e):
        widget = e.widget
        if widget.get() == '':
            if widget == self.brand_field:
                widget.insert(0, 'Brand')
            elif widget == self.model_field:
                widget.insert(0, "Model")
            elif widget == self.plate_field:
                widget.insert(0, 'Plate Number')
            elif widget == self.fuel_field:
                widget.insert(0, 'Fuel Type')
            elif widget == self.status_field:
                widget.insert(0, 'Status')
            elif widget == self.cost_field:
                widget.insert(0, 'Cost Per Day')
            elif widget == self.seater_field:
                widget.insert(0, 'Seating Capacity')
            elif widget == self.seater_field:
                widget.insert(0, 'Pickup Location')
    
    
    def go_to_fleet_page(self): 
        self.parent.change_window('Fleet_Page')        
        
        
class CustomerWindow(tk.Frame): 
    def __init__(self, master): 
        tk.Frame.__init__(self, master)
        self.parent = master
        self.configure(bg='white')
        
        
        #----- TRAVERSE LOGO
        logo = Image.open("250traverse logo.png")
        logo = logo.resize((150, 150))
        self.logo = ImageTk.PhotoImage(logo)
        
        tk.Label(self, image=self.logo, bg='white').grid(row=0, column=0, padx=(100,100))
        
        #----- HEADING PAGE TITLE
        self.heading = tk.Label(self, text='Hello, Customer!', fg='#4caf50', font=('Roboto', 40, 'bold'), bg='white')
        self.heading.grid(row=1, column=0, padx=(150,100), pady=(0, 50), sticky='n')
        
        #------ CUSTOMER FIELDS 
        self.customer_id = tk.Label(self, text='Customer ID:', fg='#4caf50', font=('Inter', 18, 'bold'), bg='white')
        self.customer_id.grid(row=2, column=0, sticky='w', padx=(100, 100), pady=(0,0))
        self.id_num = tk.Label(self, text=self.customer_id, fg='black', font=('Inter', 12), bg='white' )
        self.id_num.grid(row=2, column=0, sticky='w', padx=(300,0))
        
        self.customer_name = tk.Label(self, text='Customer Name:', fg='#4caf50', font=('Inter', 18, 'bold'), bg='white')
        self.customer_name.grid(row=3, column=0, sticky='wn', padx=(100,100), pady=(0,0))
        self.name_customer = tk.Label(self, text='Elon Musk', fg='black', font=('Inter', 12), bg='white' )
        self.name_customer.grid(row=3, column=0, sticky='wn', padx=(300,0))
        
        
        #----- SEARCH FIELD
        
        tk.Label(self, text="Search by Brand: ", font=('Inter', 13), bg='white').grid(row=3, column=0, sticky='w', pady=(70,0), padx=(100,0))
        
        self.search_field = tk.Entry(self, width=140)
        self.search_field.grid(row=3, column=0, pady=(70, 0), padx=(120, 0))
        self.search_field.bind('<KeyRelease>', self.update_table)
        
        #----- TABLE 
        columns = ('id', 'brand', 'model', 'plate#', 'fuel', 'cost', 'seating capacity', 'location', 'status')
        
        self.table = ttk.Treeview(self, columns=columns, show='headings')
        
        self.table.heading('id', text='ID')
        # self.table.heading('img', text='Car Image')
        self.table.heading('brand', text='Brand')
        self.table.heading('model', text='Model')
        self.table.heading('plate#', text='Plate Number')
        self.table.heading('fuel', text='Fuel Type')
        self.table.heading('cost', text='Cost/Day')
        self.table.heading('seating capacity', text='Seaters')
        self.table.heading('location', text='Location')
        self.table.heading('status', text='Status')
        
        self.table.grid(row=4, column=0, padx=(100, 100))

        # Set the width of each column
        self.table.column('id', width=30)
        # self.table.column('img', width=200)
        self.table.column('brand', width=150)
        self.table.column('model', width=100)
        self.table.column('plate#', width=120)
        self.table.column('fuel', width=100)
        self.table.column('cost', width=120)
        self.table.column('seating capacity', width=90)
        self.table.column('location', width=145)
        self.table.column('status', width=145)
        # self.table.tag_configure("center", anchor="center")
        self.update_table()
        
        #------ Logout BUTTON
        self.menu_button = tk.Button(self, text='Menu', width=15, fg='#4caf50', bg='white', border=0, font=('Inter', 15, 'underline'), command=self.go_to_login_page)
        self.menu_button.grid(row=5, column=0, padx=(300,0), sticky='w',pady=(20,0))
        
        #------ View Profile
       
        #-----  Billing Page
        self.rent_car = tk.Button(self, text='RENT CAR', width=15, fg='#4caf50', bg='white', border=0, font=('Inter', 15, 'underline'), command=self.rent_this_car)
        self.rent_car.grid(row=5, column=0, padx=(60, 100), pady=(20,0))
        
    def update_table(self, event=None):
        self.get_car_list()
        rental_data = self.get_rental_data()
        
        self.table.delete(*self.table.get_children())
    
        
        for car in self.car_list:
            car_data = (car.id, car.brand, car.model, car.plate_number, car.fuel_type, car.cost_per_day, car.seating_capacity, car.location)
            
            if car.id in rental_data: 
                rental_info = rental_data[car.id]
                row = car_data + (rental_info,)
            else: 
                row = car_data + ('----',)
                
            self.table.insert('', tk.END, values=row)


    def get_rental_data(self):
        db_conn = database_handler.DBHandler()
        rentals = db_conn.search_rental()
        db_conn.close()

        rental_data = {}  # Dictionary to store rental data for each customer
        for rental in rentals:
            if rental.car_id not in rental_data:
                if rental.rental_status == "UNAVAILABLE": 
                    rental.rental_status = "CURRENTLY RENTED"
                    rental_data[rental.car_id] = (
                        rental.rental_status

                )
        return rental_data
    
    def get_car_list(self):
        # pass
        key = self.search_field.get()
        db_conn = database_handler.DBHandler()
        self.car_list = db_conn.search_car(key)
        db_conn.close()
    
    def delete_car(self): 
        selected_items = self.table.selection()

        if len(selected_items) == 0: 
            messagebox.showwarning('Delete a Car', 'Please Select a Car to Delete')
            return
        
        proceed = messagebox.askyesno('Delete a Car', 'Are you sure you want to delete?')
        
        if not proceed: 
            return
        
        for item in selected_items: 
            id = self.table.item(item)['values'][0]

            db_conn = database_handler.DBHandler()
            db_conn.delete_car(id)
            db_conn.close()
            
            self.update_table()

        
    def go_to_car_page(self): 
        selected_items = self.table.selection()
        if len(selected_items) == 0:
            messagebox.showwarning("Update Car", "Select a car to update.")
            return

        for item in selected_items:
            id = self.table.item(item)['values'][0]
            self.parent.change_window('View_Car', car_id=id)

    def on_return(self, **kwargs):
        self.update_table()
        # self.id = kwargs['customer_id']
        
        print("Received kwargs:", kwargs)
        self.id = kwargs.get('customer_id', None)
        if self.id is None:
            print("Error: 'customer_id' not found in kwargs")
            return
        
        self.id = kwargs['customer_id']
        self.id_num.config(text=self.id)

        db_conn = database_handler.DBHandler()
        customer_data = db_conn.read_one_customer(self.id)
        db_conn.close
        
        # self.clear_fields()

        self.name_customer.config(text=customer_data.name)
    
    def rent_this_car(self): 
        selected_items = self.table.selection()
        if len(selected_items) == 0:
            messagebox.showwarning("Rent a Car", "Select a car to rent")
            return

        for item in selected_items:
            car_id = self.table.item(item)['values'][0]
            
        customer_id = self.id_num.cget("text")
        self.go_to_billing_page(customer_id, car_id)
    

    #----
    def go_to_login_page(self): 
        self.parent.change_window('Login_Page')
    
    def go_to_billing_page(self, customer_id, car_id): 
        self.parent.change_window('Billing_Page', customer_id=customer_id, car_id=car_id)
        
        
class BillingPage(tk.Frame): 
    def __init__(self, master): 
        tk.Frame.__init__(self, master)
        self.parent = master
        self.configure(bg='white')
        
        #----- TRAVERSE LOGO
        logo = Image.open("3traverse logo.png")
        logo = logo.resize((200, 200))
        self.logo = ImageTk.PhotoImage(logo)
        
        tk.Label(self, image=self.logo, bg='white').grid(row=0, column=0, sticky='w', padx=(250, 0))
        
        #----- HEADING PAGE TITLE
        self.heading = tk.Label(self, text='Billing Information', fg='#4caf50', font=('Roboto', 40, 'bold'), bg='white')
        self.heading.grid(row=0, column=0, columnspan=5, pady=(0, 0), padx=(450, 0), sticky='w')
        
        #----- CUSTOMER FRAME FIELDS
        self.customer_frame = tk.Frame(self, width=600, border=5 )
        self.customer_frame.grid(row=1, column=0, sticky='nw', pady=(0,0), padx=(100,0))
        
        tk.Label(self.customer_frame, text="Customer ID:", bg='white').grid(row=0, column=0, sticky='w')
        self.customer_id_entry = Entry(self.customer_frame, width=40)
        self.customer_id_entry.grid(row=0, column=1)
        
        tk.Label(self.customer_frame, text="Customer Name:", bg='white').grid(row=1, column=0, sticky='w')
        self.customer_name_entry = Entry(self.customer_frame, width=40)
        self.customer_name_entry.grid(row=1, column=1)
        
        tk.Label(self.customer_frame, text="Driver's License Number:", bg='white').grid(row=2, column=0, sticky='w')
        self.license_number_entry = Entry(self.customer_frame, width=40)
        self.license_number_entry.grid(row=2, column=1)
        
        tk.Label(self.customer_frame, text="Contact Number:", bg='white').grid(row=3, column=0, sticky='w')
        self.contact_number_entry = Entry(self.customer_frame, width=40)
        self.contact_number_entry.grid(row=3, column=1)
        
        #----- CAR FRAME FIELDS
        
        self.car_frame = tk.Frame(self,border=5)
        self.car_frame.grid(row=1, column=0, sticky='nw', pady=(100,0))
        self.car_frame.config(bg='white')
        
        car = Image.open("toyota.png")
        car = car.resize((350, 120))
        self.car = ImageTk.PhotoImage(car)
        
        tk.Label(self.car_frame, image=self.car, bg='white').grid(row=3, column=0, padx=(100, 0))
        
        tk.Label(self.car_frame, text='Selected Car Information',fg='#4caf50', font=('Roboto', 15, 'bold')).grid(row=0, column=0, sticky='w',padx=(100,0))
        
        tk.Label(self.car_frame, text="Car ID:", bg='white').grid(row=1, column=2, sticky='w')
        self.car_id_entry = Entry(self.car_frame, width=25)
        self.car_id_entry.grid(row=1, column=3)
        
        tk.Label(self.car_frame, text="Brand:", bg='white').grid(row=2, column=2, sticky='w')
        self.car_brand_entry = Entry(self.car_frame, width=25)
        self.car_brand_entry.grid(row=2, column=3)
        
        tk.Label(self.car_frame, text="Model:", bg='white').grid(row=3, column=2, sticky='w')
        self.car_model_entry = Entry(self.car_frame, width=25)
        self.car_model_entry.grid(row=3, column=3)
        
        tk.Label(self.car_frame, text="Plate Number:", bg='white').grid(row=4, column=2, sticky='w')
        self.plate_number_entry = Entry(self.car_frame, width=25)
        self.plate_number_entry.grid(row=4, column=3)
        
        tk.Label(self.car_frame, text="Fuel Type:", bg='white').grid(row=5, column=2, sticky='w')
        self.fuel_type_entry = Entry(self.car_frame, width=25)
        self.fuel_type_entry.grid(row=5, column=3)
        
        tk.Label(self.car_frame, text="Seating Capacity:", bg='white').grid(row=6, column=2, sticky='w')
        self.seating_capacity_entry = Entry(self.car_frame, width=25)
        self.seating_capacity_entry.grid(row=6, column=3)
        
        tk.Label(self.car_frame, text="Pickup Location:", bg='white').grid(row=7, column=2, sticky='w')
        self.location_entry = Entry(self.car_frame, width=25)
        self.location_entry.grid(row=7, column=3)
        
        tk.Label(self.car_frame, text="Cost Per Day:", bg='white').grid(row=8, column=2, sticky='w')
        self.cost_per_day_entry = Entry(self.car_frame, width=25)
        self.cost_per_day_entry.grid(row=8, column=3)
        
        tk.Label(self.car_frame, text="Rental Period (days):", bg='white').grid(row=9, column=2, sticky='w')
        self.rental_period_entry = Entry(self.car_frame, width=25)
        self.rental_period_entry.grid(row=9, column=3)
        
        self.confirm_rent = Button(self.car_frame, text='Confirm Rent', pady=2, padx=7, bg='#4caf50', fg='white', width=25, command=self.confirm_rent_clicked)
        self.confirm_rent.grid(row=10, column=3, pady=(20,0), padx=(10, 60))
        
        tk.Button(self.car_frame, text="Logout", pady=2, padx=7, bg='#4caf50', fg='white', width=14,  command=self.go_to_login_page).grid(row=10, column=2, pady=(20,0), padx=(0, 0))

        
        #----- BILLING FRAME FIELDS
        
        self.billing_frame = tk.Frame(self, width=600, height=400, border=1, highlightthickness=2, highlightbackground="#000", highlightcolor="#000", bd=0)
        self.billing_frame.grid(row=1, column=2, columnspan=4)
        # self.billing_frame.config(bg='white')
        
        tk.Label(self.billing_frame, text="Billing Receipt", fg='black', font=('Roboto', 15, 'bold')).grid(row=0, column=0, padx=(10,0))
        
        tk.Label(self.billing_frame, text="Customer Name:").grid(row=1, column=0, sticky='w', padx=10, pady=10)
        self.customer_name_entry_billing = Entry(self.billing_frame)
        self.customer_name_entry_billing.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="Rented Model:").grid(row=2, column=0, sticky='w', padx=10, pady=10)
        self.rented_model_entry_billing = Entry(self.billing_frame)
        self.rented_model_entry_billing.grid(row=2, column=1, padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="Rented Date-Time:").grid(row=3, column=0, sticky='w', padx=10, pady=10)
        self.rented_date_entry_billing = Entry(self.billing_frame)
        self.rented_date_entry_billing.grid(row=3, column=1, padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="Rental Period:").grid(row=4, column=0, sticky='w', padx=10, pady=10)
        self.rental_period_entry_billing = Entry(self.billing_frame)
        self.rental_period_entry_billing.grid(row=4, column=1, padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="Return Date-Time:").grid(row=5, column=0, sticky='w', padx=10, pady=10)
        self.return_date_entry_billing = Entry(self.billing_frame)
        self.return_date_entry_billing.grid(row=5, column=1, padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="Pickup Location:").grid(row=6, column=0, sticky='w', padx=10, pady=10)
        self.pickup_location_entry_billing = Entry(self.billing_frame)
        self.pickup_location_entry_billing.grid(row=6, column=1, padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="Cost Per Day:").grid(row=7, column=0, sticky='w', padx=10, pady=10)
        self.cost_per_day_billing_entry = Entry(self.billing_frame)
        self.cost_per_day_billing_entry.grid(row=7, column=1, padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="================================:").grid(row=8, column=0, columnspan=2, sticky='w', padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="Total Rent:").grid(row=9, column=0, sticky='w', padx=10, pady=10)
        self.total_rent_entry = Entry(self.billing_frame)
        self.total_rent_entry.grid(row=9, column=1, padx=10, pady=10)
        
        
        

    def on_return(self, **kwargs):
        print("Received kwargs:", kwargs)
        self.customer_id_entry.delete(0, tk.END)
        self.car_id_entry.delete(0, tk.END)
        
        customer_id = kwargs.get('customer_id')
        car_id = kwargs.get('car_id')
        
        if not car_id:
            print("Error: 'car_id' not found in kwargs")
            return
        
        db_conn = database_handler.DBHandler()
        customer_data = db_conn.read_one_customer(customer_id)
        car_data = db_conn.read_one_car(car_id)
        db_conn.close()
        
        self.clear_fields()
        
        if customer_data:
            self.customer_id_entry.insert(0, customer_data.id)
            self.customer_name_entry.insert(0, customer_data.name)
            self.license_number_entry.insert(0, customer_data.license_number)
            self.contact_number_entry.insert(0, customer_data.contact)
        
        if car_data:
            self.car_id_entry.insert(0, car_data.id)
            self.car_brand_entry.insert(0, car_data.brand)
            self.car_model_entry.insert(0, car_data.model)
            self.plate_number_entry.insert(0, car_data.plate_number)
            self.fuel_type_entry.insert(0, car_data.fuel_type)
            self.seating_capacity_entry.insert(0, car_data.seating_capacity)
            self.location_entry.insert(0, car_data.location)
            self.cost_per_day_entry.insert(0, car_data.cost_per_day)

    def clear_fields(self): 
        self.customer_id_entry.delete(0, tk.END)
        self.customer_name_entry.delete(0, tk.END)
        self.license_number_entry.delete(0, tk.END)
        self.contact_number_entry.delete(0, tk.END)

        self.car_id_entry.delete(0, tk.END)
        self.car_brand_entry.delete(0, tk.END)
        self.car_model_entry.delete(0, tk.END)
        self.plate_number_entry.delete(0, tk.END)
        self.fuel_type_entry.delete(0, tk.END)
        self.seating_capacity_entry.delete(0, tk.END)
        self.location_entry.delete(0, tk.END)
        self.cost_per_day_entry.delete(0, tk.END)

    def clear_billing_fields(self): 
        
        self.customer_name_entry_billing.delete(0, tk.END)
        self.rented_model_entry_billing.delete(0, tk.END)
        self.rented_date_entry_billing.delete(0, tk.END)
        self.rental_period_entry_billing.delete(0, tk.END)
        self.return_date_entry_billing.delete(0, tk.END)
        self.pickup_location_entry_billing.delete(0, tk.END)
        self.cost_per_day_billing_entry.delete(0, tk.END)
        self.total_rent_entry.delete(0, tk.END)
        
    def confirm_rent_clicked(self):
        current_datetime = datetime.now()
        rental_period = int(self.rental_period_entry.get())
        cost_per_day = float(self.cost_per_day_entry.get())  

        new_rental = models.Rental()
        new_rental.customer_id = self.customer_id_entry.get()
        new_rental.customer_name = self.customer_name_entry.get()  
        new_rental.car_id = self.car_id_entry.get()
        new_rental.rental_status = "UNAVAILABLE"
        new_rental.rented_model = self.car_model_entry.get()
        new_rental.rent_plateNo = self.plate_number_entry.get()
        new_rental.rental_period = rental_period
        new_rental.rent_datetime = current_datetime  # Store datetime object directly

        # Calculate return datetime
        return_datetime = current_datetime + timedelta(days=rental_period)

        new_rental.return_datetime = return_datetime  # Store datetime object directly

        new_rental.pickup_location = self.location_entry.get()
        new_rental.cost_per_day = cost_per_day
        new_rental.total_rent = cost_per_day * rental_period

        db_conn = database_handler.DBHandler()
        db_conn.add_rental(new_rental)
        db_conn.close()
        
        self.clear_billing_fields()
        
        self.customer_name_entry_billing.insert(0, new_rental.customer_name)
        self.rented_model_entry_billing.insert(0, new_rental.rented_model)
        self.rented_date_entry_billing.insert(0, new_rental.rent_datetime.strftime("%Y-%m-%d %H:%M:%S"))
        self.rental_period_entry_billing.insert(0, new_rental.rental_period)
        self.return_date_entry_billing.insert(0, new_rental.return_datetime.strftime("%Y-%m-%d %H:%M:%S"))
        self.pickup_location_entry_billing.insert(0, new_rental.pickup_location)
        self.cost_per_day_billing_entry.insert(0, new_rental.cost_per_day)
        self.total_rent_entry.insert(0, new_rental.total_rent)

        self.confirm_rent.focus_set()

        
    def go_to_login_page(self): 
        self.parent.change_window('Login_Page')