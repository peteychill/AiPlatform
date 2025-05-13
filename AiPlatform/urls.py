from django.contrib import admin
from django.urls import path, include
from oauth2_provider.urls import base_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include(base_urlpatterns)), 
    path('openAI/', include('openAI.urls')),

]

