from django.shortcuts import render


def renderIndex(request):
    return render(request, "pages/index.html")

def renderHorror(request):
    context = {
        "range": range(20)
    }
    return render(request, "pages/horror.html", context=context)

def render10x19(request):
    return render(request, "pages/10x19.html")

def renderTolv(request):
    context = {
        "range": range(12)
    }
    return render(request, "pages/tolv.html", context=context)

def renderRodic(request):
    return render(request, "pages/rodic.html")

def renderPaintbox(request):
    return render(request, "pages/paintbox.html")

def renderSchwartz(request):
    return render(request, "pages/schwartz.html")

def renderRodic(request):
    return render(request, "pages/rodic.html")

def renderBeige(request):
    return render(request, "pages/beige.html")

def renderZoo(request):
    return render(request, "pages/zoo.html")