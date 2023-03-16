from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import MasterForm, StudentForm

class MasterSignupView(CreateView):
    form_class = MasterForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class StudentSignupView(CreateView):
    form_class = StudentForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
