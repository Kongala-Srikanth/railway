from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from trainApp.forms import Register,SearchForm,Booking
from django.contrib.auth.decorators import login_required
from trainData import *
from django.contrib import messages

# Create your views here.


def homepage(request):
    return render(request,'home page/index.html')

def register(request):
    form = Register
    myform = {'form':form}

    if request.method=='POST':
        form = Register(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Registration')
            return redirect('/')
        else:
            messages.success(request,'Registration Failed. Please Try Again...')

    return render(request,'register page/register.html',myform)


@login_required
def searching(request):
    form = SearchForm
    mytrain = {'form':form}

    from_train = ''
    to_train = ''

    if request.method=='POST':
        form = SearchForm(request.POST)
        
        if form.is_valid():
            from_train = form.cleaned_data['From_location']
            to_train = form.cleaned_data['To_location']

        

        if (from_train == 'Hyderabad' and to_train == 'Delhi') or (from_train == 'Delhi' and to_train == 'Hyderabad'):
            data = hyd_delhi
            data = {'data':data}
        elif (from_train == 'Hyderabad' and to_train == 'Tamil Nadu') or (from_train == 'Tamil Nadu' and to_train == 'Hyderabad'):
            data = hyd_tamilnadu
            data = {'data':data}
        elif (from_train == 'Hyderabad' and to_train == 'Vizag') or (from_train == 'Vizag' and to_train == 'Hyderabad'):
            data = hyd_vizag
            data = {'data':data}
        elif (from_train == 'Hyderabad' and to_train == 'Mumbai') or (from_train == 'Mumbai' and to_train == 'Hyderabad'):
            data = hyd_mumbai
            data = {'data':data}
        elif (from_train == 'Hyderabad' and to_train == 'Tirupati') or (from_train == 'Tirupati' and to_train == 'Hyderabad'):
            data = hyd_tirupati
            data = {'data':data}
        elif (from_train == 'Hyderabad' and to_train == 'Karnataka') or (from_train == 'Karnataka' and to_train == 'Hyderabad'):
            data = hyd_karantaka
            data = {'data':data}
        else:
            return render(request,'train data/train_data_error.html')

         
        return render(request,'train data/train_data.html',data)

    return render(request,'train search/train-search.html',mytrain)



def booking(request):
    form = Booking
    mybooking = {'form':form}

    if request.method=='POST':
        form = Booking(request.POST)

        if form.is_valid():
            form.save()
        return homepage(request)

    return render(request,'booking/ticket-booking-page.html',mybooking)