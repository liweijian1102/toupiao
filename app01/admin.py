from django.contrib import admin
from app01 import models

# Register your models here.
class vote(admin.ModelAdmin):
    list_display=('vote_title','vote_start','vote_end','vote_zuozhe',)
    list_filter=('created_at',)

        
    
admin.site.register(models.vote)
admin.site.register(models.vote_content)
admin.site.register(models.vote_result)
admin.site.register(models.vote_ip)


