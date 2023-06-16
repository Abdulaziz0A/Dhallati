# Generated by Django 4.2.2 on 2023-06-14 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestLostItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('R', 'Red'), ('G', 'Green'), ('B', 'Blue'), ('BLA', 'Black'), ('Y', 'Yellow'), ('W', 'White')], default='B', max_length=100)),
                ('place', models.CharField(choices=[('T', 'TRAKING'), ('M', 'MATCHED'), ('F', 'FOUND')], default='T', max_length=100)),
                ('discription', models.TextField()),
                ('image', models.ImageField(default='image/default.jpg', upload_to='image/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('F', 'FRISTFLOOR'), ('S', 'SECOUNDFLOOR'), ('T', 'THIRDFLOOR')], default='F', max_length=100)),
                ('is_read', models.BooleanField(default=False)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.catagory')),
            ],
        ),
    ]