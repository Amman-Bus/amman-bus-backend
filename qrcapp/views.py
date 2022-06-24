from django.shortcuts import render
from .models import QRC


def home_view(request):
    name="welcome  "
    obj=QRC.object.get(id=1)
    context = {
        "name" :name,
        "obj":obj,
    }
    return render(request,"qrc.html",context)

