# Generated by Django 2.2.2 on 2019-07-23 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_company', '0014_auto_20190723_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list_menu',
            name='image',
            field=models.CharField(blank=True, choices=[('media/about_company/list_others_pages/Informacionnye_materialy.png', 'Informacionnye_materialy.png'), ('media/about_company/list_others_pages/Antikorrupcziya_80.png', 'Antikorrupcziya_80.png'), ('media/about_company/list_others_pages/Informaczionnye-materialy_80.png', 'Informaczionnye-materialy_80.png'), ('def', 'noimage.png'), ('media/about_company/list_others_pages/Kontakty.png', 'Kontakty.png'), ('media/about_company/list_others_pages/Proekty.png', 'Proekty.png'), ('media/about_company/list_others_pages/Rekvizity_80.png', 'Rekvizity_80.png'), ('media/about_company/list_others_pages/Sotrudnichestvo.png', 'Sotrudnichestvo.png'), ('media/about_company/list_others_pages/Istoriya_kompanii.png', 'Istoriya_kompanii.png'), ('media/about_company/list_others_pages/Struktura.png', 'Struktura.png'), ('media/about_company/list_others_pages/Firminnyj-stil_80.png', 'Firminnyj-stil_80.png'), ('media/about_company/list_others_pages/Dlya-SMI_80.png', 'Dlya-SMI_80.png'), ('media/about_company/list_others_pages/Novosti.png', 'Novosti.png'), ('media/about_company/list_others_pages/Telefonnyj-spravochnik_80.png', 'Telefonnyj-spravochnik_80.png'), ('media/about_company/list_others_pages/Vakansii.png', 'Vakansii.png'), ('media/about_company/list_others_pages/Missiya_i_celi.png', 'Missiya_i_celi.png'), ('media/about_company/list_others_pages/Vakansii_80.png', 'Vakansii_80.png'), ('media/about_company/list_others_pages/Licenzii.png', 'Licenzii.png'), ('media/about_company/list_others_pages/Adresa_80.png', 'Adresa_80.png'), ('media/about_company/list_others_pages/image_error_full.png', 'image_error_full.png')], default=('media/about_company/list_others_pages/Informacionnye_materialy.png', 'Informacionnye_materialy.png'), max_length=80, verbose_name='изображения'),
        ),
    ]
