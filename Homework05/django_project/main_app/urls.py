from django.conf.urls import url
from django.urls import path


from .views import GoodsListView, GoodsCreate

app_name = 'main_app'

urlpatterns = [
    path('', GoodsListView.as_view(), name='index'),
    path('create/', GoodsCreate.as_view(), name='create')
]
