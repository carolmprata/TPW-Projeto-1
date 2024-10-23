from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    profile_picture = models.ImageField(upload_to='profile_pictures')
    numberOfPurchases = models.IntegerField(default=0)
    
    def __str__(self):
        return self.username

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='company_logos')

    def __str__(self):
        return self.name
    

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='products/')
    artist = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='products')
    stock = models.IntegerField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Vinil(Product):
    genre = models.CharField(max_length=50)
    lpSize = models.CharField(max_length=5)
    releaseDate = models.DateField()

    def __str__(self):
        return self.name + ' - ' + self.artist
    
class CD(Product):
    genre = models.CharField(max_length=50)
    releaseDate = models.DateField()

    def __str__(self):
        return self.name + ' - ' + self.artist
    

class Clothing(Product):
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' - ' + self.artist


class Accessory(Product):
    material = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' - ' + self.artist
    
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    products = models.ManyToManyField(Product, related_name='carts')
    date = models.DateField()
    total = models.FloatField()

    def __str__(self):
        return self.user.username + ' - ' + str(self.date)

class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    quantity = models.IntegerField()
    total = models.FloatField()

    def __str__(self):
        return self.product.name + ' - ' + str(self.quantity)

class Favorite(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorites')

    def __str__(self):
        return self.user.username + ' - ' + self.product.name
    
class Purchase(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    products = models.ManyToManyField(Product, related_name='purchases')
    date = models.DateField()
    total = models.FloatField()
    paymentMethod = models.CharField(max_length=50)
    shippingAddress = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username + ' - ' + str(self.date)

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    rating = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.user.username + ' - ' + self.product.name




