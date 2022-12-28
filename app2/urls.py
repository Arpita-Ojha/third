from django.urls import path
from app2.views import*
app_name='something2'

urlpatterns=[
    path('htmlone/',htmlone,name='htmlone'),
    path('htmltwo/',htmltwo,name='htmltwo')
]