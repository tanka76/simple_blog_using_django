from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.views.generic import DetailView,CreateView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from .forms import Signup,Editprofileform,Passwordchangingform,Profilepageform
from django.contrib.auth.views import PasswordChangeView
from theblog.models import Profile


# Create your views here.
class Createprofileview(CreateView):
    model = Profile
    form_class = Profilepageform
    template_name = 'registration/create_profile.html'
    
    #fields = '__all__'


    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class Editprofileview(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    fields = ['user','boi','website_url','facebook_url']
    success_url = reverse_lazy('home')



class Showprofileview(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        
        context = super(Showprofileview, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile,id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context





class Passwordchangeview(PasswordChangeView):
    form_class = Passwordchangingform
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request,'registration/password_success.html',{})


class Userreg(generic.CreateView):
    form_class = Signup
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')



class Userprofile(generic.UpdateView):
    form_class = Editprofileform
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
         return self.request.user