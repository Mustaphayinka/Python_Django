# from django.urls import path
# from .views import article_list, article_detail
# # , article_create
# urlpatterns = [
#     path('article/', article_list),
#     path('detail/<int:pk>/', article_detail),
# ]


# Class based views
# Class based views
from django.urls import path, include
from .views import ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:id>/', ArticleDetails.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),

]