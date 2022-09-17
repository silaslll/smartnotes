from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView 
from .models import Notes

# Create your views here.

class NotesCreateView(CreateView):
    model = Notes
    fields = ['title', 'text']
    success_url = "/smart/notes"



class NotesListView(ListView):
    #specify which model we are listing object from
    model = Notes
    #the defulat context_object_name is object but we call it notes
    context_object_name = 'notes'
    #this is not necessary bacause our template name followed the standard of the class based view
    template_name = 'notes/notes_list.html'

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes' : all_notes})

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"

# def detail(request, pk):
#     try:
#         note  = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})