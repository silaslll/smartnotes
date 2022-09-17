from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView
from .models import Notes

# Create your views here.

class NotesListView(ListView):
    #specify which model we are listing object from
    model = Notes
    #the defulat context_object_name is object but we call it notes
    context_object_name = 'notes'
    #this is not necessary bacause we followed the standard naming rule
    template_name = 'notes/notes_list.html'

#def list(request):
    #all_notes = Notes.objects.all()
    #return render(request, 'notes/notes_list.html', {'notes' : all_notes})

def detail(request, pk):
    try:
        note  = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note does not exist")
    return render(request, 'notes/notes_detail.html', {'note': note})