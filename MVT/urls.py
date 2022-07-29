
from django.contrib import admin
from django.urls import path
from Familiares.views import familiares

urlpatterns = [
    path('admin/', admin.site.urls),
    path("Familiares/", familiares,name="familiares"),
    
]
