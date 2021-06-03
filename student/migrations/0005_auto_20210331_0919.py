# Generated by Django 3.1.7 on 2021-03-31 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20210331_0811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='isCompany',
        ),
        migrations.AlterField(
            model_name='resume',
            name='address',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='cgpa',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='college',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='grad_year',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='mob',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='resume',
            name='skills',
            field=models.TextField(blank=True, null=True),
        ),
    ]
