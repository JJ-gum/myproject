from django.shortcuts import render

def default_message(request):
    return render(request, 'myapp/default_message.html')
