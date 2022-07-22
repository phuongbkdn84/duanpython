import email
from django.db import models

# Create your models here.
class Quanlynhanvien(models.Model):
    ten_nv = models.CharField(max_length=100)
    chucvu_nv = models.CharField(max_length=100)
    namsinh_nv = models.CharField(max_length=100)

    def __str__(self):
        return self.tennv
# Tao ban trong SQL