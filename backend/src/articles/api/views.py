from rest_framework import viewsets
from articles.models import Article, Comment, Subscribers

from rest_framework.permissions import IsAuthenticated

from .serializer import ArticleSerializer, CommentsSerializer, SubscriberSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentsSerializer
    queryset = Comment.objects.all()

class SubscriberViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SubscriberSerializer
    queryset = Subscribers.objects.all()