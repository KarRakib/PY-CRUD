from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,UserProfileUpdate, UserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class RegisterView (View):
     def get(self, req):
          form = UserCreationForm()
          return render(req,'users/register.html',{"form":form})          
     def post(self,req):
          form = UserCreationForm(req.POST)
          if form.is_valid():
               form.save()
               return redirect('/')
          return redirect('register')
     
class ProfileView(LoginRequiredMixin,View):
     def get(self,req):
          p_form = UserProfileUpdate(instance=req.user.profile)
          u_form = UserUpdateForm(instance=req.user)
          context = {
               'p_form':p_form,
               'u_form':u_form
          }

          return render(req, "users/profile.html", context)
     def post(self,req, *args, **kwargs):
           p_form = UserProfileUpdate(req.POST,req.FILES,instance=req.user.profile)
           u_form = UserUpdateForm(req.POST,instance=req.user)
           u_form.save()
           p_form.save()
           return redirect('profile')




     


