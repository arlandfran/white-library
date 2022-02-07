# Generated by Django 4.0.2 on 2022-02-07 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.CharField(default='unknown', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='book_format',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='pages',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='release_date',
            field=models.CharField(default='unknown', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='signed_copy',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]