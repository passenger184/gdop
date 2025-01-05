# Generated by Django 5.1.4 on 2025-01-05 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mint_landing', '0016_pdfresource'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pdfresource',
            options={'verbose_name': 'PDF Resource', 'verbose_name_plural': 'PDF Resources'},
        ),
        migrations.AlterField(
            model_name='pdfresource',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/pdf_resources/'),
        ),
    ]