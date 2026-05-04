from django.shortcuts import render
from .models import *
# Create your views here.

def HomePage(request):
    intro = IntroModel.objects.all()
    about = AboutModel.objects.all()
    expertiseone = ExpertiseOneModel.objects.all()
    expertisetwo = ExpertiseTwoModel.objects.all()
    client = ClientModel.objects.all()
    logo = LogoModel.objects.all()
    testimonials = TestimonialsModel.objects.all()
    contact = ContactModel.objects.all()
    journalone = JournalOneModel.objects.all()
    journaltwo = JournalTwoModel.objects.all()
    context = {
        'intro' : intro,
        'about' : about,
        'expertiseone' : expertiseone,
        'expertisetwo' : expertisetwo,
        'client' : client,
        'logo' : logo,
        'testimonials' : testimonials,
        'contact' : contact,
        'journalone' : journalone,
        'journaltwo' : journaltwo,
    }
    return render(request, 'index.html', context)
    
