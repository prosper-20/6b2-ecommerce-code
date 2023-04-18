from django.urls import path
from .views import product_page, about, product_single_page

urlpatterns = [
    path("", product_page),
    path("about/", about, name="a"),
    path("<int:pk>/", product_single_page, name="single")
]
