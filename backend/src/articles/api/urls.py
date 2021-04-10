from articles.api.views import ArticleViewSet, CommentViewSet, SubscriberViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='articles')
router.register(r'comments', CommentViewSet, basename='comments')
router.register(r'subscribers', SubscriberViewSet, basename='subscribers')
urlpatterns = router.urls