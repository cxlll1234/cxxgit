#coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class T_USER(models.Model):
    user_id = models.CharField(max_length=8,primary_key=True,verbose_name='登陆ID')
    user_name = models.CharField(max_length=20,verbose_name='用户名')
    user_password= models.CharField(max_length=100,verbose_name='用户密码')
    user_status=models.CharField(max_length=1,verbose_name='用户状态',default='0')
    def __unicode__(self):
        return self.user_name
    class Meta:
        verbose_name_plural='用户表'
        verbose_name='用户表'
    def IsStatus(self):
        if self.user_status.strip() == '0':
            return '启用'
        else:
            return '禁用'
    IsStatus.short_description='用户状态'
class T_MODEL(models.Model):
    #model_id = models.CharField(max_length=8,primary_key=True,verbose_name='型号编号')
    model_name = models.CharField(max_length=20,verbose_name='型号名称')
    def __unicode__(self):
        return self.model_name
    class Meta:
        verbose_name_plural='型号管理'
        verbose_name='型号管理'
class T_TYPE(models.Model):
    #type_id = models.CharField(max_length=8,primary_key=True,verbose_name='类型编号')
    type_name = models.CharField(max_length=20,verbose_name='类型名称')
    def __unicode__(self):
        return self.type_name
    class Meta:
        verbose_name_plural='类型管理'
        verbose_name='类型管理'
class T_BRAND(models.Model):
    #brand_id = models.CharField(max_length=8,primary_key=True,verbose_name='品牌编号')
    brand_name = models.CharField(max_length=20,verbose_name='品牌名称')
    def __unicode__(self):
        return self.brand_name
    class Meta:
        verbose_name_plural='品牌管理'
        verbose_name='品牌管理'
class T_COMMISION(models.Model):
    #commision_id = models.CharField(max_length=8,primary_key=True,verbose_name='提成编号')
    commision_name = models.CharField(max_length=20,verbose_name='提成名称')
    commision_sum = models.FloatField(verbose_name='提成比例')
    def __unicode__(self):
        return self.commision_name
    def showSum(self):
        sum = self.commision_sum * 100
        sum = str('%.2f')%sum+'%'  #转换为有两位小数的浮点数
        return sum
    class Meta:
        verbose_name_plural='提成管理'
        verbose_name='提成管理'
    showSum.short_description='提成比例'
class T_SALESPERSON(models.Model):
    #sales_id = models.CharField(max_length=8,primary_key=True,verbose_name='营业员编号')
    sales_name = models.CharField(max_length=20,verbose_name='营业员姓名')
    sales_phone = models.CharField(max_length=8,verbose_name='营业员电话')
    sales_commision = models.ForeignKey(T_COMMISION,on_delete=models.PROTECT,verbose_name='营业员提成')
    def __unicode__(self):
        return self.sales_name
    class Meta:
        verbose_name_plural='营业员管理'
        verbose_name='营业员管理'
class T_SUPPLIER(models.Model):
    #supplier_id = models.CharField(max_length=8,primary_key=True,verbose_name='供应商编号')
    supplier_name = models.CharField(max_length=20,verbose_name='供应商姓名')
    supplier_phone = models.CharField(max_length=40,verbose_name='供应商电话')
    supplier_email = models.EmailField(verbose_name='供应商电子邮件',null = True)
    supplier_brand = models.ForeignKey(T_BRAND,on_delete=models.PROTECT,verbose_name='供应商品牌')
    def __unicode__(self):
        return self.supplier_name
    class Meta:
        verbose_name_plural='供应商管理'
        verbose_name='供应商管理'
class T_CUSTOMER(models.Model):
    #customer_id = models.CharField(max_length=8,primary_key=True,verbose_name='客户编号')
    customer_name = models.CharField(max_length=20,verbose_name='客户姓名')
    customer_phone = models.CharField(max_length=40,verbose_name='客户电话')
    customer_addr = models.CharField(max_length=400,verbose_name='客户地址')
    customer_model = models.CharField(max_length=40,verbose_name='客户户型',null = True)
    def __unicode__(self):
        return self.customer_name
    class Meta:
       verbose_name_plural='客户管理'
       verbose_name='客户管理'
class T_WAREHOUSE(models.Model): #仓库
    ware_name = models.CharField(max_length=20,verbose_name='仓库名称')
    ware_phone = models.CharField(max_length=40,verbose_name='仓库电话')
    ware_addr = models.CharField(max_length=400,verbose_name='仓库地址')
    def __unicode__(self):
        return self.ware_name
    class Meta:
       verbose_name_plural='仓库管理'
       verbose_name='仓库管理'
    