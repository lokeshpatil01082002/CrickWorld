from django.db import models


class UserDetails(models.Model):
    userid = models.CharField(max_length=30,primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    reward = models.IntegerField()
    def __str__(self):
        return self.userid


class Blog(models.Model):
    userid = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    likes = models.IntegerField()
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post/')
    date= models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.post_id)

class Memes(models.Model):
    userid = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    likes = models.IntegerField()
    meme_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='meme/')
    date= models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.meme_id)


class post_likes(models.Model):
    id=models.AutoField(primary_key=True)
    post_id= models.IntegerField()
    userid = models.CharField(max_length=30)
    def __str__(self):
        return str(self.post_id)+str(self.userid)

class meme_likes(models.Model):
    id=models.AutoField(primary_key=True)
    meme_id= models.IntegerField()
    userid = models.CharField(max_length=30)
    def __str__(self):
        return str(self.meme_id)+str(self.userid)

class post_not(models.Model):
    id=models.AutoField(primary_key=True)
    post_id= models.IntegerField()
    userid = models.CharField(max_length=30)
    def __str__(self):
        return str(self.post_id)+str(self.userid)

class meme_not(models.Model):
    id=models.AutoField(primary_key=True)
    meme_id= models.IntegerField()
    userid = models.CharField(max_length=30)
    def __str__(self):
        return str(self.meme_id)+str(self.userid)






    
