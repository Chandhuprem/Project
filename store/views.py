from django.shortcuts import render,redirect
from .forms import myform

# Create your views here.
def req(request):
    if request.method=='POST':
       
        username=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        bookname=request.POST.get('bookname')
        Authorname=request.POST.get('Authorname')
        user=user.objects.create_user(username,email,phone,bookname,Authorname)
        user.save()
    
        print(username,email,phone,bookname,Authorname)

        return redirect('req')

    return render(request,'req.html') 

def my_form(request):
  if request.method == "POST":
    form = myform(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = myform()
  return render(request, 'req.html', {'form': form})
