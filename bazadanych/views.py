from django.shortcuts import render

def default_message(request):
    return render(request, 'bazadanych/default_message.html')
