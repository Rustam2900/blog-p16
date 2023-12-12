from django.core.management.base import BaseCommand, CommandError

from blog.models import Tag


class Command(BaseCommand):
    def handle(self, *args, **options):

        tags = Tag.objects.is_deleted_false()
        for tag in tags:
            tag.is_deleted = True
            tag.save()
        self.stdout.write(
            self.style.SUCCESS('Successfully all tags is deleted')
        )
