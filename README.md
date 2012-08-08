File Lending Library
====================
This is a far cry from a functional file lending library - just the first few halting steps toward creating one. After working my way through the Django tutorial and creating the "Web-poll" app described therein, I went through the tutorial again and created this, with guidance from Jeff and Chris. Process notes below.

### 8/30/11
Didn't really get this: https://docs.djangoproject.com/en/1.3/intro/tutorial02/#customize-the-admin-index-page

Or this: https://docs.djangoproject.com/en/1.3/intro/tutorial03/#write-views-that-actually-do-something

JEFF SEZ: "Ah. There's no template yet. First, create a directory, somewhere on your filesystem, whose contents Django can access. (Django runs as whatever user your server runs.) Don't put them under your document root, though. You probably shouldn't make them public, just for security's sake. Then edit TEMPLATE_DIRS in your settings.py to tell Django where it can find templates -- just as you did in the "Customize the admin look and feel" section of Tutorial 2."

###8/31
urls: u/username - if you're friends, you'll see their list of files; if not, a friend request button

### 9/1
Learned about how to do profile models here: 
- https://docs.djangoproject.com/en/1.3/topics/auth/#storing-additional-information-about-users
- http://www.djangobook.com/en/1.0/chapter12/#cn222
- http://www.turnkeylinux.org/blog/django-profile

DB migrations: When you add new fields to a table that already has data in it - allows you to update the table without losing data. Can't be performed by Django, but there's an app for it called South.

NEXT: https://docs.djangoproject.com/en/1.3/intro/tutorial01/#database-setup

Ran syncdb; got this message: django.core.exceptions.ImproperlyConfigured: Please fill out the database NAME in the settings module before using the database.

### 9/2
If I specify in settings.py where I want the db, then run syncdb, it works!

So I need to make three models:
- User: basic stuff like name, email, password
- UserProfile: app-specific stuff, i.e. friend relationships (assume symmetry?). This table will have a many-to-many relationship with itself.
- File: foreign key (to User, or UserProfile?), title, artist, is_available

NEXT: https://docs.djangoproject.com/en/1.3/intro/tutorial01/#activating-models

### 9/6
Jeff's replacement for Django's get_profile():
```python
from profiles.models import UserProfile

def get_profile(user):
    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=user)
        try:
            profile.set_default_values()
        except AttributeError: pass
    except UserProfile.MultipleObjectsReturned:
        profiles = UserProfile.objects.filter(user=user)
        profile = profiles[0]
        for profile in profiles[1:]:
            profile.delete()
    return profile
```
NEXT: https://docs.djangoproject.com/en/1.3/intro/tutorial01/#playing-with-the-api
- figure out how User and UserProfile interact
- where to put the above method?

### 9/7
NEXT: https://docs.djangoproject.com/en/1.3/intro/tutorial03/  (views!)

### 9/8
So I need to make these views:
- login/register
- profile home
	- display friends and files
	- allow user to update profile info, search/add friends, upload files
- friend profile: display files and friends
- basic (non-friend) profile: 
	- display basic info
	- befriend button
- file detail
	- display file info
	- allow check-out (also: place hold?)

### 9/9
There's a template decorator function to return just data instead of using Django's render_to_response() boilerplate. Jeff says to ask about this once I'm comfortable with the latter.

NEXT: https://docs.djangoproject.com/en/1.3/intro/tutorial03/#write-views-that-actually-do-something - spend some more time with this stuff.

### 9/12
QUESTION: How to eliminate redundancy b/t my_profile and friend_profile views?

### 9/13
ANSWER: The simple solution: take the redundant code and put it in a function that both views can call.
The fancy solution: decorators. Jeff recommends this for when I'm ready to level up:
http://charlesleifer.com/blog/django-patterns-view-decorators/

Two directories in the root dir for the site:
- static: jpgs, CSS, JS - dev stuff. Users don't alter the contents of static.
- media: files uploaded by users.

Renamed File to FileObject; checked project into git.

QUESTION: why can't profiles.tools be found? (views.py import)

### 9/14
tutorial 3: 404 stuff, simplified URLconfs

NEXT: fix admin URLconfs: https://docs.djangoproject.com/en/1.3/intro/tutorial03/#simplifying-the-urlconfs

### 9/15
admin works fine, actually.

NEXT: Create a form to update user profile info.
https://docs.djangoproject.com/en/1.3/intro/tutorial04/

### 9/21
NEXT: figure out HttpResponseRedirect(reverse()).

### 9/23
Django forms:
```python
class UserEmailForm(forms.Form):
	email = Forms.EMailField(required=True)
	def save(self, user):
		user.email = self.cleaned_data['email']
```
In view:
```python
if request.method == 'POST':
	form = UserEmailForm(request.POST) # This is the data to be saved, in dict form
	if form.is_valid():
		form.save(request.user)
	else:
		print form.errors
```
NEXT: Still not saving to the DB - figure out why.


