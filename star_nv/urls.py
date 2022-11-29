from django.urls import path
from . import  views
from .views import DemoView

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
    path('demoview/',DemoView.as_view())

    
]