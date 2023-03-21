from django.db.models import QuerySet


class CustomBaseQuerySet(QuerySet):
    def get_oldest_task(self):
        if hasattr(self.model, "created_at"):
            return self.order_by('created_at').first()
        return self.first(self)
