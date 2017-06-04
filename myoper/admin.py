from django.contrib import admin
from myoper.models import *
# Register your models here.
class T_USERAdmin(admin.ModelAdmin):
    list_display = ('user_id','user_name','IsStatus')
    list_per_page=10
admin.site.register(T_USER,T_USERAdmin)

class T_MODELAdmin(admin.ModelAdmin):
    list_display = ('model_name',)
    list_per_page=10
admin.site.register(T_MODEL,T_MODELAdmin)

class T_TYPEAdmin(admin.ModelAdmin):
    list_display = ('type_name',)
    list_per_page=10
admin.site.register(T_TYPE,T_TYPEAdmin)

class T_SUPPLIERAdmin(admin.ModelAdmin):
    list_display = ('supplier_name','supplier_phone','supplier_email','supplier_brand')
    list_per_page=10
admin.site.register(T_SUPPLIER,T_SUPPLIERAdmin)

class T_BRANDAdmin(admin.ModelAdmin):
    list_display = ('brand_name',)
    list_per_page=10
admin.site.register(T_BRAND,T_BRANDAdmin)

class T_COMMISIONAdmin(admin.ModelAdmin):
    list_display = ('commision_name','showSum')
    list_per_page=10
admin.site.register(T_COMMISION,T_COMMISIONAdmin)
class T_SALESPERSONAdmin(admin.ModelAdmin):
    list_display = ('sales_name','sales_phone','sales_commision')
    list_per_page=10
admin.site.register(T_SALESPERSON,T_SALESPERSONAdmin)

class T_WAREHOUSEAdmin(admin.ModelAdmin):
    list_display = ('ware_name','ware_phone','ware_addr')
    list_per_page=10
admin.site.register(T_WAREHOUSE,T_WAREHOUSEAdmin)