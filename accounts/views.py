from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect

# Create your views here.
from photoapp.models import photo


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password1']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return  redirect('/')
        else:
            messages.info(request,"invalide details")
            return redirect('login')
    else:
        return render(request,"login.html")


def logout(request):
    auth.logout(request)
    return  redirect('/')



def register(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:

                user=User.objects.create_user(username=username,password=password1,email=email,first_name=fname,last_name=lname)
                user.save();
                print("user created")

        else:
            print("password not matched")
            return redirect('register')

        return redirect('/')

    else:
      return  render(request,'register.html')


def gallery(request):
    return render(request, 'gallery.html')


def add(request):
    if request.method=='POST':
        tittle=request.POST.get('tittle')
        des = request.POST.get('des')
        img = request.FILES['img']
        s=photo(tittle=tittle,des=des,img=img)
        s.save()
        print('photo added')
    return render(request,'add.html')

def about(request):
    return render(request, 'about.html')
