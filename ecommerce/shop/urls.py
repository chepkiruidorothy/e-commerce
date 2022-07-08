from django.conf.urls.static import static
from . import settings
urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
