from django.contrib import admin
from django.urls import path, include, re_path as url


from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
#from accounts.urls import urlpatterns

urlpatterns = [
    path('',include('home.urls')),
    path('login/', include('login.urls')),
    path('settings/', include('settings.urls')),
    path('manager/', include('manager.urls')),   
    path('analytics/', include('analytics.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),


    

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)