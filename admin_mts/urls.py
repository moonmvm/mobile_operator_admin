from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'AdminMTS'
admin.site.site_title = 'AdminMTS'
admin.site.index_title = 'Добро пожаловать в AdminMTS'


urlpatterns = [
    path('', admin.site.urls),
    path('services/', include('services.urls')),
]
