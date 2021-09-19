from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
# from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Appointment, User
from .forms import CreateForm
from django.contrib import messages
import json



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "gas_q/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "gas_q/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "gas_q/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "gas_q/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "gas_q/register.html")


@login_required(login_url='/login')
def index(request):

    form = CreateForm()

    if request.method == 'POST':

        form = CreateForm(request.POST or None, request.FILES or None)
        
        if form.is_valid():
            new_appointment = form.save(commit=False)
            car_num = request.POST['car_num']
            car_num_exists = Appointment.objects.filter(car_num=car_num).exists()
            user_has_app = Appointment.objects.filter(user=request.user).exists()
            if car_num_exists or user_has_app:
                return render(request, 'gas_q/index.html', {
                    'form': form,
                    'msg': 'failed'
                })
            else:
                new_appointment.user = request.user
                new_appointment.save()
                return redirect('index')

    return render(request, 'gas_q/index.html', {
        'form': form
    })

    # return render(request, "gas_q/index.html", {
    #     'test': 'hello, world!'
    # })

@login_required(login_url='/login')
def json(request):
    if request.method == 'GET':
        try:
            all_apps = Appointment.objects.all()

        except:
            return JsonResponse({"error": "Invalid."}, status=400)

        all_apps = all_apps
        return JsonResponse([post.serialize() for post in all_apps], safe=False)

