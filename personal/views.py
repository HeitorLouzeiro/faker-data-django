from django.shortcuts import render

from .models import Person


# Create your views here.
def home(request):
    template_name = 'personal/pages/home.html'
    persons = Person.objects.all().order_by('first_name')
    context = {'persons': persons}
    return render(request, template_name, context)
