# Generated by Django 3.0.6 on 2020-06-07 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200607_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicines', models.CharField(max_length=200, null=True)),
                ('symptoms', models.CharField(max_length=200, null=True)),
                ('test', models.CharField(max_length=200, null=True)),
                ('diagnosis', models.CharField(max_length=200, null=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.CreatePatient')),
            ],
        ),
    ]
