import sqlite3
import models

class DBHandler:
    def __init__(self):
        self.db_name = 'database.db'
        self.accounts_table = 'accounts'

        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
    
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
        
    def read_one_customer(self, id : int): 
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

DBHandler().read_accounts()