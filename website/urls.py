from django.urls import path
from django.views.generic import RedirectView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Default root URL redirects to Linux-based page
    path('', RedirectView.as_view(pattern_name='linux_home', permanent=False)),

    path("linux/", views.linux_home, name="linux_home"),  # Linux-style page
    path("windows/", views.home, name="windows_home"),    # Windows-style page
    path("contact-send/", views.contact_send_email, name="contact_send_email"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
