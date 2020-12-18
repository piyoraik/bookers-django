from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Book
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'books/index.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all()
