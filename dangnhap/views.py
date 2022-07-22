import email
from multiprocessing import context
from django.shortcuts import get_object_or_404, render

from dangky.models import NguoiDung
# Create your views here.
def dangnhap(request):
    return render(request,'dangnhap.html')

def trangchu(request):
    return render(request,trangchu.html)

def xuly_dangnhap(request):
    ten=request.GET.get('ten')
    mk=request.GET.get('matkhau')
    #print (ten)
    #print(mk)
    data=NguoiDung.objects.filter(ten_dang_nhap=ten, matkhau=mk) 
    #tuong duong voi lenh Query trong SQL
    danh_sach=NguoiDung.objects.all() 
    context={
        'ds_nguoidung': danh_sach # nhieu doi tuong, kieu dictionary
            }
    #bien ds_nguoidung xu ly trong danhsach.html

   # thongtin=NguoiDung.objects.filter(ten_dang_nhap=ten, matkhau=mk)
    # tuong ung SQL se tao lenh query trong SQL
    if(data.exists()):
        return render(request, 'danhsach.html', context)
       # return render(request, 'themnhanvien.html')
    else:
        return render(request,'loi.html')
# def chi_tiet(request, nguoidung_id):
#     nguoi_dung = get_object_or_404(NguoiDung, pk=nguoidung_id)
#     return render(request, 'chitiet.html',{'nd':nguoi_dung})
    
def chi_tiet(request, nguoidung_id):
    # print(nguoidung_id)
    nv =get_object_or_404(NguoiDung,pk=nguoidung_id) #primary key
    context={
        'nguoi_dung': nv
    }
    return render(request, 'chitiet.html',context)

def xuly_capnhat(request):
    ten=request.GET.get('ten')
    mk=request.GET.get('matkhau')
    mail=request.GET.get('mail')
    id_nguoidung=request.GET.get('id_nd')

    # Bien lay tu HTML

   # data=NguoiDung.objects.filter(ten_dang_nhap=ten, matkhau=mk) 
        #tuong duong voi lenh Query trong SQL
    NguoiDung.objects.filter(id=id_nguoidung).update(
        ten_dang_nhap=ten,
        matkhau=mk,
        email=mail,
        #email: cột trong SQL, mail: Bien lay tu HTML 
        )
    danh_sach=NguoiDung.objects.all() 
    context={
        'ds_nguoidung': danh_sach # nhieu doi tuong, kieu dictionary
            }
    return render(request,'danhsach.html',context)
    #bien ds_nguoidung xu ly trong danhsach.html

   # thongtin=NguoiDung.objects.filter(ten_dang_nhap=ten, matkhau=mk)
    # tuong ung SQL se tao lenh query trong SQL
    #if(data.exists()):
    #    return render(request, 'danhsach.html', context)

   # else:
        #return render(request,'loi.html')