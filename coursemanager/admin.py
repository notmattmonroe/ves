from django.contrib import admin
from .models import Course, Category, Session

class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_name", "course_instructor", "category_id", "isActive",)
    list_editable = ("course_instructor", "isActive",)
    prepopulated_fields = {"course_slug": ("session_id","course_name",)}
    fieldsets = [
        (None,               {'fields': ['session_id','course_name', 'course_slug', 'course_instructor', 'category_id', 'course_description', 'course_image']}),
        ('Date information', {'fields': ['course_start_time', 'course_end_time', 'course_days_of_week', 'course_all_day', 'course_recurring', 'custom_start_date', 'custom_end_date', 'dropins', 'dropin_price', 'is_workshop', 'publish_date', 'isActive']}),
        ('Logistics', {'fields': ['course_private', 'course_spaces', 'course_price', 'location', 'course_ticket_link']}),
    ]

admin.site.register(Course, CourseAdmin)
admin.site.register(Category)
admin.site.register(Session)




