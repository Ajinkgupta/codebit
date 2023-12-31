# Generated by Django 4.1.7 on 2023-12-07 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodePen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(max_length=50, unique=True)),
                ('html_code', models.TextField()),
                ('css_code', models.TextField()),
                ('js_code', models.TextField()),
            ],
        ),
    ]
