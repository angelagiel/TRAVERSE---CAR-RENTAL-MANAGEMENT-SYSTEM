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
        self.customer_frame = tk.Frame(self, width=600, height=400, border=1)
        self.customer_frame.grid(row=1, column=1)
        
        tk.Label(self.customer_frame, text="Customer ID:", bg='white').grid(row=0, column=0, sticky='w', padx=10, pady=10)
        tk.Entry(self.customer_frame).grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(self.customer_frame, text="Customer Name:", bg='white').grid(row=1, column=0, sticky='w', padx=10, pady=10)
        tk.Entry(self.customer_frame).grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(self.customer_frame, text="Customer Address:", bg='white').grid(row=2, column=0, sticky='w', padx=10, pady=10)
        tk.Entry(self.customer_frame).grid(row=2, column=1, padx=10, pady=10)
        
        tk.Label(self.customer_frame, text="Customer Phone:", bg='white').grid(row=3, column=0, sticky='w', padx=10, pady=10)
        tk.Entry(self.customer_frame).grid(row=3, column=1, padx=10, pady=10)
        
        #----- CAR FRAME FIELDS
        
        
        
        #----- BILLING FRAME FIELDS
        
        self.billing_frame = tk.Frame(self, width=600, height=400, border=1)
        self.billing_frame.grid(row=1, column=2, columnspan=4)
        
        tk.Label(self.billing_frame, text="Billing Date:", bg='white').grid(row=0, column=0, sticky='w', padx=10, pady=10)
        tk.Entry(self.billing_frame).grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="Billing Time:", bg='white').grid(row=1, column=0, sticky='w', padx=10, pady=10)
        tk.Entry(self.billing_frame).grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="Rental Period:", bg='white').grid(row=2, column=0, sticky='w', padx=10, pady=10)
        tk.Entry(self.billing_frame).grid(row=2, column=1, padx=10, pady=10)
        
        tk.Label(self.billing_frame, text="Pickup Location:", bg='white').grid(row=3, column=0, sticky='w', padx=10, pady=10)
        tk.Entry(self.billing_frame).grid(row=3, column=1, padx=10, pady=10)
        
        tk.Button(self.billing_frame, text="Submit").grid(row=4, columnspan=2, pady=10)
        
        
        
    def on_return(self): 
        pass