# Tafakari Django Backend


Welcome to the Django backend of the Tafakari application. This backend server handles data processing, authentication, and communication with the database for the Tafakari mobile application.


## Installation
Before you begin, please ensure you have the following prerequisites installed on your system:

- Python 3.x
- [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)

### Follow these steps to set up the backend locally:

### 1 . Clone the repository:
```
git clone https://github.com/tafakari-app/backend.git
```

### 2 - Create a virtual environment and activate it

```
virtualenv venv
source venv/bin/activate   # On Windows, use "venv\Scripts\activate"
```

### 3 -  Install the required dependencies:

```
pip install -r requirements.txt
```

### 4 - Set up the database:
```
python manage.py migrate
```

### 5 - Create a superuser (admin) for the Django admin interface:
```
python manage.py createsuperuser
```

### 6 - Start the development server:
```
python manage.py runserver
```


## Usage

Once the backend server is up and running, you can access the Django admin interface at http://localhost:8000/admin/ and log in using the superuser credentials created in step 5.

For the Tafakari mobile application to interact with the backend, ensure you have configured the appropriate API endpoints in the frontend application to make requests to this backend server.


## Development

If you wish to contribute to the development of the backend, please create a new branch for your changes:


```
git checkout -b feature/new-feature
```

After making your changes, commit and push the branch:

```
git add .
git commit -m "Add new feature"
git push origin feature/new-feature
```

Create a pull request to merge your changes into the main branch.



### Issues
If you encounter any issues or bugs with the backend, please report them in the "Issues" section of this repository.


## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

Thank you for using Tafakari! We hope this backend server helps support mental health and well-being in Kenya and beyond. If you have any questions or need assistance, feel free to reach out to us. Happy coding!



