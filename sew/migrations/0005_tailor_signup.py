# Generated by Django 4.0.4 on 2022-09-05 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sew', '0004_customer_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tailor_Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=122)),
                ('lastname', models.CharField(max_length=122)),
                ('mail', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=50)),
                ('shopname', models.CharField(max_length=122)),
                ('address', models.CharField(max_length=122)),
            ],
        ),
    ]
