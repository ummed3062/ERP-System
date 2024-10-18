# College ERP System

 - The College ERP (Enterprise Resource Planning) System is a web-based application developed using Flask and MySQL. 
 - It provides basic functionalities to manage course information and lecture schedules for different branches of B.Tech programs. 
 - The system allows users to view a list of courses, manage lecture plans, and add new lecture details. 
 - It serves as a simplified model for educational institutions to track academic plans and course management.

## Features

  - View a list of courses with branch details.
  - View and manage lecture schedules.
  - Add new lecture details to the schedule.
  - JSON API endpoint for retrieving course information.

## Technologies Used

  - Python (Flask)
  - MySQL
  - HTML/CSS for front-end templates

## Prerequisites

  - Python 3.x installed
  - MySQL server running locally
  - Flask and MySQL Connector for Python (`mysql-connector-python`)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ummed3062/ERP-System.git
   cd ERP-System
2. **Install required Python packages:**
    pip install flask mysql-connector-python

3. **Configure the MySQL database:**

   - Make sure MySQL is running on your local machine.
   - Create a database named erp_db in your MySQL instance.
   - Update the database connection details in the get_db_connection() function in app.py if needed.
   - Run the application:
      python app.py

4. **Access the application:**
   - Open a web browser and go to http://127.0.0.1:5000/

**Project Structure**
   - app.py:       The main application file that contains all the route handlers and database connection setup.
   - templates/:   Contains the HTML templates used for rendering the web pages.
   - home.html:    The homepage displaying the list of courses.
   - branch.html:  The page showing lecture schedules.
   - add.html:     The form page for adding new lecture details.
   - static/:      (Optional) Place to add CSS files, JavaScript files, and other static resources if required.

**Routes**
   - /: Displays the list of B.Tech courses.
   - /api: Returns a JSON response of the course list.
   - /courseplan: Displays the list of lectures from the database.
   - /add: Allows adding a new lecture.

**Contributions**
    Contributions are welcome! Feel free to open issues or submit pull requests for any improvements or bug fixes.

**Acknowledgments**
    This project was created to provide a basic understanding of integrating Flask with a MySQL database for educational purposes.
