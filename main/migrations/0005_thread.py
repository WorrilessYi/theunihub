# Generated by Django 2.2.28 on 2025-03-03 13:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_auto_20250303_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_on', models.DateTimeField(blank=True)),
                ('related_university', models.CharField(blank=True, choices=[('aberdeen', 'University of Aberdeen'), ('abertay', 'Abertay University'), ('caledonian', 'Glasgow Caledonian University'), ('dundee', 'University of Dundee'), ('edinburgh', 'University of Edinburgh'), ('glasgow', 'University of Glasgow'), ('heriot_watt', 'Heriot-Watt University'), ('napier', 'Edinburgh Napier University'), ('queen_margaret', 'Queen Margaret University'), ('robert_gordon', 'Robert Gordon University'), ('st_andrews', 'University of St. Andrews'), ('stirling', 'University of Stirling'), ('strathclyde', 'University of Strathclyde'), ('uws', 'University of the West of Scotland'), ('uhi', 'University of the Highlands and Islands'), ('queens', "Queen's University of Belfast"), ('ulster', 'University of Ulster'), ('aberystwyth', 'Aberystwyth University'), ('bangor', 'Bangor University'), ('cardiff', 'Cardiff University'), ('cardiff_met', 'Cardiff Metropolitan University'), ('usw', 'University of South Wales'), ('swansea', 'Swansea University'), ('tsd', 'University of Wales Trinity Saint David'), ('wrexham', 'Wrexham University'), ('oxford', 'University of Oxford'), ('cambridge', 'University of Cambridge'), ('imperial', 'Imperial College London'), ('ucl', 'University College London'), ('kcl', "King's College London"), ('lse', 'London School of Economics'), ('harvard', 'Harvard University'), ('mit', 'Massachusetts Institute of Technology'), ('stanford', 'Stanford University'), ('berkeley', 'University of California, Berkeley')], max_length=250, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Forum')),
            ],
            options={
                'verbose_name_plural': 'Threads',
                'ordering': ['title'],
            },
        ),
    ]
