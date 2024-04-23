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
        columns = ('id', 'name', 'email', 'contact', 'license_number', 'rental status', 'model', 'plate number', 'rental period')
        
        self.table = ttk.Treeview(self, columns=columns, show='headings')
        
        self.table.heading('id', text='ID')
        self.table.heading('name', text='Name')
        self.table.heading('email', text='Email')
        self.table.heading('contact', text='Contact No.')
        self.table.heading('license_number', text='License Number')
        self.table.heading('rental status', text='Rental Status')
        self.table.heading('model', text='Model')
        self.table.heading('plate number', text='Plate Number')
        self.table.heading('rental period', text='Rental Period')
        
        self.table.grid(row=2, column=0, padx=(100, 100))

        # Set the width of each column
        self.table.column('id', width=30)
        self.table.column('name', width=120)
        self.table.column('email', width=150)
        self.table.column('contact', width=100)
        self.table.column('license_number', width=120)
        self.table.column('rental status', width=100)
        self.table.column('model', width=120)
        self.table.column('plate number', width=120)
        self.table.column('rental period', width=120)
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

        self.table.delete(*self.table.get_children())

        for account in self.employee_list:
            if account.account_type == 'customer':
                row = (account.id, account.name, account.email, account.contact, account.license_number)
                self.table.insert('', tk.END, values=row)

    def get_employee_list(self):
        key = self.search_field.get()
        db_conn = database_handler.DBHandler()
        self.employee_list = db_conn.search_employee(key)
        db_conn.close()
        
    def go_to_admin_dashboard(self): 
        self.parent.change_window('Admin_Dashboard')
    
    def go_to_update_form(self): 
        self.parent.change_window('Update_Form')
    
    def delete_customer(self): 
        pass