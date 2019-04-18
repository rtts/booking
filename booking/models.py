import random
import string
from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

def random_string():
    length = 6
    chars = '234679ABCDEFGHJKLMNPRSTUVWXYZabcdefghijkmnpqrstuvwxyz'
    unique = False
    while not unique:
        slug = ''.join(random.choice(chars) for x in range(length))
        if not Subject.objects.filter(slug=slug).exists():
            unique = True
    return slug

class Photoshoot(models.Model):
    slug = models.SlugField(_('slug'), unique=True)
    title = models.CharField(_('title'), max_length=32)
    introduction = RichTextField(_('introduction'), blank=True)
    confirmation = RichTextField(_('confirmation'), blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = _('Photoshoot')
        verbose_name_plural = _('Photoshoots')

class Subject(models.Model):
    name = models.CharField(_('name'), max_length=32)
    slug = models.CharField(_('slug'), max_length=16, default=random_string, unique=True)

    def get_url(self):
        return 'http://www.superformosa.nl/portrait/' + self.slug

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _('Subject')
        verbose_name_plural = _('Subjects')

class Timeslot(models.Model):
    shoot = models.ForeignKey(Photoshoot, verbose_name=_('shoot'), related_name=_('timeslots'), on_delete=models.PROTECT)
    subject = models.OneToOneField(Subject, blank=True, null=True, verbose_name=_('subject'), related_name='timeslot', on_delete=models.PROTECT)
    time = models.DateTimeField(_('time'))

    def __str__(self):
        return str(self.time)

    class Meta:
        ordering = ['shoot', 'time']
        verbose_name = _('Timeslot')
        verbose_name_plural = _('Timeslots')
