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
        
        #----- LOGO IMAGE 
        self.logo = tk.PhotoImage(file="traverse logo.png")
        tk.Label(self, image=self.logo, bg='white').grid(row=0, column=0, padx=(150,0), pady=(0, 150), rowspan=12)
        
        #----- LOGIN HEADING
        self.heading = tk.Label(self, text="Log in", fg='#4caf50', font=('Inter', 23), bg='white')
        self.heading.grid(row=0, column=1, columnspan=10, pady=(170, 0), sticky='n', padx=(5,0))
        
        
        #----- ACCOUNT TYPE
        self.account_type = tk.StringVar()
        self.account_type.set("Admin")
        
        self.admin_radio = tk.Radiobutton(self, text="Admin", variable=self.account_type, value="admin", width=7, bg='white', command=self.hide_customer_widgets)
        self.admin_radio.grid(row=0, column=1, sticky='w', padx=(80, 60), pady=(0, 420))
        
        self.customer_radio = tk.Radiobutton(self, text="Customer", variable=self.account_type, value="customer", width=7, bg='white', command=self.toggle_customer_widgets)
        self.customer_radio.grid(row=0, column=1, padx=(120, 0), pady=(0, 420))
        
        #----- NAME FIELDS
        self.name_field = tk.Entry(self, width=40, fg='black', border=0, font=('Inter', 11))
        self.name_field.grid(row=0, column=1, sticky='w', pady=(30,350), padx=(40, 0))
        self.name_field.insert(0, 'Name')
        tk.Frame(self, width=320, height=2, bg='black').grid(row=0, column=1, pady=(80, 350), padx=(15, 0) )
        self.name_field.bind('<FocusIn>', self.on_enter)
        self.name_field.bind('<FocusOut>', self.on_leave)

        #----- PASSWORD FIELDS
        self.code_field = tk.Entry(self, width=35, fg='black', border=0, font=('Inter', 11))
        self.code_field.grid(row=0, column=1, pady=(150, 350))
        self.code_field.insert(0, "Password")
        tk.Frame(self, width=320, height=2, bg='black').grid(row=0, column=1, pady=(200, 350), padx=(15, 0) )
        self.code_field.bind('<FocusIn>', self.on_enter)
        self.code_field.bind('<FocusOut>', self.on_leave)

        #----- SIGNIN BUTTON
        self.signin_button = tk.Button(self, width=39, pady=7, text='Sign in', bg='#4caf50', fg='white', border=0, command=self.login_clicked)
        self.signin_button.grid(row=0, column=1, pady=(290, 350), padx=(20, 0))
        
        #------- For Customer Widgets
        self.label = tk.Label(self, text="New to our services?", fg='black', bg='white', font=('Inter', 9))

        #-----SIGNUP BUTTON 
        self.signup_btn = tk.Button(self, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#4caf50', command=self.go_to_signup_page)
        
        #----- CAPTCHA SECTION
        
        self.captcha = tk.Label(self, width=27, height=4, fg='#4caf50', font=('Roboto', 15, 'italic'), border=1)
        self.label_captcha = tk.Label(self, text='To continue, type the characters you see in the picture.', bg='white')
        self.entry_captcha = tk.Entry(self, width=53, fg='black', border=1)
        self.button_captcha = tk.Button(self, text="Submit", width=12, cursor='hand2', bg='#4caf50', command=self.login)
        
        #----- MENU ADMIN
        self.menu_button = tk.Button(self, text='MENU', width=10, height=2, command=self.go_to_admin_dashboard)
        self.menu_button.grid(row=0, column=0, sticky='s')
        
        self.hide_customer_widgets()
        self.hide_captcha_section()

    def go_to_admin_dashboard(self): 
        self.parent.change_window('Admin_Dashboard')
        
    def hide_customer_widgets(self): 
        self.label.grid_forget()
        self.signup_btn.grid_forget()

    def show_customer_widgets(self): 
        self.label.grid(row=0, column=1, pady=(400, 350), padx=(110, 0), sticky='w')
        self.signup_btn.grid(row=0, column=1, pady=(400, 350), padx=(140, 0))
        
    def toggle_customer_widgets(self): 
        self.hide_captcha_section()
        if self.account_type.get() == "customer": 
            self.on_return()
            self.show_customer_widgets()
        else: 
            self.hide_customer_widgets()
            self.on_return()
    
    def login_clicked(self): 
        if self.name_field.get() != '' and self.code_field.get() != '': 
            self.toggle_captcha_section()
        elif self.name_field.get() == '' or self.code_field.get() == '': 
            messagebox.showerror("Error", "Name and Password are Required")
    
    def show_captcha_section(self): 
        # self.hide_customer_widgets()
        self.captcha.grid(row=0, column=1, pady=(470,350), padx=(10, 0))
        self.label_captcha.grid(row=0, column=1, pady=(580, 350))
        self.entry_captcha.grid(row=0, column=1, pady=(300, 10))
        self.button_captcha.grid(row=0, column=1, pady=(410, 10))

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
                    elif account_type == 'customer':
                        messagebox.showinfo("Welcome!", "Login Successful. Hello, customer!")
                        self.reset_failed_attempts(name)
                        
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
        self.locked_accounts[name] = datetime.now() + timedelta(hours=24)
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
              
class SignupPage(tk.Frame): 
    def __init__(self, master): 
        tk.Frame.__init__(self, master)
        self.parent = master
        
         #----- LOGO IMAGE 
        self.logo = tk.PhotoImage(file="traverse logo.png")
        tk.Label(self, image=self.logo).grid(row=0, column=0)
             
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
        
        # image = Image.open("3traverse logo.png")
        # image = image.resize((50, 50))
        # self.tk_image = ImageTk.PhotoImage(image)
        # self.logout_button = tk.Button(self, image=self.tk_image, width=100,command=self.go_to_login_page)
        
        
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
        
    
class FleetPage(tk.Frame): 
    def __init__(self, master): 
        tk.Frame.__init__(self, master)
        self.parent = master
        self.configure(bg='white')
        
        self.logo = tk.PhotoImage(file='250traverse logo.png')
        tk.Label(self, image=self.logo, bg='white').grid(row=0, column=0, sticky='w', rowspan=8, padx=(200,0), pady=(0,0))
        
        #----- HEADING PAGE TITLE
        self.heading = tk.Label(self, text='Traverse Car Fleet', fg='#4caf50', font=('Roboto', 40, 'bold'), bg='white')
        self.heading.grid(row=0, column=1, padx=(0,0), sticky='e', pady=(100,0))
          
class RevenuePage(tk.Frame): 
    def __init__(self, master): 
        tk.Frame.__init__(self, master)
        self.parent = master
        self.configure(bg='white')
        
        self.logo = tk.PhotoImage(file='250traverse logo.png')
        tk.Label(self, image=self.logo, bg='white').grid(row=0, column=0, sticky='w', rowspan=8, padx=(200,0), pady=(0,0))
        
        #----- HEADING PAGE TITLE
        self.heading = tk.Label(self, text='Car Rental Revenue', fg='#4caf50', font=('Roboto', 40, 'bold'), bg='white')
        self.heading.grid(row=0, column=1, padx=(0,0), sticky='e', pady=(100,0))
        