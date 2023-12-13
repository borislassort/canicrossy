from django.db import models
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
import datetime
import numpy
from datetime import timedelta

## Athlete
class Athlete(models.Model):
    YEAR_CHOICES = []
    for r in range(1930, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
    GENDER_CHOICES = [('F','F'), ('M','M')]

    first_name = models.CharField('prénom' , max_length=200)
    last_name = models.CharField('nom' , max_length=200)
    birth_date = models.IntegerField('année naissance', choices=YEAR_CHOICES, blank=True, null=True)
    gender = models.CharField('sex', choices=GENDER_CHOICES, max_length=1, blank=True, null=True)
    license = models.CharField('num license', max_length=200, blank=True, null=True)
    federation = models.ForeignKey('federation' , on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.first_name +" "+ self.last_name

    class Meta:
        verbose_name = 'athlète'
        verbose_name_plural = 'athlètes'

class AthleteForm(ModelForm):
    class Meta:
        model = Athlete
        fields = ['first_name', 'last_name', 'birth_date']

class Dog(models.Model):
    name = models.CharField('nom' , max_length=200)
    race = models.CharField('race', max_length=200, blank=True, null=True)
    ident = models.CharField('ident', max_length=200)
    
    def __str__(self):
        return self.name +" : "+ self.ident

    class Meta:
        verbose_name = 'chien'
        verbose_name_plural = 'chiens'

class DogForm(ModelForm):
    class Meta:
        model = Dog
        fields = ['name', 'race', 'ident']

## Categories
class Category(models.Model):
    name = models.CharField('nom', max_length=200)
    description = models.CharField('description', max_length=200, blank=True)

    class Meta:
        verbose_name = 'categorie'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


## Event
class Event(models.Model):
    name = models.CharField('nom', max_length=200)
    date = models.DateField('date')
    location = models.CharField('lieu', max_length=200)

    #@property
    #def total_participants(self):
    #    return Participant.objects.filter(event__pk=self.pk).count()
    
    #@property
    #def participants(self):
    #    return Participant.objects.filter(event__pk=self.pk)

    @property
    def races(self):
        return Race.objects.filter(event__pk=self.pk)

    class Meta:
        verbose_name = 'evenement'
        verbose_name_plural = 'evenements'

    def __str__(self):
        return self.name

    class Counter:
        count = 0
        def increment(self):
            self.count += 1
            return ''
        def decrement(self):
            self.count -= 1
            return ''
        def double(self):
            self.count *= 2
            return ''
    
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ["name", "date", "location"]

class Race(models.Model):
    name = models.CharField('nom', max_length=200)
    event = models.ForeignKey(Event, verbose_name='evenement', on_delete=models.CASCADE, blank=True, null=True)
    categories = models.ManyToManyField(Category)

    @property
    def participants(self):
        return Participant.objects.filter(race__pk=self.pk)

    @property
    def categories_with_participant(self):
        c = []
        for p in self.participants:
            if not p.category in c:
                c.append(p.category)
        return c

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'

## Participant
class Participant(models.Model):
    athlete = models.ForeignKey(Athlete, verbose_name='athlète', on_delete=models.CASCADE)
    dog = models.ForeignKey(Dog, verbose_name='chien', on_delete=models.CASCADE, blank=True, null=True)
    race = models.ForeignKey(Race, verbose_name='course', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='categorie', on_delete=models.CASCADE)
    race_number = models.CharField('dossard', max_length=20, blank=True, null=True)
    delay = models.CharField('délai (mm:ss)', max_length=5, default="00:00")
    time = models.CharField('chrono (mm:ss)', max_length=5, blank=True, null=True)

    class Meta:
        verbose_name = 'participation'
        verbose_name_plural = 'participations'

    @property
    def time_minus_delay_in_sec(self):
        if self.time:
            m, s = self.time.split(':')
            md, sd = self.delay.split(':')
            time_in_sec = timedelta(minutes=int(m), seconds=(int(s))).total_seconds()
            delay_in_sec = timedelta(minutes=int(md), seconds=(int(sd))).total_seconds()
            return time_in_sec - delay_in_sec
        else:
            return -1

    @property
    def time_minus_delay(self):
        if self.time:
            return str(timedelta(seconds=self.time_minus_delay_in_sec))
        else:
            return ""

## Federation
class Federation(models.Model):
    name = models.CharField('nom', max_length=200)

    def __str__(self):
        return self.name

class FederationForm(ModelForm):
    class Meta:
        model = Federation
        fields = ["name"]

