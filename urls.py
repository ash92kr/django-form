from django.urls import path
from . import views   # 앱의 views.py를 의미

app_name='post'

urlpatterns = [
    path('', views.list, name='list'),   # 아무 것도 오지 않으면 views.list 실행    
    path('create/', views.create, name='create'),
    path('<int:id>/detail/', views.detail, name='detail'),  # 특정 게시물 1개를 클릭하면 보여줌
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('model_create/', views.model_create, name='model_create'),
    path('<int:id>/model_update', views.model_update, name='model-update'),
]
    
