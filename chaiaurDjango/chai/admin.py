from django.contrib import admin

from .models import chaiVariety, ChaiReview, Store, ChaiCertificate

# Register your models here.
# Inline class for ChaiReview
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2  # Display 2 empty forms for new reviews

class ChaiVarietyInline(admin.TabularInline):  # Or use admin.StackedInline
    model = Store.chai_varieties.through  # Through table for ManyToMany relationship
    extra = 1  # Number of empty forms to display for adding new varieties


# Admin class for chaiVariety
class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')  # Fields to display in the admin list view
    inlines = [ChaiReviewInline]  # Attach ChaiReviewInline to chaiVariety


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')  # Fields to display in the list view
    inlines = [ChaiVarietyInline]  # Attach the inline class
    filter_horizontal = ('chai_varieties',)  # Optional: For a many-to-many widget


# Admin class for ChaiCertificate
class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number')  # Fields to display in the admin list view

admin.site.register(chaiVariety, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)

#  we can attatch any model through admin .

