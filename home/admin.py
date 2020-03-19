from django.contrib import admin
from .models import Home,Welcome


# Register your models here.


class HomeAdmin(admin.ModelAdmin):

	list_display = ['title','publishing_date','slug']
	list_filter = ['publishing_date']
	search_fields = ['title','content']


	class Meta:
		model = Home 





admin.site.register(Home,HomeAdmin)
admin.site.register(Welcome)