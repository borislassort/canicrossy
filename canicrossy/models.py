from django.db import models
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
import datetime

## Athlete
class Athlete(models.Model):
    YEAR_CHOICES = []
    for r in range(1930, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
    GENDER_CHOICES = [('F','F'), ('M','M')]

    name = models.CharField('nom' , max_length=200)
    birth_date = models.IntegerField('année naissance', choices=YEAR_CHOICES, default=1980)
    gender = models.CharField('sex', choices=GENDER_CHOICES, max_length=1, blank=True)
    dog_name = models.CharField('chien nom', max_length=200)
    dog_race = models.CharField('chien race', max_length=200)
    license = models.CharField('num license', max_length=200)
    federation = models.ForeignKey('federation' , on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'athlète'
        verbose_name_plural = 'athlètes'

class AthleteForm(ModelForm):
    class Meta:
        model = Athlete
        fields = ['name', 'birth_date', 'dog_name']


## Race categories
class Category(models.Model):
    name = models.CharField('nom', max_length=200)
    description = models.CharField('description', max_length=200, blank=True)

    class Meta:
        verbose_name = 'categorie'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

## Race
class Race(models.Model):
    name = models.CharField('nom', max_length=200)
    date = models.DateField('date')
    city = models.CharField('ville', max_length=200)
    categories = models.ManyToManyField(Category)

    @property
    def total_participants(self):
        return Participant.objects.filter(race__pk=self.pk).count()
    
    @property
    def participants(self):
        return Participant.objects.filter(race__pk=self.pk)

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def __str__(self):
        return self.name
    
class RaceForm(ModelForm):
    class Meta:
        model = Race
        fields = ["name", "date", "city"]

## Participant
class Participant(models.Model):
    athlete = models.ForeignKey(Athlete, verbose_name='athlète', on_delete=models.CASCADE)
    race = models.ForeignKey(Race, verbose_name='course', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='categorie', on_delete=models.CASCADE)
    race_number = models.CharField('dossard', max_length=20)
    delay = models.IntegerField('délai (minutes)', default=0)
    time = models.CharField('chrono (mm:ss)', max_length=5, blank=True, null=True)

    @property
    def time_minus_delay_in_sec(self):
        if self.time:
            m, s = self.time.split(':')
            m = int(m) - self.delay
            return int(m)*60 + int(s)
        else:
            return -1


## Federation
class Federation(models.Model):
    name = models.CharField('nom', max_length=200)

    def __str__(self):
        return self.name

class FederationForm(ModelForm):
    class Meta:
        model = Federation
        fields = ["name"]

    

