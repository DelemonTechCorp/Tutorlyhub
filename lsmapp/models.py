from django.db import models
from django.urls import reverse

# from django.utils.text import slugify
from django.db.models.signals import pre_save


# Create your models here.
class Categories(models.Model):
    # icon = models.CharField(max_length=200,null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


    def get_all_category(self):
        return Categories.objects.all().order_by('id')

class Location(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Gender(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class Avilable(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class loginn(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=50)



class Author(models.Model):
    lid=models.ForeignKey(loginn, on_delete=models.CASCADE)
    author_profile = models.ImageField(upload_to="media/author")
    author_video = models.FileField(upload_to="media/videos")
    name = models.CharField(max_length=100, null=True)
    about_author = models.TextField()
    location =  models.CharField(max_length=100)
    gender =  models.CharField(max_length=100)
    avilable =  models.CharField(max_length=100)
    country =  models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phoneNumber=models.CharField(max_length=100)
    education=models.CharField(max_length=100)
    resume=models.FileField(upload_to="media/Resumes")
    password=models.CharField(max_length=100)
    confirmpassword=models.CharField(max_length=100)
    verify = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Review(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True)
    studentname=models.CharField(max_length=50)
    reviewcontent=models.CharField(max_length=300)


class Subject(models.Model):
    title = models.CharField(max_length=500)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Course(models.Model):

    title = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject,on_delete=models.SET_NULL, blank=True,null=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, blank=True,null=True)
    description = models.TextField()
    price = models.IntegerField(null=True,default=0)
    discount = models.IntegerField(null=True)
    # slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    status = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_details', args=[str(self.id)])


# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.title)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Course.objects.filter(slug=slug)
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s-%s" % (slug, qs.first())
#         return create_slug(instance, new_slug=new_slug)
#     return slug


# def pre_save_post_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)

# pre_save.connect(pre_save_post_receiver, Course)



# class what_you_learn(models.Model):
#     course = models.ForeignKey(Course,on_delete=models.CASCADE)
#     points = models.CharField(max_length=500)

#     def __str__(self):
#         return self.points

# class Requirements(models.Model):
#     course = models.ForeignKey(Course,on_delete=models.CASCADE)
#     points = models.CharField(max_length=500)

#     def __str__(self):
#         return self.points

# class Lesson(models.Model):
#     course = models.ForeignKey(Course,on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)


#     def __str__(self):
#         return self.name + " - " + self.course.title


# class Video(models.Model):
#     serial_number = models.IntegerField(null=True)

#     thumbnail = models.ImageField(upload_to="Media/yt_Thumbnail",null=True)

#     course = models.ForeignKey(Course,on_delete=models.CASCADE)

#     lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)

#     title = models.CharField(max_length=100)

#     youtube_id = models.CharField(max_length=200)

#     time_duration = models.FloatField(null=True)

#     previes = models.BooleanField(default=False)



