from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january":"Enero",
    "february": "Febrero",
    "march": "Marzo",
    "april":"Abril",
    "may": "Mayo",
    "june": "junio",
    "july":"julio",
    "august": "Agosto",
    "september": "Septiembre",
    "october": "Octubre",
    "november":"Noviembre",
    "december":"Diciembre",
}

perritos_challenge = {
    "fury": "Gury",
    "simba": "Simbatron",
    "wolfie":"Wolfiestein"
}



# Create your views here.

def monthly_challenge_by_number(request,month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Please go back")
    
    redirect_month = months[month -1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound(f"<h1>This month is not supported</h1>")
    



def perritos(request,perros):
    mascota = None
    if perros == "wolfie":
        mascota = "Wolfiestein"
    elif perros == "fury":
        mascotas = "FuryGury"
    elif perros == "simba":
        mascotas ="Simbatron"
    else:
        return HttpResponseNotFound("Esta mascota aun no existe")
    return HttpResponse(mascota)
