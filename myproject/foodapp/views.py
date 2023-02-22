from django.shortcuts import render, redirect, HttpResponse

from .forms import FoodForm

# Create your views here.
def addFoodView(request):
    form = FoodForm()
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Data saved!')
    template_name = 'foodapp/addDetails.html'
    context = {'form': form}
    return render(request, template_name, context)

