
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls # schema


urlpatterns = [
    path('', include('index.urls')),
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
    path('blog/', include('blog.urls')),
    path('chat/', include('chat.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('account/', include('account.urls')),
    path('contact/', include('contact.urls')),
    path('docs/', include_docs_urls(title='Agency project')), #default schema
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)




