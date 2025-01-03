# from django.urls import path
# from . import views

# urlpatterns = [
#     path("", views.all_chai, name='all_chai'),  # Home page for chai
#     path("<int:chai_id>/", views.chai_details, name='chai_details'),  # Chai details by ID
#     path("chai_stores/", views.chai_store_view, name='chai_stores'),  # Chai stores page
# ]

from django.urls import path
from . import views

# localhost :8000/chai
# localhost :8000/chai/order
urlpatterns = [
    path("", views.all_chai, name='all_chai'),
    path("<int:chai_id>/", views.chai_details, name='chai_details'),
    path('chai_stores/', views.chai_store_view, name='chai_stores'),


    # path("order/", views.order, name='order'),

]
# how to pass controls ::
#  bydefault we have integer key 


