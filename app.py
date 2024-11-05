# importing necessary libraries

import sqlite3
import os

# creating database

db_Name = 'Chocolate_House.db'

def create_connection():
    conn = sqlite3.connect(db_Name)
    return conn

# creating tables

def create_tables():
    conn = create_connection()
    c = conn.cursor()
    
    # creating tables for seasonal flavor offerings

    c.execute('''
    CREATE TABLE IF NOT EXISTS seasonal_flavors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT,
        season TEXT
    )''')
    
    # creating tables for ingredient inventory

    c.execute('''
    CREATE TABLE IF NOT EXISTS ingredients (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        quantity INTEGER,
        unit TEXT
    )''')
    
    # creating tables for customer flavor suggestions and allergy concerns

    c.execute('''
    CREATE TABLE IF NOT EXISTS customer_suggestions (
        id INTEGER PRIMARY KEY,
        customer_name TEXT NOT NULL,
        suggestion TEXT,
        allergy_concerns TEXT
    )''')

    conn.commit()
    conn.close()

# creating a function to insert some demo values

def insert_sample_data():
    conn = create_connection()
    c = conn.cursor()

    # inserting sample data into seasonal_flavors table

    c.execute('''
    INSERT INTO seasonal_flavors (name, description, season) VALUES
    ('Pumpkin Spice', 'A warm and spicy autumn flavor', 'Fall'),
    ('Peppermint', 'A cool, minty flavor for the holidays', 'Winter'),
    ('Strawberry Delight', 'A sweet and refreshing summer flavor', 'Summer')
    ''')

    # inserting sample data into ingredients inventory table

    c.execute('''
    INSERT INTO ingredients (name, quantity, unit) VALUES
    ('Cocoa Powder', 50, 'kg'),
    ('Sugar', 100, 'kg'),
    ('Milk', 200, 'liters')
    ''')

    # inserting sample data into customer_suggestions table

    c.execute('''
    INSERT INTO customer_suggestions (customer_name, suggestion, allergy_concerns) VALUES
    ('Peter', 'Can you add more dark chocolate options', 'None'),
    ('Bruce', 'Can you add more nut-based flavors', 'Almond allergy')
    ''')

    conn.commit()
    conn.close()

# creating function to view seasonal_flavors table

def view_seasonal_flavors():
    conn = create_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM seasonal_flavors')
    rows = c.fetchall()
    conn.close()

    print("\n--- Seasonal Flavors ---")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Description: {row[2]}, Season: {row[3]}")

# creating function to view ingredients inventory table

def view_ingredients():
    conn = create_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM ingredients')
    rows = c.fetchall()
    conn.close()

    print("\n--- Ingredient Inventory ---")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Quantity: {row[2]} {row[3]}")

# creating function to view customer_suggestions table

def view_customer_suggestions():
    conn = create_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM customer_suggestions')
    rows = c.fetchall()
    conn.close()

    print("\n--- Customer Suggestions & Allergy Concerns ---")
    for row in rows:
        print(f"ID: {row[0]}, Customer: {row[1]}, Suggestion: {row[2]}, Allergy Concerns: {row[3]}")

# creating function to add seasonal_flavors table

def add_seasonal_flavor(name, description, season):
    conn = create_connection()
    c = conn.cursor()
    c.execute('''
    INSERT INTO seasonal_flavors (name, description, season) 
    VALUES (?, ?, ?)
    ''', (name, description, season))
    conn.commit()
    conn.close()
    print(f"Added seasonal flavor: {name}")

# creating function to add ingredients inventory table

def add_ingredient(name, quantity, unit):
    conn = create_connection()
    c = conn.cursor()
    c.execute('''
    INSERT INTO ingredients (name, quantity, unit)
    VALUES (?, ?, ?)
    ''', (name, quantity, unit))
    conn.commit()
    conn.close()
    print(f"Added ingredient: {name}")

# creating function to add customer_suggestions table

def add_customer_suggestion(customer_name, suggestion, allergy_concerns):
    conn = create_connection()
    c = conn.cursor()
    c.execute('''
    INSERT INTO customer_suggestions (customer_name, suggestion, allergy_concerns)
    VALUES (?, ?, ?)
    ''', (customer_name, suggestion, allergy_concerns))
    conn.commit()
    conn.close()
    print(f"Added suggestion from {customer_name}")

# creating function to update seasonal_flavors table

def update_seasonal_flavor(id, name=None, description=None, season=None):
    conn = create_connection()
    cursor = conn.cursor()
    if name:
        cursor.execute('UPDATE seasonal_flavors SET name = ? WHERE id = ?', (name, id))
    if description:
        cursor.execute('UPDATE seasonal_flavors SET description = ? WHERE id = ?', (description, id))
    if season:
        cursor.execute('UPDATE seasonal_flavors SET season = ? WHERE id = ?', (season, id))
    conn.commit()
    conn.close()
    print(f"Updated seasonal flavor with ID: {id}")

# creating function to update ingredients inventory table

def update_ingredient(id, name=None, quantity=None, unit=None):
    conn = create_connection()
    cursor = conn.cursor()
    if name:
        cursor.execute('UPDATE ingredients SET name = ? WHERE id = ?', (name, id))
    if quantity:
        cursor.execute('UPDATE ingredients SET quantity = ? WHERE id = ?', (quantity, id))
    if unit:
        cursor.execute('UPDATE ingredients SET unit = ? WHERE id = ?', (unit, id))
    conn.commit()
    conn.close()
    print(f"Updated ingredient with ID: {id}")

# creating function to update customer_suggestions table

def update_customer_suggestion(id, customer_name=None, suggestion=None, allergy_concerns=None):
    conn = create_connection()
    cursor = conn.cursor()
    if customer_name:
        cursor.execute('UPDATE customer_suggestions SET customer_name = ? WHERE id = ?', (customer_name, id))
    if suggestion:
        cursor.execute('UPDATE customer_suggestions SET suggestion = ? WHERE id = ?', (suggestion, id))
    if allergy_concerns:
        cursor.execute('UPDATE customer_suggestions SET allergy_concerns = ? WHERE id = ?', (allergy_concerns, id))
    conn.commit()
    conn.close()
    print(f"Updated suggestion from customer with ID: {id}")

# creating function to delete seasonal_flavors table

def delete_seasonal_flavor(id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM seasonal_flavors WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    print(f"Deleted seasonal flavor with ID: {id}")

# creating function to delete ingredients inventory table

def delete_ingredient(id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM ingredients WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    print(f"Deleted ingredient with ID: {id}")

# creating function to delete customer_suggestions table

def delete_customer_suggestion(id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM customer_suggestions WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    print(f"Deleted suggestion from customer with ID: {id}")

def main():
    # creating tables and inserting sample data in this main function
    if not os.path.exists(db_Name):
        create_tables()
        insert_sample_data()

    while True:
        print("\nWelcome to the Chocolate House")
        print("1: View Seasonal Flavors")
        print("2: View Ingredients")
        print("3: View Customer Suggestions & Allergy Concerns")
        print("4: Add Seasonal Flavor")
        print("5: Add Ingredient")
        print("6: Add Customer Suggestion")
        print("7: Update Seasonal Flavor")
        print("8: Update Ingredient")
        print("9: Update Customer Suggestion")
        print("10: Delete Seasonal Flavor")
        print("11: Delete Ingredient")
        print("12: Delete Customer Suggestion")
        print("13: Exit")

        
        choice = input("Please Choose an option to View the Chocolate House Database: ")

        if choice == '1':
            view_seasonal_flavors()
        
        elif choice == '2':
            view_ingredients()
        
        elif choice == '3':
            view_customer_suggestions()
        
        elif choice == '4':
            name = input("Enter seasonal flavor name: ")
            description = input("Enter description: ")
            season = input("Enter season: ")
            add_seasonal_flavor(name, description, season)
        
        elif choice == '5':
            name = input("Enter ingredient name: ")
            quantity = int(input("Enter quantity: "))
            unit = input("Enter unit (e.g., kg, liters): ")
            add_ingredient(name, quantity, unit)
        
        elif choice == '6':
            customer_name = input("Enter customer name: ")
            suggestion = input("Enter suggestion: ")
            allergy_concerns = input("Enter allergy concerns: ")
            add_customer_suggestion(customer_name, suggestion, allergy_concerns)
        
        elif choice == '7':
            id = int(input("Enter the ID of the seasonal flavor to update: "))
            name = input("Enter new name (or press Enter to skip): ")
            description = input("Enter new description (or press Enter to skip): ")
            season = input("Enter new season (or press Enter to skip): ")
            update_seasonal_flavor(id, name, description, season)
        
        elif choice == '8':
            id = int(input("Enter the ID of the ingredient to update: "))
            name = input("Enter new name (or press Enter to skip): ")
            quantity = input("Enter new quantity (or press Enter to skip): ")
            unit = input("Enter new unit (or press Enter to skip): ")
            update_ingredient(id, name, quantity, unit)
        
        elif choice == '9':
            id = int(input("Enter the ID of the customer suggestion to update: "))
            customer_name = input("Enter new customer name (or press Enter to skip): ")
            suggestion = input("Enter new suggestion (or press Enter to skip): ")
            allergy_concerns = input("Enter new allergy concerns (or press Enter to skip): ")
            update_customer_suggestion(id, customer_name, suggestion, allergy_concerns)
        
        elif choice == '10':
            id = int(input("Enter the ID of the seasonal flavor to delete: "))
            delete_seasonal_flavor(id)
        
        elif choice == '11':
            id = int(input("Enter the ID of the ingredient to delete: "))
            delete_ingredient(id)
        
        elif choice == '12':
            id = int(input("Enter the ID of the customer suggestion to delete: "))
            delete_customer_suggestion(id)
        
        elif choice == '13':
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
