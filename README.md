 # Portfolio App - Django + React

 This project is a simple portfolio site built using React for the frontend and Django REST Framework for the backend. The frontend is prebuilt and served from the Django backend.

 ## 🛠️ Technologies Used

 - **Frontend**: React (served from `build/` directory)
 - **Backend**: Python, Django 5.2, Django REST Framework
 - **Others**: CORS Headers, WhiteNoise for static files

 ## 🚀 Getting Started

 ### Requirements

 Make sure you have Python 3.10+ installed. Then install dependencies:

 ```bash
 pip install -r requirements.txt
 ```

 ### Running the Server

 ```bash
 python manage.py runserver
 ```

 This will start the Django development server on `http://127.0.0.1:8000/`.

 The frontend is already built and will be served automatically by Django.

 ## 📁 Project Structure

 ```
 portfolio_app_django_react/
 │
 ├── backend/               # Django project files
 ├── technologies/          # Django app with API logic
 ├── frontend/build/        # Compiled React frontend
 ├── db.sqlite3             # SQLite database
 ├── manage.py              # Django entry point
 └── requirements.txt       # Python dependencies
 ```

 ## ⚙️ API

 The project exposes a basic REST API for managing portfolio content. The endpoints are defined under:

 ```
 /api/technologies/
 ```

 You can check `technologies/urls.py` and `views.py` for more details.

 ## 🎨 Assets

 The React app includes various static assets such as:

 - SVG icons for technologies (`frontend/build/images/`)
 - A fun black hole animation (`frontend/build/gifs/black_hole.gif`)

 ## 📦 Deployment

 The project uses WhiteNoise to serve static files. For production, make sure to:

 - Collect static files with `python manage.py collectstatic`
 - Configure a proper production WSGI/ASGI server

 ## 📄 License

 This project is licensed under the terms of the MIT license.
