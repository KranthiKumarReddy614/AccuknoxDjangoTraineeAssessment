##
# Question - 1 : By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. 
# The code does not need to be elegant and production ready, we just need to understand your logic.

#
# A)Yes Django Signals executes Synchronously by default That means the signal receiver function will block the caller until it finishes executing.
# this can be proved using time.sleep() method this method can be used in below code snippet as follows

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time

class TestModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=TestModel)
def post_save_handler(sender, instance, **kwargs):
    print("Signal started")
    time.sleep(5)
    print("Signal finished")

##from the above code snippet we can understand that django signals are executing synchronously and it will block signal execution.
#it will wait for the signal to get finished.

