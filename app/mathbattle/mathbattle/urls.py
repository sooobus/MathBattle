from django.contrib import admin
from django.urls import path,include
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contest/', include('contest.urls')),
    path('', index),
    path('auth/', include('authorization.urls'))
]
