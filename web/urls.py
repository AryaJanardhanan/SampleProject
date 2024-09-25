from django.urls import path
from .import views as v

urlpatterns = [
    path('', v.home, name='home'),
    path('about/', v.aboutt, name='about'),
    path('index/', v.index, name='index'),
    path('base/', v.base, name='base'),
    path('contact/', v.contact, name='contact'),
    path('sample/', v.sam, name='sam'),
    path('items/', v.item, name='item'),
    path('register/', v.user_reg, name='user_reg'),
    path('login/', v.uslogin, name='login'),
    path('logout/', v.uslogout, name='uslogout'),
    path('display/', v.display, name='display'),
    path('item/<int:pk>/delete/', v.delt, name='delt'),
    path('item/<int:pk>/edit/', v.editt, name='editt'),
]