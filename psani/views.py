from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
import random

import logging
logger = logging.getLogger(__name__)

def domu(request):
    return render(request, "domu.html")

def lgin(request):
    if not models.Uzivatel.objects.filter(email=request.user.email).exists():
        models.Uzivatel(id=request.user.id, email=request.user.email, lekce="").save()
    return redirect("/")

def get_lekce(request): #hihihiha
    try: x = models.Uzivatel.objects.get(email=request.user.email).get_lekce()
    except: x = []
    context = {
        "seznam_lekci": models.Lekce.objects.all(),
        "dokonceny": x,
    }
    return render(request, "lekce.html", context)

def cviceni(request, cislo): #generace textu
    text = ""
    pismena = models.Lekce.objects.get(id=cislo).pismena
    if cislo in [1,2,3,4]:
        for slovo in range(5):
            slovo = ""
            for _ in range(4):
                slovo += random.choice(pismena)
            slovo += " "
            text += slovo
        text = text[:len(text)-1]

    context = {
        "pismena": pismena,
        "jmeno": models.Lekce.objects.get(id=cislo).jmeno,
        "text": text,
        "delka": len(text),
        "seznam_lekci": models.Lekce.objects.all(),
        "seznam_lekci_list": list(models.Lekce.objects.all().values_list('pismena', flat=True).distinct()),
    }
    return render(request, "cviceni.html", context)

def lekce_re(request, pismena):
    lekce = models.Lekce.objects.get(pismena=pismena)
    user = models.Uzivatel.objects.get(email=request.user.email)
    if not f" {lekce.id}," in user.lekce:
        user.lekce += str(lekce.id) + ","
        user.save()
    return redirect("/lekce")

def error_404_view(request, exception=None):
    return render(request, '404.html', status=404)