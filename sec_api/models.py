from django.db import models

# Create your models here.

#We’re going to create our Note model, and then run our migrations, 
#which will set up our database with a notes table (with all the appropriate fields).
class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

#The next thing we want to do is add a __str__ method to the model. 
#This method defines what we get when we ask for a particular instance of a model.
#means that when we grab any Note model, we’ll get back only the title. This just keeps things clean. 
#(We will only be interacting with our models in this manner through the Python shell, 
#so it’s not super necessary, but good to be aware of). And now we will expand our __str__ to also include the body
def __str__(self):
    return '%s %s' % (self.title, self.body)

#Then we ran makemigrations and migrate which will set up database