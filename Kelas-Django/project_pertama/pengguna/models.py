from django.db import models

# Create your models here.
class Pengguna(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = "Pengguna"
    