from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.
class BlogTests(TestCase):
    
    #Creation of User
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
        username='test123', password='abc123')
        testuser1.save()
    
    #Creation of a post
        test_post = Post.objects.create(
        author=testuser1, title='Title', body='My message...')
        test_post.save()
    
    def test_blog(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'test123')
        self.assertEqual(title, 'Title')
        self.assertEqual(body, 'My message...')