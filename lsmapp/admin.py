from django.contrib import admin
from .models import *
from django.core.mail import send_mail
from django.utils.html import mark_safe,format_html
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# class what_you_learn_Tabularline(admin.TabularInline):
#     model = what_you_learn

# class Requirments_Tabularline(admin.TabularInline):
#     model = Requirements

# Register your models here.
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'gender', 'avilable', 'education', 'country', 'location', 'phoneNumber', 'resume', 'author_profile','verify','verify_button',)


    def verify_button(self, obj):
      if not obj.verify:
        url = reverse('verify_author')
        return format_html(
            '<button type="button" style="background-color: #007bff; color: #fff; border: none; border-radius: 4px; padding: 8px 16px; cursor: pointer;" '
            'class="verify-button" data-author-id="{}" data-verify-url="{}" data-verified="false">Verify</button>', obj.pk, url)
      else:
        url = reverse('verify_author')
        return format_html(
            '<button type="button" style="background-color: #007bff; color: #fff; border: none; border-radius: 4px; padding: 8px 16px; cursor: pointer;" '
            'class="verify-button" data-author-id="{}" data-verify-url="{}" data-verified="true">Unverify</button>', obj.pk, url)
    verify_button.allow_tags = True
    verify_button.short_description = 'Verify'


    class Media:
        js = ('admin/js/jquery.init.js', 'myapp/verify_author.js')  # Include your custom JavaScript file


    def download_resume_link(self, obj):
        if obj.resume:
            return mark_safe(f'<a href="{obj.resume.url}" download>Download Resume</a>')
        return "No Resume"

    download_resume_link.short_description = "Resume"
class LoginAdmin(admin.ModelAdmin):
    list_display=('email','password','type')
class CourseAdmin(admin.ModelAdmin):
    list_display=('subject','title','author','category','description','price','discount','status')
admin.site.register(Course,CourseAdmin)
admin.site.register(loginn,LoginAdmin)
admin.site.register(Author, TrainerAdmin)
admin.site.register(Categories)

# admin.site.register(what_you_learn)
# admin.site.register(Requirements)
# admin.site.register(Lesson)
admin.site.register(Location)
admin.site.register(Gender)
admin.site.register(Avilable)
admin.site.register(Country)
admin.site.register(Subject)
class Reviewadmin(admin.ModelAdmin):
    list_display=('studentname','reviewcontent','author',)
admin.site.register(Review,Reviewadmin)