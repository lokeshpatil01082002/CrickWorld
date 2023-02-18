from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from crcikblogs.models import UserDetails,Blog,Memes,post_likes,meme_likes,post_not,meme_not
from django.db import IntegrityError
from django.utils.datastructures import MultiValueDictKeyError
import datetime
# Create your views here.
passingalue="userid"
@login_required(login_url='login')


def saveurl(request):
    if request.method=='POST':
     print("bro finally..")
     return redirect('addmeme')
    else:
      return redirect('addmeme')  
def SignupPage(request):
    if request.method=='POST':
        
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1=="" or pass2=="" or email=="" or uname==" " or fname=="" or lname=="":
            messages.warning(request,"All Fields Are Mandetory To Fill !!!")
            return redirect('signup')
        if pass1!=pass2:
            messages.warning(request,"Password Fields Didn't Match !!! ")
            return redirect('signup')
           
        else:
            try:
                my_user=User.objects.create_user(uname,email,pass1)
                my_user.save()
             
                data=UserDetails(uname,fname,lname,email,0)
                data.save();
                messages.success(request,"Registration  Succesful!! , You Can Now LogIn To System ")
                return redirect('signup')
            except IntegrityError:
                messages.success(request,"Username Already Exists !!")
                return redirect('signup')
            
                
                
            
               
        
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if username=="" or pass1=="":
             messages.warning(request,"Fields Can't Be Empty !!")
             return redirect('login')
        if user is not None:
            login(request,user)
            print(request.user)
            y=UserDetails.objects.filter(userid=request.user)
            return redirect('home')
        else:
          
            messages.warning(request,"Username Or Password Is Incorrect !")
            return redirect('login')
        


    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


def HomePage(request):
     if request.method=='GET':
      y=Blog.objects.all().order_by('-likes').values()
      y2=post_likes.objects.all().filter(userid=request.user)
      y3=post_not.objects.all().filter(userid=request.user)
      for i in y2:
        print(i.post_id)
        y=y.exclude(post_id=i.post_id)
      for i in y3:
        y=y.exclude(post_id=i.post_id)
      return render (request,'home.html',{'y':y})
     else:
        arraystring=request.POST.get('count')
        arraystring2=request.POST.get('count2')
       
        my_list = arraystring.split(",")
        my_list2 = arraystring2.split(",")
        if(arraystring!='1'):
         for i in my_list:
           member=Blog.objects.get(post_id=int(i))
           member.likes=member.likes+1
           member.save();
           m1=Blog.objects.get(post_id=int(i))
           uid=m1.userid
           userobject=UserDetails.objects.get(userid=uid)
           userobject.reward=userobject.reward+1;
           userobject.save();
           data=post_likes(userid=request.user,post_id= int(i))
           data.save();
        if(arraystring2!='1'):
         for i in my_list2:
           data=post_not(userid=request.user,post_id= int(i))
           data.save();
        
       
        y=Blog.objects.all().order_by('-likes').values()
        y2=post_likes.objects.all().filter(userid=request.user)
        y3=post_not.objects.all().filter(userid=request.user)
        for i in y2:
         y=y.exclude(post_id=i.post_id)
        for i in y3:
         y=y.exclude(post_id=i.post_id)
        
        return render (request,'home.html',{'y':y})

       
    
    

def AddblogPage(request):
    if request.method=='POST':
     try:
       title_text=request.POST.get('title')
       content_text=request.POST.get('content')
       image_view=request.FILES['image']
       y=UserDetails.objects.filter(userid=request.user)
       for i in y:
        dataobject=Blog(userid=i.userid,email=i.email,likes=0,title=title_text,content=content_text,image=image_view)
        dataobject.save();
        messages.success(request,"Bog Added Succesfully !")
        return redirect('addblog') 
     except MultiValueDictKeyError:
          messages.success(request,"All field Cumplosry !")
           
          return render (request,'addblog.html')
    else:
     return render (request,'addblog.html')
def AddmemePage(request):
   if request.method=='POST':
     
     try:
        image_view=request.FILES['image']
        y=UserDetails.objects.filter(userid=request.user)
        for i in y:
          dataobject=Memes(userid=i.userid,email=i.email,likes=0,image=image_view)
          dataobject.save();
          messages.success(request,"Meme Added Successfully !!")
     except MultiValueDictKeyError:
                messages.success(request,"You Have Not Selected Any Image")
                return redirect('addmeme')
     return redirect('addmeme')
   else:
      return render (request,'addmeme.html')


def myblogs(request):
    if request.method=='POST':
     pid=request.POST.get('count')
     print(pid)
     member = Blog.objects.get(post_id=pid)
     member.delete()
     b=Blog.objects.filter(userid=request.user).order_by('-likes').values()
     return render (request,'myblogs.html',{'y':b})
    else:
     b=Blog.objects.filter(userid=request.user).order_by('-likes').values()
     return render (request,'myblogs.html',{'y':b})
def mymemes(request):
    if request.method=='POST':
     pid=request.POST.get('count')
     print(pid)
     member = Memes.objects.get(meme_id=pid)
     member.delete()
     b=Memes.objects.filter(userid=request.user).order_by('-likes').values()
     return render (request,'mymemes.html',{'y':b})
    else:
     b=Memes.objects.filter(userid=request.user).order_by('-likes').values()
     return render (request,'mymemes.html',{'y':b})



def MemesPage(request):
    if request.method=='GET':
      y=Memes.objects.all().order_by('-likes').values()
      y2=meme_likes.objects.all().filter(userid=request.user)
      y3=meme_not.objects.all().filter(userid=request.user)
      for i in y2:
       
        y=y.exclude(meme_id=i.meme_id)
      for i in y3:
         y=y.exclude(meme_id=i.meme_id)
      return render (request,'memes.html',{'y':y})
    else:
        arraystring=request.POST.get('count')
        arraystring2=request.POST.get('count2')
       
        my_list = arraystring.split(",")
        my_list2 = arraystring2.split(",")
        if(arraystring!='1'):
         for i in my_list:
           member=Memes.objects.get(meme_id=int(i))
           member.likes=member.likes+1
           member.save();
           m1=Memes.objects.get(meme_id=int(i))
           uid=m1.userid
           userobject=UserDetails.objects.get(userid=uid)
           userobject.reward=userobject.reward+1;
           userobject.save();
           data=meme_likes(userid=request.user,meme_id= int(i))
           data.save();
        if(arraystring2!='1'):
         for i in my_list2:
           data=meme_not(userid=request.user,meme_id= int(i))
           data.save();
        
       
        y=Memes.objects.all().order_by('-likes').values()
        y2=meme_likes.objects.all().filter(userid=request.user)
        y3=meme_not.objects.all().filter(userid=request.user)
        for i in y2:
         y=y.exclude(meme_id=i.meme_id)
        for i in y3:
         y=y.exclude(meme_id=i.meme_id)
        
        return render (request,'memes.html',{'y':y})

def ProfilePage(request):
    print(request.user.id)
    y=UserDetails.objects.filter(userid=request.user)
    for i in y:
        print(i.email)
    return render (request,'profile.html',{'y':y})
    