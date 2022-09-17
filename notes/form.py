from socket import fromshare
from django import fromshare
from .models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        mode = Notes
        fields = ('title', 'text')