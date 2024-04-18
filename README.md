# PYTHON PROJECT

## Introduction
This is a group project for the first semester Python course in Data Analysis for Business. This project creates a website that displays data using Python's flask framework, allowing students to gain experience building websites and displaying data with Python.

**Instructor**

- Mark Cassar

**Groop Members**

- Abraham Emokpare   w0860828
 
- Huihua Li    w0834927
 
- Pan Hu    w0839721

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
1.	Install the required Python packages: pip install pandas sqlite3 Flask.
2.	Run the Jupyter notebook createdatabase.ipynb to create and set up the SQLite database.
3.	Use datacollect.ipynb to preprocess and insert data into Football.db.
4.	Launch the Flask application using python index.py and navigate to http://localhost:5000 to access the web interface.
   
## Packages Used
- Pandas: For data manipulation and analysis.
- SQLite3: For database interactions.
- Flask: For setting up the web application.

## Dataset Description
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
