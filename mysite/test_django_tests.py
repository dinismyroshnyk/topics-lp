# test_django_tests.py

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from topics.models import Topic, Comment

class TopicTests(TestCase):
    def setUp(self):
        # Buscar usuário existente ou criar um novo se não existir
        self.user = User.objects.get_or_create(
            username='admin',  # Coloque aqui o username do seu usuário
            defaults={
                'password': 'admin',  # Coloque aqui a senha do seu usuário
            }
        )[0]

        # Criar um tópico de teste
        self.topic = Topic.objects.create(
            title='Test Topic',
            description='Test Description',
            author=self.user
        )

        # Criar um comentário de teste
        self.comment = Comment.objects.create(
            topic=self.topic,
            text='Test Comment',
            author=self.user
        )

        # Configurar o cliente para fazer login
        self.client = Client()
        self.client.login(username='admin', password='admin')

    def test_topic_list(self):
        """Test if the topic list page is displayed correctly"""
        response = self.client.get(reverse('topic_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.topic.title)
        self.assertContains(response, self.topic.description)

    def test_topic_detail(self):
        """Test if the topic detail page is displayed correctly"""
        response = self.client.get(reverse('topic_detail', args=[self.topic.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.topic.title)
        self.assertContains(response, self.topic.description)
        self.assertContains(response, self.comment.text)

    def test_create_topic(self):
        """Test if a user can create a new topic"""
        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('create_topic'), {
            'title': 'New Topic',
            'description': 'New Description'
        })
        self.assertEqual(response.status_code, 302)  # Verifica se o redirecionamento ocorreu
        self.assertTrue(Topic.objects.filter(title='New Topic').exists())

    def test_add_comment(self):
        """Test if a user can add a comment to a topic"""
        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('add_comment', args=[self.topic.id]), {
            'text': 'Another Test Comment'
        })
        self.assertEqual(response.status_code, 302)  # Verifica se o redirecionamento ocorreu
        self.assertTrue(Comment.objects.filter(text='Another Test Comment').exists())

    def test_edit_topic(self):
        """Test if a user can edit a topic"""
        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('edit_topic', args=[self.topic.id]), {
            'title': 'Updated Topic',
            'description': 'Updated Description'
        })
        self.assertEqual(response.status_code, 302)  # Verifica se o redirecionamento ocorreu
        self.topic.refresh_from_db()
        self.assertEqual(self.topic.title, 'Updated Topic')
        self.assertEqual(self.topic.description, 'Updated Description')

    def test_delete_topic(self):
        """Test if a user can delete a topic"""
        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('delete_topic', args=[self.topic.id]))
        self.assertEqual(response.status_code, 302)  # Verifica se o redirecionamento ocorreu
        self.assertFalse(Topic.objects.filter(id=self.topic.id).exists())

    def test_delete_comment(self):
        """Test if a user can delete a comment"""
        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('delete_comment', args=[self.comment.id]))
        self.assertEqual(response.status_code, 302)  # Verifica se o redirecionamento ocorreu
        self.assertFalse(Comment.objects.filter(id=self.comment.id).exists())