from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings('ignore')

# View for the Index/Home page
def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('diabetes_predictor:index')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')

# Register view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('diabetes_predictor:login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('diabetes_predictor:index')

# View for the Prediction page
def prediction(request):
    return render(request, 'prediction.html')

# View to handle the prediction and return the result
def result(request):
    # Correct path to the CSV file
    csv_path = os.path.join(settings.BASE_DIR, 'diabetis_predictor', 'diabetes.csv')
    
    # Load the diabetes dataset
    df = pd.read_csv(csv_path)
    
    # Preprocessing: define features (X) and label (Y)
    X = df.drop('Outcome', axis=1)
    Y = df['Outcome']
    
    # Split the data into training and testing sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    
    # Train a logistic regression model
    model = LogisticRegression()
    model.fit(X_train, Y_train)
    
    # Retrieve input values from GET request
    val1 = float(request.GET.get('n1', 0))
    val2 = float(request.GET.get('n2', 0))
    val3 = float(request.GET.get('n3', 0))
    val4 = float(request.GET.get('n4', 0))
    val5 = float(request.GET.get('n5', 0))
    val6 = float(request.GET.get('n6', 0))
    val7 = float(request.GET.get('n7', 0))
    val8 = float(request.GET.get('n8', 0))
    
    # Predict based on input values
    prediction = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])
    
    result_text = "Positive" if prediction[0] == 1 else "Negative"
    
    # Render the result back to the prediction.html page
    return render(request, 'prediction.html', {'result2': result_text})

# View for the About Us page
def about_us(request):
    return render(request, 'about_us.html')
