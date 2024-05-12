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