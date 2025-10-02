from django.contrib import admin
from pages.models import Post, Comment, Student, Course, Enrollment
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)