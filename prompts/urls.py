from django.urls import path
from .views import prompts_handler, get_prompt_detail

urlpatterns = [
    path('', prompts_handler),
    path('<uuid:id>/', get_prompt_detail),
]