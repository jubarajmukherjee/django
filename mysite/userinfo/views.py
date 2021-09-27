from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import MyModel
from .signup import MyForm
 
def my_form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm()
  return render(request, 'signup.html', {'form': form})

#def infos(request):
#	return HttpResponse("This is info list")

def login_page(requests):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm()
  return render(request, 'login.html', {'form': form})