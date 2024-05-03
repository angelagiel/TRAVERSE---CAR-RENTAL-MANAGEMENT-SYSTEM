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
        self.customer_frame = tk.Frame(self, width=600, border=1)
        self.customer_frame.grid(row=1, column=0, sticky='nw', pady=(0,0), padx=(100,0))
        
        tk.Label(self.customer_frame, text="Customer ID:", bg='white').grid(row=0, column=0, sticky='w')
        tk.Entry(self.customer_frame).grid(row=0, column=1)
        
        tk.Label(self.customer_frame, text="Customer Name:", bg='white').grid(row=1, column=0, sticky='w')
        tk.Entry(self.customer_frame).grid(row=1, column=1)
        
        tk.Label(self.customer_frame, text="Driver's License Number:", bg='white').grid(row=2, column=0, sticky='w')
        tk.Entry(self.customer_frame).grid(row=2, column=1)
        
        tk.Label(self.customer_frame, text="Contact Number:", bg='white').grid(row=3, column=0, sticky='w')
        tk.Entry(self.customer_frame).grid(row=3, column=1)
        
        #----- CAR FRAME FIELDS
        
        self.car_frame = tk.Frame(self,border=1)
        self.car_frame.grid(row=1, column=0, sticky='nw', pady=(100,0))
        self.car_frame.config(bg='white')
        
        car = Image.open("toyota.png")
        car = car.resize((150, 70))
        self.car = ImageTk.PhotoImage(car)
        
        tk.Label(self.car_frame, image=self.car, bg='white').grid(row=3, column=0, padx=(100, 0))
        
        
        
        tk.Label(self.car_frame, text='Selected Car Information',fg='#4caf50', font=('Roboto', 15, 'bold')).grid(row=0, column=0)
        
        tk.Label(self.car_frame, text="Car ID:", bg='white').grid(row=1, column=2, sticky='w')
        tk.Entry(self.car_frame).grid(row=1, column=3)
        
        tk.Label(self.car_frame, text="Brand:", bg='white').grid(row=2, column=2, sticky='w')
        tk.Entry(self.car_frame).grid(row=2, column=3)
        
        tk.Label(self.car_frame, text="Model:", bg='white').grid(row=3, column=2, sticky='w')
        tk.Entry(self.car_frame).grid(row=3, column=3)
        
        tk.Label(self.car_frame, text="Plate Number:", bg='white').grid(row=4, column=2, sticky='w')
        tk.Entry(self.car_frame).grid(row=4, column=3)
        
        tk.Label(self.car_frame, text="Fuel Type:", bg='white').grid(row=5, column=2, sticky='w')
        tk.Entry(self.car_frame).grid(row=5, column=3)
        
        tk.Label(self.car_frame, text="Seating Capacity:", bg='white').grid(row=6, column=2, sticky='w')
        tk.Entry(self.car_frame).grid(row=6, column=3)
        
        tk.Label(self.car_frame, text="Pickup Location:", bg='white').grid(row=7, column=2, sticky='w')
        tk.Entry(self.car_frame).grid(row=7, column=3)
        
        tk.Label(self.car_frame, text="Cost Per Day:", bg='white').grid(row=8, column=2, sticky='w')
        tk.Entry(self.car_frame).grid(row=8, column=3)
        
        
        #----- BILLING FRAME FIELDS
        
        self.billing_frame = tk.Frame(self, width=600, height=400, border=1, highlightthickness=2, highlightbackground="#000", highlightcolor="#000", bd=0)
        self.billing_frame.grid(row=1, column=2, columnspan=4)
        # self.billing_frame.config(bg='white')
        
        tk.Label(self.billing_frame, text="Billing Receipt", fg='black', font=('Roboto', 15, 'bold')).grid(row=0, column=0, padx=(10,0))
        
        tk.Label(self.billing_frame, text="Customer Name:").grid(row=1, column=0, sticky='w', padx=10, pady=10)
        tk.Entry(self.billing_frame).grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="Rented Model:").grid(row=2, column=0, sticky='w', padx=10, pady=10)
        tk.Entry(self.billing_frame).grid(row=2, column=1, padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="Rented Date:").grid(row=3, column=0, sticky='w', padx=10, pady=10)
        tk.Entry(self.billing_frame).grid(row=3, column=1, padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="Rented Time:").grid(row=4, column=0, sticky='w', padx=10, pady=10)
        tk.Entry(self.billing_frame).grid(row=4, column=1, padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="Rental Period:").grid(row=5, column=0, sticky='w', padx=10, pady=10)
        tk.Entry(self.billing_frame).grid(row=5, column=1, padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="Return Date:").grid(row=6, column=0, sticky='w', padx=10, pady=10)
        tk.Entry(self.billing_frame).grid(row=6, column=1, padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="Pickup Location:").grid(row=7, column=0, sticky='w', padx=10, pady=10)
        tk.Entry(self.billing_frame).grid(row=7, column=1, padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="Cost Per Day:").grid(row=8, column=0, sticky='w', padx=10, pady=10)
        tk.Entry(self.billing_frame).grid(row=8, column=1, padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="================================:").grid(row=9, column=0, columnspan=2, sticky='w', padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="Total Rent:").grid(row=10, column=0, sticky='w', padx=10, pady=10)
        tk.Entry(self.billing_frame).grid(row=10, column=1, padx=10, pady=10)
        

        
        
        
    def on_return(self): 
        pass