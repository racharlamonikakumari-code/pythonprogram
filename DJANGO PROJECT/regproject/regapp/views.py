from django.shortcuts import render

def register(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        hobby = request.POST.get("hobby")
        city = request.POST.get("city")

        return render(request, "result.html", {
            "name": name,
            "email": email,
            "gender": gender,
            "hobby": hobby,
            "city": city
        })

    return render(request, "register.html")
