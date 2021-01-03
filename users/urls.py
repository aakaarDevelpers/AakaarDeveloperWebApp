from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('authentication/', views.user_auth, name='authentication_page'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout/', views.user_logout, name='logout_user'),

    # Password reset URLS
    path('password-reset-view/', auth_views.PasswordResetView.as_view(template_name='users/password_reset_view.html'), name='password-reset-view'),
    path('password-reset-view/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done_view.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm_view.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete_view.html'), name='password_reset_complete')
]