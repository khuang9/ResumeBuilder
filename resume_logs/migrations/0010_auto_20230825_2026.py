# Generated by Django 3.2.20 on 2023-08-26 00:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resume_logs', '0009_topic_resume_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='text',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='QuestionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]