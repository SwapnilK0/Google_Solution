# Generated by Django 5.0.1 on 2024-02-08 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity_user', '0003_alter_blog_authour_name_alter_blog_blog_discreption_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_discreption',
            field=models.TextField(),
        ),
    ]
