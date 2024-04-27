import tkinter as tk

def button_click(row, col):
    print(f"Button clicked in row {row}, column {col}")

root = tk.Tk()

# Create a grid of frames
for i in range(6):  # 3 rows
    for j in range(6):  # 3 columns
        frame = tk.Frame(root, width=100, height=50, borderwidth=1, relief="solid")
        frame.grid(row=i, column=j)
        button = tk.Button(frame, text=f"Button {i}-{j}", command=lambda r=i, c=j: button_click(r, c))
        # button.pack(fill="both", expand=True)
        button.grid(row=i, column=j)

root.mainloop()
