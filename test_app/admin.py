from django.contrib import admin
from test_app.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Image)
admin.site.register(Promotion)

