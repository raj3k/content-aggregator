from django.urls import path
from .views import index, update_python_medium


urlpatterns = [
    path('', index, name='index_page'),
    path('python_medium/', update_python_medium, name='update-python-medium')
]
