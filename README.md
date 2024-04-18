# PYTHON PROJECT

## Project Introduction
This is a group project for the first semester Python course in Data Analysis for Business. This project creates a website that displays data using Python's flask framework, allowing students to gain experience building websites and displaying data with Python.
。。。。

## Project Objectives
......
......
.......

## Project Structure
•	createdatabase.ipynb: Jupyter notebook for creating and setting up the SQLite database Football.db.
•	datacollect.ipynb: Notebook for data collection and initial preprocessing.
•	database.py: Contains functions to insert data into the database and retrieve data for analysis.
•	templates: Folder containing HTML templates for the web interface.
•	static: Folder for static assets like CSS and images for the web interface.

## Setup Instructions
1.	Install the required Python packages: pip install pandas sqlite3 Flask.
2.	Run the Jupyter notebook createdatabase.ipynb to create and set up the SQLite database.
3.	Use datacollect.ipynb to preprocess and insert data into Football.db.
4.	Launch the Flask application using python app.py and navigate to http://localhost:5000 to access the web interface.
   
## Packages Used
•	Pandas: For data manipulation and analysis.
•	SQLite3: For database interactions.
•	Flask: For setting up the web application.

## Dataset Description
The original dataset contained 17,954 rows and 51 columns. After cleaning through Python coding, the resulting dataset—named 'fifa_player_clean.csv'—has been reduced to seven columns and 500 rows. The columns are as follows: 
•	id: Unique identifier for each player.
•	name: Player's name.
•	age: Age of the player.
•	nationality: Player's nationality.
•	overall_rating: Overall skill rating of the player.
•	potential: Potential future rating of the player.
•	club: Club that the player currently represents.
•	value_euro: Market value of the player in euros.

## Methodology
1.	Data Collection: Obtain the original dataset fifa_players_original from Kaggle and utilize the cleaned dataset fifa_player_clean.csv for analysis.
2.	Data Cleaning: Standardize and preprocess data within datacollect.ipynb.
3.	Data Analysis: Analyze player data to uncover patterns in performance and market value.
4.	Interpretation: Draw conclusions and provide actionable insights based on the data analysis.
   
## Usage
•	Clone the repository containing the project files to your local machine.
•	Follow the setup instructions to prepare the project environment and start the analysis.
   
## Group Members
Abraham Emokpare   w0860828
Huihua Li    w0834927
Pan Hu    w0839721
