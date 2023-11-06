from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

menu = [{'title': 'Главная', 'url_n': 'home'}, {'title': ' О сайте', 'url_n': 'about'}]

data_db = [{'id': 1, 'title': 'Илон Маск', 'content': 'Биография Маска', 'is_public': True},
           {'id': 2, 'title': 'Жириновский', 'content': 'Биография Жириновского', 'is_public': True},
           {'id': 3, 'title': 'Баба яга', 'content': 'Биография бабы яги', 'is_public': False},

           ]


# Create your views here.
def index(request):
    data = {'title': "Главная страница",
            'menu': menu,
            'float': 3.8,
            'posts': data_db

            }
    return render(request, 'women/index.html', context=data)
    return render(request, 'women/index.html', data)
    return render(request, 'women/index.html', {'title': "Главная страница"})


def about(request):
    # return redirect('spisok_pri', '12')
    return render(request, 'women/about.html',  {'title': "О программе",'menu': menu} )
    return HttpResponse('<h1> БГИТУ </h1>')

def cub(request):

    return render(request, 'women/3D_kub.html')



def pri_id(request, number_student):
    if int(number_student) > 30:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1> ПРИ 201 </h1> <p>Студент под номером {number_student} </p>')


def categories(request, cat):
    return HttpResponse(f'<h1> Ссылка {cat} </h1>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена проверьте адрес!! </h1>')


def page500(exception):
    return HttpResponseNotFound(f'<h1> Ошибка!! {exception} </h1>')


def page403(request, exception):
    return HttpResponseNotFound(f'<h1> Не пущу!! {exception} </h1>')
