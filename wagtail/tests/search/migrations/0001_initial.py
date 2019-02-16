# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-12 10:55
from __future__ import unicode_literals

import django.db.models.deletion
import taggit.managers
from django.db import migrations, models

import wagtail.wagtailsearch.index


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0024_alter_page_content_type_on_delete_behaviour'),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('live', models.BooleanField(default=False)),
                ('published_date', models.DateField(null=True)),
            ],
            bases=(wagtail.wagtailsearch.index.Indexed, models.Model),
        ),
        migrations.CreateModel(
            name='SearchTestChild',
            fields=[
                ('searchtest_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='searchtests.SearchTest')),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('extra_content', models.TextField()),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.Page')),
            ],
            bases=('searchtests.searchtest',),
        ),
        migrations.AddField(
            model_name='searchtest',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
