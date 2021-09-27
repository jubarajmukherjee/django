from django.contrib import admin
#from .models import info

from .models import MyModel
 
@admin.register(MyModel)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
MyModel._meta.get_fields()]

#admin.site.register(info)
# Register your models here.
