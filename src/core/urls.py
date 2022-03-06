from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/login/', auth_views.LoginView.as_view(template_name='login.html')),
    # add register later
    # path('admin/register/', UserRegistrationView.as_view()),
    path('admin/', admin.site.urls),
    path('api/v1/', include(('api.v1.urls', 'api_v1'))),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
