from django.urls import path
from basicapp import views


# TEMPLATE TAGGING
app_name =  'basicapp'

# to go to basicapp/relative and basicapp/other
urlpatterns = [
               path('',views.index,name='index'),
               path('relative/', views.relative, name = 'relative'),
               path('other/',views.other,name='other'),
               ]
