from django.urls import path
from .views import MasterSignupView, StudentSignupView

urlpatterns = [
    path('master/signup/', MasterSignupView.as_view(), name='master_signup'),
    path('student/signup/', StudentSignupView.as_view(), name='student_signup'),
]
