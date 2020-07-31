from django.shortcuts import render
from myapp.models  import Deginer
# Create your views here.

def home(request):
    deginers = Deginer.objects.all()
    return render(request,'home.html', {'deginer':deginers})
    #전해줄 값을 딕셔너리로 작성함
def introduce(request):
    return render(request,'introduce.html')