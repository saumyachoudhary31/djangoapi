# Generated by Django 2.1.7 on 2019-12-18 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='approvals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('dependants', models.IntegerField(default=0)),
                ('applicantincome', models.IntegerField(default=0)),
                ('coapplicantincome', models.IntegerField(default=0)),
                ('loanamt', models.IntegerField(default=0)),
                ('loanterm', models.IntegerField(default=0)),
                ('credithistory', models.IntegerField(default=0)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('married', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20)),
                ('graduatededucation', models.CharField(choices=[('Graduated', 'Graduated'), ('Not_Graduated', 'Not_Graduated')], max_length=20)),
                ('selfemployed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20)),
                ('area', models.CharField(choices=[('Rural', 'Rural'), ('Urban', 'Urban'), ('Semiurban', 'Semiurban')], max_length=20)),
            ],
        ),
    ]
