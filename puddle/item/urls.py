from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'item'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)