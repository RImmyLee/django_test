# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ArticleData(models.Model):
    index = models.IntegerField(blank=False, null=False, primary_key=True)
    정책_index = models.IntegerField(blank=True, null=True)
    기사제목 = models.TextField(blank=True, null=True)
    기사요약 = models.TextField(blank=True, null=True)
    기사_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'article_data'


class PoliticData(models.Model):
    index = models.IntegerField(blank=False, null=False, primary_key=True)
    지역명 = models.TextField(blank=True, null=True)
    지역구명 = models.TextField(blank=True, null=True)
    의원명 = models.TextField(blank=True, null=True)
    정당명 = models.TextField(blank=True, null=True)
    정책제목 = models.TextField(blank=True, null=True)
    정책설명 = models.TextField(blank=True, null=True)
    정책배경_및_사례 = models.TextField(db_column='정책배경 및 사례', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    정책_index = models.IntegerField(blank=True, null=True)
    분류 = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'politic_data'