from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('', views.index,name='home'),
        path('estrela', views.index_estrela,name='home_estrela'),
        path('betfair', views.index_betfair,name='home_betfair'),
        path('aviators_blaze', views.aviatorsblaze),
        path('aviators_estrela', views.aviatorsestrela),
        path('aviators_betfair', views.aviatorsbetfair),
        ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
