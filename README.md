# AI Loan Advisory Chatbot

An AI-powered web application developed to assist users in exploring loan options, applying for loans, receiving personalized loan recommendations, and obtaining intelligent responses to loan-related queries through an interactive chatbot.

This project was developed as the **major project** during my **Data Science Internship at Celebal Technologies**. The system combines modern web development with Artificial Intelligence techniques to provide a secure, scalable, and user-friendly loan advisory platform.

---

## Project Overview

The AI Loan Advisory Chatbot simplifies the loan application process by integrating intelligent recommendation and conversational assistance into a single web application. Users can securely register, apply for loans, track their applications, receive loan recommendations, and interact with an AI chatbot for loan-related guidance.

The project follows a modular architecture, making it easy to maintain, extend, and integrate additional features in the future.

---

## Objectives

- Develop a secure loan advisory platform.
- Provide personalized loan recommendations.
- Enable users to apply for loans online.
- Offer AI-assisted responses to loan-related queries.
- Improve user experience through an interactive dashboard.
- Build a scalable web application using Django.

---

## Key Features

- Secure User Registration and Login
- JWT-based Authentication
- Loan Recommendation System
- Online Loan Application
- Loan History Management
- AI-powered Loan Advisory Chatbot
- Document-based Question Answering
- Responsive Dashboard
- REST API Integration
- User Profile Management

---

## Technology Stack

### Programming Language
- Python

### Backend
- Django
- Django REST Framework

### Frontend
- HTML
- CSS
- JavaScript

### Database
- SQLite

### Authentication
- JWT (JSON Web Token)

### Development Tools
- Visual Studio Code
- Git
- GitHub
- Postman

---

## System Modules

### 1. User Authentication
- User Registration
- User Login
- JWT Authentication
- Session Management

### 2. Dashboard
- Displays user-specific information
- Navigation to application modules

### 3. Loan Recommendation
- Accepts financial information from users
- Generates suitable loan recommendations

### 4. Loan Application
- Submit loan applications
- Store application details
- Manage loan records

### 5. Loan History
- View previously submitted loan applications
- Track application status

### 6. AI Loan Advisory Chatbot
- Interactive chatbot interface
- Answers loan-related queries
- Provides context-aware responses

---

## Project Structure

```
AI_Loan_Advisory_Chatbot
│
├── chatbot/
├── frontend/
├── loans/
├── rag/
├── users/
├── templates/
├── static/
├── media/
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

## Workflow

```
User Registration/Login
            │
            ▼
       User Dashboard
            │
   ┌────────┼────────┐
   ▼        ▼        ▼
Apply     Loan      AI
Loan   Recommendation Chatbot
   │        │        │
   └────────┼────────┘
            ▼
      Response Display
```

---

## Installation Guide

### Clone the Repository

```bash
git clone https://github.com/Vansh2708/AI_Loan_Advisory_Chatbot.git
```

### Navigate to the Project

```bash
cd AI_Loan_Advisory_Chatbot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Database Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

### Run the Development Server

```bash
python manage.py runserver
```

Open your browser:

```
http://127.0.0.1:8000/
```

---

## Testing

The application has been tested for the following functionalities:

- User Registration
- User Login
- JWT Authentication
- Loan Recommendation
- Loan Application
- Loan History
- AI Chatbot
- API Endpoints
- Form Validation
- Error Handling

---

## Future Enhancements

- Upload personal PDF documents for AI-assisted querying
- Voice-enabled chatbot
- Multilingual support
- OCR-based document processing
- Loan EMI calculator
- Mobile application
- Cloud deployment
- Enhanced recommendation engine

---

## Learning Outcomes

This project provided practical experience in:

- Python Programming
- Django Web Development
- Django REST Framework
- REST API Development
- JWT Authentication
- Database Management
- Frontend Development
- AI-assisted Application Development
- Software Architecture
- Testing and Debugging
- Git & GitHub Version Control

---

## Internship Information

This project was developed as the capstone project during my **8-week Data Science Internship** at **Celebal Technologies**.

**Organization:** Celebal Technologies

**Role:** Data Science Intern

**Duration:** May 2026 – July 2026

**Project Type:** Internship Capstone Project
---

## Author

**Vansh Jain**

B.Tech Computer Science and Engineering

Birla Institute of Technology, Off-Campus Jaipur

GitHub: https://github.com/Vansh2708

---

## License

This project was developed as part of the Data Science Internship at Celebal Technologies for academic and educational purposes.