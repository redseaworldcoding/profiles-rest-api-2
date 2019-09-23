from django.contrib import admin

from profiles_api import models  # imoorting our model from the profiles_api model

# Register your models here.

# Next, we register our model:
admin.site.register(models.UserProfile)  # WE are adding our User Profile model with the admin sqlite3
