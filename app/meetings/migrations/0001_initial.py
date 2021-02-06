# Generated by Django 3.1.6 on 2021-02-06 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('meeting_id', models.AutoField(primary_key=True, serialize=False, verbose_name='会議ID')),
                ('meeting_name', models.CharField(blank=True, max_length=200, verbose_name='会議名')),
                ('num_men', models.IntegerField(null=True, verbose_name='男性の人数')),
                ('num_women', models.IntegerField(null=True, verbose_name='女性の人数')),
                ('duration_men', models.IntegerField(blank=True, null=True, verbose_name='男性の継続時間')),
                ('duration_women', models.IntegerField(blank=True, null=True, verbose_name='女性の継続時間')),
                ('is_done', models.BooleanField(default=False, verbose_name='会議終了済み')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
            ],
            options={
                'verbose_name': '会議',
                'verbose_name_plural': '会議',
                'db_table': 'meeting',
                'ordering': ['created_at'],
            },
        ),
    ]
