from django.shortcuts import render, redirect, HttpResponse
from .models import Food
from .forms import FoodForm

# Create your views here.
def addFoodView(request):
    form = FoodForm()
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name = 'foodapp/addDetails.html'
    context = {'form': form}
    return render(request, template_name, context)

def showDetailsView(request):
    obj = Food.objects.all()
    template_name = 'foodapp/showDetails.html'
    context = {'obj': obj}
    return render(request, template_name, context)

def editDetailsView(request):
    obj = Food.objects.all()
    template_name = 'foodapp/editDetails.html'
    context = {'obj': obj}
    return render(request, template_name, context)

def updateDetailsView(request,id):
    obj = Food.objects.get(id=id)
    form = FoodForm(instance=obj)
    if request.method == 'POST':
        form = FoodForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name = 'foodapp/addDetails.html'
    context = {'form': form}
    return render(request, template_name, context)

def deleteDetailsView(request,id):
    obj = Food.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('show')
    template_name = 'foodapp/confirmDelete.html'
    context = {'obj': obj}
    return render(request, template_name, context)
