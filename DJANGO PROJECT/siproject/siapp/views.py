from django.shortcuts import render

def simpleinterest(request):
    result = None

    if request.method == "POST":
        p = float(request.POST.get("p"))
        r = float(request.POST.get("r"))
        t = float(request.POST.get("t"))

        result = (p * r * t) / 100

    return render(request, "si.html", {"result": result})
