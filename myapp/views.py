from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'title': 'Welcome to MyApp',
        'message': 'This is a simple Django application.',
    }
    return render(request, 'index.html', context)