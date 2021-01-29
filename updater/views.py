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




def delet_user(request):
    if request.method == 'POST' :
        files = request.POST["img"]
        os.remove(settings.BASE_DIR+"/updater/unknown/"+str(files))
        print(files)
    print("file deleted")


    
    return render(request , 'home.html', {'hists':hists , 'names' : names})




# def delet_user(request):
#     if request.method == 'POST' :
#         files = request.POST["img"]
#         os.remove(settings.BASE_DIR+"/updater/unknown/"+str(files))
#         print(files)
#     print("file deleted")


    return redirect(index , request)






# def load_images_from_folder(folder):
#     images = []
#     for filename in os.listdir(folder):
#         img = cv2.imread(os.path.join(folder,filename))
#         if img is not None:
#             images.append(img)
#     return images
# def load_images_from_folder(folder):
#     images = []
#     for filename in os.listdir(folder):
#         img = cv2.imread(os.path.join(folder,filename))
#         if img is not None:
#             images.append(img)
#     return images
# folder="directory/folder path"