from django.urls import path
from .views import homepage, detailpage

urlpatterns = [
    path("", homepage),
    path("<int:pk>/", detailpage, name="detail")
]