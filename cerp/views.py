from django.shortcuts import render

def login(request):
    return render(request, 'cerp/login.html', {})

def base(request):
    return render(request, 'cerp/base.html', {})

def counsel(request):
    return render(request, 'cerp/counsel.html', {})
