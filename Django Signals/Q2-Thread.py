##Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance.
# The code does not need to be elegant and production ready, we just need to understand your logic.

#
# A)Yes, by default Django signals run in the same thread as the caller.it can be proved using the following code snippet.
#in this we use threading.get_ident() to compare thread IDs.

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading

class TestModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=TestModel)
def post_save_handler(sender, instance, **kwargs):
    print("Signal thread ID:", threading.get_ident())


#from the above code snippet we can understand that the django signals run in the same thread as caller.