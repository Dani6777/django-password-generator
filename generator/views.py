from django.shortcuts import render
import random
import string


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,  'about.html')

def password(request):
    characters = list(string.ascii_lowercase)
    generated_password = ''
    
    length = max(int(request.GET.get('length', 12)), 1)

    if request.GET.get('uppercase'):
        characters.extend(list(string.ascii_uppercase))

    if request.GET.get('special'):
        characters.extend(list(string.punctuation))

    if request.GET.get('numbers'):
        characters.extend(list(string.digits))

    for _ in range(length):
        generated_password += random.choice(characters)

    return render(request, 'password.html', {'password': generated_password})