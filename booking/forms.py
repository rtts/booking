from django import forms
from .models import Subject

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
