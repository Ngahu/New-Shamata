from django import forms

from  .models import Post,Sell_to_us

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
            "video",
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



class SellToUs(forms.ModelForm):
    
    class Meta:
        model = Sell_to_us
        fields = [
            "property_name",
            "owners_phone_number",
            "property_image",
            "property_image_2",
            "description",
            "size_of_land",
            "location_details",
            "price",
        ]
