import os

from django.contrib.auth.models import User
from django.db import models


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="%(class)s_created_by"
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="%(class)s_updated_by"
    )

    class Meta:
        abstract = True


class GDOPModule(AbstractBaseModel):
    title = models.CharField(max_length=100, help_text="Title of the component")
    subtitle = models.CharField(max_length=100, help_text="A very short description")
    description = models.TextField(help_text="Description of the component")
    key_advantages = models.CharField(
        max_length=500, help_text="Comma separated list of advantages"
    )
    image = models.ImageField(
        upload_to="uploads/components/", help_text="Image for the component"
    )
    redirect_url = models.URLField()
    is_active = models.BooleanField(default=False)
    icon_name = models.CharField(
        max_length=100, help_text="Bootstrap icon class name (e.g., bi-people"
    )

    class Meta:
        verbose_name = "GDOP Module"
        verbose_name_plural = "GDOP Modules"

    def __str__(self):
        return self.title


class Announcement(AbstractBaseModel):
    title = models.CharField(max_length=100, help_text="Title of the announcement")
    sub_title = models.CharField(
        max_length=100, help_text="Subtitle of the announcement"
    )
    image = models.ImageField(
        upload_to="uploads/announcements/",
        blank=True,
        null=True,
        help_text="Image for the announcement",
    )
    description = models.TextField(help_text="Description of the announcement")
    icon_name = models.CharField(
        max_length=100, help_text="Bootstrap icon class name (e.g., bi-people"
    )

    def __str__(self):
        return self.title


class AboutUs(AbstractBaseModel):
    title = models.CharField(max_length=100, help_text="Title of the about us section")
    description_1 = models.TextField(help_text="Description of the about us section")
    description_2 = models.TextField(help_text="Description of the about us section")
    bullet_points = models.CharField(
        max_length=255, help_text="Comma separated list of bullet points"
    )

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"

    def __str__(self):
        return self.title


class FAQ(AbstractBaseModel):
    question = models.CharField(
        max_length=300, help_text="The frequently asked question"
    )
    answer = models.TextField(help_text="Answer to the question")
    order = models.PositiveIntegerField(default=0, help_text="Display order of the FAQ")

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        ordering = ["order"]

    def __str__(self):
        return self.question


class SupportType(models.TextChoices):
    TECHNICAL = "technical", "Technical Issue"
    SYSTEM_ACCESS = "system_access", "System Access"
    GENERAL = "general", "General Inquiry"
    FEEDBACK = "feedback", "Feedback"
    OTHER = "other", "Other"


class UrgencyLevel(models.TextChoices):
    LOW = "low", "Low"
    MEDIUM = "medium", "Medium"
    HIGH = "high", "High"
    CRITICAL = "critical", "Critical"


class SupportRequest(AbstractBaseModel):
    PENDING = "pending"
    RESOLVED = "resolved"
    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (RESOLVED, "Resolved"),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    support_type = models.CharField(max_length=50, choices=SupportType.choices)
    description = models.TextField()
    attachment = models.FileField(
        upload_to="uploads/support_requests/", blank=True, null=True
    )
    urgency = models.CharField(max_length=10, choices=UrgencyLevel.choices)
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)

    def __str__(self):
        return f"{self.name} - {self.support_type}"


class ResourceCategory(AbstractBaseModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Resource Category"
        verbose_name_plural = "Resource Categories"

    def __str__(self):
        return self.name


class PDFResource(AbstractBaseModel):
    icon_name = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to="uploads/pdf_resources/", blank=True, null=True)
    category = models.ForeignKey(
        ResourceCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="pdf_resources",
    )
    is_featured = models.BooleanField(default=False)
    download_count = models.PositiveIntegerField(default=0)

    @property
    def filesize(self):
        if self.file and self.file.path:
            size_in_bytes = os.path.getsize(self.file.path)
            size_in_mb = size_in_bytes / (1024 * 1024)
            return round(size_in_mb, 2)
        return 0

    class Meta:
        verbose_name = "PDF Resource"
        verbose_name_plural = "PDF Resources"

    def __str__(self):
        return self.title


class TeamMember(AbstractBaseModel):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    project = models.ForeignKey(GDOPModule, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="uploads/team_members/", blank=True, null=True)

    def __str__(self):
        return self.name


class SocialLink(AbstractBaseModel):
    name = models.CharField(max_length=50)
    icon_class = models.CharField(
        max_length=50,
        help_text="CSS class for the social media icon (e.g., 'bi bi-twitter-x')",
    )
    url = models.URLField()

    def __str__(self):
        return self.name


class UsefulLink(AbstractBaseModel):
    name = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.name


class AboutUsFooter(AbstractBaseModel):
    name = models.CharField(max_length=50)
    url = models.URLField()

    class Meta:
        verbose_name = "About Us (Footer)"
        verbose_name_plural = "About Us (Footer)"

    def __str__(self):
        return self.name


class FooterContent(AbstractBaseModel):
    about_text = models.TextField()
    logo_image = models.ImageField(upload_to="uploads/footer/", blank=True, null=True)
    contact_address_line1 = models.CharField(max_length=255)
    contact_address_line2 = models.CharField(max_length=255, blank=True, null=True)
    contact_address_line3 = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    copyright_text = models.CharField(max_length=255)

    def __str__(self):
        return "Footer Content"


class FTPConfiguration(AbstractBaseModel):
    host = models.CharField(max_length=255, help_text="FTP Server Host")
    port = models.IntegerField(help_text="FTP Server Port")
    user = models.CharField(max_length=255, help_text="FTP User", blank=True, null=True)
    password = models.CharField(
        max_length=255, help_text="FTP Password", blank=True, null=True
    )
    network_folder_path = models.CharField(
        max_length=255, help_text="Network Folder Path"
    )
    metadata_file = models.CharField(
        max_length=255, help_text="Metadata File Name", default="metadata.json"
    )

    class Meta:
        verbose_name = "FTP Configuration"
        verbose_name_plural = "FTP Configurations"

    def __str__(self):
        return f"FTP Configuration: {self.host}:{self.port}"
