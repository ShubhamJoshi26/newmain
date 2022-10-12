from re import L
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
        return  render(request,'index.html')

def about(request):
        return HttpResponse("this is about page")

def login(request):
        is_private = request.POST.get('is_private', False)
        login_ajax = request.POST['userid']
        return render(request, 'login.py',{'logindata':login_ajax},is_private)
