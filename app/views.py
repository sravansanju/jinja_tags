from django.shortcuts import render

# Create your views here.
def jinja_tags(request):
    d={'a':10000,'b':2000,'c':400}
    return render(request,'jinja_tags.html',d)