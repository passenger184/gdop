import json
import os
from ftplib import FTP
from io import BytesIO

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from django.db.models import F
from django.http import FileResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from mint_landing.models import (
    FAQ,
    AboutUs,
    AboutUsFooter,
    Announcement,
    FooterContent,
    FTPConfiguration,
    GDOPModule,
    PDFResource,
    SocialLink,
    SupportRequest,
    TeamMember,
    UsefulLink,
)

# Render the homepage


@login_required
def home(request):
    # Function to create a default slide entry from an image filename
    def create_slide_from_image(image_name, image_content):
        # Save the image content to the media folder
        file_path = os.path.join(settings.MEDIA_ROOT, image_name)
        with default_storage.open(file_path, "wb") as file:
            file.write(image_content)

        # Generate media URL for the image
        image_url = os.path.join(settings.MEDIA_URL, image_name)
        return {
            "image_url": image_url,
            "title": "",
            "subtitle": "",
            "cta_text": "",
            "cta_link": "",
        }

    # Initialize slides
    slides = [
        {
            "image_url": "/static/assets/img/first_slide.jpg",
            "title": "Government Digital Office Platforms Portal (GDOP)",
            "subtitle": "Modern Office | Automated Process | Online Services",
            "cta_text": "Learn More",
            "cta_link": "/about",
        }
    ]

    # Check if metadata file exists on the FTP server
    try:
        # Retrieve FTP configuration from the database
        ftp_config = FTPConfiguration.objects.first()

        ftp_host = ftp_config.host
        ftp_port = ftp_config.port
        ftp_user = ftp_config.user
        ftp_pass = ftp_config.password
        network_folder_path = ftp_config.network_folder_path
        metadata_file = ftp_config.metadata_file

        # Connect to the FTP server
        ftp = FTP()
        ftp.connect(ftp_host, ftp_port)
        ftp.login(user=ftp_user, passwd=ftp_pass)

        ftp.cwd(network_folder_path)
        ftp.nlst()
        if metadata_file in ftp.nlst():
            # Read metadata.json from FTP
            with BytesIO() as bio:
                ftp.retrbinary(f"RETR {metadata_file}", bio.write)
                bio.seek(0)
                dynamic_slides = json.load(bio)

            for slide in dynamic_slides:
                image_name = slide["image_name"]
                with BytesIO() as image_bio:
                    ftp.retrbinary(f"RETR {image_name}", image_bio.write)
                    image_bio.seek(0)
                    image_content = image_bio.read()

                slide["image_url"] = create_slide_from_image(image_name, image_content)[
                    "image_url"
                ]
                slides.append(slide)
        else:
            # Fallback: List image files in the folder
            image_files = ftp.nlst()
            for image_name in image_files:
                if image_name.lower().endswith((".png", ".jpg", ".jpeg")):
                    with BytesIO() as image_bio:
                        ftp.retrbinary(f"RETR {image_name}", image_bio.write)
                        image_bio.seek(0)
                        image_content = image_bio.read()

                    slides.append(create_slide_from_image(image_name, image_content))
        ftp.quit()
    except Exception as e:
        print(f"Error accessing FTP: {e}")

    # Add the last static slides
    slides.extend(
        [
            {
                "image_url": "/static/assets/img/last_slide.jpg",
                "title": "Feedback and Support",
                "subtitle": "We value your feedback. Get in touch!",
                "cta_text": "Contact Us",
                "cta_link": "/request-support",
            },
            {
                "image_url": "/static/assets/img/first_slide.jpg",
                "title": "Government Digital Office Platforms Portal (GDOP)",
                "subtitle": "Modern Office | Automated Process | Online Services",
                "cta_text": "Learn More",
                "cta_link": "/about",
            },
        ]
    )

    projects = GDOPModule.objects.all().order_by("-is_active")
    announcements = Announcement.objects.all()
    about_us = AboutUs.objects.last()
    about_us_items = AboutUs.objects.last().bullet_points.split(",")
    faqs = FAQ.objects.all()
    resources = PDFResource.objects.filter(is_featured=True)
    members = TeamMember.objects.all()

    footer_content = FooterContent.objects.first()
    social_links = SocialLink.objects.all()
    useful_links = UsefulLink.objects.all()
    focus_areas = AboutUsFooter.objects.all()

    return render(
        request,
        "index.html",
        {
            "slides": slides,
            "projects": projects,
            "announcements": announcements,
            "about_us": about_us,
            "about_us_items": about_us_items,
            "faqs": faqs,
            "resources": resources,
            "team_members": members,
            "footer_content": footer_content,
            "social_links": social_links,
            "useful_links": useful_links,
            "focus_areas": focus_areas,
        },
    )


@login_required
def resources(request):
    footer_content = FooterContent.objects.first()
    social_links = SocialLink.objects.all()
    useful_links = UsefulLink.objects.all()
    focus_areas = AboutUsFooter.objects.all()

    resource_list = PDFResource.objects.annotate(filename=F("file")).order_by(
        "created_at"
    )

    per_page = request.GET.get("per_page", 5)
    try:
        per_page = int(per_page)
    except ValueError:
        per_page = 5

    paginator = Paginator(resource_list, per_page)

    page = request.GET.get("page")
    try:
        resources = paginator.page(page)
    except PageNotAnInteger:
        resources = paginator.page(1)
    except EmptyPage:
        resources = paginator.page(paginator.num_pages)

    return render(
        request,
        "resources.html",
        {
            "footer_content": footer_content,
            "social_links": social_links,
            "useful_links": useful_links,
            "focus_areas": focus_areas,
            "resources": resources,
        },
    )


@login_required
def news(request):
    footer_content = FooterContent.objects.first()
    social_links = SocialLink.objects.all()
    useful_links = UsefulLink.objects.all()
    focus_areas = AboutUsFooter.objects.all()
    return render(
        request,
        "news.html",
        {
            "footer_content": footer_content,
            "social_links": social_links,
            "useful_links": useful_links,
            "focus_areas": focus_areas,
        },
    )


@login_required
def announcement_detail(request, id):
    announcement = get_object_or_404(Announcement, id=id)
    footer_content = FooterContent.objects.first()
    social_links = SocialLink.objects.all()
    useful_links = UsefulLink.objects.all()
    focus_areas = AboutUsFooter.objects.all()
    return render(
        request,
        "announcement.html",
        {
            "announcement": announcement,
            "footer_content": footer_content,
            "social_links": social_links,
            "useful_links": useful_links,
            "focus_areas": focus_areas,
        },
    )


@login_required
def about(request):
    footer_content = FooterContent.objects.first()
    social_links = SocialLink.objects.all()
    useful_links = UsefulLink.objects.all()
    focus_areas = AboutUsFooter.objects.all()

    active_modules = GDOPModule.objects.filter(is_active=True)
    return render(
        request,
        "about.html",
        {
            "footer_content": footer_content,
            "social_links": social_links,
            "useful_links": useful_links,
            "focus_areas": focus_areas,
            "modules": active_modules,
        },
    )


@login_required
def contact(request):
    footer_content = FooterContent.objects.first()
    social_links = SocialLink.objects.all()
    useful_links = UsefulLink.objects.all()
    focus_areas = AboutUsFooter.objects.all()
    return render(
        request,
        "contact.html",
        {
            "footer_content": footer_content,
            "social_links": social_links,
            "useful_links": useful_links,
            "focus_areas": focus_areas,
        },
    )


@login_required
def submit_support_request(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        support_type = request.POST.get("supportType")
        description = request.POST.get("description")
        attachment = request.FILES.get("attachment")
        urgency = request.POST.get("urgency")

        SupportRequest.objects.create(
            name=name,
            email=email,
            support_type=support_type,
            description=description,
            attachment=attachment,
            urgency=urgency,
        )

        return redirect("success_view")
    return render(request, "contact.html")


@login_required
def success_view(request):
    footer_content = FooterContent.objects.first()
    social_links = SocialLink.objects.all()
    useful_links = UsefulLink.objects.all()
    focus_areas = AboutUsFooter.objects.all()
    return render(
        request,
        "support_request_success.html",
        {
            "footer_content": footer_content,
            "social_links": social_links,
            "useful_links": useful_links,
            "focus_areas": focus_areas,
        },
    )


@login_required
def v_m_s(request):
    footer_content = FooterContent.objects.first()
    social_links = SocialLink.objects.all()
    useful_links = UsefulLink.objects.all()
    focus_areas = AboutUsFooter.objects.all()
    return render(
        request,
        "vission.html",
        {
            "footer_content": footer_content,
            "social_links": social_links,
            "useful_links": useful_links,
            "focus_areas": focus_areas,
        },
    )


@login_required
def o_s(request):
    footer_content = FooterContent.objects.first()
    social_links = SocialLink.objects.all()
    useful_links = UsefulLink.objects.all()
    focus_areas = AboutUsFooter.objects.all()
    return render(
        request,
        "structure.html",
        {
            "footer_content": footer_content,
            "social_links": social_links,
            "useful_links": useful_links,
            "focus_areas": focus_areas,
        },
    )


@login_required
def p_d(request):
    footer_content = FooterContent.objects.first()
    social_links = SocialLink.objects.all()
    useful_links = UsefulLink.objects.all()
    focus_areas = AboutUsFooter.objects.all()
    return render(
        request,
        "power.html",
        {
            "footer_content": footer_content,
            "social_links": social_links,
            "useful_links": useful_links,
            "focus_areas": focus_areas,
        },
    )


# Load translations from the specified language file
@login_required
def load_translation(language_code):
    translations_dir = os.path.join(settings.BASE_DIR, "translations")
    lang_file_mapping = {
        "en": "eng.json",
        "am": "amh.json",
    }

    json_file = lang_file_mapping.get(language_code)

    if not json_file:
        return None, {"error": "Language not supported"}, 400

    full_path = os.path.join(translations_dir, json_file)

    try:
        with open(full_path, "r", encoding="utf-8") as file:
            translations = json.load(file)
        return translations, None, 200
    except FileNotFoundError:
        return None, {"error": "Translation file not found"}, 404


# Handle translation requests
@login_required
def get_translations(request):
    # Default to English if no lang parameter
    lang = request.GET.get("lang", "en")
    translations, error_response, status_code = load_translation(lang)

    if error_response:
        return JsonResponse(error_response, status=status_code)

    return JsonResponse(translations)


@login_required
def component_detail(request, id):
    component = get_object_or_404(GDOPModule, id=id)
    advantages = component.key_advantages.split(",")
    return render(
        request, "component.html", {"component": component, "advantages": advantages}
    )


@login_required
def resource_download(request, id):
    resource = get_object_or_404(PDFResource, pk=id)

    resource.download_count = models.F("download_count") + 1
    resource.save(update_fields=["download_count"])

    response = FileResponse(
        resource.file.open("rb"), as_attachment=True, filename=resource.file.name
    )
    return response


@login_required
def team_members(request):
    team_members = TeamMember.objects.all()
    return render(request, "team.html", {"team_members": team_members})


def custom_login_view(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "auth/login.html")


@login_required
def profile_view(request):
    return render(request, "profile.html")


def logout_view(request):
    logout(request)
    return redirect("login")
