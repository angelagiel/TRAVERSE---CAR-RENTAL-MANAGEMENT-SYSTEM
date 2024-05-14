from datetime import datetime



class Accounts:
    def __init__(self):
        self.id = 0
        self.account_type = ''
        self.name = ''
        self.email = ''
        self.contact = 0
        self.password = ''
        self.license_number = ''
        
        
class Cars: 
    def __init__(self): 
        self.id = 0
        self.car_image = ''
        self.brand = ''
        self.model =''
        self.plate_number = ''
        self.fuel_type = ''
        self.availability = ''
        self.cost_per_day = 0
        self.seating_capacity = 0
        self.location = ''


class Rental:
    def __init__(self):
        self.id = 0
        self.customer_id = 0
        self.customer_name = ''
        self.car_id = 0
        self.rental_status = ''
        self.rented_model = ''
        self.rent_plateNo = ''
        self.rental_period = 0  # Initialize with 0
        self.rent_date = datetime.now().date()  # Initialize with current date
        self.rent_time = datetime.now().time()  # Initialize with current time
        self.return_date = datetime.now().date()  # Initialize with current date
        self.pickup_location = ''
        self.cost_per_day = 0.0
        self.total_rent = 0.0
