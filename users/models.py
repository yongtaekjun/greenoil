# users/models.py

from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.core.validators import RegexValidator
from companies.choices import TUPLE2_USER_ROLES, dict1, TUPLE1_USER_TITLES
from companies.models import Company

# class UserRole ( models.Model ):

#     user        = models.ForeignKey ( User, on_delete=models.CASCADE)
#     company     = models.ForeignKey ( 'Company', on_delete=models.CASCADE)
#     role        = models.PositiveSmallIntegerField(
#         choices=TUPLE2_USER_ROLES,
#         default=111,
#     )

#     is_active   = models.BooleanField (default=False) # false when de-activate
#     started_on  = models.DateTimeField (null=True, blank = True ) # when this role started

#     class Meta:
#         auto_created = True
#         unique_together = ( ('user', 'company', 'role'), )

#     def __str__(self):
#         return '%s %s' % (self.description_of_role, self.user)

#     @property
#     def description_of_role(self):
#         return dict1 (TUPLE2_USER_ROLES) [self.role]


class UserProfile ( models.Model ):


    user = models.OneToOneField ( User, on_delete=models.CASCADE, primary_key=True, related_name = 'userprofile')
    title     = models.PositiveSmallIntegerField(
        choices=TUPLE1_USER_TITLES,
        default=1,
    )
    image = models.ImageField(default='user_profile_images/default.jpg', upload_to='user_profile_images')

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    dob       = models.DateTimeField(),
    # role      = models.ManyToManyField (Role, related_name="user-role",),

    def __str__(self):
        return '%s %s' % (self.title, self.user)

    def save(self, *args, **kwargs ):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.title, self.user)



class UserInfoChangedLog(models.Model):
    user        = models.ForeignKey( User, on_delete=models.CASCADE,  related_name = 'UserInfoChangedLog_user')
    description = models.CharField(max_length=128) # created, updated password, phone, email, role...
    created_on  = models.DateTimeField(default=timezone.now) # false when de-activate

    def __str__(self):
        return self.description