from django.db import models


# Create your models here.
class city_info(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=50)

    class meta:
        db_table = "city_info"


class area_info(models.Model):
    area_id = models.AutoField(primary_key=True)
    area_name = models.CharField(max_length=50)
    cid = models.ForeignKey(city_info, on_delete=models.CASCADE)

    class meta:
        db_table = "Area_info"


class user_info(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=8)
    contact = models.IntegerField(max_length=11)
    address = models.CharField(max_length=50)
    area_id = models.ForeignKey(area_info, on_delete=models.CASCADE)
    dob = models.DateField()
    otp = models.IntegerField(max_length=30)
    otp_used = models.CharField(max_length=30)
    is_admin = models.IntegerField(max_length=10)

    class meta:
        db_table = "user_info"


class pg_owner(models.Model):
    pg_id = models.AutoField(primary_key=True)
    pg_name = models.CharField(max_length=20)
    pg_price = models.IntegerField(max_length=11)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=8)
    location = models.CharField(max_length=50)
    area_id = models.ForeignKey(area_info, on_delete=models.CASCADE)
    area_rating = models.IntegerField(max_length=10)
    avg_rating = models.IntegerField(max_length=5)
    # cover_image = models.CharField(max_length=30)
    des = models.CharField(max_length=30)

    class meta:
        db_tabel = "pg_owner"


class room_type(models.Model):
    r_id = models.AutoField(primary_key=True)
    r_name = models.CharField(max_length=20)
    des = models.CharField(max_length=30)

    class meta:
        db_tabel = "room_type"


class pg_room(models.Model):
    pg_room_id = models.AutoField(primary_key=True)
    r_id = models.ForeignKey(room_type, on_delete=models.CASCADE)
    pg_id = models.ForeignKey(pg_owner, on_delete=models.CASCADE)
    no_of_room = models.CharField(max_length=50)
    changes = models.CharField(max_length=30)

    class meta:
        db_tabel = "pg_room"


class pg_room_gallary(models.Model):
    gallary_id = models.AutoField(primary_key=True)
    image_patten = models.CharField(max_length=20000, null=False)
    pg_room_id = models.ForeignKey(pg_room, on_delete=models.CASCADE)

    class meta:
        db_tabel = "pg_room_gallary"


class feedback(models.Model):
    f_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(user_info, on_delete=models.CASCADE)
    pg_id = models.ForeignKey(pg_owner, on_delete=models.CASCADE)
    f_date = models.DateField()
    des = models.CharField(max_length=40)
    rating = models.IntegerField(max_length=11)

    class meta:
        db_tabel = "feedback"


class notifiaction(models.Model):
    n_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(user_info, on_delete=models.CASCADE)
    des = models.CharField(max_length=40)
    n_date = models.DateField()

    class meta:
        db_tabel = "notification"


class booking(models.Model):
    b_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(user_info, on_delete=models.CASCADE)
    pg_room_id = models.ForeignKey(pg_room, on_delete=models.CASCADE)
    status = models.IntegerField(max_length=5)
    b_date = models.DateField()
    payment_status = models.IntegerField(max_length=5)
    payment_amount = models.IntegerField(max_length=50)

    class meta:
        db_tabel = "booking"


class inquiry(models.Model):
    i_id = models.AutoField(primary_key=True)
    i_user_name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    contact = models.IntegerField(max_length=10)
    des = models.CharField(max_length=40)

    class meta:
        db_tabel = "inquiry"
