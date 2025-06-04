from django.shortcuts import render, redirect
from app_name.models import PrintClass, PingLog, DomainLog, HttpLog, ChecksslClass, CheckcmtechClass, CheckcveClass, \
    CloudClass, NsClass
from django.shortcuts import render
from .models import PingLog
from app_name.utils import ping, ssl_info, check_http_security_headers, check_ssllabs, detect_cms_with_whatweb, \
    cve_lookup_tech, detect_waf_and_cloudflare, ns_lookup


# def index(request):
#     response1 = printfun(request)
#     response2 = ping_view(request)
#     _v = PrintClass.objects.all()
#     req = PingLog.objects.all()
#     content = {
#         "app_title": _v,
#         "app_ping": req
#     }
#     return render(request, 'index.html', content)


def printfun(request):
    response2 = ping_view(request)
    response3 = ssl_view(request)
    response4 = check_http_view(request)
    response5 = check_ssl_view(request)
    response6 = check_cmtech_view(request)
    response7 = check_cloudfare_view(request)
    response7 = check_ns_view(request)
    v = PrintClass.objects.order_by('-id')[:5]
    content = {
        "app_title": v
    }
    if request.method == "POST":
        name = request.POST.get("user_name")
        if name:
            PrintClass.objects.create(user_name=name)
    return render(request, "index.html", content)


def ping_view(request):
    req = PingLog.objects.all()
    content = {
        "app_ping": req
    }
    if request.method == "POST":
        out = request.POST.get("ping_host")
        if out:
            PingLog.objects.create(ping_host=out)
            res = ping(out)
            print("result: : : ", res)
        return redirect("app_name:ping_view")
    return render(request, "index.html", content)


def ssl_view(request):
    mod = DomainLog.objects.all()
    content = {
        "app_domain": mod
    }
    if request.method == "POST":
        dom = request.POST.get("ssl_domain")
        if dom:
            DomainLog.objects.create(ssl_domain=dom)
            mod = ssl_info(dom)
            print("result: : : ", mod)
        return redirect("app_name:ssl_view")
    return render(request, "index.html", content)


def check_http_view(request):
    check = HttpLog.objects.all()
    content = {
        "app_domain": check
    }
    if request.method == "POST":
        dom = request.POST.get("securityheaders_domain")
        if dom:
            HttpLog.objects.create(securityheaders_domain=dom)
            check = check_http_security_headers(dom)
        return redirect("app_name:check_http_view")
    return render(request, "index.html", content)


def check_ssl_view(request):
    check = ChecksslClass.objects.all()
    content = {
        "app_domain": check
    }
    if request.method == "POST":
        dom = request.POST.get("ssllabs_domain")
        if dom:
            ChecksslClass.objects.create(ssllabs_domain=dom)
            check = check_ssllabs(dom)
        return redirect("app_name:check_ssl_view")
    return render(request, "index.html", content)


def check_cmtech_view(request):
    check = CheckcmtechClass.objects.all()
    content = {
        "app_domain": check
    }
    if request.method == "POST":
        dom = request.POST.get("domain")
        if dom:
            CheckcmtechClass.objects.create(domain=dom)
            check = detect_cms_with_whatweb(dom)
            print("result: : : ", check)
        return redirect("app_name:check_cmtech_view")
    return render(request, "index.html", content)


def check_cloudfare_view(request):
    check = CloudClass.objects.all()
    content = {
        "app_domain": check
    }
    if request.method == "POST":
        dom = request.POST.get("cloudflare_domain")
        if dom:
            CloudClass.objects.create(cloudflare_domain=dom)
            check = detect_waf_and_cloudflare(dom)
        return redirect("app_name:check_cloudfare_view")
    return render(request, "index.html", content)


def check_ns_view(request):
    check = NsClass.objects.all()
    content = {
        "app_domain": check
    }
    if request.method == "POST":
        dom = request.POST.get("ns_lookup_domain")
        if dom:
            NsClass.objects.create(ns_lookup_domain=dom)
            check = ns_lookup(dom)
        return redirect("app_name:check_ns_view")
    return render(request, "index.html", content)



