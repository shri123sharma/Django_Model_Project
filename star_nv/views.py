from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from django.template.response import SimpleTemplateResponse,TemplateResponse
from .models import *
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from django.views.generic import TemplateView
from django.views import View
from django.urls import reverse
from django.http import Http404
from star_nv.models import *
from django.db.models import Q
from django.template import loader
import  datetime


# Create your views here.
def blog(request):
    return HttpResponse("hello world")

def year_archive(request,year=2005):
    return HttpResponse("2005 year")

def month_archive(request,year=2010,month=9):
    return HttpResponse("request%response with the year and month")

def page(request,num=1):
    return HttpResponse("if integer value")

def year_archive_demo(request,year=2005,month=6,foo='bar'):
    return HttpResponse('this is bar')

def redirect_to_year(request):
    year=2006
    return HttpResponseRedirect(reverse('name_for_year'),args=(year,))

def current_date(request):
    now=datetime.datetime.now()
    html="<html><body>It is now %s</html></body>"%now
    return HttpResponse(html)

def my_view(request,foo):
    if foo:
        return HttpResponseNotFound('<h1> Page Not found</h1>')

    else:
        return HttpResponse('<p> page found</p>')
    
def detail(request,id):
    try:
        blog=Blog.objects.get(pk=id)
        
    except Blog.DoesNotExist:
        raise Http404('page not found')
    return render(request,'demo.html',{"blog":blog})

def index(request,id):
    try:
        entry=Entry.objects.get(pk=id)
               
    except Entry.DoesNotExist:
        raise Http404('page not found')
    return render(request,'index.html',{'entry':entry})

def my_view(request):
    t=loader.get_template('myview.html')
    c={'foo':'bar'}
    return HttpResponse(t.render(c,request),content_type='application/xhtml+xml')  

def my_view_1(request,id,*args,**kwargs):
    # import pdb;pdb.set_trace()
    e1=Entry.objects.filter(blog__name__startswith='Beat').values_list()
    for tup in e1:
        for item in tup:
            item=item
        # return render(request,'my_view_1.html',{'item':item})
    return redirect('https://docs.djangoproject.com/',permanent=True)

def get_object(request,id,*args,**kwargs):
    obj=get_object_or_404(Author,pk=id)
    return render(request,'get_object.html',{'obj':obj})

def my_view_2(request,id,*args,**kwargs):
    obj=get_list_or_404(Blog,pk=id)
    return render(request,'get_list_object.html',{'obj':obj})

def my_view_3(request,*args,**kwrags):
    entry=Entry.objects.filter(blog__name__startswith='Beat').distinct().count()
    entry_1=Entry.objects.filter(author__name='joe').values_list()
    return TemplateResponse(request,'my_view_3.html',{'entry':entry,'entry1':entry_1})

def my_view_4(request):
    if request.method=='GET':
        return HttpResponse('Result')
    
class DemoView(View):
    def get(self,request,*args,**kwrags):
        # import pdb;pdb.set_trace()
        blog=Blog.objects.exclude(entry__author__name__startswith='john').values().count()
        author=Author.objects.filter(entry__blog__name__startswith="Beat").distinct().count()
        entry=Entry.objects.filter(blog__tagline__istartswith='All').values()
        for obj in entry:
            for item in obj.items():
                item=item
        return render(request,'demoview.html',{'blog':blog,'author':author,'item':item})
    

        
    
    




    
    
    