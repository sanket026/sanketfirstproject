from urllib.request import Request
from django.shortcuts import render, HttpResponse, redirect
from .models import contactdata, usersignup
from .forms import signupform,notesdataform,contactform
from django.contrib.auth import logout
from django.core.mail import send_mail
from Myfirstproject import settings




def userlogin(request):
    unm=request.POST['username']
    pas=request.POST['password']

    userID=usersignup.objects.get(username=unm)
    print("userID :",userID.id)
    user=usersignup.objects.filter(username=unm,password=pas)
    if user:
        print('login successfully')
        request.session["user"]=unm
        request.session["userid"]=userID.id
    else:    
        print('try again')

def newusersignup(request):
   user=request.POST["username"]
   stfrm=signupform(request.POST)
   if stfrm.is_valid():
        stfrm.save()
        print('signup succesfully')
        request.session['username']=user

           #sending mail 
        sub="GOOD NEWS"
        msg=" hello user\n how are you\n good news for you"
        from_id=settings.EMAIL_HOST_USER
        to_id=[request.POST["username"]]
        send_mail(sub,msg,from_id,to_id)
        return redirect('/')      
   else:
        print(stfrm.errors) 
           
            

        return redirect(request,'notes')                     

# Create your views here.
def index(request):
    user=request.session.get('username')
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
           newusersignup(request)
           return redirect('notes')
        elif request.POST.get('login')=='login':
            userlogin(request) 
            return redirect('notes')        
        else:    
            print('something want wrong')            
    return render(request,'index.html',{'user':user})

def notes(request):
    user=request.session.get('username')
    if request.method=='POST':
        notesform=notesdataform(request.POST,request.FILES)
        if notesform.is_valid():
            notesform.save()
            print('your post has been saved')
        else:
            notesform.errors    

    return render(request,'notes.html',{'user':user})    

def userlogout(request):
    logout(request)
    return redirect('/')

def profile(request):
    user=request.session.get('username')
    userid=request.session.get('userid')
    id=usersignup.objects.get(id=userid)
    if request.method=='POST':
        userupdate=signupform(request.POST)
        if userupdate.is_valid():
            userupdate=signupform(request.POST,instance=id)
            userupdate.save()
            print('YOUR PROFILE UPDATED')
            return redirect('/')
        else:
            print(userupdate.errors)    
    return render(request,'profile.html',{'user':user,'userid':usersignup.objects.get(id=userid)}) 


def about(request):
    user=request.session.get('username')    
    return render(request,'about.html',{'user':user}) 


def contact(request):
    user=request.session.get('username') 
    if request.method=='POST':
        uscontact=contactform(request.POST)
        if uscontact.is_valid():
            uscontact.save()
            print('contact saved')
            return redirect('/')
        else:
            print(uscontact.errors)    
    return render(request,'contact.html',{'user':user}) 

