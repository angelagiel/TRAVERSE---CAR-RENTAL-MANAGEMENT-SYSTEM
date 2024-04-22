import tkinter as tk 
import pages
import members_page

class MainWindow(tk.Tk):
    def __init__(self): 
        tk.Tk.__init__(self)
        self.title("Car Rental Management System")
        self.configure(bg='white')
        self.geometry("1200x700")
        self.frames = dict()
        self.frames['Login_Page'] = pages.LoginPage(self)
        self.frames["Signup_Page"] = pages.SignupPage(self)
        self.frames["Admin_Dashboard"] = pages.AdminDashboard(self)
        self.frames['Fleet_Page'] = pages.FleetPage(self)
        self.frames['Members_Page'] = members_page.MembersPage(self)
        self.frames['Revenue_Page'] = pages.RevenuePage(self)
        
        # self.change_window('Login_Page')
        self.change_window('Members_Page')

    def change_window(self, name, **kwargs): 
        print("Changine the window to", name)
        for frame in self.frames.values(): 
            frame.grid_forget()

        # self.frames[name].on_return(**kwargs)
        self.frames[name].grid(row=0, column=0)

root = MainWindow()
root.mainloop()