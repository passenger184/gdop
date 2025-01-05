# GDOP Project

## Overview

The GDOP project is a web application built using Django. It includes various features such as user authentication, dynamic content management, and interactive UI components.

## Features

- User Authentication
- Dynamic Content Management
- Interactive UI Components

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/gdop.git
   cd gdop
   ```

2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Setup environmental variables (see .env.example)

4. Apply migrations:

   ```sh
   python manage.py migrate
   ```

5. Populated the database with initial data:

   ```sh
   python manage.py seed
   ```

6. Run the development server:

   ```sh
   python manage.py runserver
   ```

## Usage

- Access the application at http://127.0.0.1:8000/.
- Use the admin interface at http://127.0.0.1:8000/admin/ for content management.
