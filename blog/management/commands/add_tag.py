from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

from blog.models import Tag

BASE_DIR = str(Path(__file__).resolve().parent.parent.parent.parent)+'/import_files/'
class Command(BaseCommand):
    help = 'Add a tag to'
    def add_arguments(self, parser):
        parser.add_argument('filename', nargs='+', type=str)

    def handle(self, *args, **options):
        with open(BASE_DIR+options['filename'][0]) as file:
            content = file.readlines()
            for tag in content:
                Tag.objects.create(name=tag)

        self.stdout.write(
            self.style.SUCCESS('Successfully')
        )
