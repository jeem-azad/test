from django.conf.urls import url
from . import views 
urlpatterns = [
    url(r'^$',views.index, name='study'), 
    url(r'^detail_teacher',views.detail_teacher, name='detail_teacher'),  
]