
from django.shortcuts import render
from Familiares.models import Familiar

def familiares(request):
    familiar1=Familiar.objects.create(name="Juan", last_name="Galvez", age= 30)
    familiar2=Familiar.objects.create(name="Luciana", last_name="Galvez", age= 40)
    familiar3=Familiar.objects.create(name="Alberto", last_name="Galvez", age= 20)
    context={
        "Familiares":[familiar1,familiar2,familiar3]
    }
    return render(request,"Familiares.html",context=context)
