from .models import Category, Tag


class Base:
    def category(self):
        return Category.objects.all()

    def tag(self):
        return Tag.objects.all()
