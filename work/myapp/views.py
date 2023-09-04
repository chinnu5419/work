from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def my_list(request):
    movies = [
        "RRR",
        "Pushpa",
        "Jailer",
    ]
    return render(request, 'my_list.html', {'movies': movies})