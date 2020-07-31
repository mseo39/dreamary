from django.contrib import admin

# Register your models here.
from myapp.models import Deginer
admin.site.register(Deginer) #admin에 model이 생긴 것을 알려줘야 사이트에서 관리할 수 있음