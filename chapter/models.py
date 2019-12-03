from django.db import models
from django.contrib.auth.models import AbstractUser
from localflavor.us.models import USStateField


# Create your models here.
class ChapterUser(AbstractUser):
    pledge_class = models.TextField(null=False, default='PC', max_length=5)

    user_state = USStateField(default='TX')
    user_city = models.TextField(null=True, max_length=50)
    major = models.TextField(null=False, max_length=50, default='Unspecified')
    avatar = models.ImageField(upload_to='images', null=True)
    has_been_authenticated = models.BooleanField(default=False, null=False)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return ' '.join([self.first_name, self.last_name])


class Member(models.Model):
    user = models.OneToOneField(to=ChapterUser, on_delete=models.CASCADE)
    paid_dues = models.BooleanField(default=False, null=True)
    expected_graduation_date = models.TextField(null=False, default='May 2020')

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return ' '.join([self.user.first_name, self.user.last_name])


class Active(models.Model):
    member = models.OneToOneField(to=Member, on_delete=models.CASCADE)
    rush_credits = models.PositiveSmallIntegerField(default=0)
    philanthropy_credits = models.PositiveSmallIntegerField(default=0)
    professional_credits = models.PositiveSmallIntegerField(default=0)
    tech_credits = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return ' '.join([self.member.user.first_name, self.member.user.last_name])


class Alumni(models.Model):
    user = models.OneToOneField(to=ChapterUser, on_delete=models.CASCADE)
    industry = models.TextField(null=True, max_length=50)
    graduation_date = models.TextField(default='May 2018')

    class Meta:
        verbose_name_plural = "alumni"

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return ' '.join([self.user.first_name, self.user.last_name])


class Post(models.Model):
    author = models.ForeignKey(to=ChapterUser, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    subject = models.TextField(max_length=80)
    content = models.TextField(max_length=400)

    def __str__(self):
        return ''.join([self.author, ': ', self.subject])


class Comment(models.Model):
    author = models.ForeignKey(to=ChapterUser, on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)

    def __str__(self):
        return ''.join([self.author, ': ', self.content])


class CommentResponse(models.Model):
    author = models.ForeignKey(to=ChapterUser, on_delete=models.CASCADE)
    comment = models.ForeignKey(to=Comment, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)

    def __str__(self):
        return ''.join([self.author, ': ', self.content])
