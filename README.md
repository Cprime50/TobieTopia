# Tobietopia Blog
This is the official repository for the Tobietopia Blog, a Django-based blogging platform.

**Features**

Create, update, and delete blog posts.

Commenting system for engaging discussions.

Responsive design for optimal viewing on various devices.

Search functionality to easily find specific blog posts.

Tagging system for organizing posts by topics.

User-friendly admin panel for managing blog content.
Installation


**Create a virtual environment**

python -m venv env


**Activate the virtual environment:**

On Windows:

env\Scripts\activate


On macOS and Linux:

source env/bin/activate


**Install the project dependencies:**

pip install -r requirements.txt


**Apply the database migrations:**

python manage.py makmigrations
python manage.py migrate

**I use postgreSQL database here but you can switch to mySQL or Sqlite** 

**Run the development server:**

python manage.py runserver

Visit http://localhost:8000 in your web browser to access the Tobietopia Blog.

**Contributing**
Contributions are welcome! If you'd like to contribute to the Tobietopia Blog project, please follow these steps:

**Note:** Passwords, usernames, and database configurations are not included in this repository. It's recommended to store sensitive information like passwords and database credentials in the OS environment variables or a separate configuration file. Users should configure these environment variables or files themselves before running the application.

![](https://github.com/Cprime50/Web-dev-stuff/blob/master/full%20tobie.png)
