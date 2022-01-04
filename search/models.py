# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TestData(models.Model):
    index = models.IntegerField(blank=True, null=False, primary_key=True)
    지역명 = models.TextField(blank=True, null=True)
    지역구명 = models.TextField(blank=True, null=True)
    의원명 = models.TextField(blank=True, null=True)
    정당명 = models.TextField(blank=True, null=True)
    정책제목 = models.TextField(blank=True, null=True)
    정책설명 = models.TextField(blank=True, null=True)
    정책배경및사례 = models.TextField(blank=True, null=True)
    기사 = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'test_data'
