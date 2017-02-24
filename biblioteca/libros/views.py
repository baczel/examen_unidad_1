from django.shortcuts import render

# Create your views here.
def ahitor(request):
    context=locals()
    template='home.html'
    return render(request,template,context)
