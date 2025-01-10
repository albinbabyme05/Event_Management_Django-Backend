from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        #check password matches
        if password == confirmpassword:
            
            if User.objects.filter(username=username).exists():
                #to alert if the user already exists
                messages.info(request, "username already taken")
                return redirect('register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exists")
                return redirect('register/')
            else:
                user_reg = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                messages.info(request, "Succssfully created")
                return redirect('/')
        else:
            messages.info(request, " paswords are not same")
            return redirect('register/')
                
                
        
        
    return render(request, 'registration.html')