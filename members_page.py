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
        
        #----- TABLE 
        columns = ('id', 'name', 'email', 'contact', 'license_number')
        
        self.table = ttk.Treeview(self, columns=columns, show='headings')
        
        self.table.heading('id', text='Member ID')
        self.table.heading('name', text='Name')
        self.table.heading('email', text='Email')
        self.table.heading('contact', text='Contact No.')
        self.table.heading('license_number', text='License Number')
        
        self.table.grid(row=2, column=0, padx=(100, 100))
        
        #----- SEARCH FIELD
        self.search_field = tk.Entry(self)
        self.search_field.grid(row=0, column=1, columnspan=2, sticky='we', padx=10, pady=10)
        
        self.update_table()
        
        self.search_field.bind('<KeyRelease>', self.update_table)
        
        tk.Label(self, text="Search by Name: ").grid(row=0, column=0, sticky='e')
        
        
    
    def update_table(self, event=None):
        self.get_employee_list()

        self.table.delete(*self.table.get_children())

        for account in self.employee_list:
            row = (account.id, account.name, account.email, account.contact, account.license_number)
            self.table.insert('', tk.END, values=row)

    def get_employee_list(self):
        key = self.search_field.get()
        db_conn = database_handler.DBHandler()
        self.employee_list = db_conn.search_employee(key)
        db_conn.close()
        
        