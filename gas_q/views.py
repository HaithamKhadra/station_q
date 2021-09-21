from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse , HttpResponse, response
# from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Appointment, User
from .forms import CreateForm
from django.contrib import messages
import json
import csv
import xlwt
import datetime


def login_view(request):

    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        user = User.objects.filter(username=username).exists()

        # Check if authentication successful
        if user:
            user_name = User.objects.get(username=username)            
            login(request, user_name)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "gas_q/login.html", {
                "message": "Invalid username."
            })
    else:
        return render(request, "gas_q/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]      

        # Attempt to create new user
        try:
            user = User.objects.create_user(username)
            user.save()
        except IntegrityError:
            return render(request, "gas_q/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "gas_q/register.html")


# @login_required(login_url='/login')
def index(request):

    form = CreateForm()

    if request.method == 'POST':

        form = CreateForm(request.POST or None, request.FILES or None)
        
        if form.is_valid():
            new_appointment = form.save(commit=False)
            car_num = request.POST['car_num']
            day = request.POST['day']
            timeslot = request.POST['timeslot']
            user = request.POST['user']
            car_num_exists = Appointment.objects.filter(car_num=car_num).exists()
            user_has_app = Appointment.objects.filter(user=user).exists()
            time_taken = Appointment.objects.filter(day=day, timeslot=timeslot).count() >= 2
            # timeslot_taken = Appointment.objects.filter(timeslot=timeslot).count() > 2

            # print(time_taken)
            if car_num_exists or user_has_app or time_taken:
                return render(request, 'gas_q/error.html')
            else:
                new_appointment.user = user
                new_appointment.save()
                # return redirect('index')
                return render(request, 'gas_q/done.html')

    return render(request, 'gas_q/index.html', {
        'form': form
    })

    # return render(request, "gas_q/index.html", {
    #     'test': 'hello, world!'
    # })

# @login_required(login_url='/login')
def json(request):
    if request.method == 'GET':
        try:
            all_apps = Appointment.objects.all()

        except:
            return JsonResponse({"error": "Invalid."}, status=400)

        all_apps = all_apps
        return JsonResponse([post.serialize() for post in all_apps], safe=False)

# @login_required(login_url='/login')
# def export_data(request):
    
#     response = HttpResponse(content_type='text/csv')
#     response['Content_Desposition']='attachment; filename=Appointment'+str(datetime.datetime.now())+'.csv'
    
#     writer = csv.writer(response, dialect='excel-tab')
#     writer.writerow(['user', 'car_make', 'car_num', 'day', 'timeslot'])

#     appointments = Appointment.objects.all()

#     for appointment in appointments:
#         for slot in range(len(appointment.TIMESLOT_LIST)):
#             if appointment.TIMESLOT_LIST[slot][0] == appointment.timeslot:
#                 for day in range(len(appointment.DAYS)):
#                     if appointment.DAYS[day][0] == appointment.day:
#                         writer.writerow([appointment.user.username, appointment.car_make, 
#                             appointment.car_num, appointment.DAYS[day][1], appointment.TIMESLOT_LIST[slot][1]]) 
    
    
#     return response


# @login_required(login_url='/login')
def export_data(request):
    
    response = HttpResponse(content_type='application/ms-excel')
    response['Content_Desposition']='attachment; filename=Appointment'+str(datetime.datetime.now())+'.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Appointment')
    row_num = 0
    font_style = xlwt.XFStyle() 
    font_style.font.bold = True

    columns = ['user', 'car_make', 'car_num', 'day', 'timeslot']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle() 
    # appointments = Appointment.objects.all().values_list('user', 'car_make', 'car_num', 'day', 'timeslot')
    appointments = Appointment.objects.all()
    # print(appointments)

    for appointment in appointments:
        row_num += 1

        # for slot in range(len(appointment.TIMESLOT_LIST)):
        #     print(str(appointment.TIMESLOT_LIST[slot][1]))
            # if appointment.TIMESLOT_LIST[slot][0] == appointment.timeslot:
            #     for day in range(len(appointment.DAYS)):
            #         if appointment.DAYS[day][0] == appointment.day:
            #             writer.writerow([appointment.user.username, appointment.car_make, 
            #                 appointment.car_num, appointment.DAYS[day][1], appointment.TIMESLOT_LIST[slot][1]])

        for col_num in range(5):
            if col_num == 0:
                ws.write(row_num, col_num, str(appointment.user), font_style)
            elif col_num == 1:
                ws.write(row_num, col_num, str(appointment.car_make), font_style)
            elif col_num == 2:
                ws.write(row_num, col_num, str(appointment.car_num), font_style)
            elif col_num == 3:
                for slot in range(len(appointment.DAYS)):
                    if appointment.DAYS[slot][0] == appointment.day:
                    # print(str(appointment.TIMESLOT_LIST[slot][1]))
                        ws.write(row_num, col_num, str(appointment.DAYS[slot][1]), font_style)
            elif col_num == 4:
                for slot in range(len(appointment.TIMESLOT_LIST)):
                    if appointment.TIMESLOT_LIST[slot][0] == appointment.timeslot:
                    # print(str(appointment.TIMESLOT_LIST[slot][1]))
                        ws.write(row_num, col_num, str(appointment.TIMESLOT_LIST[slot][1]), font_style)
        # for col_num in range(len(appointment)):
        #     ws.write(row_num, col_num, str(appointment[col_num]), font_style)
            # ws.write(row_num, col_num, str(appointment), font_style)

    wb.save(response)

    return response

def excel(request):
    return render(request, "gas_q/excel.html")
