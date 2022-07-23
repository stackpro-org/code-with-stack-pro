
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('index.urls')),
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
    path('blog/', include('blog.urls')),
    path('chat/', include('chat.urls')),
    # path('pricing/', include('pricing.urls')),
    path('services/', include('services.urls')),
    path('team/', include('team.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('account/', include('account.urls')),
    path('contact/', include('contact.urls')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
