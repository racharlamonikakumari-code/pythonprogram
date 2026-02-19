from django.shortcuts import render


# form page
def home(request):
    return render(request, "form.html")

# result page
def result(request):
    if request.method == "POST":
        n1 = int(request.POST["num1"])
        n2 = int(request.POST["num2"])

        add = n1 + n2

        return render(request, "result.html", {"output": add})
