from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from .models import Subject, Photoshoot, Timeslot

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['timeslot', 'name', 'get_url']
    list_display_links = ['name']
    list_filter = ['timeslot__time']

    def get_url(self, subject):
        return mark_safe('<a href="{url}" target="_blank">{url}</a>'.format(url=subject.get_url()))
    get_url.short_description = _('url')

@admin.register(Timeslot)
class TimeslotAdmin(admin.ModelAdmin):
    list_display = ['shoot', 'time', 'subject', 'get_url']
    list_display_links = ['time']
    list_filter = ['shoot', 'time']

    def get_url(self, slot):
        if slot.subject:
            return mark_safe('<a href="{url}" target="_blank">{url}</a>'.format(url=slot.subject.get_url()))
        else:
            return '-'
    get_url.short_description = _('url')

@admin.register(Photoshoot)
class PhotoshootAdmin(admin.ModelAdmin):
    list_display = ['title']
