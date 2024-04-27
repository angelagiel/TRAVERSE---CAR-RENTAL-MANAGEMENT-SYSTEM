import tkinter as tk
from PIL import Image, ImageTk

# Create a Tkinter window
root = tk.Tk()

# Load the image
image = Image.open("3traverse logo.png")
# Resize the image if needed
image = image.resize((100, 100))

# Convert the image to Tkinter format
tk_image = ImageTk.PhotoImage(image)

# Create a button with the image
button = tk.Button(root, image=tk_image, command=lambda: print("Button clicked"))
button.pack()

# Run the Tkinter event loop
root.mainloop()
