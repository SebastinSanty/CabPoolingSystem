from django.contrib import admin

# Register your models here.
from .models import SignUp
from .forms import SignUpModelForm
class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__str__","full_name","timestamp"]
	form = SignUpModelForm
#	class Meta:
#		model = SignUp
admin.site.register(SignUp, SignUpAdmin)