from django.urls import path
from .views import *
urlpatterns = [
    path("login",login),
    path("addtest",addtest),
    path("vtest",viewtest),
    path("edittest/<int:id>",edittest),
    path("delecttest/<int:id>",removetest),
    path("viewbooking/",viewbooking),
    path("abooking/<int:id>",approvebooking),
    path("rbooking/<int:id>",rejectbooking),
    path("logout/",logout),
    path("addreport/<int:id>",add_report),
    path("editreport/<int:id>",edit_report),
    path("vr",vreport)
]
