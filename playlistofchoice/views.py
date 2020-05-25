from django.shortcuts import render, redirect
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Create your views here.


def log_and_reg(request):

    print(" Log and Reg Page is Invoked Successfully ")

    return render(request,'log_and_reg.html')

def home(request):

    print(" Home Page is Invoked Successfully ")

    return render(request,'home.html')

def new_releases(request):
    cid = 'fcabf1c8ee3d4bbc81275366fd4bfacf'
    secret = '39c9ebdb80bb41d89de106bb59e4e205'
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    results = sp.new_releases(country=None, limit=20, offset=0)
    new_realeases_list = []
    for i in results['albums']['items']:
        new_realeases_list.append(
            {
                "artist": i['artists'][0]['name'],
                "album_id": i['id'],
                "album": i['name'],
                "image_url": i['images'][0]['url'],
            }
        )
    context = {
        'new_releases_list': new_realeases_list
    }
    return render(request, 'new_releases.html', context)