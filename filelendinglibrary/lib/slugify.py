from django.template.defaultfilters import slugify as django_slugify

def slugify(name, model):    
    tempslug = django_slugify(name)
    i = 1
    if not tempslug:
        tempslug += '_2'
        i = 3
    while True:
        try:
            model.objects.get(slug=tempslug)
            if i == 1:
                tempslug = tempslug + '_2'
            else:
                tempslugparts = tempslug.split('_')[:-1]
                tempslug = '_'.join(tempslugparts)+'_'+str(i)
            i += 1

        except model.DoesNotExist:
            return tempslug
        except model.MultipleObjectsReturned:
            pass


