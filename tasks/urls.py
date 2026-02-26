from django.urls import path
from . import views
app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('detail/<int:task_id>', views.detail, name='detail'),
    path('edit/<int:task_id>', views.edit, name='edit'),
    path('delete/<int:task_id>', views.delete, name='delete'),
    path('login/', views.TaskLoginView.as_view(), name='login'),
    path('logout/', views.TaskLogoutView.as_view(), name='logout'),
    path('signup/', views.AccountRegistrationView.as_view(), name='signup'),
    path('account/', views.AccountDetailView.as_view(), name='account_detail'),
    path('account/edit/', views.AccountEditView.as_view(), name='account_edit'),
    path('password_change/', views.TaskPasswordChangeView.as_view(), name='password_change'),
    path('account/delete/', views.AccountDeleteView.as_view(), name='account_delete'),
]
