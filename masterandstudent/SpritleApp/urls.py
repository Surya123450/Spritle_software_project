from django.contrib import admin
from django.urls import path
from core.views import home_view, signup_view, login_view, logout_view, dashboard_view, ask_question_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('ask_question/', ask_question_view, name='ask_question'),
]
