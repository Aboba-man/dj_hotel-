# Create your views here.
from django.shortcuts import render
from django.views.generic import View
import datetime
from django.shortcuts import render,redirect

from .models import Rooms,Booking
from django.views.generic import ListView
from django.contrib import messages
from django.http import HttpResponse
# def home(request):
#     context = {
        
#     }
#     return render(request, 'home.html', context)

# class Fr_viw(View):

def home(request):
        
    return render(request, 'index.html', {})


# def book(request):
#     if request.method=="POST":
#         start_date=request.POST['start_date']
#         end_date=request.POST['end_date']
#         request.session['start_date']=start_date
#         request.session['end_date']=end_date
#         start_date=datetime.datetime.strptime(start_date, "%d/%b/%Y").date()
#         end_date=datetime.datetime.strptime(end_date, "%d/%b/%Y").date()
#         no_of_days=(end_date-start_date).days
#         data=Rooms.objects.filter(is_available=True,no_of_days_advance__gte=no_of_days,start_date__lte=start_date)
#         request.session['no_of_days']=no_of_days
#         return render(request,'book.html',{'data':data})
#     else:
#         return redirect('home')
    
class Roms(ListView):
    model=Rooms
    template_name='rooms.html'

    # ordering=['-id']
    # paginate_by = 6

class Bockig(ListView):
    model=Booking
    template_name='booking.html'
