from django.db import models


# Create your models here.
class NguoiDung(models.Model):
    ten_dang_nhap=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    matkhau=models.CharField(max_length=100)

    def __str__(self):
        return self.ten_dang_nhap