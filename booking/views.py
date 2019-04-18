from django.shortcuts import reverse
from django.views.generic import FormView, DetailView
from django.views.generic.detail import SingleObjectMixin
from .models import Photoshoot, Subject
from .forms import BookingForm

class Welcome(SingleObjectMixin, FormView):
    template_name = 'booking/welcome.html'
    model = Photoshoot

    def get_success_url(self):
        return reverse('booking:welcome', args=[self.object.slug])

    def get_form_class(self):
        return BookingForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['shoot'] = self.object
        try:
            kwargs['instance'] = Subject.objects.get(id=self.request.session.get('subject_id'))
        except Subject.DoesNotExist:
            pass
        return kwargs

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        subject = form.save()
        self.request.session['subject_id'] = subject.id
        return super().form_valid(form)

class Success(DetailView):
    template_name = 'booking/success.html'
    model = Photoshoot

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['subject'] = Subject.objects.get(id=self.request.session.get('subject_id'))
        except Subject.DoesNotExist:
            pass
        return context
