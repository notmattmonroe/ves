from django.db import models
import datetime
import recurrence.fields

DOW = (('1', 'Sunday'),
      ('2', 'Monday'),
      ('3', 'Tuesday'),
      ('4', 'Wednesday'),
      ('5', 'Thursday'),
      ('6', 'Friday'),
      ('7', 'Saturday'))

class Course(models.Model):
    course_name = models.CharField(blank=False, null=False, max_length=250)
    course_slug = models.SlugField(unique=True)
    course_description = models.TextField(blank=False, null=False)
    course_start_time = models.TimeField(blank=False, null=False)
    course_end_time = models.TimeField(blank=False, null=False)
    course_days_of_week = models.CharField(max_length=1, choices=DOW, blank=True)
    course_all_day = models.BooleanField(default=False)
    custom_start_date = models.DateField(blank=True, null=True)
    custom_end_date = models.DateField(blank=True, null=True)
    session_id = models.ForeignKey('Session')
    course_private = models.BooleanField(default=False)
    course_spaces = models.IntegerField(default=15)
    course_date_created = models.DateTimeField(blank=True, null=False, auto_now=True)
    course_date_modified = models.DateTimeField(blank=True, null=False, auto_now=True)
    course_instructor = models.ForeignKey('auth.User')
    course_image = models.ImageField(upload_to='course_images')
    course_price = models.IntegerField(blank=True, null=True, default=160)
    location        = models.ForeignKey('location.Location', null=True)
    category_id = models.ForeignKey('Category')
    course_recurring  = recurrence.fields.RecurrenceField(null=True)
    is_workshop = models.BooleanField(default=False)
    dropins = models.BooleanField(default=True)
    dropin_price = models.IntegerField(default=20)
    course_ticket_link = models.CharField(blank=True, max_length=250)
    publish_date = models.DateField(blank=False, default=datetime.datetime.now)
    isActive = models.BooleanField(default=True)
    
    def __str__(self):
        return self.course_name

class CourseImage(models.Model):
    course_image = models.ImageField()
    
    def _str__(self):
        return self.courseimage_id

class Session(models.Model):
    session_name = models.CharField(blank=False, null=False, max_length=250)
    session_start_date = models.DateField(blank=False, null=False)
    session_end_date = models.DateField(blank=False, null=False)
    session_notes = models.TextField(blank=True)

    def __str__(self):
        return self.session_name

class Category(models.Model):
    category_name = models.CharField(blank=False, null=False, max_length=250)
    category_slug = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.category_name
        