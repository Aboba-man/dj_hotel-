from django.urls import path, include
from accounts import views
from .views import home,Roms,Bockig
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import LoginView, RegisterView

urlpatterns = [
    # path('', include('blog.urls')),
    path('', home, name = "home"),
    # path("signup/", views.SignUpView.as_view(), name="signup"),
    path('register/', RegisterView.as_view(), name='register'),
    path('rooms/',Roms.as_view(),name='roms'),
    path('book/',Bockig.as_view(),name='book'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


