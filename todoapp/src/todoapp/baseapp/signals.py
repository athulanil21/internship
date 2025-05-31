from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver, Signal
from django.http import HttpResponse
from .models import Book

# Custom Signal (declare a signal)
book_reviewed = Signal(providing_args=["instance", "reviewer"])


# pre_save signal
@receiver(pre_save, sender=Book)
def before_book_saved(sender, instance, **kwargs):
    print(f"[pre_save] Book '{instance.title}' is about to be saved.")


# post_save signal
@receiver(post_save, sender=Book)
def after_book_saved(sender, instance, created, **kwargs):
    if created:
        print(f"[post_save] New book created: '{instance.title}'")
    else:
        print(f"[post_save] Book updated: '{instance.title}'")


# pre_delete signal
@receiver(pre_delete, sender=Book)
def before_book_deleted(sender, instance, **kwargs):
    print(f"[pre_delete] Book '{instance.title}' is about to be deleted.")


# post_delete signal
@receiver(post_delete, sender=Book)
def after_book_deleted(sender, instance, **kwargs):
    print(f"[post_delete] Book '{instance.title}' has been deleted.")


# custom signal receiver
@receiver(book_reviewed)
def handle_book_review(sender, instance, reviewer, **kwargs):
    print(f"[custom signal] Book '{instance.title}' was reviewed by {reviewer}.")


def review_book(request, book_id):
    book = Book.objects.get(id=book_id)
    reviewer = request.user.username
    book_reviewed.send(sender=Book, instance=book, reviewer=reviewer)
    return HttpResponse(f"Book '{book.title}' reviewed by {reviewer}")


# Config
def ready(self):
    import baseapp.signals  # replace with your app name
