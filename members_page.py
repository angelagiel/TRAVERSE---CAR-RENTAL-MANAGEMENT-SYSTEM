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