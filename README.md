# **integrated_bus_project**  
Bus Management System

## **Description**  
A Django-based bus management system that enables administrators to manage buses and travel schedules, while allowing passengers to book tickets and make payments.

## **Features**
- Admin dashboard for managing:
  - Buses
  - Travel times
  - Bookings and passengers
- Passenger booking form with dynamic travel options
- Payment section for processing ticket payments
- Single Django app structure for simplicity and maintainability

## **Technologies Used**
- Django (Python)
- SQLite (can be changed to MySQL/PostgreSQL)
- HTML, CSS, Bootstrap
- (Optional) Payment APIs for real-time transactions

## **How to Run the Project**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/integrated_bus_project.git
   cd integrated_bus_project
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the system:
   - Admin Panel: `http://127.0.0.1:8000/admin/`
   - Passenger Booking: `http://127.0.0.1:8000/`

## **Project Structure**
```
integrated_bus_project/
├── bus/               # Main Django app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── static/
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## **Author**
Vincent Kyalo
