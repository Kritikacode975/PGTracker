import sys
from django.shortcuts import render, redirect
from django.http import HttpResponse
from pgfinder_admin.models import (
    city_info,
    area_info,
    user_info,
    pg_owner,
    room_type,
    pg_room,
    pg_room_gallary,
    feedback,
    notifiaction,
    booking,
    inquiry,
)
from pgfinder_admin.forms import (
    cityForm,
    areaForm,
    roomtypeForm,
    pgroomForm,
    pg_room_gallaryForm,
)
from django.contrib import messages
from django.core.mail import send_mail
import random
from django.conf import settings
from pgfinder_admin.function import handle_uploaded_file
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date
from datetime import date


def export(request):
    city = city_info.objects.all()
    return render(request, "city.html", {"c": city})


def Area(request):
    area = area_info.objects.all()
    return render(request, "area.html", {"a": area})


# Create your views here.


def User(request):
    user = user_info.objects.all()
    return render(request, "user.html", {"u": user})


def PGOWNER(request):
    pg = pg_owner.objects.all()
    return render(request, "pgowner.html", {"p": pg})


def Room(request):
    room = room_type.objects.all()
    return render(request, "room.html", {"r": room})


def PRoom(request):
    proom = pg_room.objects.all()
    return render(request, "pgroom.html", {"pr": proom})


def Gallary(request):
    galary = pg_room_gallary.objects.all()
    return render(request, "gallary.html", {"g": galary})


def Feedback(request):
    fedback = feedback.objects.all()
    return render(request, "feedback.html", {"f": fedback})


def Notifiaction(request):
    notifiection = notifiaction.objects.all()
    return render(request, "notification.html", {"n": notifiection})


def Booking(request):
    boking = booking.objects.all()
    return render(request, "booking.html", {"b": boking})


def Inquiry(request):
    inquiri = inquiry.objects.all()
    return render(request, "inquiry.html", {"i": inquiri})


def insert_city(request):
    if request.method == "POST":
        form = cityForm(request.POST)
        print("---------------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect("/city")
            except:
                print("-------------------", sys.exc_info())
    else:
        form = cityForm()
    return render(request, "InsertCity.html", {"form": form})


def insert_area(request):
    c = city_info.objects.all()
    if request.method == "POST":
        form = areaForm(request.POST)
        print("---------------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect("/area")
            except:
                print("-------------------", sys.exc_info())
    else:
        form = areaForm()
    return render(request, "InsertArea.html", {"form": form, "data": c})


def insert_roomtype(request):
    if request.method == "POST":
        form = roomtypeForm(request.POST)
        print("---------------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect("/room")
            except:
                print("-------------------", sys.exc_info())
    else:
        form = roomtypeForm()
    return render(request, "InsertRoomtype.html", {"form": form})


def insert_pgroom(request):
    r = room_type.objects.all()
    g = pg_owner.objects.all()
    if request.method == "POST":
        form = pgroomForm(request.POST)
        print("---------------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect("/pgroom")
            except:
                print("-------------------", sys.exc_info())
    else:
        form = pgroomForm()
    return render(request, "InsertPGroom.html", {"form": form, "d": r, "data": g})


def insert_pg_room_gallary(request):
    p = pg_room.objects.all()
    if request.method == "POST":
        form = pg_room_gallaryForm(request.POST, request.FILES)
        print("---------------------", form.errors)
        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES["image_patten"])
                form.save()
                return redirect("/galary")
            except:
                print("-------------------", sys.exc_info())
    else:
        form = pg_room_gallaryForm()
    return render(request, "InsertPG_room_gallary.html", {"form": form, "data": p})


def delete_city(request, id):
    cid = city_info.objects.get(city_id=id)
    cid.delete()
    return redirect("/city")


def delete_area(request, id):
    aid = area_info.objects.get(area_id=id)
    aid.delete()
    return redirect("/area")


def delete_user(request, id):
    uid = user_info.objects.get(user_id=id)
    uid.delete()
    return redirect("/user")


def delete_PGowner(request, id):
    pid = pg_owner.objects.get(pg_id=id)
    pid.delete()
    return redirect("/pg")


def delete_roomtype(request, id):
    rid = room_type.objects.get(r_id=id)
    rid.delete()
    return redirect("/room")


def delete_PGroom(request, id):
    prid = pg_room.objects.get(pg_room_id=id)
    prid.delete()
    return redirect("/proom")


def delete_Gallary(request, id):
    gid = pg_room_gallary.objects.get(gallary_id=id)
    gid.delete()
    return redirect("/galary")


def delete_Feedback(request, id):
    fid = feedback.objects.get(f_id=id)
    fid.delete()
    return redirect("/fedback")


def delete_Booking(request, id):
    bid = booking.objects.get(b_id=id)
    bid.delete()
    return redirect("/boking")


def delete_Notification(request, id):
    nid = notifiaction.objects.get(n_id=id)
    nid.delete()
    return redirect("/notificetion/")


def delete_Inquiry(request, id):
    iid = inquiry.objects.get(i_id=id)
    iid.delete()
    return redirect("/inquiri/")


def updateCity(request, id):
    if request.method == "POST":
        e = city_info.objects.get(city_id=id)
        form = cityForm(request.POST, instance=e)
        print("--------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect("/city")
            except:
                print("----------------", sys.exc_info())
    else:
        e = city_info.objects.get(city_id=id)
    return render(request, "UpdateCity.html", {"data": e})


def updateArea(request, id):
    if request.method == "POST":
        e = area_info.objects.get(area_id=id)
        form = areaForm(request.POST, instance=e)
        print("--------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect("/area")
            except:
                print("----------------", sys.exc_info())
    else:
        e = area_info.objects.get(area_id=id)
    return render(request, "UpdateArea.html", {"data": e})


def updateRoomtype(request, id):
    if request.method == "POST":
        e = room_type.objects.get(r_id=id)
        form = roomtypeForm(request.POST, instance=e)
        print("--------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect("/room")
            except:
                print("----------------", sys.exc_info())
    else:
        e = room_type.objects.get(r_id=id)
    return render(request, "UpdateRoomtype.html", {"data": e})


def updatePGroom(request, id):
    r = room_type.objects.all()
    g = pg_owner.objects.all()
    if request.method == "POST":
        e = pg_room.objects.get(pg_room_id=id)
        form = pgroomForm(request.POST, instance=e)
        print("--------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect("/pgroom")
            except:
                print("----------------", sys.exc_info())
    else:
        e = pg_room.objects.get(pg_room_id=id)
    return render(
        request,
        "updatePGroom.html",
        {"data": e, "d": r, "data": g},
    )


def updateGallary(request, id):
    g = pg_room.objects.all()
    if request.method == "POST":
        e = pg_room_gallary.objects.get(gallary_id=id)
        form = pg_room_gallaryForm(request.POST, request.FILES, instance=e)
        print("--------------", form.errors)

        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES["image_patten"])
                form.save()
                return redirect("/galary")
            except:
                print("----------------", sys.exc_info())
    else:
        g = pg_room.objects.all()
        e = pg_room_gallary.objects.get(gallary_id=id)
    return render(request, "UpdateGallary.html", {"data": e, "gall": g})


def dashboards(request):
    u = user_info.objects.all().count()
    b = booking.objects.all().count()
    b1 = booking.objects.all()
    f = feedback.objects.all().count()
    p = pg_owner.objects.all().count()
    return render(
        request,
        "index.html",
        {"user": u, "booking": b, "booking1": b1, "feedback": f, "Total": p},
    )


def Login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        val = user_info.objects.filter(
            email=email, password=password, is_admin=1
        ).count()
        print("------------------------------", email, "---------------", password)
        print("+++++++++++++", val)
        if val == 1:
            return redirect("/dashboards/")
        else:
            messages.error(request, "Invalid user name and password")
            return redirect("/login")
    else:
        return render(request, "login.html")


def logout(request):
    try:
        del request.session["email"]
        del request.session["password"]
        return redirect("/login")
    except:
        pass
    return redirect("/login")


def sendotp(request):
    otp1 = random.randint(10000, 99999)
    e = request.POST["email"]

    request.session["temail"] = e
    obj = user_info.objects.filter(email=e).count()
    if obj == 1:
        val = user_info.objects.filter(email=e).update(otp=otp1, otp_used=0)
        subject = "OTP Verification"
        messages = str(otp1)
        email_from = settings.EMAIL_HOST_USER
        recipients_list = [
            e,
        ]
        send_mail(subject, messages, email_from, recipients_list)
    return render(request, "set_password.html")


def set_password(request):
    if request.method == "POST":
        T_OTP = request.POST["otp"]
        T_pass = request.POST["pass"]
        T_cpass = request.POST["cpass"]

        if T_pass == T_cpass:
            e = request.session["temail"]
            val = user_info.objects.filter(email=e, otp=T_OTP, otp_used=0).count()

            if val == 1:
                user_info.objects.filter(email=e).update(otp_used=1, password=T_pass)
                return redirect("/login/")
            else:
                messages.error(request, "Invalid OTP")
            return render(request, "forgotpasssword.html")

        else:
            messages.error(request, "New password and Confirm password does not match")
            return render(request, "set_password.html")

    else:
        return redirect("/forgot_password/")


def forgot_password(request):
    return render(request, "forgotpasssword.html")


def upload_images(request):
    if request.method == "POST":
        g = pg_room_gallaryForm(request.POST, request.FILES)
        print("-------------", g.errors)

        if g.is_valid():
            try:
                handle_uploaded_file(request.FILES["g_path"])
                g.save()
                return HttpResponse("File uploaded successfuly")
            except:
                print("--------------", sys.exc_info())
    else:
        g = pg_room_gallaryForm()
        return render(request, "gallary.html", {"form": g})


from django.db import connection
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html", {"customers": 10})


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # qs = Company.objects.all()
        cursor = connection.cursor()
        cursor.execute(
            """SELECT a.area_name , count(*) FROM pgfinder_admin_pg_owner p join pgfinder_admin_area_info a 
where p.area_id_id = a.area_id
group by p.area_id_id;"""
        )
        qs = cursor.fetchall()
        print("------------+++++++++++++++++++-----------------")
        labels = []
        default_items = []

        for item in qs:
            labels.append(item[0])
            default_items.append(item[1])

        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)


@csrf_exempt
def order_report1(request):
    s = pg_owner.objects.all()
    if request.method == "POST":
        key = request.POST.get("area_info")
        print("--- KEyword --------", key)
        sql = "select * from pgfinder_admin_booking b join pgfinder_admin_pg_room r join pgfinder_admin_pg_owner p join pgfinder_admin_user_info u where b.pg_room_id_id = r.pg_room_id and r.pg_id_id = p.pg_id and b.user_id_id = u.user_id and p.pg_id  = %s"
        d = pg_owner.objects.raw(sql, [key])
        return render(request, "report1.html", {"booking": d})
    else:
        d = booking.objects.all()

    return render(request, "Order_Report.html", {"booking": d, "area_info": s})


@csrf_exempt
def order_report2(request):

    if request.method == "POST":

        start = request.POST["sd"]
        end = request.POST["ed"]

        start = parse_date(start)
        end = parse_date(end)

        if start < end:
            print("----", start, "---------", end)
            d = booking.objects.filter(b_date__range=[start, end])
            return render(request, "Order_Report2.html", {"booking": d})
        else:
            d = booking.objects.all()
            messages.error(request, "start date must be smaller than end date")
            return render(request, "Order_Report2.html", {"booking": d})
    else:
        d = booking.objects.all()
        print("-------------------------", d)
    return render(request, "Order_Report2.html", {"booking": d})


def order_report3(request):

    sql1 = "select b.b_id, u.user_name as user, count(*) as totalbooking from pgfinder_admin_booking b join pgfinder_admin_user_info u WHERE b.user_id_id = u.user_id GROUP by b.user_id_id"
    d = booking.objects.raw(sql1)
    print("-------------------------", d)
    return render(request, "Order_Report3.html", {"b1": d})


def reject_order(request, id):
    # o = booking.objects.filter(b_id=id).update(status=2)
    # o.save()
    # return redirect("/boking")
    o = booking.objects.get(b_id=id)
    u = o.user_id_id
    bid = o.b_id
    use = user_info.objects.get(user_id=u)
    print(use, "---------------------------------------")
    mail = use.email
    print(mail)
    obj = user_info.objects.filter(email=mail).count()
    da = date.today()
    n = notifiaction(user_id_id=u, n_date=da, des="Your request has Rejected")
    n.save()
    if obj == 1:
        re = booking.objects.filter(b_id=bid).update(status=1)
        subject = "Booking success"
        message = "Your request has been Reject"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [
            mail,
        ]
        print("------------------", subject, messages, email_from, recipient_list)
        send_mail(subject, message, email_from, recipient_list)
    return redirect("/boking")


def accept_order(request, id):
    o = booking.objects.get(b_id=id)
    u = o.user_id_id
    bid = o.b_id
    use = user_info.objects.get(user_id=u)
    print(use, "---------------------------------------")
    mail = use.email
    print(mail)
    obj = user_info.objects.filter(email=mail).count()
    da = date.today()
    n = notifiaction(user_id_id=u, n_date=da, des="Your request has Accepted")
    n.save()
    if obj == 1:
        re = booking.objects.filter(b_id=bid).update(status=1)
        subject = "Booking success"
        message = "Your request has been Accpted"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [
            mail,
        ]
        print("------------------", subject, messages, email_from, recipient_list)
        send_mail(subject, message, email_from, recipient_list)
    return redirect("/boking")
