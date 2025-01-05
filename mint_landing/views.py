import json
import os
from django.conf import settings
from django.http import HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from mint_landing.models import FAQ, AboutUs, Announcement, Resource, HeroSection, Figure, GDOPComponent, SupportRequest

# Render the homepage


def home(request):
    hero_section = HeroSection.objects.last()
    projects = GDOPComponent.objects.all()
    announcements = Announcement.objects.all()
    about_us = AboutUs.objects.last()
    about_us_items = AboutUs.objects.last().bullet_points.split(',')
    numbers = Figure.objects.all()
    faqs = FAQ.objects.all()
    contact_us = Resource.objects.last()
    return render(
        request, 'index.html',
        {'hero_section': hero_section,
         'projects': projects,
         'announcements': announcements,
         'about_us': about_us,
         'about_us_items': about_us_items,
         'numbers': numbers,
         'faqs': faqs,
         'contact_us': contact_us,
         }
    )


def news(request):
    return render(request, 'news.html')


def announcement_detail(request, id):
    announcement = get_object_or_404(Announcement, id=id)
    return render(request, 'announcement.html', {'announcement': announcement})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def submit_support_request(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        support_type = request.POST.get('supportType')
        description = request.POST.get('description')
        attachment = request.FILES.get('attachment')
        urgency = request.POST.get('urgency')

        SupportRequest.objects.create(
            name=name,
            email=email,
            support_type=support_type,
            description=description,
            attachment=attachment,
            urgency=urgency,
        )

        return redirect('success_view')
    return render(request, 'contact.html')


def success_view(request):
    return render(request, 'support_request_success.html')


def v_m_s(request):
    return render(request, 'vission.html')


def o_s(request):
    return render(request, 'structure.html')


def p_d(request):
    return render(request, 'power.html')

# Load translations from the specified language file


def load_translation(language_code):
    translations_dir = os.path.join(settings.BASE_DIR, 'translations')
    lang_file_mapping = {
        "en": "eng.json",
        "am": "amh.json",
    }

    json_file = lang_file_mapping.get(language_code)

    if not json_file:
        return None, {"error": "Language not supported"}, 400

    full_path = os.path.join(translations_dir, json_file)

    try:
        with open(full_path, 'r', encoding='utf-8') as file:
            translations = json.load(file)
        return translations, None, 200
    except FileNotFoundError:
        return None, {"error": "Translation file not found"}, 404

# Handle translation requests


def get_translations(request):
    # Default to English if no lang parameter
    lang = request.GET.get("lang", "en")
    translations, error_response, status_code = load_translation(lang)

    if error_response:
        return JsonResponse(error_response, status=status_code)

    return JsonResponse(translations)
