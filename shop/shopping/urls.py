"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path ,include
from .import views
app_name="shopping"
urlpatterns=[
    #主页，views.总览页表示执行的方法，返回到shopping/home.html
    path('',views.总览页,name='总览页'),
    #'<每个类别_id>/' 表示打开的链接的网址显示类似于www.baidu.com/2
    path('<每个类别_id>/',views.单类页,name='单类页'),
    path('<每个类别_id>/<每件商品_id>/',views.详情页,name='详情页'),
]