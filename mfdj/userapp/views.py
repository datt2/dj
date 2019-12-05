from django.shortcuts import render,redirect
from .forms import UserRegisterForm, UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method=='POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,'Your Account has been created. You can now Log In!')
            return redirect('login')
    else:
        form =UserRegisterForm()
    return render(request,'userapp/register.html',{'form':form})

@login_required
def profile(request):
    u_form=UserUpdateForm()
    p_form=ProfileUpdateForm()
    context={'u_form':u_form,'p_form':p_form}
    return render(request,'userapp/profile.html',context)
