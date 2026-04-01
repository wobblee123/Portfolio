Car Storage System

A simple command-line car storage manager built with Python.

Overview

The car storage system allows you to store, manage, and track cars using a unique storage number for each entry.

Features

* Add cars with model, make, and registration
* Automatically assign storage numbers
* Remove cars using their storage number
* View all stored cars
* Simple menu-based interaction

How to Use

1. Run the script:

   python car_storage.py

2. Choose an option from the menu:

* 1 to add a car
* 2 to remove a car
* 3 to check storage
* 4 to quit

3. Follow the prompts to manage your car storage

Example Actions

* Add a car with model, make, and registration
* Remove a car using its storage number
* View all stored cars and their details

Built With

* Python
* Standard library (time)

Purpose

This project was created for learning purposes, focusing on:

* Dictionaries and data storage
* User input and validation
* Functions and program structure
* Building simple CLI systems

Known Issues

* Removing a car may not work correctly due to referencing the wrong storage key
* No persistence (data resets when program stops)
* Limited input validation

Future Improvements

* Fix removal bug using correct storage number reference
* Add save and load functionality
* Improve input validation
* Add search functionality for cars

Final Note

A basic project to understand how data can be stored and managed in Python using dictionaries and user input.
