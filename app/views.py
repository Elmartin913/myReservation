from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import *
import datetime


# Create your views here.

time_now = datetime.date.today().strftime('%Y-%m-%d')

def rooms(request):
    all_rooms = Room.objects.all()
    context = {'all_rooms': all_rooms}
    return render(request, 'app/rooms.html', context)

@csrf_exempt
def room_new(request):
    if request.method == "GET":
        return render(request, template_name='app/new.html')
    else:
        name = request.POST.get('name')
        capacity = request.POST.get('capacity')
        description = request.POST.get('description')
        projector = request.POST.get('projector')
        all_rooms = Room.objects.create(name=name,
                                        capacity=capacity,
                                        description=description,
                                        projector=projector)
        return HttpResponseRedirect('/room/')


def modify(request, id):
    pass

@csrf_exempt
def room_modify(request, id):
    id = int(id)

    if request.method == 'GET':
        print('dzizla')
        r1 = Room.objects.get(pk=id)
        context = {'r1': r1}
        return render(request, 'app/roommodify.html', context)
    else:
        print('dzizla')
        r1 = Room.objects.get(pk=id)
        print(vars(r1))
        name = request.POST.get('name')
        capacity= request.POST.get('capacity')
        description = request.POST.get('description')
        r1.name = name
        r1.capacity = capacity
        r1.description = description
        print(vars(r1))
        r1.save()
        return HttpResponseRedirect('/room/')


def room_delete(request, id):
    if request.method == 'GET':
        id = int(id)
        r = Room.objects.get(pk=id)
        r.delete()
        return HttpResponseRedirect('/room/')

def room(request,id):
    id = int(id)
    r1 = Room.objects.get(pk=id)
    b1 = Booking.objects.filter(room_id=id).filter(date__gte=time_now)
    context = {'r1':r1, 'b1':b1}
    return render(request, 'app/roomshow.html', context)

@csrf_exempt
def reservation(request, id):
    id = int(id)
    b1 = Booking.objects.filter(room_id=id).filter(date__gte=time_now)
    if request.method == 'GET':
        r1 = Room.objects.get(pk=id)
        context = {'r1': r1, 'b1': b1, 'time_now':time_now}
        return render(request, 'app/reservation.html', context)
    else:
        date = request.POST.get('date')
        comments = request.POST.get('comments')
        booking_tab = [b.date for b in b1 if b.date == date]
        print(booking_tab)
        if len(booking_tab)==1:
                return HttpResponse('Termin już zajęty')
        elif len(booking_tab)==0:
            Booking.objects.create(date=date, comments=comments, room_id=id)
            return HttpResponseRedirect('/room/{}'.format(str(id)))
        else:
            return HttpResponse('Za dużo rezerwacji !!!')