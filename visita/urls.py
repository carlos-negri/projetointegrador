from django.urls import path
from .views import IndexView

urlpatterns = [
    path('cadastroVisita', IndexView.as_view(), name='cadastroVisita'),
]