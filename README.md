# PROJECT

## Introduction

This is a group project for the first semester Python course in Data Analysis for Business. This project creates a website that displays data using Python's flask framework, allowing students to gain experience building websites and displaying data with Python.

**Instructor**

Mark Cassar

**Group Members**

Abraham Emokpare

Huihua Li

Pan Hu


## Files Structure
 - root
    - data collection
        - datacollect.ipynb
        - fifa_players_original.csv
     - data processing
        - fifa_players_clean.csv
    - database
        - createdatabase.ipynb
        - Football.db
    - website
        - assets
        - templates
            - about.html
            - data.html
            - index.html
        - index.py
    - README.md
    - requirements.txt   

## Setup Instructions
1.	Download the file and unzip it
2.	Open the folder using Visual Studio Code
3.	In VS Code, Select `View -> Terminal` from the top menu.
4.	Create Virtual Environment: In the terminal, run the flowing command: python -m venv venv
5.	Activate the Virtual Environment: In the terminal, run the flowing command: .\venv\Scripts\activate
6.	Install Dependencies: In the terminal, , run the flowing command: pip install -r requirements.txt
7.	Open index.py under website folder and run it. The message 'Running on http://127.0.0.1:5000' will show.
8.	Open a browser and input 'http://localhost:5000' in the address bar. If everything is right, the page will show.
   

## Data Collection and Processing

The project's data set originates from  [Football Players Data](https://www.kaggle.com/datasets/maso0dahmed/football-players-data) on [Kaggle Datasets](https://www.kaggle.com/datasets). This comprehensive dataset offers detailed information on approximately 17,000 FIFA football players, meticulously scraped from [SoFIFA.com](https://sofifa.com/).

The original data set has 17,000 rows and 51 columns. For the convenience of display, we selected 8 columns which are `name`, `birth_date`, `height_cm`, `weight_kgs`, `positions`, `nationality`, `overall_rating`, and 500 rows.

The initial data is acquired in CSV format, undergoes processing via pandas, and is subsequently stored within an SQLite database.

The name of the database is `Football` and the table name is `players`

## Website

The template of the website is from [NiceAdmin Free](https://bootstrapmade.com/nice-admin-bootstrap-admin-html-template/). The assets folder includes all static resources such as JavaScript files, CSS stylesheets, and images. The templates folder includes three pages: index.html, about.html, and data.html. The index.py file contains the python code needed.

When presenting data, the "age" column is included, calculated from the individual's date of birth. And for better understanding, the field columns have been renamed, which are `Name`, `Age`, `Birthday`, `Height (cm)`, `Weight (kg)`, `Positions`, `Over Rating`.

To alleviate server load, we implemented pagination to retrieve 10 data entries from the database per request.

## Conclusion

We extend our sincere gratitude to everyone who contributed to the success of this project. 
