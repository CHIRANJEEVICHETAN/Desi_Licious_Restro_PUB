# Deci_Licious_Restro_PUB

Restro PUB is a Django web application designed for managing restaurant reservations, user authentication, and providing information about the restaurant's services and offerings.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Models](#models)
- [Views](#views)
- [URLs](#urls)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication (login and signup)
- Reservation system for tables
- Contact form for inquiries
- Subscription to newsletters
- Information pages (About, Menu, Specials, Events, Chefs, Gallery)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/CHIRANJEEVICHETAN/Desi_Licious_Restro_PUB
   cd restro_pub
   ```

````

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Open your browser and go to `http://127.0.0.1:8000/`.

## Project Structure

```
restro_pub/
│
├── manage.py
├── Restro_PUB/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── models.py
│   └── ...
└── templates/
    ├── index.html
    ├── login.html
    ├── SignUp.html
    ├── TermsOfservices.html
    ├── index_login.html
    ├── our_branches.html
    ├── about.html
    ├── menu.html
    ├── specials.html
    ├── events.html
    ├── chefs.html
    └── gallery.html
```

## Models

### `bookTable`

- **Tname**: Name of the person making the reservation.
- **Temail**: Email address of the person.
- **Tphone**: Phone number of the person.
- **Tdate**: Date of the reservation.
- **Ttime**: Time of the reservation.
- **Tpeople**: Number of people for the reservation.
- **Tmessage**: Additional message.

### `ContactUS`

- **ContactName**: Name of the person contacting.
- **ContactEmail**: Email address of the person.
- **subject**: Subject of the inquiry.
- **ContactMessage**: Message content.

### `SubEmail`

- **email**: Email address for subscription.

## Views

- **index**: Handles the main page, including reservation and contact forms.
- **login**: Manages user login.
- **signup**: Handles user registration.
- **termsOfServices**: Displays terms of service.
- **indexLogin**: Displays the login index page.
- **ourBranches**: Displays information about branches.
- **about**: Displays information about the restaurant.
- **menu**: Displays the menu.
- **specials**: Displays special offers.
- **events**: Displays upcoming events.
- **chefs**: Displays information about chefs.
- **gallery**: Displays a gallery of images.

## URLs

The following URLs are defined in the application:

- `/` or `/index`: Main page
- `/login`: User login page
- `/signup`: User signup page
- `/TermsOfServices`: Terms of service page
- `/indexLogin`: Login index page
- `/ourBranches`: Branches information page
- `/about`: About page
- `/menu`: Menu page
- `/specials`: Specials page
- `/events`: Events page
- `/chefs`: Chefs page
- `/gallery`: Gallery page

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

````
