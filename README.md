# Website Design For Restaurant Application (Deci_Licious_Restro_PUB)

## Project Overview

Deci_Licious_Restro_PUB is a Django-based web application designed for a restaurant. It provides various functionalities such as table booking, contact forms, user authentication, and information about the restaurant's branches, menu, specials, events, and more.

## File Structure

- **Deci_Licious_Restro_PUB/**

- `static/`
  - `assets/`
    - `css/`
      - `branches.css`
      - `header.css`
      - `style.css`
    - `js/`
      - `main.js`
    - `img/`
    - `vendor/`
  - `LOGIN-SIGNUP/`
    - `Login/`
      - `css/`
        - `main.css`
        - `util.css`
      - `js/`
        - `main.js`
      - `images/`
      - `fonts/`
      - `vendor/`
    - `Sign-UP/`
      - `css/`
        - `main.css`
        - `util.css`
      - `js/`
        - `main.js`
      - `images/`
      - `fonts/`
      - `vendor/`
- `template/`
  - `about.html`
  - `chefs.html`
  - `events.html`
  - `footer.html`
  - `gallery.html`
  - `index_login.html`
  - `index.html`
  - `login.html`
  - `menu.html`
  - `nav.html`
  - `navbar.html`
  - `our_branches.html`
  - `SignUp.html`
  - `specials.html`
  - `TermsOfServices.html`
- `__init__.py`
- `asgi.py`
- `settings.py`
- `urls.py`
- `wsgi.py`
- **Restro_PUB/**
  - `migrations/`
  - `__init__.py`
  - `admin.py`
  - `apps.py`
  - `models.py`
  - `tests.py`
  - `urls.py`
  - `views.py`
  - `.gitattributes`
  - `db.sqlite3`
  - `manage.py`
  - `README.md`
  - `.gitignore`
  - `requirements.txt`

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/CHIRANJEEVICHETAN/Desi_Licious_Restro_PUB
   ```

2. Navigate to the project directory:
   ```bash
   cd Deci_Licious_Restro_PUB
   ```
3. Create a virtual environment:
   ```bash
   python3 -m venv env
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```
5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Apply migrations:
   ```bash
   python manage.py migrate
   ```
7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Features

### Table Booking

Users can book a table by providing their name, email, phone number, date, time, number of people, and a message.

### Contact Form

Users can send messages to the restaurant through the contact form.

### User Authentication

Users can sign up, log in, and log out. The authentication system checks for existing usernames and emails during sign-up.

### Information Pages

The application includes several informational pages such as:

- About
- Menu
- Specials
- Events
- Chefs
- Gallery
- Our Branches
- Terms of Services

## File Descriptions

### views.py

This file contains the views for handling HTTP requests and rendering the appropriate templates. It includes the following views:

- `index`
- `login`
- `signup`
- `termsOfServices`
- `indexLogin`
- `ourBranches`
- `about`
- `menu`
- `specials`
- `events`
- `chefs`
- `gallery`

### models.py

This file contains the database models for the application, including:

- `bookTable`: Stores table booking information.
- `ContactUS`: Stores contact form submissions.
- `SubEmail`: Stores subscription emails.

### urls.py

This file contains the URL patterns for the application, mapping URLs to their corresponding views.

### index.html

The main landing page of the website. It includes forms for table booking, contact, and subscription, as well as sections for displaying various restaurant information.

## Report

For more detailed information, please refer to the project report: [Website_Design_For_Restaurant_Application(Deci_Licious_Restro_PUB).pdf](https://drive.google.com/file/d/177wNUz5s4dmhdgnOcfLR54NQIqQOiL0X/view?usp=sharing)

## License

This project is licensed under the MIT License.

## Acknowledgements

Special thanks to all contributors and the open-source community.

---

For any further questions, please contact the project maintainers.

# Project Maintainers

Name: [@CHIRANJEEVICHETAN]
Email: [chiranjeevichetan1998@gmail.com](mailto:chiranjeevichetan1998@gmail.com)
Phone: +91 6363451047
