
from django.shortcuts import render
from .models import Registration

def register(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        hobby = request.POST.get("hobby")
        city = request.POST.get("city")

        # Save to database
        data = Registration(
            name=name,
            email=email,
            gender=gender,
            hobby=hobby,
            city=city
        )
        data.save()

        return render(request, "result.html", {"data": data})

    return render(request, "register.html")
