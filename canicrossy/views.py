from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Participant

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def set_participant_chrono(request, pk):
    participant_instance = get_object_or_404(Participant, pk=pk)
    if request.method == 'POST':
        print(request)
        #participant_instance.chrono = request.
        ##return HttpResponseRedirect(reverse('all-borrowed'))



