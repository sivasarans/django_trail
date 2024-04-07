from django.test import TestCase
from django.contrib.auth.models import User
from .models import Supplier, Product, Tag, UserProfile, Article

class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.supplier = Supplier.objects.create(name="ABC Company")
        self.tag1 = Tag.objects.create(name="Technology")
        self.tag2 = Tag.objects.create(name="Science")

    def test_product_with_supplier(self):
        product = Product.objects.create(title="Product A", supplier=self.supplier)
        self.assertEqual(product.supplier, self.supplier)

    def test_article_with_tags(self):
        article = Article.objects.create(title="New Tech Article", content="...")
        article.tags.add(self.tag1, self.tag2)
        self.assertIn(self.tag1, article.tags.all())
        self.assertIn(self.tag2, article.tags.all())

    def test_userprofile_creation(self):
        profile = UserProfile.objects.create(user=self.user, bio="Test bio")
        self.assertEqual(profile.user, self.user)

    def test_article_with_user(self):
        article = Article.objects.create(title="New Article", content="...")
        article.author = self.user
        self.assertEqual(article.author, self.user)
