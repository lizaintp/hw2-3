from django.shortcuts import render
from apps.base.models import Settings, Portfolio,AcademicPositions, EducationTraining,Rewards, Works, Experience, AboutYourself, Journal, Research, Contacts
# Register your models here.
# Create your views here. 

def index(request):
    settings = Settings.objects.latest("id")
    portfolio = Portfolio.objects.latest('id')
    academicpositions = AcademicPositions.objects.all()
    educationtraining = EducationTraining.objects.all()
    rewards = Rewards.objects.all()
    works = Works.objects.all()
    experience = Experience.objects.all()
    aboutyourself = AboutYourself.objects.all()
    journal = Journal.objects.all()
    research = Research.objects.latest('id')
    contacts = Contacts.objects.latest('id')
    
    return render(request, 'index.html', locals())