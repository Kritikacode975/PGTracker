"""
URL configuration for pgfinder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from pgfinder_admin import views
from django.urls import include, re_path
from pgfinder_admin.views import HomeView, ChartData

urlpatterns = [
    path("admin/", admin.site.urls),
    path("city/", views.export),
    path("area/", views.Area),
    path("user/", views.User),
    path("pg/", views.PGOWNER),
    path("room/", views.Room),
    path("proom/", views.PRoom),
    path("galary/", views.Gallary),
    path("fedback/", views.Feedback),
    path("notificetion/", views.Notifiaction),
    path("boking/", views.Booking),
    path("inquiri/", views.Inquiry),
    path("insertcity/", views.insert_city),
    path("insertarea/", views.insert_area),
    path("insertroomtype/", views.insert_roomtype),
    path("insertpgroom/", views.insert_pgroom),
    path("insertpgroom_gallary/", views.insert_pg_room_gallary),
    path("deleteCity/<int:id>", views.delete_city),
    path("deleteArea/<int:id>", views.delete_area),
    path("deleteUser/<int:id>", views.delete_user),
    path("deletePGowner/<int:id>", views.delete_PGowner),
    path("deleteRoomtype/<int:id>", views.delete_roomtype),
    path("deletePGroom/<int:id>", views.delete_PGroom),
    path("deleteGallary/<int:id>", views.delete_Gallary),
    path("deleteFeedback/<int:id>", views.delete_Feedback),
    path("deleteBooking/<int:id>", views.delete_Booking),
    path("deleteNotification/<int:id>", views.delete_Notification),
    path("deleteInquiry/<int:id>", views.delete_Inquiry),
    path("updatecity/<int:id>", views.updateCity),
    path("updateArea/<int:id>", views.updateArea),
    path("updateRoomtype/<int:id>", views.updateRoomtype),
    path("updatePGroom/<int:id>", views.updatePGroom),
    path("updateGallary/<int:id>", views.updateGallary),
    path("dashboards/", views.dashboards),
    path("login/", views.Login),
    path("logout/", views.logout, name="logout"),
    path("send_otp/", views.sendotp),
    path("forgot_password/", views.forgot_password),
    path("set_password/", views.set_password),
    path("upload/", views.upload_images),
    path("accpet/<int:id>", views.accept_order),
    path("reject/<int:id>", views.reject_order),
    re_path(r"home", HomeView.as_view(), name="home"),
    re_path(r"^api/chart/data/$", ChartData.as_view(), name="api-data"),
    path("order_report1/", views.order_report1),
    path("order_report2/", views.order_report2),
    path("order_report3/", views.order_report3),
    path("client/", include("client.client_urls")),
]
