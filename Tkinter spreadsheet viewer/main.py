from tkinter import *
from tkinter import messagebox, ttk, filedialog
import pandas as pd

root = Tk()
root.title('Excel Datasheet Viewer')
root.geometry('1100x500+200+200')

def open_file():
    filename = filedialog.askopenfilename(
        title="Open a file",
        filetypes=(("Excel files", "*.xlsx *.xls"), ("All files", "*.*"))
    )
    
    if filename:
        try:
            # Read the excel file
            df = pd.read_excel(filename)
            
            # Clear previous data
            tree.delete(*tree.get_children())

            # Update columns
            tree['columns'] = list(df.columns)
            tree['show'] = "headings"

            for col in tree['columns']:
                tree.heading(col, text=col)
                tree.column(col, width=100) # Set a default width

            # Insert data
            df_rows = df.fillna("").values.tolist()
            for row in df_rows:
                tree.insert("", "end", values=row)
                
        except Exception as e:
            messagebox.showerror("Error", f"Could not read file: {e}")

# Try-except to prevent crash if icon file is missing
try:
    image_icon = PhotoImage(file="favicon.png")
    root.iconphoto(False, image_icon)
except:
    pass 

# Frame for Treeview and Scrollbars
frame = Frame(root)
frame.pack(pady=20, fill=BOTH, expand=True)

# Add Scrollbars
tree_scroll_y = Scrollbar(frame)
tree_scroll_y.pack(side=RIGHT, fill=Y)

tree_scroll_x = Scrollbar(frame, orient='horizontal')
tree_scroll_x.pack(side=BOTTOM, fill=X)

tree = ttk.Treeview(frame, yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set)
tree.pack(fill=BOTH, expand=True)

tree_scroll_y.config(command=tree.yview)
tree_scroll_x.config(command=tree.xview)

# Button
button = Button(root, text='Open Excel File', width=40, height=2, 
                fg='white', bg='#0078d7', font=('Arial', 12, 'bold'), 
                command=open_file)
button.pack(pady=20)

root.mainloop()
