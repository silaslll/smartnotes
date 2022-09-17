from django.contrib import admin

from . import models

# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    #we don't need any configuration on this admin model
    pass

admin.site.register(models.Notes, NotesAdmin)