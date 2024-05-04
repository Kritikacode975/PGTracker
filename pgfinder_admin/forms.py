from django import forms
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


class cityForm(forms.ModelForm):
    class Meta:
        model = city_info
        fields = ["city_name"]


class areaForm(forms.ModelForm):
    class Meta:
        model = area_info
        fields = ["area_name", "cid"]


class roomtypeForm(forms.ModelForm):
    class Meta:
        model = room_type
        fields = ["r_name", "des"]


class pgroomForm(forms.ModelForm):
    class Meta:
        model = pg_room
        fields = ["r_id", "pg_id", "no_of_room", "changes"]


class pg_room_gallaryForm(forms.ModelForm):
    image_patten = forms.FileField()

    class Meta:
        model = pg_room_gallary
        fields = ["image_patten", "pg_room_id"]
