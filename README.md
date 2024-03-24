# HEALTHY FOODS API

## Overview
This project creates a Django API that can be used for accessing information about healthy foods. It provides endpoints to retrieve details about various types of foods, their nutritional values, and more.

## Features
- **Authentication**: Secure API endpoints using token-based authentication.
- **Food Information**: Retrieve information about different healthy foods, including nutritional values.
- **Categories**: Categorization of foods into various types for easy browsing.
- **Search**: Search for specific foods based on name, category, or nutritional content.
- **Favorites**: Allow users to mark their favorite foods and access them later.

## Installation
Follow these steps to set up the project locally:

### Requirements
- Python 3.10.x
- Django
- Django REST framework

### Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/healthy-foods-api.git
   ```

2. Navigate to the following directory:
   ```bash
   cd healthy-foods-api
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install dependencies:
   ```bash
   pip install -r requirements.txt

   ```
6. Navigate to the main project directory
```bash 
cd dataAPI
```
7. Run migrations:
   ```bash
   python manage.py migrate
   ```

8. Create a superuser (admin):
   ```bash
   python manage.py createsuperuser
   ```

9. Start the development server:
   ```bash
   python manage.py runserver
   ```

10. The API will be available at `http://localhost:8000/foods/`

## Usage
- **Admin Interface**: Visit `http://localhost:8000/admin/` to access the admin interface. Log in with the superuser credentials created earlier.
- **API Endpoints**: Explore the API endpoints at `http://localhost:8000/foods/`

## API Endpoints
- `GET /foods/`: List all healthy foods.
- `GET /foods/{id}/`: Retrieve details of a specific food.
- `POST /foods/`: Create a new food entry.
- `PUT /foods/{id}/`: Update a specific food.
- `DELETE /foods/{id}/`: Delete a specific food.

## Authentication
- Token-based authentication is used.
- Obtain a token by sending a POST request to `/api/token/` with `username` and `password`.
- Include the token in the Authorization header for protected endpoints:
  ```
  Authorization: Bearer <your_token>
  ```

## Contributing
We welcome contributions to improve the project! To contribute:
- Fork the repository
- Create your feature branch (`git checkout -b feature/YourFeature`)
- Commit your changes (`git commit -am 'Add YourFeature'`)
- Push to the branch (`git push origin feature/YourFeature`)
- Create a new Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE.md](https://www.mit.edu/~amini/LICENSE.md) file for details.

## Acknowledgements
- This project was inspired by the need for a simple and accessible way to access information about healthy foods.
- We thank the Django and Django REST framework communities for their excellent tools and documentation.
