from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from django.template.response import SimpleTemplateResponse,TemplateResponse
from django.views.generic.edit  import CreateView,UpdateView,DeleteView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.db import connection,connections
from .models import *
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound,HttpResponseForbidden
from django.views.generic import TemplateView
from django.views import View
from django.urls import reverse
from.forms import *
from django.http import Http404
from star_nv.models import *
from django.db.models import Q,Sum
from django.template import loader
from django.views.generic.list import ListView
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
       
class IndexView(View):
    greeting='good morning'
    def get(self,request,*args,**kwrags):
        return HttpResponse(self.greeting)
    
class DayStatusView(IndexView):
    greeting='Good day'
    
class AddBookForm(CreateView):
    form_class=Book_1_Form
    template_name='base.html'
    success_url='/book/'
    

class Entry_Form_View(CreateView):
    form_class=Entry_Form
    template_name='base1.html'
    sucess_url='/Book/'
    
    def get(self,request,*args,**kwrags):
        form=self.form_class()
        return render(request,self.template_name,{'form':form})
    
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            blog=form.cleaned_data['blog']
            headline=form.cleaned_data['headline']
            
            return HttpResponse('/sucess/')
        return render(request,self.template_name,{'form':form})
    
class PublisherListView(ListView):
    model=Publisher
    context_object_name='publisher_name'
    template_name= 'publisher_list.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["publisher_list"]=Publisher.objects.filter(book1__publisher__name='sam')
    
    
class PublisherDetailView(DetailView):
    model=Publisher
    context_object_name='publisher_detail_name'
    template_name='publisher_detail.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["book_list"] =Publisher.objects.get(id=1)
        return context
    
class ContactForm(FormView):
    form_class='Contact'
    template_name='contactform.html'
    success_url='/sucess/' 
    
    def form_valid(self,form):
        form.send_email
        return super().form_valid(form)
        
class Author2CreateView(CreateView):
    model=Author2
    fields=['name']
    template_name='author2_create.html'
    
class Author2UpdateView(UpdateView):
    model=Author2
    fields=['name']
    template_name='author2_update.html'
    
class Author2DeleteView(DeleteView):
    model=Author2
    fields=['name']
    template_name='author2_delete.html'
    
class RecordInterestView(SingleObjectMixin,View):
    model=Publisher
    
    def post(self,request,pk,*args,**kwargs):
        if not request.user.is_authenticatd:
            return HttpResponseForbidden()
        self.object=self.get_object()
        
        return HttpResponseRedirect(reverse('datetime',kwargs={'pk':self.object.pk}))
    
    
class PublisherListView(SingleObjectMixin,ListView):
    model=Publisher
    context_object_name='publisher_name'
    template_name='publisher_list1.html'
    # import pdb;pdb.set_trace()
    def get(self,request,*args,**kwrags):
        self.object=self.get_object(queryset=Publisher.objects.all())
        return super().get(request,*args,**kwrags)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["publisher"] = self.object
        return context
    
    def get_queryset(self):
        return self.Publisher.objects.all()
    
class AuthorDetailView(DetailView):
    model=Author1
    context_object_name='hello_world'
    template_name='author1_detail.html'
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context["form"] = AuthorInterestForm
        return context
    
class AuthorInterestFormView(SingleObjectMixin,FormView):
    model=Author1
    template_name="author_detail.html"
    form_class=AuthorInterestForm  
    
    def post(self,request,*args,**kwargs):
        import pdb;pdb.set_trace()
        if request.user.is_authenticated:
            return HttpResponseForbidden
        self.object=self.get_object
        return super().post(request,*args,**kwargs)
    
    def get_success_url(self):
        return super().get_success_url('publisher')
    
class PublisherListView_1(ListView):
    model=Publisher
    context_object_name='object_list'
    template_name='publisher_list_1.html'
    
class CompanyListView(ListView):
    model=Company
    context_object_name='object_list'
    template_name='company_list.html'
    
class CompanyDetailView(DetailView):
    model=Company
    context_object_name='objects'
    # template_name='company_detail.html'
    
class CompanyFormView(FormView):
    model=Company
    template_name='company_form.html'
    form_class=CompanyForm
    success_url='/Blog/'
    
class FilmListView(SingleObjectMixin,ListView):
    paginate_by=3
    template_name="film_list.html"
    
    def get(self,request,*args,**kwargs):
        self.object = self.get_object(queryset=Publisher.objects.all())
        return super().get(request,*args,**kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] =self.object 
        return context
    
    def get_queryset(self):
        return self.object.book1_set.all()
    
class FilmListView_1(ListView):
    paginate_by=1
    model=Film
    template_name='film_list_1.html'
    
    
def listing(request,id):
    # import pdb;pdb.set_trace()
    film_list=Film.objects.all().values()
    paginator=Paginator(film_list,2)
    page_number=request.GET.get('page_number')
    page_obj=paginator.get_page(page_number)
    
    return render(request,'fun_1_paginator.html',{'page_obj':page_obj})
    
    
# from django.core.paginator import Paginator
# from django.shortcuts import render

# from star_nv.models import Film

def listing(request):
    contact_list = Film.objects.all()
    paginator = Paginator(contact_list, 2) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list.html', {'page_obj': page_obj})

class Listing_View(View):
    def listing_view(self,request,*args,**kwargs):
        return HttpResponse('Hello World')
    

class HomePageView(TemplateView):
    template_name='home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_film"] = Film.objects.all()[:5]
        return context
    
    
def get_name(request):
    # import pdb;pdb.set_trace()
    if request.method=='POST':
        form=NameForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse('/Submitted_data/')
            
    else:
        form=NameForm()
        return render(request,'home1.html',{'form':form})
    
def get_name_1(request):
    # import pdb;pdb.set_trace()
    if request.method=='POST':
        form=ContactForm(request.POST or None)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            recipients = ['info@example.com']
            if cc_myself:
                recipients.append(sender)
                send_mail(subject,message,sender,recipients)
                return  HttpResponse('/thanks/')
    else:
        form=ContactForm()
        return render(request,'mail.html',{'form':form})
    
def book_1(request):
    if request.method=='POST':
        form=Book_1_Form(request.POST or None)
        if form.is_valid():
            title=form.cleaned_data['title']
            slug=form.cleaned_data['slug']
            genere=form.cleaned_data['genere']
            author=form.cleaned_data['author']
            isbn=form.cleaned_data['isbn']
            count=form.cleaned_data['count']
            if form.save():
                return HttpResponse('/thanks/')
    else:
        form=Book_1_Form()
        return render(request,'first_response.html',{'form':form})
    
def item(request):
    # import pdb;pdb.set_trace()
    item=Item.objects.all()
    carts=Cart.objects.all()
    length=len(Cart.objects.all())
    cart=carts[length-1]
    cart_item=cart.item.all()
    total=cart_item.aggregate(Sum('price'))
    
    return render(request,'cart.html',{'cart':cart,'item':item,'cart_item':cart_item,'total':total})

def add_to_cart(request,item):
    item=Item.objects.get(id=item)
    carts=Cart.objects.all()
    length=len(Cart.objects.all())
    cart=carts[length-1]
    cart_items=cart.item.add(item)
    
    return render(request,'cart.html',{'cart_items':cart_items})

def my_custom_sql(request):
    with connection.cursor() as cursor:
        query="select sns.name,snb3.pages,snb3.price,snb3.rating,snb3.pubdate from star_nv_publisher3 as snp3 inner join star_nv_book3 as  snb3 on snp3.id=snb3.publisher_3_id inner join star_nv_store as sns on (snb3.id=sns.id);select sns.name,snb3.pages,snb3.price,snb3.rating,snb3.pubdate from star_nv_publisher3 as snp3 inner join star_nv_book3 as  snb3 on snp3.id=snb3.publisher_3_id inner join star_nv_store as sns on (snb3.id=sns.id);"
        cursor.execute(query)
        row=cursor.fetchall
        return HttpResponse(row)

def result(request):
    # import pdb;pdb.set_trace()
    with connection.cursor() as cursor:
        query='select snb.name,snb.tagline,sna.name,sne.headline,sne.body_text from star_nv_blog as snb inner join star_nv_author as sna on snb.id=sna.id inner join star_nv_entry as sne on sna.id=sne.id order by snb.name desc limit 10;'
        cursor.execute(query)
        cursor=cursor.fetchall
        return HttpResponse(cursor)

def Demo_sql(request):
    with connection.cursor() as cu:
        query='select snb.name,snb.tagline,sna.name,sne.headline,sne.body_text from star_nv_blog as snb inner join star_nv_author as sna on snb.id=sna.id inner join star_nv_entry as sne on sna.id=sne.id order by snb.name desc limit 10;'
        cu.execute(query)
        cursor=cu.fetchall()
        return HttpResponse(cursor)
    
    
def index_sql(request):
    with connection.cursor() as co:
        query='select snb.name,snb.tagline,sna.name,sne.headline,sne.body_text from star_nv_blog as snb inner join star_nv_author as sna on snb.id=sna.id inner join star_nv_entry as sne on sna.id=sne.id order by snb.name desc limit 10;'
        try:
            co.execute(query)
            cursor=co.fetchall()
            return HttpResponse(cursor)
        finally:
            co.close
            
            
        
            
    
    
