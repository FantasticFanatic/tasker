from django.test import TestCase
from .models import Task


class HomePageTest(TestCase):

    def test_uses_task_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_see_tasks(self):
        Task.objects.create(title="Task Item 1")
        Task.objects.create(title="Task Item 2")
        response = self.client.get('/')
        self.assertIn('Task Item 1', response.content.decode())
        self.assertIn('Task Item 2', response.content.decode())


class AddTaskPageTest(TestCase):
    def test_uses_add_task_template(self):
        response = self.client.get('/tasks/add/')
        self.assertTemplateUsed(response, 'add_task.html')

    def test_redirects_to_home_after_post(self):
        response = self.client.post('/tasks/add/', data={'task_title': 'New Task'})
        self.assertRedirects(response, '/')

    def test_saves_new_task_on_POST(self):
        response = self.client.post('/tasks/add/', data={'task_title': 'New Task'})
        self.assertEqual(Task.objects.count(), 1)
        new_task = Task.objects.first()
        self.assertEqual(new_task.title, "New Task")