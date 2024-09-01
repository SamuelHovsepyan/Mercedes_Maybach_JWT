from django.db import models

class Logo(models.Model):
    name = models.CharField('Logo Name', max_length=40, blank=True)
    img = models.ImageField('Logo image', upload_to='images')

    def __str__(self):
        return self.name

class Homebg(models.Model):
    text1 = models.TextField('Home text1')
    text2 = models.TextField('Home text2')

    def __str__(self):
        return self.text1

class Year(models.Model):
    year = models.CharField('Year', max_length=4)

    def __str__(self):
        return self.year

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField('service img')

    def __str__(self):
        return self.title

class Car(models.Model):
    TRANSMISSION_CHOICES = [
        ('automatic', 'automatic'),
        ('manual', 'manual'),
    ]

    image = models.ImageField('Car image', upload_to='images')
    name = models.CharField('Car name', max_length=100)
    price = models.PositiveIntegerField('Car Price')
    running = models.FloatField('Car running')
    horsepower = models.PositiveIntegerField('Car horsepower')
    transmission = models.CharField('Transmission name', max_length=30, choices=TRANSMISSION_CHOICES)
    about = models.TextField('Car about')
    date = models.DateTimeField(auto_now=True)
    year = models.IntegerField('Car year')

    def __str__(self):
        return self.name

    
class Client(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='client_images/')
    report = models.TextField()

    def __str__(self):
        return self.name

# class Car3(models.Model):
    # image = models.ImageField('Car image', upload_to='home_images')
    # price = models.PositiveIntegerField('Car Price')

class Brand(models.Model):
    image = models.ImageField('Car image', upload_to='images')

class Price(models.Model):
    price = models.PositiveIntegerField('Car Price')


class Car2(models.Model):
    TRANSMISSION_CHOICES = [
        ('automatic', 'automatic'),
        ('manual', 'manual'),
    ]

    image = models.ImageField(upload_to='brands/')
    name = models.CharField('Car name', max_length=100)
    price = models.PositiveIntegerField('Car Price')
    running = models.FloatField('Car running')
    horsepower = models.PositiveIntegerField('Car horsepower')
    transmission = models.CharField('Transmission name', max_length=30, choices=TRANSMISSION_CHOICES)
    about = models.TextField('Car about')
    year = models.IntegerField('Car year')

    def __str__(self):
        return self.name
    
class Sign(models.Model):
    image1 = models.ImageField(upload_to='brands/')
    image2 = models.ImageField(upload_to='brands/')
    image3 = models.ImageField(upload_to='brands/')
    image4 = models.ImageField(upload_to='brands/')
    image5 = models.ImageField(upload_to='brands/')
    image6 = models.ImageField(upload_to='brands/')

class Contacts(models.Model):
    number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)