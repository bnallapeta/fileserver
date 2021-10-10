from django.urls import path, include
from rest_framework.routers import DefaultRouter
from fileops import views
from rest_framework.urlpatterns import format_suffix_patterns

# from .views import FilesViewSet
# from .views import files_list

# router = DefaultRouter()
# router.register(r"files", FilesViewSet)

urlpatterns = [
    # path("api/", include(router.urls)),

    path('api/files/wc/', views.FilesWordCount.as_view()),
    path('api/files/fw/', views.FilesFreqWordCount.as_view()),
    path('api/files/', views.FilesList.as_view()),
    path('api/files/<int:pk>/', views.FilesDetail.as_view()),    
]

urlpatterns = format_suffix_patterns(urlpatterns)
