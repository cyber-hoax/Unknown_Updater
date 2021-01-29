from django.shortcuts import render
import os
import shutil
# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .models import UserDetail
from unknown_updater import settings

def index(request ):
    
    fileNames = os.listdir('updater/unknown/')
    hists = [ file for file in fileNames]
    print(hists)
    names = UserDetail.objects.all()
    
    
    print(names)

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









