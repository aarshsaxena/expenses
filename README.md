# Daily Expenses Sharing Application

This is a Django REST Framework-based application that allows users to manage and share expenses. Users can create expenses, select participants, and specify how expenses are split among them.

## Features

- User registration and management
- Create and manage expenses
- Support for different split methods (equal, exact, percentage)
- JSON response format for API endpoints

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**

   git clone https://github.com/aarshsaxena/expenses.git
   cd expenseshare


2. **Create a virtual environment:**

python -m venv myenv
source myenv/bin/activate  # On Windows use: myenv\Scripts\activate


3. **Install required packages:**

pip install -r requirements.txt


4. **Run the development server:**

python manage.py runserver


**Endpoints**
User Endpoints
POST /users/create/: Create a new user.
GET /users/<user_id>/: Retrieve details of a specific user.
Expense Endpoints
POST /expenses/create/: Create a new expense.
GET /expenses/: List all expenses.
GET /expenses/<expense_id>/: Retrieve details of a specific expense.

