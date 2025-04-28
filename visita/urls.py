from django.urls import path
from .views import IndexView

urlpatterns = [
    path('visitas', IndexView.as_view(), name='visitas'),
]