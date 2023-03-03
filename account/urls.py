from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('blockchain/', views.index, name='index'),
    path('block-chain/', views.index2, name='index2'),
    path('block--chain/', views.index3, name='index3'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)