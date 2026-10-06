from django.test import TestCase
from django.urls import reverse
from .models import Task


class TaskAppTests(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title='Test Django task', priority='High')

    def test_task_list_loads(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Django task')

    def test_create_task(self):
        response = self.client.post(reverse('task_create'), {
            'title': 'New assignment',
            'description': 'Finish it',
            'priority': 'Medium',
            'due_date': '',
        })
        self.assertRedirects(response, reverse('task_list'))
        self.assertTrue(Task.objects.filter(title='New assignment').exists())

    def test_toggle_task(self):
        self.client.post(reverse('task_toggle', args=[self.task.pk]))
        self.task.refresh_from_db()
        self.assertTrue(self.task.completed)

    def test_delete_task(self):
        self.client.post(reverse('task_delete', args=[self.task.pk]))
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())
