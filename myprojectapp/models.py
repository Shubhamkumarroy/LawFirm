from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Room(models.Model):
    name = models.CharField(max_length=255)
class Eitheruserlawyer(models.Model):
    type=models.CharField(max_length=255)
class User_detail(models.Model):
    eitheruserlawyer = models.ForeignKey(Eitheruserlawyer, default=1,on_delete=models.CASCADE)
    user_detail_name = models.CharField(max_length=255)
    user_detail_email = models.CharField(max_length=255)
    type = models.CharField(default='user', editable=False, max_length=255)
    user_detail_password = models.CharField(max_length=255)

    def __str__(self):
        return self.user_detail_name
class UserProfilePhoto(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return f'Profile Photo of {self.user.username}'
    
class Extradetaillawer(models.Model):
    catagory=models.CharField(max_length=255,default="N/A")
    contact=models.CharField(max_length=255,default="N/A")
    country=models.CharField(max_length=255,default="N/A")
class Laweruser(models.Model):
    eitheruserlawyer = models.ForeignKey(Eitheruserlawyer,default=1, on_delete=models.CASCADE)
    extradetaillawer=models.ForeignKey(Extradetaillawer,default=1, on_delete=models.CASCADE)
    room=models.ForeignKey(Room,default=1,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(default='lawer', editable=False, max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

    


class Blog(models.Model):
    title=models.TextField()
    description=models.TextField()
    author=models.ForeignKey(User_detail, on_delete=models.CASCADE)
    date=today_date = timezone.now().date()
    def __str__(self):
        return self.title

class Lawyer(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255,)
    password=models.CharField(max_length=255)
    catagory=models.CharField(max_length=255)
    contact=models.CharField(max_length=255)
    country=models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(Lawyer, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} -> {self.recipient}: {self.content}'

class Typelawer(models.Model):
    laweruser=models.ForeignKey(Laweruser,default=1,on_delete=models.CASCADE)
    type=models.TextField(default="Criminals laweyers")


class ChatRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(Extradetaillawer, on_delete=models.CASCADE, related_name='received_requests')
    accepted = models.BooleanField(default=False)





class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)


class Advocatecatagory(models.Model):
    cat=models.TextField(default="N/A")

class Advocate(models.Model):
    name = models.CharField(max_length=255, default='N/A')  # Default name is 'N/A'
    location = models.CharField(max_length=255, default='N/A')  # Default location is 'N/A'
    experience = models.CharField(max_length=255, default='N/A')  # Default experience is 'N/A'
    type = models.CharField(max_length=255, default='Other')  # Default type is 'Other'
    rating = models.CharField(max_length=255, default='N/A')  # Default rating is 'N/A'
    image_url = models.URLField(default='https://example.com/default-image.jpg')  # Default image URL

    def __str__(self):
        return self.name
    


class Advocatefin(models.Model):
    name = models.CharField(max_length=255, default='N/A')
    location = models.CharField(max_length=255, default='N/A')
    experience = models.CharField(max_length=255, default='N/A')
    type = models.CharField(max_length=255,default='other')
    rating = models.CharField(max_length=255, default='N/A')
    image_url = models.URLField(default='https://example.com/default-image.jpg')
    practice_area_skills = models.TextField(default="Criminals & Consumer Court")

    def __str__(self):
        return self.name

class Advocatecatagoryfin(models.Model):
    cat = models.CharField(max_length=255)

    def __str__(self):
        return self.cat
    
class Aribitration_mediator(models.Model):
    name = models.CharField(max_length=255)
    rating = models.CharField(max_length=255,null=True, blank=True)
    experience = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    practice_areas = models.TextField(null=True, blank=True)
    language = models.CharField(max_length=255, null=True, blank=True)
    photo_url = models.URLField(null=True, blank=True)
    contact_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


# Create your models here.
