# Generated by Django 4.0.4 on 2022-09-03 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sew', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=122)),
                ('lastname', models.CharField(max_length=122)),
                ('mail', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=122)),
                ('Password', models.CharField(max_length=122)),
                ('Shopname', models.CharField(max_length=122)),
                ('Address', models.CharField(max_length=122)),
            ],
        ),
        migrations.DeleteModel(
            name='login',
        ),
    ]
