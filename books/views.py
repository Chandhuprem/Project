from django.shortcuts import render,HttpResponse,redirect
from .models import MyModel
from .forms import MyForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.
#def log(request):
    #return render(request,'log.html')


    
def index(request):
    if 'q' in request.GET:
        q=request.GET['q']
        multiple_q=Q(Q(bname__icontains=q) | Q(story__icontains=q) )
        MyModel1= MyModel.objects.filter(multiple_q)

    else:
        MyModel1=MyModel.objects.all() 
    return render(request,'index.html', {'MyModel1':MyModel1})
    #books1=MyModel.objects.all()
    #return render(request,'index.html',{'books1':books1})
def signup(request):
    if request.method=='POST':
       
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('password1')
        user=User.objects.create_user(username,email,pass1)
        user.save()
    
        print(username,email,pass1,pass2)
        
        return redirect('signin')

    return render(request,'signup.html') 
def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
            print(username,pass1)
    return render(request,'signin.html')        
def newbooks(request):
    

    return render(request,'newbooks.html')
def aboutus(request):
    

    return render(request,'aboutus.html')
def logout(request):
    

    return render(request,'signin.html')
   


#def my_form(request):
    #if request.method=='POST':
        ##form = MyForm(request.POST)
        #if form.is_valid():
        # form.save()
         #return HttpResponse("<h1>saved success</h1>")
        #else:
         ##form = MyForm()
       # return render(request, 'temp.html', {'form': form})
def search(request):
    if 'q' in request.GET:
        q=request.GET['q']
        multiple_q=Q(Q(bname__icontains=q) | Q(story__icontains=q) | Q(author__icontains=q))
        MyModel1= MyModel.objects.filter(multiple_q)

    else:
        MyModel=MyModel.objects.all() 
    return render(request,'index.html', {'MyModel1':MyModel1})