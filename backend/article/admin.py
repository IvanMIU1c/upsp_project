from django.contrib import admin

from .models import Group, Student,AccessPending, AccessData, AccessQR
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(AccessData)
admin.site.register(AccessPending)
admin.site.register(AccessQR)