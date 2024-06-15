from django.contrib import admin
from django.urls import path, include

######################## untuk menampilkan gambar yang sydah di upload pada folder media ####################
from django.conf import settings
from django.conf.urls.static import static

from myproject.views import home, about, detail_artikel,contact
from myproject.authentikasi import akun_login, akun_registrasi, akun_logout

from berita.api import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', home, name="home"),
    path('about', about, name="about"),
    path('contact', contact, name="contact"),
    path('detail/<slug:slug>', detail_artikel, name="detail_artikel"),
    
    path('Dashboard/', include("berita.urls")),

    path('api/author/list', api_author_list),
     path('api/author/detail/<int:id_author>', api_author_detail),

    path('api/kategori/list', api_kategori_list),
    path('api/kategori/add', api_kategori_add),
    path('api/kategori/detail/<int:id_kategori>', api_kategori_detail),

    path('api/artikel/list', api_artikel_list),
    path('api/artikel/add', api_artikel_add),
    path('api/artikel/detail/<int:id_artikel>', api_artikel_detail),



    path('authentikasi/login', akun_login, name="akun_login"),
    path('authentikasi/registrasi', akun_registrasi, name="akun_registrasi"),
    path('authentikasi/logout', akun_logout, name="akun_logout"),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api-auth/', include('rest_framework.urls'))
]

######################## untuk menampilkan gambar yang sydah di upload pada folder media ####################
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)