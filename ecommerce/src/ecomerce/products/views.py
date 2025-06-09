# from django.shortcuts import render, get_object_or_404
# from .models import TV, Speaker
#
#
# def tv_list(request):
#     tvs = TV.objects.all()
#     return render(request, "products/tv_list.html", {"tvs": tvs})
#
#
# def tv_detail(request, tv_id):
#     tv = get_object_or_404(TV, id=tv_id)
#     return render(request, "products/tv_detail.html", {"tv": tv})
#
#
# def speaker_list(request):
#     speakers = Speaker.objects.all()
#     return render(request, "speakers/speaker_list.html", {"speakers": speakers})
#
#
# def speaker_detail(request, pk):
#     speaker = get_object_or_404(Speaker, pk=pk)
#     return render(request, "speakers/speaker_detail.html", {"speaker": speaker})
def product_list():
    return None