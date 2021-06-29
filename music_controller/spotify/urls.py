from django.urls import path
from .views import AuthURL, spotifyCallback, isAuthentcated, CurrentSong
urlpatterns = [
    path('get-auth-url', AuthURL.as_view()),
    path('redirect', spotifyCallback),
    path('is-authenticated', isAuthentcated.as_view()),
    path('current-song', CurrentSong.as_view()),
]