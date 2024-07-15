from tkinter import *
from tkinter import ttk
import os
import openpyxl

BACKGROUND_COLOR = "#cce7ff"
FG_COLOR = "#000000"

def enter_data():
  
    # User info
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    age = age_spinbox.get()
    country = country_combobox.get()
    state = state_entry.get() 
    zip_code = zip_code_entry.get()
    address = address_entry.get()
            
    # Delivery info
    product_category = product_category_combobox.get()
    product_name = product_name_entry.get()
    quantity_ordered = product_quantity_spinbox.get()

    print("------------------------------------------")        
    print("First name: ", firstname, "Last name: ", lastname, "Age: ", age)
    print("Country: ", country, "State: ", state, "zip_code: ", zip_code)
    print("Address: ", address)
    print("Product Category: ", product_category)
    print("Product Name: ", product_name, "Quantity Ordered: ", quantity_ordered)
    print("------------------------------------------")

    # files path where it is saved   
    filepath = "c:\\documents\\data.xlsx"
            
    if not os.path.exists(filepath):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        heading = ["First Name", "Last Name", "Age", "Country", "State", "Zip code", "Address",
                         "Product Category"  ,"Product Name", "Product Quantity"]
        sheet.append(heading)
        workbook.save(filepath)
    workbook = openpyxl.load_workbook(filepath)
    sheet = workbook.active
    sheet.append([firstname, lastname, age, country, state, zip_code, address, product_category,product_name, quantity_ordered])
    workbook.save(filepath)
                

window = Tk()
window.title("Sales Data Entry Form")

frame = Frame(window, bg=BACKGROUND_COLOR)
frame.pack()

# Saving User Info
user_info_frame = LabelFrame(frame, text="User Information", bg=BACKGROUND_COLOR, fg=FG_COLOR, font=("Arial, 16"))
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

first_name_label = Label(user_info_frame, text="First Name",bg=BACKGROUND_COLOR, fg=FG_COLOR, font=("Arial, 12"))
first_name_label.grid(row=0, column=0)
first_name_entry = Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)

last_name_label = Label(user_info_frame, text="Last Name", bg=BACKGROUND_COLOR, fg=FG_COLOR, font=("Arial, 12"))
last_name_label.grid(row=0, column=1)
last_name_entry = Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

age_label = Label(user_info_frame, text="Age",bg=BACKGROUND_COLOR, fg=FG_COLOR, font=("Arial, 12"))
age_spinbox = Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=0, column=2)
age_spinbox.grid(row=1, column=2)

country_label = Label(user_info_frame, text="Country", bg=BACKGROUND_COLOR, fg=FG_COLOR, font=("Arial, 12"))
country_combobox = ttk.Combobox(user_info_frame, values=["USA", "India", "Canada", "Uk", "France", "Italy", "Germany"])
country_label.grid(row=2, column=0)
country_combobox.grid(row=3, column=0)

state_label = Label(user_info_frame, text="State", bg=BACKGROUND_COLOR, fg=FG_COLOR, font=("Arial, 12"))
state_label.grid(row=2, column=1)
state_entry = Entry(user_info_frame)
state_entry.grid(row=3, column=1)

zip_code_label = Label(user_info_frame, text="Zip Code",  bg=BACKGROUND_COLOR, fg=FG_COLOR, font=("Arial, 12"))
zip_code_label.grid(row=2, column=2)
zip_code_entry = Entry(user_info_frame)
zip_code_entry.grid(row=3, column=2)

address_label = Label(user_info_frame, text="Address", bg=BACKGROUND_COLOR, fg=FG_COLOR, font=("Arial, 12"))
address_label.grid(row=4, column=0)
address_entry = Entry(user_info_frame)
address_entry.grid(row=5, column=0)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Product Info
product_frame = LabelFrame(frame, text="Product Information",   bg=BACKGROUND_COLOR, fg=FG_COLOR, font=("Arial, 16"))
product_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

product_category_label = Label(product_frame, text="Product Category",  bg=BACKGROUND_COLOR, fg=FG_COLOR, font=("Arial, 12"))
product_category_combobox = ttk.Combobox(product_frame, values=["Clothing and Fashion", "Furniture", "Books and Media", "Electronics", "Health and Beauty", "Kitchen Applience"])
product_category_label.grid(row=0, column=0)
product_category_combobox.grid(row=1, column=0)

product_name_label = Label(product_frame, text="Product Name",  bg=BACKGROUND_COLOR, fg=FG_COLOR, font=("Arial, 12"))
product_name_label.grid(row=0, column=1)
product_name_entry = Entry(product_frame)
product_name_entry.grid(row=1, column=1)

product_quantity_label = Label(product_frame, text= "Product Quantity",  bg=BACKGROUND_COLOR, fg=FG_COLOR, font=("Arial, 12"))
product_quantity_spinbox = Spinbox(product_frame, from_=1, to='infinity')
product_quantity_label.grid(row=0, column=2)
product_quantity_spinbox.grid(row=1, column=2)

for widget in product_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Button
button = Button(frame, text="Enter data", command= enter_data,  bg=BACKGROUND_COLOR, fg=FG_COLOR, font=("Arial, 12"))
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
 
window.mainloop()