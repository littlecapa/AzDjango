from django.contrib import admin
from .models import UserStory, EstimateChoice, Estimate

class UserStoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserStory, UserStoryAdmin)

class EstimateChoiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(EstimateChoice, EstimateChoiceAdmin)

class EstimateAdmin(admin.ModelAdmin):
    pass

admin.site.register(Estimate, EstimateAdmin)