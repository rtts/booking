from django.shortcuts import reverse
from django.views.generic import FormView, DetailView
from django.views.generic.detail import SingleObjectMixin
from .models import Photoshoot
from .forms import BookingForm

class Welcome(SingleObjectMixin, FormView):
    template_name = 'booking/welcome.html'
    model = Photoshoot

    def get_success_url(self):
        return reverse('booking:success', args=[self.object.slug])

    def get_form_class(self):
        return BookingForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'shoot': self.object,
        })
        return kwargs

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Success(DetailView):
    template_name = 'booking/success.html'
    model = Photoshoot
