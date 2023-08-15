from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import random
import string

# class userProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone = models.CharField(unique=True, max_length=15)
#     address = models.TextField()
#     country = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     pin = models.CharField(max_length=50)

married_choice = [
    ('married', 'Married'),
    ('unmarried', 'UnMarried'),
]

def resize_image(image):
    img = Image.open(image)
    img.thumbnail((500, 450))
    img.save(image.path)

class customer(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    customer_id = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50)
    dob = models.DateField()
    mobile = models.CharField(unique=True,max_length=15)
    email = models.EmailField(max_length=254)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    married_status = models.CharField(max_length=50, choices=married_choice)
    nominee = models.CharField(max_length=50)
    aadhar = models.CharField(unique=True,max_length=20)
    pan = models.CharField(unique=True,max_length=20)
    address = models.TextField()
    pin = models.CharField(max_length=10)
    pan_image = models.ImageField(upload_to='upoaded_image', max_length=500)
    passport_image = models.ImageField(upload_to='upoaded_image', max_length=500) 
    aadhar_front_image = models.ImageField(upload_to='upoaded_image', max_length=500)
    aadhar_back_image = models.ImageField(upload_to='upoaded_image', max_length=500)
    signeture_image = models.ImageField(upload_to='upoaded_image', max_length=500)
    account_status = models.BooleanField(default=0)
    created_at = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        randomid = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(20)])
        self.customer_id = str('Customer_'+randomid)
        super(customer, self).save(*args, **kwargs)
        if self.pan_image:
            resize_image(self.pan_image)

        if self.passport_image:
            resize_image(self.passport_image)

        if self.aadhar_front_image:
            resize_image(self.aadhar_front_image)

        if self.aadhar_back_image:
            resize_image(self.aadhar_back_image)

        if self.signeture_image:
            resize_image(self.signeture_image)

    def __str__(self):
        return self.customer_id


# class BankDetails(models.Model):
#     customer = models.OneToOneField(customer, on_delete=models.SET_NULL, null=True)
#     account_number = models.CharField(max_length=50)
#     ifsc_code = models.CharField(max_length=50)
#     card_number = models.CharField(max_length=50)
#     card_cvv = models.CharField( max_length=10)
#     card_pin = models.CharField( max_length=10)
#     created_at = models.DateField( auto_now=True)