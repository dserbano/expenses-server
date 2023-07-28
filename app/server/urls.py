"""expenses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from expenses.views import get_expense, all_expenses, new_expense, edit_expense, delete_expense


urlpatterns = [
    path("", all_expenses),
    path("get_expense/", get_expense, name="get_expense"),
    path("all_expenses/", all_expenses, name="all_expenses"),
    path("new_expense/", new_expense, name="new_expense"),
    path("edit_expense/", edit_expense, name="edit_expense"),
    path("delete_expense/", delete_expense, name="delete_expense"),

    path("admin/", admin.site.urls)
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
