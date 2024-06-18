from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import *

class HomeTempLateView(TemplateView)
    template_name = 'base.html'

    def get_context_data(self, **kwargs): 
         context = super().get_context_data(**kwargs)
         context['UserProfile'] = UserProfile.objects.first()
         context['PetrusProject'] = PetrusProject.objects.all()
         context['PetrusSkill'] = PetrusSkill.objects.all()
         return context