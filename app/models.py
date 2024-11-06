from django.db import models

# Create your models here.

from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User  
from django import forms  
import datetime



class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Sub_Category(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    Availability = (('In Stock','In Stock'),('Out Of Stock','Out Of Stock'))
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=False,default='')
    sub_category = models.ForeignKey(Sub_Category,on_delete=models.CASCADE,null=False,default='')
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='bakery/pimg')
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    Availability = models.CharField(choices=Availability,null=True,max_length=150)

    def __str__(self):
        return self.name


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True,label="Email",error_messages={'exists':'This Email already exist'})

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'


    
    def save(self,commit=True):
        user = super(UserCreateForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if(commit):
            user.save()
        return user

    def clean_email(self):
        if(User.objects.filter(email=self.cleaned_data['email']).exists()):
            raise forms.ValidationError(self.fields['email'].error_message['exists'])
        return self.cleaned_data['email']
   
class Contact_Us(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.email

class Order(models.Model):
    image = models.ImageField(upload_to='bakery/order/image')
    product = models.CharField(max_length=1000,default='')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.CharField(max_length=5)
    total = models.CharField(max_length=10000,default='')
    address = models.TextField()
    phone = models.CharField(max_length=10)
    pincode = models.CharField(max_length=10)
    date = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return self.product

class OrderNew(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    # lastname = models.CharField(max_length=1000)
    country = models.CharField(max_length=1000)
    address = models.TextField()
    city =  models.CharField(max_length=1000)
    state =  models.CharField(max_length=1000)
    postcode = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField(max_length=10)
    amount  =  models.CharField(max_length=10000)
    payment_id = models.CharField(max_length=300,null=True,blank=True)
    paymentmode = models.CharField(max_length=1000,null=True,blank=True)
    paid = models.BooleanField(default=False,null=True)
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.user.username

class OrderItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    order = models.ForeignKey(OrderNew,on_delete=models.CASCADE)
    product = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='bakery/ordernew/image')
    quantity = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    total = models.CharField(max_length=10000)
    
    # def __str__(self):
    #     return self.user.username