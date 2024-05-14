import sqlite3
import models

class DBHandler:
    def __init__(self):
        self.db_name = 'database.db'
        self.accounts_table = 'accounts'
        self.carfleet_table = 'cars'
        self.rentals_table = 'rental'

        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

#---------- ACCOUNT DATABASE
    def read_accounts(self):
        accounts = []

        query = f'SELECT * FROM {self.accounts_table}'
        self.cursor.execute(query)
        
        for row in self.cursor:
            new_account = models.Accounts()
            new_account.id = row[0]
            new_account.account_type = row[1]
            new_account.name = row[2]
            new_account.email = row[3]
            new_account.contact = row[4]
            new_account.password = row[5]
            new_account.license_number = row[6]
            accounts.append(new_account)

        return accounts
    
    def add_customer(self, accounts: models.Accounts):
        query = "INSERT INTO accounts (account_type, name, email, contact, password, license_number) VALUES (?, ?, ?, ?, ?, ?)"
        values = (accounts.account_type, accounts.name, accounts.email, accounts.contact, accounts.password, accounts.license_number)
        self.cursor.execute(query, values)
        self.conn.commit()
        
    def delete_customer(self, id: int): 
        query = f"DELETE FROM {self.accounts_table} WHERE id = ?"
        values = (id, )

        self.cursor.execute(query, values)
        self.conn.commit()
        
    def read_one_customer(self, id): 
        query = f"SELECT * FROM {self.accounts_table} WHERE id = ?" 
        values = (id, )
        self.cursor.execute(query, values)
        
        for row in self.cursor: 
            new_customer = models.Accounts()
            new_customer.id= row[0]
            new_customer.account_type = row[1]
            new_customer.name = row[2]
            new_customer.email = row[3]
            new_customer.contact = row[4]
            new_customer.password = row[5]
            new_customer.license_number = row[6]
            return new_customer
    
    def update_customer(self, customer : models.Accounts): 
        query = f"UPDATE accounts SET name = ?, email = ?, contact = ?, license_number = ?, password = ? WHERE id = ? "
        values = (customer.name, customer.email, customer.contact, customer.license_number, customer.password, customer.id)
        
        self.cursor.execute(query, values)
        self.conn.commit()
        
    def search_employee(self, key):
        key = '%' + key + '%'
        query = f'SELECT * FROM {self.accounts_table} WHERE name LIKE ?'
        values = (key, )
        self.cursor.execute(query, values)

        accounts = []
        for row in self.cursor:
            new_account = models.Accounts()
            new_account.id = row[0]
            new_account.account_type = row[1]
            new_account.name = row[2]
            new_account.email = row[3]
            new_account.contact = row[4]
            new_account.license_number = row[6]
            new_account.password = row[5]
            accounts.append(new_account)

        return accounts

    def close(self):
        self.conn.close()

#---------- CAR DATABASE

    def search_car(self, key):
            key = '%' + key + '%'
            query = f'SELECT * FROM {self.carfleet_table} WHERE brand LIKE ?'
            values = (key, )
            self.cursor.execute(query, values)

            cars = []
            for row in self.cursor:
                new_car = models.Cars()
                new_car.id = row[0]
                new_car.car_image = row[1]
                new_car.brand = row[2]
                new_car.model = row[3]
                new_car.plate_number = row[4]
                new_car.fuel_type = row[5]
                new_car.availability = row[6]
                new_car.cost_per_day = row[7]
                new_car.seating_capacity = row[8]
                new_car.location = row[9]
                cars.append(new_car)

            return cars
        
    def delete_car(self, id : int):
        query = f"DELETE FROM {self.carfleet_table} WHERE id = ?"
        values = (id, )

        self.cursor.execute(query, values)
        self.conn.commit()
        
    def read_one_car(self, id): 
        query = f"SELECT * FROM {self.carfleet_table} WHERE id = ?" 
        values = (id, )
        self.cursor.execute(query, values)
        
        for row in self.cursor: 
            new_car = models.Cars()
            new_car.id= row[0]
            new_car.car_image = row[1]
            new_car.brand = row[2]
            new_car.model = row[3]
            new_car.plate_number = row[4]
            new_car.fuel_type = row[5]
            new_car.availability = row[6]
            new_car.cost_per_day = row[7]
            new_car.seating_capacity = row[8]
            new_car.location = row[9]
            return new_car

    def update_car(self, car : models.Cars): 
        query = f"UPDATE cars SET brand = ?, model = ?, plate_number = ?, fuel_type = ?, availability = ?, cost_per_day = ?, seating_capacity = ?, location = ? WHERE id = ? "
        values = (car.brand, car.model, car.plate_number, car.fuel_type, car.availability, car.cost_per_day, car.seating_capacity, car.location, car.id)
        
        self.cursor.execute(query, values)
        self.conn.commit()

#---------- RENTAL DATABASE
    def search_rental(self): 
        # key = '%' + key + '%'
        # query = f'SELECT * FROM {self.rentals_table} WHERE rental_status LIKE ?'
        # values = (key, )
        # self.cursor.execute(query, values)

        query = f'SELECT * FROM {self.rentals_table}'
        self.cursor.execute(query)
        
        rentals = []
        for row in self.cursor:
            new_rental = models.Rental()
            new_rental.id = row[0]
            new_rental.customer_id = row[1]
            new_rental.customer_name = row[2]
            new_rental.car_id = row[3]
            new_rental.rental_status = row[4]
            new_rental.rented_model = row[5]
            new_rental.rent_plateNo = row[6]
            new_rental.rental_period = row[7]
            new_rental.rent_date = row[8]
            new_rental.rent_time = row[9]
            new_rental.return_date = row[10]
            new_rental.pickup_location = row[11]
            new_rental.cost_per_day = row[12]
            new_rental.total_rent = row[13]

            rentals.append(new_rental)

        return rentals


    def read_one_rental(self, id: int): 
        query = f"SELECT * FROM {self.rentals_table} WHERE id = ?" 
        values = (id,)
        self.cursor.execute(query, values)
        
        for row in self.cursor: 
            new_rental = models.Rental()
            new_rental.id = row[0]
            new_rental.customer_id = row[1]
            new_rental.customer_name = row[2]
            new_rental.car_id = row[3]
            new_rental.rental_status = row[4]
            new_rental.rented_model = row[5]
            new_rental.rent_plateNo = row[6]
            new_rental.rental_period = row[7]
            new_rental.rent_date = row[8]
            new_rental.rent_time = row[9]
            new_rental.return_date = row[10]
            new_rental.pickup_location = row[11]
            new_rental.cost_per_day = row[12]
            new_rental.total_rent = row[13]

            return new_rental
        
    # def add_rental(self, rental: models.Rental):
    #     query = "INSERT INTO rental (customer_id, customer_name, car_id, rental_status, rented_model, rent_plateNo, rental_period, rent_date, rent_time, return_date, pickup_location, cost_per_day, total_rent) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    #     values = (rental.customer_id, rental.customer_name, rental.car_id, rental.rental_status, rental.rented_model, rental.rent_plateNo, rental.rental_period, rental.rent_date, rental.rent_time, rental.return_date, rental.pickup_location, rental.cost_per_day, rental.total_rent)
    #     self.cursor.execute(query, values)
    #     self.conn.commit()
    
    def add_rental(self, rental: models.Rental):
        query = "INSERT INTO rental (customer_id, customer_name, car_id, rental_status, rented_model, rent_plateNo, rental_period, rent_datetime, return_datetime, pickup_location, cost_per_day, total_rent) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        values = (rental.customer_id, rental.customer_name, rental.car_id, rental.rental_status, rental.rented_model, rental.rent_plateNo, rental.rental_period, rental.rent_date.strftime("%Y-%m-%d %H:%M:%S"), rental.return_date.strftime("%Y-%m-%d %H:%M:%S"), rental.pickup_location, rental.cost_per_day, rental.total_rent)
        self.cursor.execute(query, values)
        self.conn.commit()




DBHandler().read_accounts()