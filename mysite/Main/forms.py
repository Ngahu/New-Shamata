from django import forms

from  .models import Post

from .models import Team_Meamber


class PostForm(forms.ModelForm):
    image = forms.ImageField(label='Your images')
    class Meta:
        model = Post
        fields = [
            "title",
            "description",
            "image",
            "image_2",
            "image_3",
            "image_4",
            "image_5",
            "location_details",
            "size_of_land",
            "price",
            "features",
        ]



class TeamForm(forms.ModelForm):
    class Meta:
        model = Team_Meamber
        fields = [
            "members_name",
            "members_role",
            "members_details",
            "members_phone_number",
            "members_email",
            "members_image"
        ]