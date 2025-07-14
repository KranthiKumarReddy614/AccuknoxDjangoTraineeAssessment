##Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance.
# The code does not need to be elegant and production ready, we just need to understand your logic.

#A)Yes, by default they run in the same transaction. it can be proved using the following code snippet.
# this code sbnippet is ued to to simulate a failure in the signal that should rollback DB Transaction.
# if the signal raises an exception the object won't get saved

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class TestModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=TestModel)
def post_save_handler(sender, instance, **kwargs):
    print("Raising exception to test transaction rollback")
    raise Exception("Signal failure")


#From the code snippet we can understand once the code gets executed it will check for the signal.
# the signal rollbacks the db operation this and this proves the django signals participate in the same DB transaction.


