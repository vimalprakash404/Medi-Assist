from django.urls import path
from .views import reportdetails,viewreport,allbook,book_test, view_branch, view_test, viewstatus,login,register,vsample,viewbooking,logout
urlpatterns = [
    path("book/<int:id>",book_test),
    path("vbranch",view_branch),
    path("vtest/<int:id>",view_test),
    path("vstat/<int:id>",viewstatus),
    path("register/",register),
    path("",login),
    path("vs",vsample),
    path("viewb/<int:id>",viewbooking),
    path("logout",logout,name="logout"),
    path("allbook",allbook),
    path("vr",viewreport),
    path("vdetails/<int:id>",reportdetails)

]
