INFO-B 211 — Assignment 1: Object Oriented Programming
Purpose

The purpose of this project is to practice Object Oriented Programming (OOP) in Python by modeling a used-car inventory system. We use a real dataset of used cars (USA_cars_dataset.csv from Kaggle) to build classes for cars and sellers, then interact with the data through a simple menu-driven program.

Learning Goals

Use classes, attributes, and methods in Python

Understand how to design and implement objects

Practice error handling and good coding style

Load and work with real-world CSV data

Gain experience with GitHub documentation and version control

Project Structure

car.py — Car class
seller.py — Seller class
inventory_loader.py — Loads cars from CSV into Car objects
app.py — Menu-driven program (main entry point)
README.md — Documentation (this file)
CHATLOG.md — AI usage log (academic honesty)
data/USA_cars_dataset.csv — Kaggle dataset (place here manually)

Car (car.py)

Attributes: manufacturer, model, year, mileage, engine, transmission, drivetrain, mpg (optional), exterior_color, interior_color, accident, price

Methods:

Paint(color): change exterior color

Repair(part, replacement): update engine, transmission, or drivetrain

Reupholster(color): change interior color

Drive(miles): add miles to odometer

Modify_Price(value): if value >= 1 set exact price, if value < 1 apply discount (asks to confirm)

Seller (seller.py)

Attributes: name, rating (default 4.5), inventory (list of Car objects)

Methods:

Buy(car): add car to inventory

Sell(car): remove car from inventory

list_brief(): show inventory in short format

Data Loading (inventory_loader.py)

Uses csv.DictReader (no external libraries).

Handles flexible column names (e.g., make or brand → manufacturer).

Groups cars by seller_name if present. If missing, cars are distributed across 5 default sellers.

Main Program (app.py)

Loads cars and groups them by seller.

Startup can show a debug summary if DEBUG = True.

Provides a text-based menu to interact with the data.

Menu options:

List sellers

Show a seller’s inventory

Modify a car (Paint / Repair / Reupholster / Drive / Modify Price)

Move a car between sellers (Sell → Buy)

Quit

Extra feature: search sellers by name. Enter a keyword to find matching sellers (e.g., “Toyota”) and view their inventory.

How to Run

Download the dataset from Kaggle: USA Cars Dataset (Andrei Novikov)

Place the CSV in the data/ folder as data/USA_cars_dataset.csv

Run the program with Python: python app.py data/USA_cars_dataset.csv

Example Run

Program loads all cars from the dataset.

Shows seller count and car assignments (if DEBUG = True).

Menu appears with options to list sellers, view inventory, search, modify cars, or move cars between sellers.

Error Handling & Robustness

Drive: must be greater than 0 miles

Repair: only accepts engine, transmission, or drivetrain

Modify_Price: must be positive; discounts require confirmation

Missing data: replaced with “Unknown” or 0

Documentation & AI Use

Code is organized with comments and clear error messages.

This README explains project purpose, design, usage, and limitations.

ChatGPT was used to brainstorm class design and CSV loading logic. AI usage is documented in CHATLOG.md.

Limitations

If dataset headers differ, update MAP in inventory_loader.py.

Text-based only (no GUI).

MPG is optional (shown as “n/a” if missing).

Grading Criteria Check

Functionality: all required methods implemented
Usability: menu provides clear interaction
Robustness: input checks and error handling included
Readability: code is structured and commented
Documentation: README and CHATLOG.md included
