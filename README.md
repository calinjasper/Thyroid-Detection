# Thyroid Detection Project

This repository contains a Django web application that classifies thyroid ultrasound images into TIRADS categories using a trained Keras model. It also includes datasets and training notebooks used during model development.

## Features

- Thyroid ultrasound image classification into NORMAL, TIRADS1–TIRADS5.
- Secure user registration, login, and logout flow.
- Image upload form for prediction with stored image and predicted label.
- Result page with predicted label and informational guidance content.
- Public landing and informational pages (Home, Problem Statement, About).
- Django admin and SQLite database for local development.
- Training notebooks for multiple CNN architectures.

## Setup Guide

### Prerequisites

- Python 3.9+ recommended
- Pip
- (Optional) Virtual environment tool such as venv or conda

### Install Dependencies

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Initialize the Database

```bash
cd Deploy/project
python manage.py migrate
```

### Run the App

```bash
python manage.py runserver
```

Open the app at http://127.0.0.1:8000/.

## User Guidelines

1. Open the landing page and navigate to the app.
2. Register a new account or log in with an existing account.
3. Go to Thyroid Detection to upload an ultrasound image.
4. Submit the form to receive a predicted TIRADS label.
5. Review the results and guidance provided on the output page.
6. Use Logout when finished.

## Feature Details

- **Classification Pipeline**: Uploaded images are resized to 224x224, normalized, and passed into a Keras model to produce a class prediction.
- **Image Storage**: Uploaded images are saved in the media directory and linked to prediction records.
- **User Management**: The app uses Django’s built-in authentication for registration, login, and session handling.
- **Pages**:
  - Landing page for introduction and navigation
  - Home page with overview content
  - Problem statement page outlining the project motivation
  - Prediction page for image upload and inference
  - Output page with prediction result and informational content

## Repository Tour

- `Deploy/project/`: Django project root
  - `app/`: Application logic, templates, forms, and models
  - `project/`: Django settings and URL configuration
- `DATASET/`: Image datasets organized by TIRADS category
- `M1 - MANUAL NET.ipynb`: Manual CNN training notebook
- `M2 - DENCENET.ipynb`: DenseNet training notebook
- `M3 - LENET.ipynb`: LeNet training notebook
- `requirements.txt`: Python dependencies

## Notes

- The model file lives at `Deploy/project/app/keras_model.h5`.
- TensorFlow may log oneDNN initialization warnings on startup; this is expected.
