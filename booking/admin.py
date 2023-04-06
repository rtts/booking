from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.shortcuts import resolve_url
from django.contrib.admin.templatetags.admin_urls import admin_urlname
from .models import Subject, Photoshoot, Timeslot

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_timeslot', 'get_url', 'slug']
    list_filter = ['timeslot__time']
    search_fields = ['name']

    def get_timeslot(self, subject):
        if subject.timeslot:
            url = resolve_url(admin_urlname(Timeslot._meta, 'change'), subject.timeslot.pk)
            return format_html('<a href="{url}">{name}</a>'.format(url=url, name=str(subject.timeslot)))
        return '-'
    get_timeslot.short_description = _('timeslot')
    get_timeslot.admin_order_field = 'timeslot'

    def get_url(self, subject):
        return mark_safe('<a href="{url}" target="_blank">{url}</a>'.format(url=subject.get_url()))
    get_url.short_description = _('url')

@admin.register(Timeslot)
class TimeslotAdmin(admin.ModelAdmin):
    list_display = ['time', 'get_subject', 'dummy', 'get_url', 'get_slug']
    list_display_links = ['time']
    list_filter = ['shoot', 'time', 'dummy']
    list_editable = ['dummy']
    search_fields = ['subject__name']

    def get_subject(self, slot):
        if slot.subject:
            url = resolve_url(admin_urlname(Subject._meta, 'change'), slot.subject.pk)
            return format_html('<a href="{url}">{name}</a>'.format(url=url, name=str(slot.subject.name)))
        return '-'
    get_subject.short_description = _('subject')
    get_subject.admin_order_field = 'subject'

    def get_slug(self, slot):
        return slot.subject.slug if slot.subject else '-'
    get_slug.short_description = _('slug')

    def get_url(self, slot):
        if slot.subject:
            return mark_safe('<a href="{url}" target="_blank">{url}</a>'.format(url=slot.subject.get_url()))
        else:
            return '-'
    get_url.short_description = _('url')

@admin.register(Photoshoot)
class PhotoshootAdmin(admin.ModelAdmin):
    list_display = ['title']
