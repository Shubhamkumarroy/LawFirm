from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('home/',views.home,name="home"),
    path('carousel/',views.carousel,name="carousel"),
    path("signup/",views.signup,name="signup"),
    path("signuplawyer/",views.signuplawyer,name="signuplawyer"),
    path('loginuser/', views.loginuser, name ='loginuser'),
    path('logoutuser/', views.logoutuser, name ='logoutuser'),
    path('accountcreate/',views.accountcreate,name='accountcreate'),
    path('blog/',views.blog,name="blog"),
    path('chat/<int:id1>/<int:id2>',views.chat,name="chat"),
    path('readmore/<int:id1>',views.readmore,name='readmore'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('setting/',views.setting,name='setting'),
    path('lawyer/<int:id1>',views.lawyer,name='lawyer'),
    path('room/<int:id1>/<int:id2>',views.room,name='room'),
    path('send_chat_request/<int:receiver_id>',views.send_chat_request,name='send_chat_request'),
    path('typelawyer/<str:type>',views.typelawyer,name='typelawyer'),
    path('update/<int:id1>',views.update,name='update'),
    path('consult',views.consult,name='consult'),
    path('submitproblem',views.submitproblem,name="submitproblem"),
    path('storedata',views.storedata,name="storedata"),
    path('advocates/<str:advocate_type>/', views.advocates_by_type, name='advocates_by_type'),
    path('searchlawyer',views.searchlawyer,name="searchlawyer"),
    path('somebestadvocates',views.somebestadvocates,name="somebestadvocates"),
    path('arbitration_mediation_lawyers_data',views.arbitration_mediation_lawyers_data,name="arbitration_mediation_lawyers_data"),
    path('webscrapdata',views.webscrapdata,name="webscrapdata"),
     path('Arbitrators_Mediators',views.Arbitrators_Mediators,name="Arbitrators_Mediators"),



    
]
