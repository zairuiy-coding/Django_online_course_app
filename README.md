# Online Course App

**Introduction**

The "onlinecourse" app is a web application designed to manage and deliver online courses. It allows instructors to create and manage courses, lessons, and quizzes, while learners can enroll in courses, complete lessons, and take quizzes. This app is built using the **Django** framework as a practice project to learn and demonstrate web development skills.

**General Notes**

This is the first application I built with the **Django** framework for practice purposes. 🤗

**ER Diagram**

This is the ER diagram design for the system.

![Onlinecourse ER Diagram](https://github.com/ibm-developer-skills-network/final-cloud-app-with-database/blob/master/static/media/course_images/onlinecourse_app_er.png)

**Setup Instructions**

### Set up a Virtual Environment
1. Install necessary packages:
    ```sh
    pip install --upgrade distro-info
    pip3 install --upgrade pip==23.2.1
    pip install virtualenv
    ```

2. Create and activate a virtual environment:
    ```sh
    virtualenv djangoenv
    source djangoenv/bin/activate
    ```

### Set up the Python Runtime
1. Install the required Python packages:
    ```sh
    pip install -U -r requirements.txt
    ```

### Database Setup
1. Create the initial migrations and generate the database schema:
    ```sh
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

### Run the Server
1. Start the development server:
    ```sh
    python3 manage.py runserver
    ```