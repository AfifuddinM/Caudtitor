from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
from django.utils.timezone import now
from django.contrib.messages import success
import ollama
import os
from django.conf import settings

# Create your views here.

def testCode(request):
    link = os.path.join(settings.MEDIA_ROOT, 'badCode.py')
    with open(link,'rb') as file:
        content = file.read()

    prompts = f'Review this code, Rate the code "bad","mediocre","decent","good" alert any security vulnerabilities first such as sql injection and risks of attacks, provide suggestions for improvement, coding best practices, improve readability, and maintainability. Provide code examples for your suggestion." {content}'

    response = ollama.generate(model='codellama:7b',prompt=prompts)
    aResponse = response['response']

    file_path = os.path.join(settings.MEDIA_ROOT, 'output.txt')

    with open(file_path, 'w') as file:
        file.write(f"Response: {aResponse}\n\n")
        print(f"Response saved to {file_path}")

    return render(request,'cauditorApp/index.html')

def index(request):
    return render(request,'cauditorApp/index.html')