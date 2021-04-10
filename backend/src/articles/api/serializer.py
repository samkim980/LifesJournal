from rest_framework import serializers
from articles.models import Article, Comment, Subscribers

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribers
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    # comments = CommentsSerializer(many = True)
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Article
        fields = ('id', 'title', 'article_image', 'description', 'content', 'created_on', 'author', 'comments')