# Generated by Django 4.1.3 on 2022-12-05 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_courses_options_alter_users_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users_documents',
            name='users_documents_passport_photo',
            field=models.ImageField(null=True, upload_to='img/', verbose_name='Фотография паспорта пользователя'),
        ),
        migrations.AddField(
            model_name='users_documents',
            name='users_documents_snils_photo',
            field=models.ImageField(null=True, upload_to='img/', verbose_name='Фотография снилса пользователя'),
        ),
        migrations.AlterField(
            model_name='users_documents',
            name='users_documents_education',
            field=models.ImageField(upload_to='img/', verbose_name='Документ об образовании пользователя'),
        ),
    ]
