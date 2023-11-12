# Generated by Django 3.1.4 on 2023-11-11 07:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RepeatNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100, verbose_name='Номер повтора')),
            ],
            options={
                'verbose_name': 'Номер повтора',
                'verbose_name_plural': 'Номера повтора',
            },
        ),
        migrations.CreateModel(
            name='WordsCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_en', models.JSONField(blank=True, verbose_name='Английский')),
                ('word_ru', models.JSONField(blank=True, verbose_name='Русский')),
                ('transcription', models.JSONField(blank=True, verbose_name='Транскрипция')),
                ('phrases_en', models.JSONField(blank=True, verbose_name='Фразы-Английский')),
                ('phrases_ru', models.JSONField(blank=True, verbose_name='Фразы-Русский')),
            ],
            options={
                'verbose_name': 'Слово',
                'verbose_name_plural': 'Слова',
            },
        ),
        migrations.CreateModel(
            name='WordsToRepeat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100, verbose_name='Слово')),
                ('repeat_number', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='words.repeatnumber')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Слово для повторения',
                'verbose_name_plural': 'Слова для повторения',
            },
        ),
        migrations.CreateModel(
            name='WordsConfigJson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WORD_DATA', models.JSONField(null=True)),
                ('WORD_USER', models.JSONField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Configs',
            },
        ),
        migrations.CreateModel(
            name='Word_Accumulator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_en', models.CharField(max_length=100, verbose_name='Слово на английском')),
                ('word_ru', models.CharField(max_length=100, verbose_name='Слово на русском')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Накопитель слов',
                'verbose_name_plural': 'Накопитель слов',
            },
        ),
        migrations.CreateModel(
            name='SettingsWordNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_words', models.IntegerField(default=20, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(5)], verbose_name='Количество слов за день')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Количество слов за день',
                'verbose_name_plural': 'Количество за день',
            },
        ),
        migrations.CreateModel(
            name='IntroductionWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_en', models.CharField(max_length=100, verbose_name='На английском')),
                ('transcription', models.CharField(max_length=100, verbose_name='Транскрипция')),
                ('word_ru', models.CharField(max_length=100, verbose_name='На русском')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Слова для ознакомления',
                'verbose_name_plural': 'Слова для ознакомления',
            },
        ),
    ]
