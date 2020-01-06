from django.db import models


# Create your models here.
GENDER_CHOICES=(
    ('Male','Male'),
    ('Female','Female')
)
MARRIED_CHOICES=(
    ('Yes','Yes'),
    ('No','No')
)
GRADUATED_CHOICES=(
    ('Graduated','Graduated'),
    ('Not_Graduated','Not_Graduated')
)
SELFEMPLOYED_CHOICES=(
    ('Yes','Yes'),  
    ('No','No')  
)
PROPERTY_CHOICES=(
    ('Rural','Rural'),
    ('Urban','Urban'),
    ('Semiurban','Semiurban')
)
class approvals(models.Model):
    first_name               =models.CharField(max_length=20)
    last_name                =models.CharField(max_length=20)
    dependants               =models.IntegerField(default=0)
    applicantincome          =models.IntegerField(default=0)
    coapplicantincome        =models.IntegerField(default=0)
    loanamt                  =models.IntegerField(default=0)
    loanterm                 =models.IntegerField(default=0)
    credithistory            =models.IntegerField(default=0)
    gender                   =models.CharField(max_length=20,choices=GENDER_CHOICES)
    married                  =models.CharField(max_length=20,choices=MARRIED_CHOICES)
    graduatededucation       =models.CharField(max_length=20,choices=GRADUATED_CHOICES)
    selfemployed             =models.CharField(max_length=20,choices=SELFEMPLOYED_CHOICES)
    area                     =models.CharField(max_length=20,choices=PROPERTY_CHOICES)

    def __str__(self):
        return self.first_name

