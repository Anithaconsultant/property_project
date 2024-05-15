import datetime
from django.db import models

# Create your models here.
class property(models.Model):
    class Meta:
        db_table = "property"
    propnumber = models.CharField(unique=True,max_length=120, blank = False,null = False,primary_key = True)
    OwnerName=models.CharField(max_length=120, blank = False,null = False)
    Village=models.CharField(max_length=120, blank = False,null = False)
    District=models.CharField(max_length=120,  blank = True,null = True)
    Taluk=models.CharField(max_length=120, blank = True,null = True)
    City=models.CharField(max_length=120, blank = False,null = False)
    State=models.CharField(max_length=120, blank = False,null = False)
    Location=models.CharField(max_length=120, blank = False,null = False)
    Size=models.CharField(max_length=120,choices=[('acres', 'Acres'), ('sqft', 'Sq.ft'), ('cents', 'Cents')])
    Bookvalue=models.CharField(blank = False,null = False,max_length=120,)
    guidelinevalue=models.CharField(max_length=120,blank = False,null = False)
    mortagage=models.CharField(max_length=120, choices=[('yes', 'Yes'), ('no', 'No')])
    assetcategory=models.CharField(max_length=120,choices=[('land', 'Land'), ('leasehold', 'Lease hold land'), ('building', 'Building'), ('landbuilding', 'Land and Building'), ('factory', 'Factory Building'), ('agriland', 'Agricultural Land'), ('commercial', 'Commercial Building'), ('resident', 'Residential Building'), ('other', 'Other Asset')])
    approvedplan=models.CharField(max_length=120, choices=[('yes', 'Yes'), ('no', 'No')])
    registrationdate=models.DateField(default=datetime.date.today)
    disposaldate=models.DateField(default=datetime.date.today)
    documentloc=models.CharField(max_length=120)
    description=models.CharField(max_length=120)
    
class propertyDocument(models.Model):
    class Meta:
        db_table = "document"    
    propnumber=models.ForeignKey(property, on_delete=models.CASCADE)
    Saledeed = models.FileField(upload_to='documents/',null=True,blank=True,max_length=1000)
    Patta = models.FileField(upload_to='documents/',null=True,blank=True,max_length= 1000)
    Taxpayments = models.FileField(upload_to='documents/',null=True,blank=True,max_length= 1000)
    Fieldmeasurement = models.FileField(upload_to='documents/',null=True,blank=True,max_length= 1000)
    Adangal = models.FileField(upload_to='documents/',null=True,blank=True,max_length= 1000)
    Encumbrance = models.FileField(upload_to='documents/',null=True,blank=True,max_length= 1000)
    Approvals = models.FileField(upload_to='documents/',null=True,blank=True,max_length= 1000)
    EB = models.FileField(upload_to='documents/',null=True,blank=True,max_length= 1000)
    Parent = models.FileField(upload_to='documents/',null=True,blank=True,max_length= 1000)
    Legal = models.FileField(upload_to='documents/',null=True,blank=True,max_length= 1000)
    Mortgage = models.FileField(upload_to='documents/',null=True,blank=True,max_length= 1000)
    Poweratorny = models.FileField(upload_to='documents/',null=True,blank=True,max_length= 1000)
    FormRegister = models.FileField(upload_to='documents/',null=True,blank=True,max_length= 1000)
    Revenue = models.FileField(upload_to='documents/',null=True,blank=True,max_length= 1000)
    Miscellaneous = models.FileField(upload_to='documents/',null=True,blank=True,max_length= 1000)
   