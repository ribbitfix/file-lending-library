from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    friends = models.ManyToManyField('self', blank=True)
    
    def __unicode__(self):
        return self.user.username
    
    def befriend(self, friend):
        #add friend to self.friends
        pass
    
class FileObject(models.Model):
    owner = models.ForeignKey(User, related_name='owner')
    holder = models.ForeignKey(User, related_name='holder')
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.title
    
    def check_in(self):
        #self.holder = self.owner, or null?
        pass
        
    def check_out(self, friend):
        #self.holder = friend
        pass
        
    def status(self):
        #return "available" or "checked out to so-and-so"
        pass
    
