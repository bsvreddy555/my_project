from django import forms

class feedback_form(forms.Form):
    name=forms.CharField(
        label="Name",
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Enter Your Name"
            }
        )
    )
    rateing = forms.FloatField(
        label="Rateing",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Your Rateing",

            }
        )
    )
    feedback = forms.CharField(
        label="FeedBack",
        widget=forms.Textarea(
            attrs={
                "class": "form-control specific-textarea ",
                "placeholder": "Enter Your FeedBack"
            }
        )
    )
