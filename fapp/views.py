from django.shortcuts import render 
import requests as rq
from . import loading as ld
from . import converter as con
from . import problems as pr

def homepage(request):
    return render(request,'homepg.html')

def secondpg(request):
    url_user = request.POST.get('uname')
    
    try:
        rq.get(url_user)
        val = 200
    except Exception:
        val = 202
    if val < 201:
        ld.Load(url_user)
        return render(request,'download.html',{'mess1':'Download Successfully and stored in YoutubeAllDownloads named folder in your file manager'})
    else:
        return render(request,'download.html',{'mess1':'Please select whole url of youtube videos that you want to download !! copy the whole url from YouTube and paste it here in input tag'})

    return render(request,'download.html')

def convert(request):
    if request.method == 'POST':
        fl_name = request.POST.get('user_fl')
        userfl_name = request.POST.get('namefile')
        fl = str(fl_name)
        if fl == '' :
            return render(request,'converter.html',{'mess':'select any file from file manager'})
        else:
            con.Conv(fl[:-4],userfl_name)
            return render(request,'converter.html',{'mess':'Coverted from video to audio in YoutubeAllAudios named folder in your file manager'})
            
    return render(request,'converter.html')

def contact(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        user_mess = request.POST.get('message')
        pr.Send_me(user_name,user_email,user_mess)
        return render(request,'index.html',{'send_mess':'We have sent your problem to server Thankyou for us to known this issue will resolve this as soon as possible '})
    return render(request,'index.html')