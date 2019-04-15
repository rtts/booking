from django.contrib import admin
from .models import Subject, Photoshoot, Timeslot

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'timeslot']

class TimeslotAdmin(admin.StackedInline):
    model = Timeslot
    extra = 0
    exclude = ['subject']

@admin.register(Photoshoot)
class PhotoshootAdmin(admin.ModelAdmin):
    inlines = [TimeslotAdmin]
