from django.shortcuts import render
from .models import  *


from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect   
from .forms import CreateNewTask
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import *
from django.conf import settings 
from django.template.loader import get_template  
from django.core.mail import get_connection, EmailMessage
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMessage
import weasyprint

# Create your views here.

def index(request):
    title = "Hola Gabriela, ¡Bienvenida al Sistema Contable"
    return render(request,'index.html', {
        'title' : title 
    })


def login(request):
     return render(request, 'registration/login.html')

#def login(request):
    #if request.method == 'POST':
       # email = request.POST.get('email')
       # password = request.POST.get('password')

        #user = authenticate(request, email=email, password=password)
       # if user is not None:
            #login(request, user)
            #return redirect('') # ruta del tablero 
       # else:
           # messages.error(request, 'Correo inválido. Inténtalo de nuevo.')

    #return render(request, 'registration/login.html')

def sendmailChargeAccountToPdf(data):
    messageBody = get_template("sendChargeAccountForm.html").render(data)

    # Generar PDF a partir del HTML
    pdf = weasyprint.HTML(string=messageBody).write_pdf()

    email = EmailMessage(
        "CollectionAccount Form",
        "Please find the CollectionAccount Form attached.",
        settings.DEFAULT_FROM_EMAIL,
        to=["pinedapablo6718@gmail.com"]
    )

    # Adjuntar el PDF generado
    email.attach('collection_account.pdf', pdf, 'application/pdf')

    return email.send()

def createChargeAccountForm(request):
    if request.method == 'POST':
        form = ChargeAccountForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            data = { "name" : request.POST.get('name'),
                "identification" : request.POST.get('identification'),
                "concept" : request.POST.get('concept'),
                "value"  : request.POST.get('value'),
                "retention_392_401"  : request.POST.get('retention_392_401'),
                "retention_383" : request.POST.get('retention_383'),
                "declarant"  : request.POST.get('declarant'),
                "colombian_resident"  : request.POST.get('colombian_resident'),
                "city"  : request.POST.get('city'),
                "date"  : request.POST.get('date'),
                "cex"  : request.POST.get('cex'),
                "bank"  : request.POST.get('bank'),
                "type"  : request.POST.get('type'),
                "account_number"  : request.POST.get('account_number')
            }
            sendmailChargeAccountToPdf(data)
            return redirect("viewChargeAccountForm")
    else:
        form = ChargeAccountForm()
    return render(request, "chargeAccountForm.html", {"form": form})

def ventanillaUnicaResumida(request):
     datosSeguimiento = Following.objects.all()
      
     return render(request, 'ventanillaUnicaResumida.html',{ 'ventanilla' : datosSeguimiento})

def ventanillaUnica(request):
    datosSeguimiento = Following.objects.all()
    attachedDocuments = AttachedDocument.objects.all()

    return render(request, 'ventanillaUnica.html', {'ventanilla': datosSeguimiento, 'files': attachedDocuments})
