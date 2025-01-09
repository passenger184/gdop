import json
import os
from django.conf import settings
from django.http import FileResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from mint_landing.models import FAQ, AboutUs, Announcement, AboutUsFooter, FooterContent, PDFResource, HeroSection, Figure, GDOPComponent, SocialLink, SupportRequest, TeamMember, UsefulLink

# Render the homepage


def home(request):
    hero_section = HeroSection.objects.last()
    projects = GDOPComponent.objects.all().order_by("-is_active")
    announcements = Announcement.objects.all()
    about_us = AboutUs.objects.last()
    about_us_items = AboutUs.objects.last().bullet_points.split(',')
    numbers = Figure.objects.all()
    faqs = FAQ.objects.all()
    resources = PDFResource.objects.all()
    members = TeamMember.objects.all()

    footer_content = FooterContent.objects.first()
    social_links = SocialLink.objects.all()
    useful_links = UsefulLink.objects.all()
    focus_areas = AboutUsFooter.objects.all()
    return render(
        request, 'index.html',
        {'hero_section': hero_section,
         'projects': projects,
         'announcements': announcements,
         'about_us': about_us,
         'about_us_items': about_us_items,
         'numbers': numbers,
         'faqs': faqs,
         'resources': resources,
         'team_members': members,
         'footer_content': footer_content,
         'social_links': social_links,
         'useful_links': useful_links,
         'focus_areas': focus_areas,
         }
    )


def news(request):
    footer_content = FooterContent.objects.first()
    social_links = SocialLink.objects.all()
    useful_links = UsefulLink.objects.all()
    focus_areas = AboutUsFooter.objects.all()
    return render(request, 'news.html', {'footer_content': footer_content,
                                         'social_links': social_links,
                                         'useful_links': useful_links,
                                         'focus_areas': focus_areas, })


def announcement_detail(request, id):
    announcement = get_object_or_404(Announcement, id=id)
    footer_content = FooterContent.objects.first()
    social_links = SocialLink.objects.all()
    useful_links = UsefulLink.objects.all()
    focus_areas = AboutUsFooter.objects.all()
    return render(request, 'announcement.html', {'announcement': announcement, 'footer_content': footer_content,
                                                 'social_links': social_links,
                                                 'useful_links': useful_links,
                                                 'focus_areas': focus_areas, })


def about(request):
    footer_content = FooterContent.objects.first()
    social_links = SocialLink.objects.all()
    useful_links = UsefulLink.objects.all()
    focus_areas = AboutUsFooter.objects.all()
    return render(request, 'about.html', {'footer_content': footer_content,
                                          'social_links': social_links,
                                          'useful_links': useful_links,
                                          'focus_areas': focus_areas, })


def contact(request):
    footer_content = FooterContent.objects.first()
    social_links = SocialLink.objects.all()
    useful_links = UsefulLink.objects.all()
    focus_areas = AboutUsFooter.objects.all()
    return render(request, 'contact.html', {'footer_content': footer_content,
                                            'social_links': social_links,
                                            'useful_links': useful_links,
                                            'focus_areas': focus_areas, })


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
    footer_content = FooterContent.objects.first()
    social_links = SocialLink.objects.all()
    useful_links = UsefulLink.objects.all()
    focus_areas = AboutUsFooter.objects.all()
    return render(request, 'support_request_success.html', {'footer_content': footer_content,
                  'social_links': social_links,
                                                            'useful_links': useful_links,
                                                            'focus_areas': focus_areas, })


def v_m_s(request):
    footer_content = FooterContent.objects.first()
    social_links = SocialLink.objects.all()
    useful_links = UsefulLink.objects.all()
    focus_areas = AboutUsFooter.objects.all()
    return render(request, 'vission.html', {'footer_content': footer_content,
                                            'social_links': social_links,
                                            'useful_links': useful_links,
                                            'focus_areas': focus_areas, })


def o_s(request):
    footer_content = FooterContent.objects.first()
    social_links = SocialLink.objects.all()
    useful_links = UsefulLink.objects.all()
    focus_areas = AboutUsFooter.objects.all()
    return render(request, 'structure.html', {'footer_content': footer_content,
                                              'social_links': social_links,
                                              'useful_links': useful_links,
                                              'focus_areas': focus_areas, })


def p_d(request):
    footer_content = FooterContent.objects.first()
    social_links = SocialLink.objects.all()
    useful_links = UsefulLink.objects.all()
    focus_areas = AboutUsFooter.objects.all()
    return render(request, 'power.html', {'footer_content': footer_content,
                                          'social_links': social_links,
                                          'useful_links': useful_links,
                                          'focus_areas': focus_areas, })

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


def component_detail(request, id):
    component = get_object_or_404(GDOPComponent, id=id)
    advantages = component.key_advantages.split(',')
    return render(request, 'component.html', {'component': component, 'advantages': advantages})


def resource_preview(request, id):
    resource = get_object_or_404(PDFResource, pk=id)
    return render(request, 'resource_preview.html', {'resource': resource})


def resource_download(request, id):
    resource = get_object_or_404(PDFResource, pk=id)
    response = FileResponse(resource.file.open(
        'rb'), as_attachment=True, filename=resource.file.name)
    return response


def team_members(request):
    team_members = TeamMember.objects.all()
    return render(request, 'team.html', {'team_members': team_members})
