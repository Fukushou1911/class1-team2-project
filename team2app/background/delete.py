from django.shortcuts import render, redirect
from django.http import Http404

def delete(request, article_id):
    try:
        article = message.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")

    article.delete()

    return redirect(index)