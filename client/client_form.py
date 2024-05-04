from django import forms
from pgfinder_admin.models import feedback, user_info, inquiry

# class FeedbackForm(forms.Form):
# name = forms.CharField(max_length=100)
# email = forms.EmailField()
# feedback = forms.CharField(widget=forms.Textarea)


class feedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ["user_id", "pg_id", "f_date", "des", "rating"]


class signupFrom(forms.ModelForm):
    class Meta:
        model = user_info
        fields = [
            "user_name",
            "email",
            "password",
            "contact",
            "address",
            "area_id",
            "dob",
            "otp",
            "is_admin",
        ]


class ContactForm(forms.ModelForm):
    class Meta:
        model = inquiry
        fields = ["i_user_name", "email", "contact", "des"]
