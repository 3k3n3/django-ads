from ads.views import AdImpressionView, AdClickView
from django.urls import path

app_name = 'ads'
urlpatterns = [
    path('<int:pk>/', AdClickView.as_view(), name='ad-click'),
    path('get-ads-by-zones/', AdImpressionView.as_view(), name='ad-impression'),
]
