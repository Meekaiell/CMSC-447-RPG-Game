from django.urls import path

from django.contrib import admin

admin.autodiscover()

import Heroku.hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", Heroku.hello.views.index, name="index"),
    path("db/", Heroku.hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]
