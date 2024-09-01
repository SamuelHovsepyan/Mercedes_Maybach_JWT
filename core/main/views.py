from django.shortcuts import render
from .models import Logo, Homebg, Year, Service, Car, Client, Brand, Price, Contacts, Car2, Sign

def index(request):
    logo = Logo.objects.all().first()
    homebg = Homebg.objects.all().first()
    year = Year.objects.all()
    service= Service.objects.all()
    car = Car.objects.all()[:3]
    clients = Client.objects.all()
    car2 = Car2.objects.all()
    sign = Sign.objects.first()
    brands = Brand.objects.all()
    prices = Price.objects.all()
    contact = Contacts.objects.first()
    return render(request, 'index.html', context= {
        'logo': logo,
        'homebg': homebg,
        'year': year,
        'service': service,
        'car': car,
        'clients': clients,
        'Car2': car2,
        'Sign': sign,
        'brands':brands,
        'prices':prices,
        'contact':contact,
    })
