from django.http import HttpResponseRedirect
from product.forms import CommentForm
from product.models import Comment
from django.contrib import messages


def addcomment(request,id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.product_id = id
            data.save()
            messages.success(request, "Sizning kommentariyangiz qabul qilindi!")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)

