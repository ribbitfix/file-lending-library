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

        
