# Generated by Django 4.1.2 on 2022-11-10 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_alter_student_teachers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentTeacher',
        ),
    ]