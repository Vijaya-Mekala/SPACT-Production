from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def NewRequest(request):
    return render(request,'NewRequest.html')

def SubmitToResult(request):
    return render(request,'DisplayResult.html')
