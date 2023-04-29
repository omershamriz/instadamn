from django.urls import path
from dms import views

urlpatterns = [
    path('inbox/', views.inbox, name='message'),
    path('dms/<username>/', views.Directs, name='dms'),
    path('send/', views.SendMessage, name='send-message'),
    path('new/', views.UserSearch, name='user-search'),
    path('new/<username>', views.NewMessage, name='new-message')

]