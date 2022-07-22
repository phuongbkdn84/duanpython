from django.shortcuts import render
from nhanvien.models import Quanlynhanvien

# Create your views here.
def themnhanvien(request):
    return render(request,'themnhanvien.html')

def xuly_themnhanvien(request):
    tennv = request.GET.get('tennv')
    chucvunv = request.GET.get('chucvunv')
    namsinhnv = request.GET.get('namsinhnv')

    if(len(tennv) <5):
        return render(request,'loi_themnhanvien.html')
    else:
        dulieu = Quanlynhanvien(
            ten_nv = tennv,
            chucvu_nv = chucvunv,
            namsinh_nv = namsinhnv
        )
        dulieu.save()
       
        return render(request, 'new_themnhanvien.html')    #dangnhap.html

def xuly_thoat(request):
    return render(request,'dangnhap.html')      #dangnhap.html

