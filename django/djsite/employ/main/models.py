from django.db import models
from django.urls import reverse


class courses(models.Model):
    courses_name = models.CharField(max_length=20, verbose_name="Название курса")
    courses_description = models.CharField(max_length=200, verbose_name="Описание курса")
    courses_requirements = models.CharField(max_length=20, verbose_name="Требования к курсу")
    courses_urls = models.CharField(max_length=30, verbose_name="Ссылка на курс", null=True)
    courses_published = models.BooleanField(default=True, verbose_name="Активна")

    def __str__(self):
        return self.courses_name

    def get_absolute_url(self):
        return reverse('progs', kwargs={'courses_id': self.pk})

    class Meta:
        verbose_name = "Курсы"
        verbose_name_plural = "Курсы"
        ordering = ['courses_name']


class users(models.Model):
    users_pass = models.CharField(max_length=200, verbose_name="Пароль пользователя")
    users_login = models.CharField(max_length=30, verbose_name="Логин пользователя")
    users_phone = models.CharField(max_length=20, verbose_name="Телефон пользователя")
    users_email = models.EmailField(max_length=30, verbose_name="Почта пользователя")
    users_surname = models.CharField(max_length=20, verbose_name="Фамилия пользователя", null=True)
    users_name = models.CharField(max_length=20, verbose_name="Имя пользователя", null=True)
    users_patronymic = models.CharField(max_length=20, verbose_name="Отчество пользователя", null=True)
    users_region = models.CharField(max_length=45, verbose_name="Регион проживания пользователя")

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"


class users_documents(models.Model):
    users_documents_passport = models.CharField(max_length=10, verbose_name="Паспорт пользователя")
    users_documents_passport_photo = models.ImageField(upload_to="img/",
                                                       verbose_name="Фотография паспорта пользователя", null=True)
    users_documents_education = models.ImageField(upload_to="img/",
                                                  verbose_name="Документ об образовании пользователя")
    users_documents_snils = models.CharField(max_length=20, verbose_name="Снилс пользователя", null=True)
    users_documents_snils_photo = models.ImageField(upload_to="img/",
                                                    verbose_name="Фотография снилса пользователя", null=True)

    class Meta:
        verbose_name = "Документы пользователей"
        verbose_name_plural = "Документы пользователей"


class submissions(models.Model):
    submissions_date = models.DateField()
