from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import UserAccount
from core.tasks import MakeFaceEncoding


@receiver(post_save, sender=UserAccount)
def register_user_face_encoding(sender, instance, created, **kwargs):
    print("Registering user face encoding")

    print("UserAccount created")
    MakeFaceEncoding.delay()
    print("MakeFaceEncoding task scheduled")

# post_save.connect(MakeFaceEncoding, sender=User)
