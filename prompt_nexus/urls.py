from django.urls import path, include

urlpatterns = [
    # all prompt related routes go here
    path('prompts/', include('prompts.urls')),
]
