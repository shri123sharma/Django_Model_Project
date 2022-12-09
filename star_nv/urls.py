from django.urls import path
from . import  views
from .views import *

app_name='star_nv'

urlpatterns=[
    path('blog/',views.blog),
    path('blog/<int:year>/',views.year_archive),
    path('blog/<int:year>/<int:month>/',views.month_archive),
    path('page/<int:num>/',views.page),
    path('page/<int:year>/<int:month>',views.year_archive_demo,{'foo':'bar'}),
    path('demo/<int:year>/',views.year_archive_demo,name='name_for_year'),
    path('datetime/',views.current_date,name='datetime'),
    path('my_view/',views.my_view,name='myview'),
    path('detail/<int:id>/',views.detail,name='detail'),
    path('index/<int:id>/',views.index,name='index'),
    path('myview/',views.my_view,name='myview'),
    path('my_view_1/<int:id>/',views.my_view_1,name='myview1'),
    path('getobject/<int:id>/',views.get_object,name='getobject'),
    path('myview2/<int:id>/',views.my_view_2,name='myview2'),
    path('myview3/',views.my_view_3,name='myview3'),
    path('myview4/',views.my_view_4,name="myview4"),
    path('demoview/',DemoView.as_view()),
    path('indexview/',IndexView.as_view()),
    path('addbookform/',AddBookForm.as_view(),name='add'),
    path('entryfromview/',Entry_Form_View.as_view(),name='entryview'),
    path('publisher/',PublisherListView.as_view(),name='pub_list_view'),
    path('publisherdetail/<int:pk>/',PublisherDetailView.as_view(),name='publisherdetail'),
    path('author/add/',Author2CreateView.as_view(),name='author-add'),
    path('author/<int:pk>/',Author2UpdateView.as_view(),name='author-update'),
    path('author/<int:pk>/delete/',Author2DeleteView.as_view(),name='author-delete'),
    path('recordinterest/<int:pk>',RecordInterestView.as_view(),name='record'),
    path('Publisherlist/<int:pk>/',PublisherListView.as_view(),name='publisher'),
    path('authordetailview/<int:pk>/',AuthorDetailView.as_view(),name='author'),
    path('authorinterest/',AuthorInterestFormView.as_view(),name='author_I_form'),
    path('publishermodified/',PublisherListView_1.as_view(),name='publishermodified'),
    path('company/',CompanyListView.as_view(),name='company'),
    path('<int:pk>/',CompanyDetailView.as_view(),name='companydetail'),
    path('companyformview/',CompanyFormView.as_view(),name='companyform'),
    path('filmlist/<int:pk>/',FilmListView.as_view()),
    path('filmlist_1/<int:pk>/',FilmListView_1.as_view(),name='filmlist'),
    path('listing/<int:id>/',views.listing,name='listing'),
    path('listingview/',Listing_View.as_view(),name='listing_view'),
    path('homepage/',HomePageView.as_view,name='homepage'),
    path('getname/',views.get_name,name='getname'),
    path('get_name_1/',views.get_name_1,name='get_name_1'),
    path('book_1/',views.book_1,name='book_1'), 
    path('item/',views.item,name='item'),
    path('addcart/<int:item>/',views.add_to_cart,name='addcart'),
    path('mycustom/',views.my_custom_sql,name='mycustom'),
    path('result/',views.result,name='result'),
    path('demosql/',views.Demo_sql,name='demosql'),
    path('indexsql/',views.index_sql,name='indexsql'),
    
    

    
]