from django.contrib import admin
from django.urls import path,include
from .import views,user_login
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import GetSubjectsView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('base', views.BASE, name='base'),
    path('404',views.PAGE_NOT_FOUND,name='404'),
    path('', views.HOME1, name='home1'),
    path('home', views.HOME, name='home'),
    path('tutors_all',views.TUTORS_ALL, name='tutors_all'),
    # path('course/tutors_details',views.TUTORS_DETAILS,name='tutors_details'),
    path('courses', views.TUTORS_ALL, name='tutors_all'),
    path('courses/filter-data',views.filter_data,name="filter-data"),
    path('form',views.FORM,name='form'),
    path('form1',views.FORM1,name='form1'),
    path('course/<str:course_id>',views.COURSE_DETAILS,name='course_details'),
    path('search', views.SEARCH_COURSE, name='search_course'),
    path('search/', GetSubjectsView.as_view(), name='get_subjects'),


    path('contact', views.CONTACT_US, name='contact_us'),
    path('about', views.ABOUT_US, name='about_us'),

    path('register', user_login.REGISTER, name='register'),
    path('register1', user_login.REGISTER1, name='register1'),
    # path('doLogin', user_login.DO_LOGIN, name='doLogin'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/profile/<int:id>', user_login.PROFILE, name='profile'),
    # path('accounts/profile/update', user_login.PROFILE_UPDATE, name='profile_update'),
    #  path('get_subjects/', GetSubjectsView.as_view(), name='get_subjects'),


    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"),
         name='password_reset'),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),


    # path('checkpassword',user_login.CHECKPASSWORD,name='checkpassword'),
    path('loginn',user_login.LOGIN,name='loginn'),
    path('loginform',user_login.LOGINFORM,name='loginform'),
    path('reviews/<int:course_id>/',views.REVIEW,name='reviews'),
    path('profile',user_login.PROFILE,name='profile'),
    path('profileupdate',user_login.PROFILEUPDATE,name='profileupdate'),
    path('forgetpwd',user_login.forgetpwd,name='forgetpwd'),
    path('getpwd',user_login.getpwd, name="getpwd"),
    path('addcourse',user_login.COURSE,name='addcourse'),
    path('insertcourse',user_login.ADDCOURSE,name='insertcourse'),
    path('verify-author/', views.verify_author, name='verify_author'),
    path('registrationstep1',user_login.REGISTERSTEP1,name="registrationstep1"),
    path('registrationstep2',user_login.REGISTERSTEP2,name="registrationstep2"),
    path('registrationstep3',user_login.REGISTERSTEP3,name="registrationstep3"),
    path('registrationstep4',user_login.REGISTERSTEP4,name="registrationstep4"),
    path('registrationstep5',user_login.REGISTERSTEP5,name="registrationstep5"),
    path('step2',user_login.step2,name='step2'),
    path('step3',user_login.step3,name='step3'),
    path('step4',user_login.step4,name='step4'),
    path('step5',user_login.step5,name='step5'),
    path('privacy',views.privacy,name="privacy"),
    path('terms',views.terms,name="terms"),



]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
