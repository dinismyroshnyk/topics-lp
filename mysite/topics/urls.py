from django.urls import path
from . import views

urlpatterns = [
    path('', views.topic_list, name='topic_list'),
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    path('topic/<int:topic_id>/comment/', views.add_comment, name='add_comment'),
    path('topic/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('topic/<int:topic_id>/edit/', views.edit_topic, name='edit_topic'),
    path('comment/<int:topic_id>/delete/', views.delete_topic, name='delete_topic'),
    path('topic/new/', views.create_topic, name='create_topic'),
]