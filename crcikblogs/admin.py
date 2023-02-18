from django.contrib import admin

# Register your models here.

from .models import UserDetails,Blog,Memes,post_likes,meme_likes,post_not,meme_not

# Register your models here.
admin.site.register(UserDetails)
admin.site.register(Blog)
admin.site.register(Memes)
admin.site.register(post_likes)
admin.site.register(meme_likes)
admin.site.register(post_not)
admin.site.register(meme_not)

