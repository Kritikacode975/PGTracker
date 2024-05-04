from django.shortcuts import render, redirect
from pgfinder_admin.models import (
    pg_owner,
    user_info,
    feedback,
    area_info,
    pg_room,
    booking,
    inquiry,
)
from client.client_form import feedbackForm, signupFrom, ContactForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail
from datetime import date
import sys
from django.http import HttpResponse
from datetime import date


# Create your views here.
def clientlogin(request):
    if request.method == "POST":
        e = request.POST["email"]
        p = request.POST["password"]
        val = user_info.objects.filter(email=e, password=p, is_admin=0).count()
        print("-----------------------", val)
        if val == 1:
            data = user_info.objects.filter(email=e, password=p)
            for items in data:
                request.session["client_id"] = items.user_id
                request.session["client_name"] = items.user_name
                request.session["client_email"] = items.email
                if request.POST.get("rememberme"):
                    print("++++++++++++++++++++++++++++++++cdjhfcdbvfhjjbc")
                    response = redirect("/client/client_index")
                    response.set_cookie(
                        "cookie_cemail", request.POST["email"], 3600 * 24 * 365 * 2
                    )
                    response.set_cookie(
                        "cookie_cpass", request.POST["password"], 3600 * 24 * 365 * 2
                    )
                    return response
                return redirect("/client/client_index")
        else:
            messages.error(request, "invalid username or password")
            # return render(request,"client_login.html")
            return redirect("/client/clientlogin/")
    else:
        if request.COOKIES.get("cookie_cemail"):
            return render(
                request,
                "client_login.html",
                {
                    "client_email": request.COOKIES["cookie_cemail"],
                    "client_password": request.COOKIES["cookie_pass"],
                },
            )
        else:
            return render(request, "client_login.html")


def client_logout(request):
    try:
        del request.session["client_id"]
        del request.session["client_name"]
        del request.session["temail"]
        return redirect("/client/clientlogin")
    except:
        pass
    return redirect("/client/clientlogin")


def clientprofile(request):
    ar = area_info.objects.all()
    id = request.session["client_id"]
    print(id, "--------------------")
    if request.method == "POST":
        user = user_info.objects.get(user_id=id)
        form = signupFrom(request.POST, instance=user)
        print("-------------error----", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect("/client/client_index")
            except:
                print("-----------------", sys.exc_info())
        else:
            pass
    else:
        form = signupFrom()
        user = user_info.objects.get(user_id=id)
    return render(request, "client_profile.html", {"form": form, "user": user, "a": ar})


def clienthome(request):
    return render(request, "home.html")


def layout(request):
    context = {}
    return render(request, "layout.html", context)


def about(request):
    context = {}
    return render(request, "about.html", context)


def service(request):
    context = {}
    return render(request, "service.html", context)


def gallery(request):
    context = {}
    return render(request, "gallery.html", context)


def feedback1(request):
    context = {}
    return render(request, "feedback1.html", context)


def clientvilla(request, id):
    if id == 0:
        pg = pg_owner.objects.all()
    else:
        pg = pg_owner.objects.filter(area_id=id)
    return render(request, "client_villagrid2.html", {"pg": pg})


def client_villaDetails(request, id):
    pg_i = pg_owner.objects.get(pg_id=id)
    pgr = pg_room.objects.get(pg_id=id)
    print("----------------pg room----------------", pgr)
    feed = feedback.objects.filter(pg_id=id)
    return render(
        request, "villa-Details.html", {"pgdetail": pg_i, "fed": feed, "pgr": pgr}
    )


def search(request):
    if request.method == "GET":
        pg_name = request.GET.get("pg_name")
        if pg_name:
            request.session["search"] = pg_name
            obj = pg_owner.objects.filter(pg_name__icontains=pg_name)
            print("--------------------------------pg", obj)
            return render(request, "client_villagrid2.html", {"pg": obj})
        else:
            return redirect("/client/villa/")


def insert_Feedback(request):
    p = pg_owner.objects.all()
    u = user_info.objects.all()
    if "client_id" in request.session:
        if request.method == "POST":
            print("Inside Post")
            de = request.POST["des"]
            p = request.POST["pg_id"]
            r = request.POST["rating"]
            id = request.session["client_id"]
            d = date.today()
            f = feedback(user_id_id=id, pg_id_id=p, rating=r, des=de, f_date=d)
            print("--------------------------------", f)
            f.save()
            return redirect("/client/villadetails/%s" % p)
        else:
            return HttpResponse("Get Method")
    else:
        return render(
            request, "villa-Details.html", {"pg": p, "us": u, "id": id, "fed": f}
        )


def client_registrtion(request):
    ar = area_info.objects.all()
    if request.method == "POST":
        form = signupFrom(request.POST)
        print("-------------------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/client/clientlogin/")
            except:
                print("-------------", sys.exc_info())
    else:
        form = signupFrom()
    return render(request, "registration.html", {"form": form, "a": ar})


def client_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        print("-------------------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/client/contact/")
            except:
                print("-------------", sys.exc_info())
    else:
        form = ContactForm()
    return render(
        request,
        "contact.html",
        {
            "form": form,
        },
    )


import datetime


def client_Booking(request):
    p = pg_room.objects.all()
    pg = pg_room.objects.all()
    da = date.today()
    print("boookingggggggggggggggggggggggggggggg")
    if request.method == "POST":
        cid = request.session["client_id"]
        rid = request.POST.get("pg_room_id")
        print("-------------------------------------------room id in booking", rid)
        bokingd = request.POST.get("b_date")
        print("----------------date of booking", bokingd)
        pg_rid = pg_room.objects.filter(pg_room_id=rid)
        print("pg room id -------------", pg_rid)
        for data in pg_rid:
            p_id = data.pg_id_id
        pg_p = pg_owner.objects.filter(pg_id=p_id)
        print("-----------------------------pg id from room", pg_p)
        for dat in pg_p:
            amt = dat.pg_price

        book = booking(
            user_id_id=cid,
            pg_room_id_id=rid,
            status=0,
            b_date=bokingd,
            payment_status=0,
            payment_amount=amt,
        )
        book.save()
        return redirect("/client/checkout/")
    # d = datetime.datetime.strptime(str(date.today), "%m/%d/%y").date()
    # print("--------------------", d)
    return render(request, "client_booking.html", {"p": pg, "da": da})


def Checkout(request):

    if "client_id" in request.session:
        ar = user_info.objects.all()
        id = request.session["client_id"]

        u1 = user_info.objects.get(user_id=id)

        u = booking.objects.latest("b_id")

        total = int(u.payment_amount)
        print("total---------------------------", total)

        return render(
            request,
            "client_checkout.html",
            {"booking": u, "user": u1, "a": ar, "total": total},
        )
    else:
        return redirect("/client/checkout/")


def bookSuccess(request):
    Booking_online(request)
    return render(request, "Booking-Success.html")


def Booking_online(request):
    if request.session.has_key("client_id"):
        uid = request.session["client_id"]
        ca = booking.objects.filter(user_id_id=uid)
        amt = 0
        for val in ca:
            amt = amt + (int(val.payment_amount))
            r_id = val.pg_room_id_id
        date1 = date.today().strftime("%Y-%m-%d")
        o = booking(
            user_id_id=uid,
            pg_room_id_id=r_id,
            payment_amount=amt,
            b_date=date1,
            status=1,
            payment_status=1,
        )
        o.save()
        id = booking.objects.latest("b_id")
        c = booking.objects.filter(user_id_id=uid)
        c1 = booking.objects.filter(user_id_id=uid).count()
        if c1 >= 1:
            e = request.session["client_email"]
            obj = user_info.objects.filter(email=e).count()
            val = user_info.objects.filter(email=e)
            for data in val:
                name = data.user_name
            print(name)
            print("user count", obj, "----------------------", val)
            if obj == 1:
                ord1 = booking.objects.filter(b_id=id.b_id)
                subject = "Booking Conformation"
                message = (
                    f"Dear {name} \n\n\t "
                    f"Your Booking request has been received. "
                    f"Your Booking details are as follows:"
                )
                message += f"\n---------------------------------------------------------------------"
                message += f"\n  PG Name"
                message += f"\n----------------------------------------------------------------------"
                for data in ord1:
                    print("---------------------------------", data)
                    message += f"\n {data.b_id} ,{data.pg_room_id.pg_id.pg_name}"
                message += f"\n----------------------------------------------------------------------"
                message += f"\n  Total \t\t\t {amt}"
                message += f"\n----------------------------------------------------------------------"
                message += f"\n\n Thank uou,\n For Booking"
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [
                    e,
                ]
                send_mail(subject, message, email_from, recipient_list)
        else:
            messages.error(request, "You don't have any booking!")
            return render(request, "client_booking.html")
        return redirect("/client/client_index/")
    return render(request, "client_booking.html", {"total": amt})


def load_area(request):
    ar = area_info.objects.all()
    print("--------------------------", ar)
    return render(request, "load_area.html", {"areaaa": ar})


def client_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        print("-------------------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/client/contact/")
            except:
                print("-------------", sys.exc_info())
    else:
        form = ContactForm()
    return render(
        request,
        "contact.html",
        {
            "form": form,
        },
    )


def forgo(request):
    return render(request, "recover_pass.html")


def set_pass(request):
    if request.method == "POST":
        T_OTP = request.POST["otp"]
        T_pass = request.POST["pass"]
        T_cpass = request.POST["cpass"]

        if T_pass == T_cpass:
            e = request.session["temail"]
            val = user_info.objects.filter(email=e, otp=T_OTP, otp_used=0).count()

            if val == 1:
                user_info.objects.filter(email=e).update(otp_used=1, password=T_pass)
                return redirect("/client/clientlogin/")
            else:
                messages.error(request, "Invalid OTP")
            return render(request, "recover_pass.html")

        else:
            messages.error(request, "New password and Confirm password does not match")
            return render(request, "client_otp.html")

    else:
        return redirect("/forget/")


def OTP(request):
    otp1 = random.randint(10000, 99999)
    print("-------------------------------inside otp")
    e = request.POST["email"]
    print("---------------email---------------------", e)

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
    return render(request, "client_otp.html")


def mybooking(request):
    uid = request.session["client_id"]
    b = booking.objects.filter(user_id=uid)
    return render(request, "mybooking.html", {"my": b})
