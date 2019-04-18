from datetime import datetime
from django import forms
from django.utils import timezone
from .models import Subject, Timeslot

class BookingForm(forms.ModelForm):
    timeslot = forms.ModelChoiceField(queryset=None, empty_label=None, widget=forms.RadioSelect)

    def __init__(self, *args, shoot=None, instance=None, initial={}, **kwargs):
        if hasattr(instance, 'timeslot'):
            initial['timeslot'] = instance.timeslot.id
        super().__init__(*args, instance=instance, initial=initial,**kwargs)
        self.fields['timeslot'].queryset = shoot.timeslots

    def save(self):
        subject = super().save()
        if hasattr(subject, 'timeslot'):
            t = subject.timeslot
            t.subject = None
            t.save()
        timeslot = self.cleaned_data['timeslot']
        if not timeslot.subject:
            timeslot.subject = subject
            timeslot.save()
        return subject

    class Meta:
        model = Subject
        exclude = ['slug']

class ScheduleForm(forms.Form):
    date = forms.DateField()

    def save(self, shoot):
        date = self.cleaned_data['date']
        for hour in [10,11,12,13,14,15,16]:
            for minute in [0,10,20,30,40,50]:
                dt = timezone.make_aware(datetime(date.year, date.month, date.day, hour=hour, minute=minute))
                Timeslot(time=dt, shoot=shoot, dummy=(minute==50)).save()
