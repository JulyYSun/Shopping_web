from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import 商品类别表,产品列表
# Create your views here.

def 总览页(request):
    所有类别=商品类别表.objects.all()
    类别与商品=[]
    
    
    for 每个类别 in 所有类别:
        类别与商品.append((每个类别, 产品列表.objects.filter(所属类别=每个类别)[:3]))
    content={'类别与商品':类别与商品   }
    return render(request,'shopping/home.html',content)

