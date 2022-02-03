from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # 127.0.0.1:8000 과 views.py 폴더의 home 함수 연결
    path('info/', views.place, name='place'), # 127.0.0.1:8000/tweet 과 views.py 폴더의 tweet 함수 연결
    path('info/delete/<int:id>', views.delete_place, name='delete-place'),
    path('info/<int:id>',views.detail_place, name='detail-place'),
    path('info/comment/<int:id>',views.write_comment, name='write-comment'),
    path('info/comment/delete/<int:id>',views.delete_comment, name='delete-comment'),
]