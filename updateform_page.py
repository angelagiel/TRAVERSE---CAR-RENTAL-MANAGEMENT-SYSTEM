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
        self.id = kwargs['customer_id']
        self.id_field.config(text=self.id)

        db_conn = database_handler.DBHandler()
        customer_data = db_conn.read_one_customer(self.id)
        db_conn.close()

        self.clear_fields()

        self.name_field.insert(0, customer_data.name)
        self.email_field.insert(0, customer_data.email)
        self.contact_field.insert(0, customer_data.contact)
        self.license_field.insert(0, customer_data.license_number)
        self.code_field.insert(0, customer_data.password)
        self.confirm_field.insert(0, customer_data.password)
        

    def clear_fields(self):
        self.name_field.delete(0, tk.END)
        self.email_field.delete(0, tk.END)
        self.contact_field.delete(0, tk.END)
        self.license_field.delete(0, tk.END)
        self.code_field.delete(0, tk.END)

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
            messagebox.showerror("Update Employee", "Age and Salary Rate must be numbers")
    
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