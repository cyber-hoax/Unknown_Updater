# Unknown_Updater
upodate image from unknown to know directory or delete the image from folder using Django.

This is the one of the side experiments i have done with Django.
---


### prerequisite
---
> django

> python 

---
### Creating an app in Django
> python3 manage.py startapp updater


### settings.py
we have to integrate the html page from the backend for that we have to set the directory.

```python 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

set the static directory to fetch the images 

```python
STATIC_URL = '/updater/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, "updater")]
```


#### models.py
---

creating database with three fields first name, second name and uid, which can be utilize to identify uniquness between users

``` python
from django.db import models

class UserDetail(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    hybrid_uid = models.CharField(max_length=50, default="")
```

### views.py
---

in view.py we right all our business logic inside of it

```python
from django.shortcuts import render
import os
import shutil
# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .models import UserDetail
from unknown_updater import settings

#grab all the images in list and render in frontend
def index(request ):
    
    fileNames = os.listdir('updater/unknown/')
    hists = [ file for file in fileNames]
    print(hists)
    names = UserDetail.objects.all()
    
    
    print(names)
    
    #extract value from form from forntend
    if request.method == 'POST' :
        if request.POST['submit'] == 'Submit':
            a = request.POST['user_id']
            firstName, lastName = a.split(' ', )
            print(firstName) 
            print(lastName)
            uids  = UserDetail.objects.get(first_name=firstName ,last_name = lastName)
            print(uids.hybrid_uid)
            files = request.POST["img"]
            source_directory = settings.BASE_DIR+"/updater/unknown/"+str(files)
            destination_directory = settings.BASE_DIR+"/updater/known_user/"+str(uids.hybrid_uid)+"/"+str(files)
            shutil.move(source_directory , destination_directory)
            print(files)
            return HttpResponseRedirect('/polls')
        else:
            if request.POST['submit'] == 'delete':
                files = request.POST["img"]
                os.remove(settings.BASE_DIR+"/updater/unknown/"+str(files))
                print(files)
                return HttpResponseRedirect('/polls')


    
    return render(request , 'home.html', {'hists':hists , 'names' : names})




```



---



