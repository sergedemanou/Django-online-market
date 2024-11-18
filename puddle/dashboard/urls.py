from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'dashboard'

urlpatterns = [
    path('index2/', views.my_items, name='index2'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)