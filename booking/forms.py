from django import forms
from .models import Subject

class BookingForm(forms.ModelForm):
    timeslot = forms.ModelChoiceField(queryset=None, empty_label=None)

    def __init__(self, *args, shoot=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['timeslot'].queryset = shoot.timeslots

    def save(self):
        subject = super().save()
        timeslot = self.cleaned_data['timeslot']
        timeslot.subject = subject
        timeslot.save()

    class Meta:
        model = Subject
        fields = '__all__'
