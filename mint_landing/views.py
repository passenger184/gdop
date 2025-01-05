import json
import os
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

# Render the homepage
def home(request):
    return render(request, 'index.html')

def news(request):
    return render(request, 'news.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

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
    lang = request.GET.get("lang", "en")  # Default to English if no lang parameter
    translations, error_response, status_code = load_translation(lang)

    if error_response:
        return JsonResponse(error_response, status=status_code)

    return JsonResponse(translations)



