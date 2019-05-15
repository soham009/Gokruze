from django.db import models

# Create your models here.
class Leads(models.Model):
    def number():
        no = Leads.objects.count()
        if no == None:
            return 1
        else:
            return no + 1

    LEAD_STATUS = (('Interested','Interested'),
                   ('Undecided','Undecided'),
                   ('Uncontacted','Uncontacted'),
                   ('Converted','Converted'))

    PICK_LOCATION = (('Virar','Virar'), 
('Nallasopara','Nallasopara'), 
('Vasai','Vasai'),
('Naigaon','Naigaon'), 
('Bhayander','Bhayander'), 
('Mira Road','Mira Road'), 
('Dahisar','Dahisar'), 
('Borivali','Borivali'), 
('Kandivali','Kandivali'), 
('Malad','Malad'), 
('Goregaon','Goregaon'), 
('Ram Mandir','Ram Mandir'), 
('Jogeshwari','Jogeshwari'), 
('Andheri','Andheri'), 
('Vile Parle','Vile Parle'), 
('Santacruz','Santacruz'), 
('Khar Rd','Khar Rd'), 
('Bandra','Bandra'), 
('Mahim','Mahim'), 
('Matunga','Matunga'), 
('Dadar','Dadar'), 
('Prabhadevi','Prabhadevi'),
('Lower Parel','Lower Parel'), 
('Mahalaxmi','Mahalaxmi'), 
('Mumbai Central','Mumbai Central'), 
('Grant Rd','Grant Rd'), 
('Charni Rd','Charni Rd'),
('Marine Lines','Marine Lines'), 
('Churchgate','Churchgate'), 
('CST - Fort','CST - Fort'), 
('Masjid Bunder','Masjid Bunder'), 
('Sandhurst Rd','Sandhurst Rd'), 
('Byculla','Byculla'), 
('Chinchpokli','Chinchpokli'), 
('Currey Rd','Currey Rd'), 
('Parel','Parel'), 
('Sion','Sion'), 
('Kurla','Kurla'), 
('Vidya Vihar','Vidya Vihar'), 
('Ghatkopar','Ghatkopar'), 
('Vikhroli','Vikhroli'), 
('Kangur Marg','Kangur Marg'), 
('Bhandup','Bhandup'), 
('Nahur','Nahur'),
)

    SHIFT_TIME = (
     ("6:00 AM", "6:00 AM"), ("6:15 AM", "6:15 AM"), ("6:30 AM", "6:30 AM"), ("6:45 AM", "6:45 AM"),
    ("7:00 AM", "7:00 AM"), ("7:15 AM", "7:15 AM"), ("7:30 AM", "7:30 AM"), ("7:45 AM", "7:45 AM"),
    ("8:00 AM", "8:00 AM"), ("8:15 AM", "8:15 AM"), ("8:30 AM", "8:30 AM"), ("8:45 AM", "8:45 AM"),
    ("9:00 AM", "9:00 AM"), ("9:15 AM", "9:15 AM"), ("9:30 AM", "9:30 AM"), ("9:45 AM", "9:45 AM"),
    ("10:00 AM", "10:00 AM"), ("10:15 AM", "10:15 AM"), ("10:30 AM", "10:30 AM"), ("10:45 AM", "10:45 AM"),
    ("11:00 AM", "11:00 AM"), ("11:15 AM", "11:15 AM"), ("11:30 AM", "11:30 AM"), ("11:45 AM", "11:45 AM"),
    ("12:00 PM", "12:00 PM"), ("12:15 PM", "12:15 PM"), ("12:30 PM", "12:30 PM"), ("12:45 PM", "12:45 PM"),
    ("01:00 PM", "01:00 PM"), ("01:15 PM", "01:15 PM"), ("01:30 PM", "01:30 PM"), ("01:45 PM", "01:45 PM"),
    ("02:00 PM", "02:00 PM"), ("02:15 PM", "02:15 PM"), ("02:30 PM", "02:30 PM"), ("02:45 PM", "02:45 PM"),
    ("03:00 PM", "03:00 PM"), ("03:15 PM", "03:15 PM"), ("03:30 PM", "03:30 PM"), ("03:45 PM", "03:45 PM"),
    ("04:00 PM", "04:00 PM"), ("04:15 PM", "04:15 PM"), ("04:30 PM", "04:30 PM"), ("04:45 PM", "04:45 PM"),
    ("05:00 PM", "05:00 PM"), ("05:15 PM", "05:15 PM"), ("05:30 PM", "05:30 PM"), ("05:45 PM", "05:45 PM"),
    ("06:00 PM", "06:00 PM"), ("06:15 PM", "06:15 PM"), ("06:30 PM", "06:30 PM"), ("06:45 PM", "06:45 PM"),
    ("07:00 PM", "07:00 PM"), ("7:15 PM", "7:15 PM"), ("7:30 PM", "7:30 PM"), ("7:45 PM", "7:45 PM"),
    ("08:00 PM", "08:00 PM"), ("08:15 PM", "08:15 PM"), ("08:30 PM", "08:30 PM"), ("08:45 PM", "08:45 PM"),
    ("09:00 PM", "09:00 PM"), ("09:15 PM", "09:15 PM"), ("09:30 PM", "09:30 PM"), ("09:45 PM", "09:45 PM"),
    ("10:00 PM", "10:00 PM"), ("10:15 PM", "10:15 PM"), ("10:30 PM", "10:30 PM"), ("10:45 PM", "10:45 PM"),
    ("11:00 PM", "11:00 PM"), ("11:15 PM", "11:15 PM"), ("11:30 PM", "11:30 PM"), ("11:45 PM", "11:45 PM"),
    ("12:00 PM", "12:00 PM"), ("12:15 PM", "12:15 PM"), ("12:30 PM", "12:30 PM"), ("12:45 PM", "12:45 PM"),
    ("01:00 PM", "01:00 PM"), ("01:15 PM", "01:15 PM"), ("01:30 PM", "01:30 PM"), ("01:45 PM", "01:45 AM"),
    )
    Lead_No = models.IntegerField(max_length=6, unique=True, default=number)
    Date_of_Lead = models.DateField()
    Full_Name = models.CharField(max_length=264)
    Email = models.EmailField(max_length = 75)
    Mobile = models.CharField(max_length=264)
    Company_Name = models.CharField(max_length=264)
    Shift_Start = models.CharField(choices=SHIFT_TIME, default="6:00 AM",max_length=100)
    Shift_End = models.CharField(choices=SHIFT_TIME, default="6:00 AM",max_length=100)
    Pick_Up_Location = models.CharField(choices=PICK_LOCATION,max_length=100)
    Pick_Up_Land_Mark = models.CharField(max_length=264)
    Drop_Location= models.CharField(choices=PICK_LOCATION,max_length=100)
    Drop_Land_Mark = models.CharField(max_length=264)
    Remark = models.CharField(max_length=264)
    Lead_Status = models.CharField(choices=LEAD_STATUS,max_length=264)

    def __str__(self):
        return self.Full_Name

    class Meta:
        verbose_name_plural = "Fill Lead Tracking Form"
        verbose_name = "Lead"