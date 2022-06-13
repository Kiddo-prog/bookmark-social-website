from django.urls import path
from accounts import views as auth_view
from django.contrib.auth import views as user_view

app_name = "accounts"
urlpatterns = [
    path("login/", auth_view.user_login, name="login"),
    path("logout/", user_view.LogoutView.as_view(), name="logout"),
    path("dashboard/", auth_view.dashboard, name="dashboard"),
    path("register/", auth_view.register, name="register"),
    path("edit/", auth_view.editProfile, name="edit"),
    # url for password change
    path(
        "password_change/",
        user_view.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "password_change/done/",
        user_view.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    # urls for password reset
    path(
        "password_reset/", user_view.PasswordResetView.as_view(), name="password_reset"
    ),
    path(
        "password_reset/done/",
        user_view.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>",
        user_view.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        user_view.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
