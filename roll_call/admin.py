from django.contrib import admin
from roll_call.models import set_number,set_time,attendence

# Register your models here.

class attendenceAdmin(admin.ModelAdmin):
	list_display=("student","attend","date")
	list_filter=('date',)
	search_field=['student','date']

class set_timeAdmin(admin.ModelAdmin):
		list_display=("start","end")
		list_filter=('end',)

class set_numberAdmin(admin.ModelAdmin):
	list_display=("number","created_date")
	list_filter=('created_date',)

admin.site.register(set_number,set_numberAdmin)
admin.site.register(set_time,set_timeAdmin)
admin.site.register(attendence,attendenceAdmin)
