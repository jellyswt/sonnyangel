from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['lala', 'aksks'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')