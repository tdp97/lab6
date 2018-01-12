from django.shortcuts import render, HttpResponseRedirect
from .forms import BooksForm
from .models import Books
from django.views.generic import ListView


# Create your views here.



def fun(request):
    form = BooksForm(request.POST or None)

    if request.method == 'POST':
        print(request.POST)
        # if  form.is_valid():
        # return HttpResponseRedirect('/thanks/')
        new_form = form.save()

    return render(request, 'index.html', locals())


class BookList(ListView):
    template_name = 'book_list.html'
    model = Books
