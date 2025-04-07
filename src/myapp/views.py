from django.http import HttpResponse
from django.shortcuts import render
import pathlib

from visits.models import PageVisits

this_dir = pathlib.Path(__file__).resolve().parent


def home_view(request, *args, **kwargs):
    qs_total = PageVisits.objects.all()
    qs_page = PageVisits.objects.filter(path=request.path)
    titulo = "Início"
    corpo = "Isso é um teste TESTADO!"
    context = {
        "titulo": titulo,
        "corpo": corpo,
        "page_visits": qs_page.count(),
        "total_visits": qs_total.count(),
    }

    html_ = "index.html"

    PageVisits.objects.create(path=request.path)
    return render(request, html_, context)


def about_view(request, *args, **kwargs):
    titulo = "Sobre"
    corpo = "Sobre a ferramenta"
    context = {
        "titulo": titulo,
        "corpo": corpo,
    }

    html_ = "about.html"
    return render(request, html_, context)


def old_home_view(request, *args, **kwargs):

    titulo = "Apascentar Kids!"
    corpo = "Isso é um teste!"
    context = {
        "titulo": titulo,
        "corpo": corpo,
    }

    html_ = """<!DOCTYPE html>
            <html lang="en">

                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>{titulo}</title>
                </head>

                <body>
                    <h1>Isso é uma página!</h1>
                    meu corpo: {corpo}
                </body>

            </html>""".format(
        **context
    )

    return HttpResponse(html_)
