from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dbsmanagement import views


urlpatterns = [
    path('accounts/', include('registration.backends.default.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('search/', views.search, name='search'),
    path('update/<str:pk>/', views.update, name="update"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
