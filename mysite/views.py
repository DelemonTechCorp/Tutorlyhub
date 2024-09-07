from django.shortcuts import render,redirect
from lsmapp.models import Course,Categories,Location,Gender,Avilable,Country,Subject
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.views import View
from django.db.models import query
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from lsmapp.models import Course,Subject,Review,Author
from django.shortcuts import render,redirect,get_object_or_404


def BASE(request):
    return render(request, 'base.html')
def HOME1(request):
    category = Categories.objects.all().order_by('id')[0:6]
    course = Course.objects.filter(status = 'PUBLISH').order_by('id')[0:6]
    location = Location.objects.all()
    subject = Subject.objects.all()
    review = Review.objects.all()
    locations = Course.objects.values_list('author__location', flat=True).distinct()



    context = {
        'category':category,
        'course':course,
        'subject':subject,
        'locations':locations,
        'review':review,


    }

    return render(request, 'Main/home1.html',context)
def privacy(request):
    return render(request,"Main/privacy.html")
def terms(request):
    return render(request,"Main/terms.html")

class GetSubjectsView(View):
    def get(self, request, *args, **kwargs):
        category_id = request.GET.get('category_id')
        subjects = Subject.objects.filter(category__id=category_id)
        subjects_data = [{'id': subject.id, 'title': subject.title} for subject in subjects]
        return JsonResponse({'subjects': subjects_data})




def HOME(request):
    category = Categories.objects.all().order_by('id')[0:4]
    course = Course.objects.filter(status = 'PUBLISH').order_by('id')
    location = Location.objects.all()
    subject = Subject.objects.all()
    name=Author.objects.all()

    context = {
        'category':category,
        'course':course,
        'location':location,
        'subject':subject,
        'name':name

    }
    return render(request, 'Main/home.html',context)



def COURSE_DETAILS(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    category = Categories.get_all_category(Categories)
    location = Location.objects.all()
    gender = Gender.objects.all()
    avilable=Avilable.objects.all()
    country=Country.objects.all()
    subject=Subject.objects.all()

    context = {
        'course':course,
        'category':category,
        'location':location,
        'gender':gender,
        'avilabe':avilable,
        'country':country,
        'subject':subject,

    }

    return render(request,'course/course_details.html',context)
def TUTORS_ALL(request):
    category = Categories.get_all_category(Categories)
    location = Location.objects.all()
    gender = Gender.objects.all()
    course = Course.objects.all().order_by('id')[0:6]
    country=Country.objects.all()
    subject=Subject.objects.all()

    course_count = Course.objects.all().count()
    context = {
        'category':category,
        'location':location,
        'gender':gender,
        'course':course,
        'course_count': course_count,
        'country':country,
        'subject':subject,

    }

    return render(request, 'Main/tutors_all.html',context)

def filter_data(request):
    category = request.GET.getlist('category[]')
    # level =request.GET.getlist('level[]')
    price = request.GET.getlist('price[]')

    if price == ['PriceFree']:
        course = Course.objects.filter(price=0)
    elif price == ['PricePaid']:
        course = Course.objects.filter(price__gte=1)
    elif price == ['PriceAll']:
        course = Course.objects.all()
    elif category:
        course = Course.objects.filter(category__id__in = category).order_by('-id')
    # elif level:
        # course = Course.objects.filter(Level__id__in = level).order_by('-id')
    else:
        course = Course.objects.all().order_by('-id')

    context = {
        'course':course
    }


    t = render_to_string('ajax/course.html', context)
    return JsonResponse({'data': t})

def SEARCH_COURSE(request):
    query = request.GET.get('query', '')

    subject_id = request.GET.get('subject')
    location_id = request.GET.get('location')

    # Start with all courses and filter based on subject and location
    course_queryset = Course.objects.all()

    if subject_id:
        course_queryset = course_queryset.filter(subject=subject_id)

    if location_id:
         course_queryset = course_queryset.filter(author__location=location_id)

    # You might want to apply additional filters based on the query parameter

    # Final course queryset after applying filters
    course = course_queryset
    print(course)

    category = Categories.objects.all()
    location = Location.objects.all()
    gender = Gender.objects.all()
    subject = Subject.objects.all()

    context = {
        'course': course,
        'category': category,
        'gender': gender,
        'location': location,
        'subject': subject,
    }

    return render(request, 'search/search.html', context)




def FORM(request):
    return render(request,'Main/form.html')


def FORM1(request):
    return render(request,'Main/form1.html')


def CONTACT_US(request):
    category = Categories.get_all_category(Categories)

    context = {
        'category':category


     }

    return render(request, 'Main/contact_us.html')

def ABOUT_US(request):
    category = Categories.get_all_category(Categories)

    context = {
        'category':category

     }

    return render(request, 'Main/about_us.html')



def PAGE_NOT_FOUND(request):
    category = Categories.get_all_category(Categories)

    context = {
        'category':category

     }

    return render(request,'error/404.html')
def REVIEW(request,course_id):
    if request.method == 'POST':
        student = request.POST['studentname']
        content=request.POST['reviewcontent']
        course = get_object_or_404(Course, id=course_id)
        author_id = course.author
        ob2=Review()
        ob2.studentname=student
        ob2.reviewcontent=content
        ob2.author=author_id
        ob2.save()



        return HttpResponse("<script>alert('Review is submitted successfully');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('Invalid request');window.location='/'</script>")
@csrf_exempt
# def verify_author(request):
#     if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
#         author_id = request.POST.get('author_id')
#         try:
#             author = Author.objects.get(pk=author_id)
#             author.verify = True
#             author.save()
#             return JsonResponse({'status': 'success'})
#         except Author.DoesNotExist:
#             pass
#     return JsonResponse({'status': 'error'}, status=400)
def verify_author(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        author_id = request.POST.get('author_id')
        try:
            author = Author.objects.get(pk=author_id)
            author.verify = not author.verify  # Toggle the verification status
            author.save()
            login_location = "http://127.0.0.1:8000/loginform"
            username=author.email
            password=author.password
            subject = 'Verification Status Updated'
            if author.verify:
                message = (
                    f'Your verification status has been updated.\n'
                    f'You are now verified. Login here: {login_location}\n'
                    f'Your username is :{username}\n and password is:{password}'
                )
            else:
                message = (
                    f'Your verification status has been updated. '
                    f'You are now unverified because of some verification issues.'
                )
            from_email = 'asharafsaleena22@gmail.com'  # Change this to your email
            to_email = author.email
            send_mail(subject, message, from_email, [to_email])
            return JsonResponse({'status': 'success'})
        except Author.DoesNotExist:
            pass
    return JsonResponse({'status': 'error'}, status=400)
