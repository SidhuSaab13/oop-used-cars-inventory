INFO-B 211 — Assignment 1: Object Oriented Programming
Purpose

The purpose of this project is to practice Object Oriented Programming (OOP) in Python by modeling a used-car inventory system.
We use a real dataset of used cars (USA_cars_dataset.csv from Kaggle) to build classes for cars and sellers, and then interact with the data through a simple menu program.

Learning Goals

Use classes, attributes, and methods in Python

Understand how to design and implement objects

Practice error handling and good coding style

Load and work with real-world CSV data

Gain experience with GitHub documentation and version control

Project Structure

info-b211-assignment1/
├── car.py # Car class
├── seller.py # Seller class
├── inventory_loader.py # Loads cars from CSV into Car objects
├── app.py # Menu-driven program to use the classes
├── README.md # Documentation (this file)
├── CHATLOG.md # AI usage log (academic honesty)
└── data/
└── USA_cars_dataset.csv # Kaggle dataset (place here manually)

Car (car.py)

Attributes:

manufacturer, model, year, mileage, engine, transmission, drivetrain, mpg (optional), exterior_color, interior_color, accident, price

Methods:

Paint(color) → change exterior color

Repair(part, replacement) → update engine, transmission, or drivetrain

Reupholster(color) → change interior color

Drive(miles) → add miles to odometer

Modify_Price(value) → if value >= 1 set exact price, if value < 1 apply discount (asks to confirm)

Seller (seller.py)

Attributes:

name, rating (default 4.5), inventory (list of Car objects)

Methods:

Buy(car) → add car to inventory

Sell(car) → remove car from inventory

list_brief() → show inventory in short format

Data Loading

The dataset is loaded with csv.DictReader (no external libraries like pandas).
inventory_loader.py maps different possible column names to the correct fields.
Examples: make or brand → manufacturer, odometer → mileage.

If a seller/dealer column exists, cars are grouped by that seller. If not, cars are spread across 5 default sellers.

How to Run

Download the dataset from Kaggle: USA Cars Dataset (Andrei Novikov)

Place the CSV in the data/ folder as data/USA_cars_dataset.csv

Run the program:
python app.py

Use the menu:

[1] List sellers

[2] Show a seller’s inventory

[3] Modify a car (Paint, Repair, Reupholster, Drive, Modify Price)

[4] Move a car between sellers (Sell -> Buy)

[5] Quit

Example Run

Loaded 2499 cars into 5 sellers.

=== MENU ===
[1] List sellers
[2] Show a seller's inventory
[3] Modify a car (Paint / Repair / Reupholster / Drive / Modify Price)
[4] Move a car between sellers (Sell -> Buy)
[5] Quit
Choose: 1

Seller_1 | Rating 4.5 | 500 cars

Seller_2 | Rating 4.5 | 500 cars
...

Error Handling & Robustness

Drive: must be > 0 miles

Repair: only accepts engine, transmission, or drivetrain

Modify_Price: price must be positive; discounts require confirmation

Missing data: replaced with "Unknown" or 0

Documentation & AI Use

Code is organized with comments and clear error messages.

This README explains the project purpose, design, how to run, and limitations.

ChatGPT was used to help brainstorm class design and CSV loader logic. AI usage is documented in CHATLOG.md as required.

Limitations

If your dataset headers don’t match, update MAP in inventory_loader.py.

The program is text-based only (no GUI).

MPG is optional (shown as “n/a” if missing).

Grading Criteria Check

Functionality (50 pts): all required methods work

Usability (10 pts): simple menu to test everything

Robustness (10 pts): input checks and error handling

Readability (10 pts): clean structure, comments, docstrings

Documentation (20 pts): README + comments + AI usage log