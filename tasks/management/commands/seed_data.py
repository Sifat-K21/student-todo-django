from datetime import date, timedelta
from django.core.management.base import BaseCommand
from tasks.models import Task


class Command(BaseCommand):
    help = 'Create simple sample tasks for the classroom demonstration.'

    def handle(self, *args, **options):
        Task.objects.all().delete()
        today = date.today()
        sample_tasks = [
            ('Complete FDS assignment', 'Finish the Django project.', 'High', today + timedelta(days=2), False),
            ('Practice Django', 'Practice models and views.', 'Medium', today + timedelta(days=4), False),
            ('Submit lab record', 'Complete and submit the practical record.', 'Low', today + timedelta(days=6), True),
        ]
        for title, description, priority, due_date, completed in sample_tasks:
            Task.objects.create(
                title=title,
                description=description,
                priority=priority,
                due_date=due_date,
                completed=completed,
            )
        self.stdout.write(self.style.SUCCESS('3 sample tasks created.'))
