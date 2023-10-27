# Generated by Django 4.1.1 on 2022-10-28 17:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_category_subscribers_alter_post_author_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(related_name='cats', to=settings.AUTH_USER_MODEL, verbose_name='Подписчики'),
        ),
    ]