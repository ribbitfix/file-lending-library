from django.http import HttpResponse
from django.shortcuts import render_to_response
from lendinglibapp.models import UserProfile, FileObject
from lib.decorators import template
#from profiles.tools import get_profile

def get_profile_details(user_id):
    user = UserProfile.objects.get(pk=user_id)
    friend_list = UserProfile.objects.filter(friends=user_id)
    file_list = FileObject.objects.filter(owner=user_id)
    return (user, friend_list, file_list)

@template('lendinglib/index.html')
def index(request):
    '''home page: login/register'''
    user_list = UserProfile.objects.all()
    return {'user_list': user_list}
    
def my_profile(request, user_id):
    '''user can view and change their profile details, friends, and files'''
    user, friend_list, file_list = get_profile_details(user_id)
    return render_to_response('lendinglib/my_profile.html', {'user': user,
        'friend_list': friend_list, 'file_list': file_list})

def friend_profile(request, user_id):
    '''private profile, available to friends only'''
    friend, friend_list, file_list = get_profile_details(user_id)
    return render_to_response('lendinglib/friend_profile.html', 
        {'friend': friend, 'friend_list': friend_list, 'file_list': file_list})

def basic_profile(request, username):
    '''public profile, visible to anyone'''
    return HttpResponse("This person is not your friend yet.")
    
def file_detail(request, file_id):
    '''provides info about and checkout option for a file'''
    file = FileObject.objects.get(pk=file_id)
    title = file.title
    artist = file.artist
    owner = file.owner
    return render_to_response('lendinglib/file_detail.html', 
        {'file': file, 'title': title, 'artist': artist, 'owner': owner})       
    