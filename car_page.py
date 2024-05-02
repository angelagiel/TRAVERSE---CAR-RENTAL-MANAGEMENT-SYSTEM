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