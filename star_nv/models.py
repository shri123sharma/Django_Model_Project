from django.db import models

# Create your models here.
class person(models.Model):
    first_name=models.CharField(max_length=200,null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.first_name
    
class musician(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    instrument=models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name
    
class album(models.Model):
    artist=models.ForeignKey(musician,null=True,blank=True,on_delete=models.CASCADE,help_text="Relation")
    name=models.CharField(max_length=100,null=True,blank=True)
    release_date=models.DateTimeField(auto_now_add=True)
    num_star=models.IntegerField()
    
    def __str__(self):
        return self.name
    
class student(models.Model):
    shrit_size=(
        ("Small","S"),
        ("Medium","M"),
        ("Large","L"),
        
    )
    name=models.CharField(max_length=59,null=True,blank=True,primary_key=False)
    shrit_size=models.CharField(max_length=50,null=True,blank=True,choices=shrit_size,default="S")
    
    def __str__(self):
        return self.name
# foriegn key relation   
class Manufactur(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    manufactur_brand=models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.name

class Car(models.Model):
    company_car=models.ForeignKey(Manufactur,verbose_name="car_R",null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.company_car
    
# many-to-many relation
class Topping(models.Model):
    Top_flavour=models.CharField(max_length=100,null=True,blank=True)
class Pizza(models.Model):
    top_pizza=models.ManyToManyField(Topping)
    
class Person_1(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.name
class Group(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    member=models.ManyToManyField(Person_1)
    
    def __str__(self):
        return self.name
    
class Membership(models.Model):
    person=models.ForeignKey(Person_1,null=True,blank=True,on_delete=models.CASCADE)
    group=models.ForeignKey(Group,null=True,blank=True,on_delete=models.CASCADE)
    date_joined=models.DateField(auto_now_add=True)
    invite_reason=models.CharField(max_length=10)
    
    def __str__(self):
        return self.invite_reason
    
class Ox(models.Model):
    horn_length=models.IntegerField()
    class Meta:
        ordering=['horn_length']
        verbose_name_plural="oxen"

class person_2(models.Model):
    first_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    date_birth=models.DateField()
    
    def baby_boomer_status(self):
        import datetime
        if self.date_birth<=datetime.date(1948,10,1):
            return "pre_boomer"
        elif self.date_birth>=datetime.date(19965,11,12):
            return "baby boomer"
        else:
            return "post_boomer"
        
    @property
    def full_name(self):
        return '%s %s'%(self.first_name,self.last_name)
    
    def __str__(self):
        return self.first_name
    
class Blog(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    tagline=models.TextField()
    
    def save(self,*args,**kwargs):
        if self.name=="hello world":
            return  "hello world"
        else:
            super().save(*args,**kwargs)
            
class common_info(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    age=models.PositiveIntegerField()
    
    class Meta:
        abstract = True
class student_2(common_info):
    home_group=models.CharField(max_length=100,null=True,blank=True)
    
class common_info_1(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    age=models.PositiveIntegerField()
    
    class Meta:
        abstract=True
        ordering=['name']
        
class album_1(common_info_1):
    release_date=models.DateField()
    
    class Meta(common_info_1.Meta):
        db_table='album'

class Commmon_info_3(models.Model):
    first_name=models.CharField(max_length=100,null=True,blank=True) 
    last_name=models.CharField(max_length=100,null=True,blank=True)
    age=models.PositiveIntegerField()
    
    class Meta:
        abstract=True
        ordering=['first_name']
        
class Unmanged(models.Model):
    class Meta:
        abstract=True
    
        
class Student_3(Commmon_info_3,Unmanged):
    home_group=models.CharField(max_length=100,null=True,blank=True)
    class Meta(Commmon_info_3.Meta,Unmanged.Meta):
        pass
    
class places(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    
class Restaurent(places):
    city=models.CharField(max_length=100,null=True,blank=True)
    state=models.CharField(max_length=100,null=True,blank=True)
    
class Article(models.Model):
    article_id=models.AutoField(primary_key=True)
    article_name=models.CharField(max_length=100,null=True,blank=True)
    
    class Meta:
        abstract=True
        ordering=['article_name']

class Book(models.Model):
    book_name=models.CharField(max_length=100,null=True,blank=True)
    
    class Meta:
        abstract=True
        ordering=['book_name']
        
class Book_Review(Article,Book):
    # book_rating=models.CharField(max_length=100,null=True,blank=True)
    pass

class Blog(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    tagline=models.TextField()
    
    def __str__(self):
        return self.name 
    
class Author(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100)
    
    def __str__(self):
        return self.name

class Entry(models.Model):
    blog=models.ForeignKey(Blog,null=True,blank=True,on_delete=models.CASCADE)
    headline=models.CharField(max_length=100)
    body_text=models.TextField()
    pub_date=models.DateField()
    mod_date=models.DateField()
    author=models.ManyToManyField(Author,blank=True)
    number_comment=models.IntegerField()
    number_pingback=models.IntegerField()
    rating=models.IntegerField(default=5)
    
    def __str__(self):
        return self.headline
    
class Dog(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    data=models.JSONField(null=True)
    
    def __str__(self):
        return self.name
    
class publication(models.Model):
    title=models.CharField(max_length=100,null=True,blank=True)
    
    class Meta:
        ordering=['title']
    def __str__(self):
        return self.title
    
class Article(models.Model):
    headline=models.CharField(max_length=100,null=True,blank=True)
    publication=models.ManyToManyField(publication)
    
    class Meta:
        ordering=['headline']
    def __str__(self):
        return self.headline

    
    

        
    