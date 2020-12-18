import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='blog_images')),
                ('date_posted', models.DateTimeField(default=datetime.datetime(2020, 12, 11, 20, 4, 4, 258301))),
                ('author', models.CharField(max_length=50)),
            ],
        ),
    ]
