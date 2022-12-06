from django.contrib import admin
from .models import *


class CoursesAdmin(admin.ModelAdmin):
    list_display = ('id', 'courses_name', 'courses_description', 'courses_requirements', 'courses_published')
    list_display_links = ('id', 'courses_name')
    search_fields = ('courses_name', 'courses_description')
    list_editable = ('courses_published',)
    list_filter = ('courses_published',)


admin.site.register(courses, CoursesAdmin)


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'users_login', 'users_name',
                    'users_surname', 'users_patronymic', 'users_phone', 'users_email')
    list_display_links = ('id', 'users_login', 'users_email', 'users_phone')
    search_fields = ('users_login', 'users_phone', 'users_email', 'users_name')


admin.site.register(users, UsersAdmin)


class UsersDocumentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'users_documents_passport', 'users_documents_education', 'users_documents_snils')
    list_display_links = ('id', 'users_documents_passport')
    search_fields = ('id', 'users_documents_passport')


admin.site.register(users_documents, UsersDocumentsAdmin)
