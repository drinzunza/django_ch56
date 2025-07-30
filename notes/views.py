from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Note
from .forms import NoteForm
from django.urls import reverse_lazy

"""
Class-based views:

View        = generic view
ListView    = get a list of records
DetailView  = get a single(detail) record
CreateView  = create a new record
DeleteView  = remove a record
UpdateView  = modify an existing record
LoginView   = login
"""


class NoteList(ListView):
    template_name = "notes/list.html"
    model = Note


class NoteCreate(CreateView):
    template_name  = "notes/create.html"
    form_class = NoteForm
    success_url = reverse_lazy("note_list")