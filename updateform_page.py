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
        
        
        #----- NAME FIELDS
        tk.Label(self, text='Customer Name', font=('Inter', 11), fg='black', bg='white').grid(row=2, column=0, padx=(0, 300))
        
        self.name_field = Entry(self, width=70, border=0, fg='black', bg='white', font=('Microsoft yahei UI Light', 11))
        self.name_field.grid(row=2, column=0, padx=(500, 100))
        self.name_field.insert(0, 'Name')
        self.name_field.bind('<FocusIn>', self.on_enter)
        self.name_field.bind('<FocusOut>', self.on_leave)
        
        #----- EMAIL FIELDS
        self.email_field = Entry(self, width=20, border=0, fg='black', bg='white', font=('Microsoft Yahei UI Light', 11))
        self.email_field.grid(row=3, column=0)
        self.email_field.insert(0, 'Email Address')
        self.email_field.bind('<FocusIn>', self.on_enter)
        self.email_field.bind('<FocusOut>', self.on_leave)
        #----- CONTACT NUMBER FIELDS
        self.contact_field = Entry(self, width=20, border=0, fg='black', bg='white', font=('Microsoft Yahei UI Light', 11))
        self.contact_field.grid(row=4, column=0)
        self.contact_field.insert(0, 'Contact Number')
        self.contact_field.bind('<FocusIn>', self.on_enter)
        self.contact_field.bind('<FocusOut>', self.on_leave)
        #----- PASSWORD FIELDS
        self.code_field = Entry(self, width=20, border=0, fg='black', bg='white', font=('Microsoft Yahei UI Light', 11))
        self.code_field.grid(row=5, column=0)
        self.code_field.insert(0, 'Password')
        self.code_field.bind('<FocusIn>', self.on_enter)
        self.code_field.bind('<FocusOut>', self.on_leave)
        #----- LICENSE NUMBER FIELDS
        self.license_field = Entry(self, width=20, border=0, fg='black', bg='white', font=('Microsoft yahei UI Light', 11))
        self.license_field.grid(row=6, column=0)
        self.license_field.insert(0, "Driver's License Number")
        self.license_field.bind('<FocusIn>', self.on_enter)
        self.license_field.bind('<FocusOut>', self.on_leave)
        
        
        
    #----- FUNCTIONS
    
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