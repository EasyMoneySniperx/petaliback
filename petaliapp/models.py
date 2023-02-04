from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    username = models.CharField(max_length=50, default="Laika")
    email = models.EmailField(default="juanrevelo@gmail.com")
    password = models.CharField(max_length=30, default="12345")

class Parques(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    latitud = models.DecimalField(default=-76.525633)
    longitud = models.DecimalField(default=3.45412)
    name = models.CharField(max_length=200, default="Parque San Nicolas")
    src = models.CharField("https://www.elpais.com.co/files/article_main/uploads/2017/02/03/5894cbcd09a41.jpeg")

class Favorite(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_parque = models.ForeignKey(Parques, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

