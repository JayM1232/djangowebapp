from django.shortcuts import render 
import requests as rq
import youtube_dl
import moviepy.editor as mp
import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# from . import loading as ld
# from . import converter as con
# from . import problems as pr

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
        # ld.Load(url_user)
        ydl_opts = {'outtmpl':'Download/%(title)s.%(ext)s'}

        def dwl_vid():
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([zxt])

        channel = 1
        while (channel == int(1)):
            # link_of_the_video = input("Copy & paste the URL of the YouTube video you want to download:- ")
            zxt = url_user.strip()

            dwl_vid()
            channel = int(0)

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
            # con.Conv(fl[:-4],userfl_name)
            fll = fl[:-4]
            if userfl_name == '' or userfl_name == None:
                clip = mp.VideoFileClip(f'Download/{fll}.mp4')
                if os.path.isdir('Download/YoutubeAllAudios') == False:
                    path = os.path.join('Download/YoutubeAllAudios')
                    os.mkdir(path)
                clip.audio.write_audiofile(f'Download/YoutubeAllAudios/{fll}.wav', codec='pcm_s16le')
            else:
                clip = mp.VideoFileClip(f'Download/{fll}.mp4')
                if os.path.isdir('Download/YoutubeAllAudios') == False:
                    path = os.path.join('Download/YoutubeAllAudios')
                    os.mkdir(path)
                clip.audio.write_audiofile(f'Download/YoutubeAllAudios/{userfl_name}.wav', codec='pcm_s16le')

            return render(request,'converter.html',{'mess':'Coverted from video to audio in YoutubeAllAudios named folder in your file manager'})
            
    return render(request,'converter.html')

def contact(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        user_mess = request.POST.get('message')
        # pr.Send_me(user_name,user_email,user_mess)

        # email code i.e. smtp starts from here

        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = "misaljay1221@gmail.com"
        receiver_email = "tanajim580@gmail.com"
        password = "jaymisal123"

        message = MIMEMultipart("alternative")
        message["Subject"] = "Your Website Issues"
        message["From"] = sender_email
        message["To"] = receiver_email

        # Create the plain-text and HTML version of your message
        html = f"""\
        <html>
        <body>
            <p>
                Name - > {user_name}<br>
                Email -> {user_email}<br>
                User's Issues -> {user_mess}<br>
                Thankyou from user.
            </p>
        </body>
        </html>
        """

        part2 = MIMEText(html, "html")
        message.attach(part2)

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            # server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.login(sender_email, password)
            server.sendmail(sender_email,receiver_email,message.as_string())

        # ends here smtp email code 
        return render(request,'index.html',{'send_mess':'We have sent your problem to server Thankyou for us to known this issue will resolve this as soon as possible '})
    return render(request,'index.html')