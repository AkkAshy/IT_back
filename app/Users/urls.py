from django.urls import path
from .views import UserListCreateView, UserDetailView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-list-create'),  # Получение списка и создание пользователя
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),  # Получение, обновление и удаление конкретного пользователя
]