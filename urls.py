from django.urls import path
from app import views
urlpatterns=[ path('admin/',admin.site.urls),path("",views.my_view),]
