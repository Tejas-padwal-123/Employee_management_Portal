from django.contrib import admin
from .models import Empployee, Role, Department
# Register your models here.

admin.site.register(Empployee)
admin.site.register(Role)
admin.site.register(Department)