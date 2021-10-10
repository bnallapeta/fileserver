from django.urls import path
from fileops import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    path('api/files/wc/', views.FilesWordCount.as_view()),
    path('api/files/fw/', views.FilesFreqWordCount.as_view()),
    path('api/files/', views.FilesList.as_view()),
    path('api/files/<int:pk>/', views.FilesDetail.as_view()),    
]

urlpatterns = format_suffix_patterns(urlpatterns)
