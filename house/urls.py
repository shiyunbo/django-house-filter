from django.urls import path
from . import views

# namespace
app_name = 'house'

urlpatterns = [

    # 展示文章列表并筛选 -  登录/未登录均可
    path('', views.house_filter, name='house_filter'),

    ]