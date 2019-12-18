from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from ckeditor_uploader.fields import RichTextUploadingField
# from django_mysql.models import JSONField

# Create your models here.
# Manager for Custom User Model
class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, reg_no, password=None):
        if not email:
            raise ValueError("Users must have a email")
        if not username:
            raise ValueError("Users must have a username")
        
        user =  self.model(
                    email = self.normalize_email(email),
                    username = username,
                    first_name = first_name,
                    last_name = last_name,
                    reg_no = reg_no
                )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, first_name, last_name, reg_no, password):
        user = self.create_user(email, username, first_name, last_name, reg_no, password = password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Custom User Model
class UserAccount(AbstractBaseUser):
    # Basic fields required for a custom user model.
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=40, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    # Extra fields added as per your requirements.
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    reg_no = models.CharField(max_length=10, unique=True)
    profile_img = models.ImageField(null=True)
    year = models.CharField(max_length=12, null=True)
    course = models.CharField(max_length=20, null=True)
    branch = models.CharField(max_length=20, null=True)
    bio = models.CharField(max_length=150, null=True)
    
    # Using this value for logging 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'reg_no']
    
    objects = UserManager()
    def __str__(self):
        return f"{self.email}"

    # These 2 func are for user roles.
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

# Timetable model
class Timetable(models.Model):
    # SELECT_DAY = (
    #     ('Mon', 'Modnday'),
    #     ('Tue', 'Tuesday'),
    #     ('Wed', 'Wednesday'),
    #     ('Thu', 'Thursday'),
    #     ('Fri', 'Friday'),
    #     ('Sat', 'Saturday'),
    # )
    # day = models.CharField(max_length=5, choices=SELECT_DAY)
    # start = models.TimeField()
    # end = models.TimeField()
    # subject = models.CharField(max_length=100)
    # room = models.CharField(max_length=50)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    timetable = models.TextField(default=None)

    def __str__(self):
        return f"{self.user.username}"

# Models for Forum
# Categories Model
class Categories(models.Model):
    cat_name = models.CharField(max_length=255, unique=True)
    cat_desc = models.CharField(max_length=255)
    cat_topics = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.cat_name}"

# Topics Models - Each categories will have lots of topics which are the posts user create
class Topics(models.Model):
    topic_name  = models.CharField(max_length=255)
    topic_desc  = models.CharField(max_length=255)
    topic_date  = models.DateTimeField(auto_now_add=True)
    topic_cat   = models.ForeignKey(Categories, on_delete=models.CASCADE)
    topic_by    = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    topic_posts = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.topic_name}"

# Posts(Replies) on a topic
class Posts(models.Model):
    post_content    = RichTextUploadingField()
    post_date       = models.DateTimeField(auto_now_add=True)
    post_topic      = models.ForeignKey(Topics, on_delete=models.CASCADE)
    post_by         = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    post_upvote     = models.IntegerField(verbose_name='Upvotes', default=0)
    post_downvote   = models.IntegerField(verbose_name='Downvotes', default=0) 

    def __str__(self):
        return f"Post by {self.post_by}"

class Notes(models.Model):
    title       = models.CharField(max_length=255)
    content     = RichTextUploadingField()
    created_on  = models.DateTimeField(auto_now_add=True)
    notes_by    = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    color       = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title}"

class Tasks(models.Model):
    tasks = models.TextField(default=None)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    created_on  = models.DateTimeField(auto_now_add=True)
    color       = models.CharField(max_length=255, default='#121212')
