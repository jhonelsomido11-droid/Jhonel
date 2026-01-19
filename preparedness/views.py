from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def facts(request):
    return render(request, 'facts.html')

def checklist(request):
    return render(request, 'checklist.html')

def quiz(request):
    return render(request, 'quiz.html')

def plan(request):
    return render(request, 'plan.html')
