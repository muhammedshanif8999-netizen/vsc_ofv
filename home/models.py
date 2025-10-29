from django.db import models


class Costumer(models.Model):
    COUNTRY_CHOICES = [
        ('India', 'India'),
    ]
    STATE_CHOICES = [
        ('AN', 'Andaman and Nicobar Islands'),
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CH', 'Chandigarh'),
        ('CG', 'Chhattisgarh'),
        ('DL', 'Delhi'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JH', 'Jharkhand'),
        ('JK', 'Jammu and Kashmir'),
        ('KA', 'Karnataka'),
        ('Kerala','Kerala'),
        ('LA', 'Ladakh'),
        ('LD', 'Lakshadweep'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OD', 'Odisha'),
        ('PB', 'Punjab'),
        ('PY', 'Puducherry'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TS', 'Telangana'),
        ('TR', 'Tripura'),
        ('UP', 'Uttar Pradesh'),
        ('UK', 'Uttarakhand'),
        ('WB', 'West Bengal'),
    ]
    image = models.ImageField(upload_to='users')
    name = models.CharField(max_length=200)
    number = models.IntegerField()
    email = models.EmailField(unique=True)
    country = models.CharField(choices=COUNTRY_CHOICES,default='India')
    house_name = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    pincode = models.IntegerField()
    city = models.CharField(max_length=200)
    state = models.CharField(choices=STATE_CHOICES, default='Kerala')
    username = models.CharField()
    password = models.CharField()
    location = models.CharField(max_length=200)
    points = models.IntegerField(default=0,null=True,blank=True)

class Seller(models.Model):
    COUNTRY_CHOICES = [
        ('India', 'India'),
    ]
    STATE_CHOICES = [
        ('AN', 'Andaman and Nicobar Islands'),
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CH', 'Chandigarh'),
        ('CG', 'Chhattisgarh'),
        ('DL', 'Delhi'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JH', 'Jharkhand'),
        ('JK', 'Jammu and Kashmir'),
        ('KA', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('LA', 'Ladakh'),
        ('LD', 'Lakshadweep'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OD', 'Odisha'),
        ('PB', 'Punjab'),
        ('PY', 'Puducherry'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TS', 'Telangana'),
        ('TR', 'Tripura'),
        ('UP', 'Uttar Pradesh'),
        ('UK', 'Uttarakhand'),
        ('WB', 'West Bengal'),
    ]
    image = models.ImageField(upload_to='users')
    name = models.CharField(max_length=200)
    number = models.IntegerField()
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=200,choices=COUNTRY_CHOICES,default='India')
    shop_name = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    pincode = models.IntegerField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=50, choices=STATE_CHOICES, default='Kerala')
    image1 = models.ImageField(upload_to='users')
    image2 = models.ImageField(upload_to='users')
    image3 = models.ImageField(upload_to='users')
    licens = models.IntegerField(max_length=200)
    GST_Number = models.IntegerField(max_length=200)
    username = models.CharField()
    password = models.CharField()
    location = models.CharField(max_length=200)

class Item(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products')
    image1 = models.ImageField(upload_to='products',null=True, blank=True)
    image2 = models.ImageField(upload_to='products',null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    org_price = models.DecimalField(max_digits=10, decimal_places=0)
    selling_price = models.DecimalField(max_digits=10, decimal_places=0)
    discount = models.DecimalField(max_digits=10, decimal_places=0,null=True, blank=True)
    stock = models.IntegerField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2,null=True,blank=True)

    
    def __str__(self):
        return self.name




class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2,null=True,blank=True)
    review = models.TextField(null=True,blank=True)
    review_img = models.ImageField(upload_to='products',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.product.name


class Cart(models.Model):
    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    amount = models.DecimalField(max_digits=10,decimal_places=0, default=0, null=True, blank=True)
    points = models.IntegerField(default=0,null=True, blank=True)

class Orders(models.Model):
    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=10,decimal_places=0, default=0, null=True, blank=True)
    points = models.IntegerField(default=0,null=True, blank=True)
    n = models.DecimalField(max_digits=100,decimal_places=0, default=0, null=True, blank=True)
    payment_method = models.CharField(max_length=200,null=True, blank=True)
    


class Order(models.Model):
    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=10,decimal_places=0, default=0, null=True, blank=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE,null=True, blank=True)
    status = models.CharField(null=True, blank=True)
    points = models.IntegerField(default=0,null=True, blank=True)
    n = models.DecimalField(max_digits=100,decimal_places=0, default=0, null=True, blank=True)
    def __str__(self):
        return self.product.name

