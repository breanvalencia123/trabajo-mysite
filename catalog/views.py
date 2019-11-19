from django.shortcuts import render
from .models import Bicicleta

# Create your views here.
def index(request):
	Bici= Bicicleta.objects.all()
	return render(request,'catalog/index.html',context={'Bici':Bici,})