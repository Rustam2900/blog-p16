from django.db import models


class TagCustumManager(models.Manager):
    def is_deleted_false(self):
        return self.get_queryset().filter(is_deleted=False)

    def is_deleted_true(self):
        return self.get_queryset().filter(is_deleted=True)