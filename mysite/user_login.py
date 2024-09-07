from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib import messages
from lsmapp.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,login,logout
from lsmapp.models import loginn,Author,Course,Subject,Categories
from django.http.response import HttpResponse
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404


from django.core.files.storage import FileSystemStorage

def REGISTER1(request):
     ob=Author.objects.all()
     return render(request,'registration/register.html',{'val':ob})
def step2(request):
    return render(request,'registration/regstep2.html')
def step3(request):
    return render(request,'registration/step3.html')
def step4(request):
    return render(request,'registration/step4.html')
def step5(request):
    return render(request,'registration/step5.html')
def LOGINFORM(request):
    return render(request,'registration/login.html')

def REGISTER(request):

    if request.method == 'POST':
        Fname = request.POST['firstname']
        Lname = request.POST['lastname']
        gender = request.POST['gender']
        dob = request.POST['birthday']
        country = request.POST['country']
        city = request.POST['city']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        education = request.POST['education']
        uploadimage = request.FILES.get('uploadimage')
        uploadvideo = request.FILES.get('uploadvideo')
        upload = request.FILES.get('upload')
        fs = FileSystemStorage('media/')
        if uploadimage:
            fs.save(uploadimage.name, uploadimage)

        if uploadvideo:
            fs.save(uploadvideo.name, uploadvideo)

        if upload:
            fs.save(upload.name, upload)
        aboutme = request.POST['aboutme']
        availability = request.POST['availability']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']

        ob= loginn()
        ob.email=email
        ob.password=password
        ob.type='tutor'
        ob.save()

        ob1 = Author()
        ob1.lid=ob
        ob1.name = Fname + " " + Lname
        ob1.gender = gender
        ob1.dob = dob
        ob1.country = country
        ob1.location = city
        ob1.email = email
        ob1.phoneNumber = phonenumber
        ob1.education = education
        ob1.resume = upload
        ob1.author_profile = uploadimage
        ob1.author_video = uploadvideo
        ob1.about_author = aboutme
        ob1.avilable = availability
        ob1.password = password
        ob1.confirmpassword = confirmpassword
        ob1.save()
        request.session['Aid'] = ob1.id
        return HttpResponse("<script>alert('Inserted successfully');window.location='/loginform'</script>")
    else:
        return HttpResponse("<script>alert('Invalid request');window.location='/loginform'</script>")
def REGISTERSTEP1(request):
    if request.method == 'POST':
        Fname = request.POST.get('firstname', '')
        Lname = request.POST.get('lastname', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        confirmpassword = request.POST.get('confirmpassword', '')
        fullname = Fname + " " + Lname
        # Store data in session
        request.session['registration_data'] = {
            'fullname': fullname,
            'email': email,
            'password': password,
            'confirmpassword': confirmpassword
        }
        request.session.save()
        print(request.session['registration_data'])
        return redirect('step2')
def REGISTERSTEP2(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phonenumber', '')
        dob = request.POST.get('birthday', '')
        gender = request.POST.get('gender', '')
        request.session['registration_data']['phone_number'] = phone_number
        request.session['registration_data']['dob'] = dob
        request.session['registration_data']['gender'] = gender
        print(request.session['registration_data'])
        request.session.save()
        return redirect('step3')

def REGISTERSTEP3(request):
     if request.method == 'POST':
        country = request.POST.get('country', '')
        city = request.POST.get('city', '')
        request.session['registration_data']['country'] = country
        if city == 'Other':
            other_city = request.POST.get('otherCity', '')  # Get the value from the textbox
            request.session['registration_data']['city'] = other_city
        else:
            request.session['registration_data']['city'] = city
        print(request.session['registration_data'])
        request.session.save()
        return redirect('step4')
def REGISTERSTEP4(request):
     if request.method == 'POST':
        availability = request.POST.get('availability', '')
        aboutme = request.POST.get('aboutme', '')
        education=request.POST.get('education', '')
        request.session['registration_data']['availability'] = availability
        request.session['registration_data']['aboutme'] = aboutme
        request.session['registration_data']['education'] = education
        print(request.session['registration_data'])
        request.session.save()
        return redirect('step5')
def REGISTERSTEP5(request):
    if request.method == 'POST':
        uploadimage = request.FILES.get('photo')
        uploadvideo = request.FILES.get('video')
        upload = request.FILES.get('resume')

        # Retrieving data from session
        registration_data = request.session.get('registration_data', None)

        # Creating a new user object
        ob = loginn()
        ob.email = registration_data['email']
        ob.password = registration_data['password']
        ob.type = 'tutor'
        ob.save()

        # Creating a new Author object and saving it
        ob1 = Author()
        ob1.lid = ob
        ob1.name = registration_data['fullname']
        ob1.gender = registration_data['gender']
        ob1.dob = registration_data['dob']
        ob1.country = registration_data['country']
        ob1.location = registration_data['city']
        ob1.email = registration_data['email']
        ob1.phoneNumber = registration_data['phone_number']
        ob1.education = registration_data['education']
        ob1.resume = upload
        ob1.author_profile = uploadimage
        ob1.author_video = uploadvideo
        ob1.about_author = registration_data['aboutme']
        ob1.avilable = registration_data['availability']
        ob1.password = registration_data['password']
        ob1.confirmpassword = registration_data['confirmpassword']
        ob1.save()

        # Clearing session data
        del request.session['registration_data']

        # Redirecting to login page
        return HttpResponse("<script>alert('Inserted successfully');window.location='/loginform'</script>")
    else:
        return HttpResponse("<script>alert('Invalid request');window.location='/loginform'</script>")
# def REGISTERSTEP5(request):
#      if request.method == 'POST':
#         uploadimage = request.FILES.get('photo')
#         uploadvideo = request.FILES.get('video')
#         upload = request.FILES.get('resume')
#         fs = FileSystemStorage('media/')
#         if uploadimage:
#             fs.save(uploadimage.name, uploadimage)

#         if uploadvideo:
#             fs.save(uploadvideo.name, uploadvideo)

#         if upload:
#             fs.save(upload.name, upload)

#         # request.session.save()

#         print(request.session['registration_data'])
#         registration_data = request.session.get('registration_data', None)
#         ob= loginn()
#         ob.email=registration_data['email']
#         ob.password=registration_data['password']
#         ob.type='tutor'
#         ob.save()

#         ob1 = Author()
#         ob1.lid=ob
#         ob1.name = registration_data['fullname']
#         ob1.gender =  registration_data['gender']
#         ob1.dob =  registration_data['dob']
#         ob1.country =  registration_data['country']
#         ob1.location =  registration_data['city']
#         ob1.email =  registration_data['email']
#         ob1.phoneNumber =  registration_data['phone_number']
#         ob1.education =  registration_data['education']
#         ob1.resume =  upload
#         ob1.author_profile = uploadimage
#         ob1.author_video =  uploadvideo
#         ob1.about_author =  registration_data['aboutme']
#         ob1.avilable = registration_data['availability']
#         ob1.password = registration_data['password']
#         ob1.confirmpassword = registration_data['confirmpassword']
#         ob1.save()
#         request.session['Aid'] = ob1.id
#         return HttpResponse("<script>alert('Inserted successfully');window.location='/loginform'</script>")
#      else:
#         return HttpResponse("<script>alert('Invalid request');window.location='/loginform'</script>")
def LOGIN(request):
    uname=request.POST.get('email2','')
    pwd=request.POST.get('password','')
    print(uname, pwd)
    try:
        ob=loginn.objects.get(email=uname,password=pwd)
        if ob.type=="tutor":
            author = Author.objects.get(email=uname)
            verify_status = author.verify
            if verify_status:
                request.session['lid']=ob.id
                return render(request, 'Main/home.html', {'username': author.name})
            else:
                return HttpResponse("<script>alert('Your account is not verified yet. Please contact the administrator.');window.location='/loginform'</script>")
        else:
            return HttpResponse("<script>alert('Invalid username or password');window.location='/loginform'</script>")
    except:
        return HttpResponse("<script>alert('Invalid username or password');window.location='/loginform'</script>")
# def LOGIN(request):
#     if request.method == 'POST':
#         uname = request.POST['email']
#         pwd = request.POST['password']
#         try:
#             # Fetch the loginn object
#             ob = loginn.objects.get(email=uname, password=pwd)
#             if ob.type == "tutor":
#                 request.session['lid']=ob.id
#                 # Get the related Author object
#                 author = Author.objects.get(email=uname)
#                 # Pass the author's name to the template context
#                 return render(request, 'Main/home.html', {'username': author.name})
#             else:
#                 return HttpResponse("<script>alert('Invalid username or password');window.location='/loginform'</script>")
#         except:
#             return HttpResponse("<script>alert('Invalid username or password');window.location='/loginform'</script>")
#     else:
#         return HttpResponse("<script>alert('Invalid request');window.location='/loginform'</script>")
# def DO_LOGIN(request):
#     if request.method == "POST":
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         user = EmailBackEnd.authenticate(request,
#                                      username=email,
#                                      password=password)
#         if user!=None:
#            login(request,user)
#            return redirect('home')
#         else:
#            messages.error(request,'Email and Password Are Invalid !')
#            return redirect('login')

    # return redirect('home')
def PROFILE(request):
    login_id = request.session.get('lid')
    authors = Author.objects.filter(lid_id=login_id)
    return render(request,'registration/profile.html',{'authors': authors})
# def PROFILE_UPDATE(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user_id = request.user.id

#         user = User.objects.get(id=user_id)
#         user.first_name = first_name
#         user.last_name = last_name
#         user.username = username
#         user.email = email

#         if password != None and password != "":
#             user.set_password(password)

#         user.save()
#         messages.success(request,'Profile Are Successfully Updated. ')
#         return redirect('profile')
def PROFILEUPDATE (request):

    name = request.POST['firstname']
    gender = request.POST['gender']
    dob = request.POST['birthday']
    country = request.POST['country']
    city = request.POST['city']
    email = request.POST['email']
    phonenumber = request.POST['phonenumber']
    address = request.POST['address']
    education = request.POST['education']
    uploads = request.POST['uploads']
    uploadimages = request.POST['uploadimages']
    uploadvideos = request.POST['uploadvideos']
    aboutme = request.POST['aboutme']
    availability = request.POST['availability']
    login_id = request.session.get('lid')
    ob= loginn.objects.get(id=request.session['lid'])
    ob.email=email
    ob.save()

    ob1 = Author.objects.get(lid_id=login_id)
    ob1.lid=ob
    ob1.name =name
    ob1.gender = gender
    ob1.dob = dob
    ob1.country = country
    ob1.location = city
    ob1.email = email
    ob1.phoneNumber = phonenumber
    ob1.address = address
    ob1.education = education
    ob1.resume = uploads
    ob1.author_profile = uploadimages
    ob1.author_video = uploadvideos
    ob1.about_author = aboutme
    ob1.avilable = availability
    ob1.save()
    author = Author.objects.get(lid_id=login_id)
    return render(request, 'Main/home.html', {'username': author.name, 'message': 'edited successfully'})

def forgetpwd(request):
    return render(request,'registration/forgetpwd.html')
def getpwd(request):
    print(request.POST)
    email = request.POST['email1']
    try:
        validate_email(email)
    except ValidationError:
        return HttpResponse("<script>alert('Invalid email address.');window.location='/forgetpwd'</script>")


    ob1 = loginn.objects.get(email=email)

    if ob1 is not None:
        send_mail('CREDITCARD FRAUD DETECTION', "YOUR  PASSWORD IS  -" + ob1.password, 'email@gmail.com', [email],
                  fail_silently=False)
        return HttpResponse("<script>alert('Email sent successfully.');window.location='/loginform'</script>")
    else:
        return HttpResponse("<script>alert('Invalid username or email.');window.location='/forgetpwd'</script>")

def COURSE(request):
    ob=Subject.objects.all()
    ob1=Categories.objects.all()
    return render(request,'Main/course.html',{"val":ob,"var":ob1})

def ADDCOURSE(request):
    sub=request.POST['subject']
    cat=request.POST['category']
    des=request.POST['des']
    price=request.POST['price']
    discount=request.POST['discount']
    status=request.POST['status']
    author_id = request.session.get('lid')

    ob1=Course()
    obs=Subject.objects.get(id=sub)
    obc=Categories.objects.get(id=cat)
    author_instance = get_object_or_404(Author, lid__id=author_id)
    ob1.author =author_instance
    ob1.title=obs
    ob1.subject=obs
    ob1.category=obc
    ob1.description=des
    ob1.price=price
    ob1.discount=discount
    ob1.status=status
    ob1.save()
    author = Author.objects.get(lid_id=author_id)
    return render(request, 'Main/home.html', {'username': author.name, 'message': 'inserted successfully'})
def step2(request):
    return render(request,'registration/regstep2.html')
def step3(request):
    return render(request,'registration/step3.html')
def step4(request):
    return render(request,'registration/step4.html')
def step5(request):
    return render(request,'registration/step5.html')