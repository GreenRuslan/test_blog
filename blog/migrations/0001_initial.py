# Generated by Django 2.1.5 on 2019-01-22 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Коммент')),
                ('created', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата коммента')),
                ('moderation', models.BooleanField(default=False, verbose_name='Модерация')),
            ],
            options={
                'verbose_name': 'Коммент',
                'verbose_name_plural': 'Комменты',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=130, verbose_name='Текст заголовка')),
                ('text_short', models.TextField(max_length=400, verbose_name='Краткое описание')),
                ('text', models.TextField(verbose_name='Текст статьи')),
                ('date_create', models.DateTimeField(auto_now=True, verbose_name='Дата создания поста')),
                ('description', models.CharField(max_length=200, verbose_name='Описание всего этого добра')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Аффтар')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
        migrations.AddField(
            model_name='comments',
            name='pos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post', verbose_name='Пост'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Юзверь'),
        ),
    ]
