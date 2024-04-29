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


class CarPage(tk.Frame): 
    def __init__(self, master): 
        tk.Frame.__init__(self, master)
        self.parent = master
        self.configure(bg='white')
        
         #----- TRAVERSE LOGO
        logo = Image.open("3traverse logo.png")
        logo = logo.resize((200, 200))
        self.logo = ImageTk.PhotoImage(logo)
        
        tk.Label(self, image=self.logo, bg='white').grid(row=0, column=0)
        
        #----- HEADING PAGE TITLE
        self.heading = tk.Label(self, text='Car Information Details', fg='#4caf50', font=('Roboto', 40, 'bold'), bg='white')
        self.heading.grid(row=0, column=0, columnspan=5, pady=(0, 0), padx=(100, 0))
        #----- CAR IMAGE 
        car = Image.open('toyota.png')
        # car = car.resize((500, 200))
        self.car = ImageTk.PhotoImage(car)
        tk.Label(self, image=self.car, bg='white', borderwidth=1).grid(row=2, column=0, padx=(0, 0), sticky='nws')
        
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
    
    
    def on_enter(self, e): 
        widget = e.widget
        widget.delete(0, 'end')
        
    def on_leave(self, e):
        widget = e.widget
        name = widget.get()
        if name == '':
            widget.insert(0, 'Name' if widget == self.name_field else 'Password')
    
    def on_return(self): 
        pass