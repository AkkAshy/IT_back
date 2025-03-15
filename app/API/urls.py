from django.urls import path, include
from app.API.views.user_views import UserCreateView, NewUserListView, UpdateUserStatusView

urlpatterns = [
    path('users/', include('app.Users.urls')),  # Подключаем пути из приложения Users
    path('courses/', include('app.courses.urls')),  # Подключаем пути из приложения Courses
    path('users/register/', UserCreateView.as_view(), name='user-register'),
    path('users/new', NewUserListView.as_view(), name='new-users-list'),
    path('users/<int:pk>/update-status/', UpdateUserStatusView.as_view(), name='update-user-status'),
]