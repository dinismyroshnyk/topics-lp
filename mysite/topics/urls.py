from django.urls import path
from . import views

urlpatterns = [
    path('', views.topic_list, name='topic_list'),
    path('<int:topic_id>/', views.topic_detail, name='topic_detail'),
    path('<int:topic_id>/comment/', views.add_comment, name='add_comment'),
    path('<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]