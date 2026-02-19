from django.shortcuts import render

def interest(request):

    if request.method == "POST":
        p = int(request.POST.get('p'))
        r = int(request.POST.get('r'))
        t = int(request.POST.get('t'))

        si = (p*r*t)/100

        return render(request,'result.html',{'result':si})

    return render(request,'form.html')

