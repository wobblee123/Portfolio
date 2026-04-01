Shop Stocking System

A simple command-line stock management system written in Python.

Overview

The shop stocking system allows you to manage inventory through a text-based interface. You can create, update, and track stock items in real time.

Features

* Add stock to existing items
* Remove stock with validation checks
* Create new stock items dynamically
* Delete existing stock items
* View current stock levels at any time
* Simple command-based interaction system

How to Use

1. Run the script:

   python shop_system.py

2. Enter one of the following commands when prompted:

* add
* remove
* create
* delete
* check
* quit

3. Follow the prompts to manage stock items

Example Actions

* Add stock to "Apples"
* Remove stock from "Bananas"
* Create a new item like "Bread"
* Delete an item from the system
* Check all current stock levels

Built With

* Python
* Standard libraries (time)

Purpose

This project was created for learning purposes, focusing on:

* Dictionaries and data handling
* User input processing
* Control flow and validation
* Building simple CLI applications

Known Issues

* No input validation for non-integer values when adding/removing stock
* No persistence (data resets when program stops)
* Case sensitivity inconsistencies in some commands

Future Improvements

* Save and load stock data
* Better input validation
* Case-insensitive commands everywhere
* Improved user interface and formatting

Final Note

A small but practical project for understanding how basic inventory systems work in Python.
