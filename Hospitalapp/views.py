from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')


def test(request):
    return render(request,'test.html')