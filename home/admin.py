from django.contrib import admin
from home.models import ContactMessage, FAQ, Blog, Comment_blog, Aboutus, NewsLatter, Informations, Slider
admin.site.register(Comment_blog)
admin.site.register(ContactMessage)
admin.site.register(FAQ)
admin.site.register(Blog)
admin.site.register(Aboutus)
admin.site.register(NewsLatter)
admin.site.register(Informations)
admin.site.register(Slider)