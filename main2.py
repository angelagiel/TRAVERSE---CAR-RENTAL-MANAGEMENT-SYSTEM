import tkinter as tk 
import pages
import members_page
import updateform_page
import fleet_page
import car_page
# import rent_car

class MainWindow(tk.Tk):
    def __init__(self): 
        tk.Tk.__init__(self)
        self.title("Car Rental Management System")
        self.configure(bg='white')
        self.geometry("1200x700")
        self.frames = dict()
        self.frames['Login_Page'] = pages.LoginPage(self)
        self.frames["Signup_Page"] = pages.SignupPage(self)
        self.frames['Admin_Dashboard'] = pages.AdminDashboard(self)
        self.frames['Members_Page'] = members_page.MembersPage(self)
        self.frames['Revenue_Page'] = pages.RevenuePage(self)
        self.frames['Update_Form'] = updateform_page.UpdateForm(self)
        self.frames['Fleet_Page'] = fleet_page.FleetPage(self)
        self.frames['View_Car'] = car_page.CarPage(self)
        # self.frames['Rent_Car'] = rent_car.RentCar(self)
        
        # self.change_window('Update_Form')
        # self.change_window('Members_Page')
        # self.change_window('View_Car')
        # self.change_window('Login_Page')
        self.change_window('Admin_Dashboard')

    def change_window(self, name, **kwargs): 
        print("Changine the window to", name)
        for frame in self.frames.values(): 
            frame.grid_forget()

        self.frames[name].on_return(**kwargs)
        self.frames[name].grid(row=0, column=0)

root = MainWindow()
root.mainloop()