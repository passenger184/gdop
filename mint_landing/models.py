from django.db import models
from django.contrib.auth.models import User


class HeroSection(models.Model):
    title = models.CharField(
        max_length=255, help_text="Main heading text for the hero section")
    subtitle = models.TextField(
        help_text="Subheading text for the hero section")
    button_text = models.CharField(
        max_length=50, help_text="Text for the call-to-action button")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='hero_created_by')
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='hero_updated_by')

    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Section"

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100, help_text="Title of the project")
    subtitle = models.TextField(help_text="Description of the project")
    is_active = models.BooleanField(default=False)
    icon_name = models.CharField(
        max_length=100, help_text="Bootstrap icon class name (e.g., bi-people")
    button_url = models.URLField(
        help_text="URL the button points to", blank=True, null=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='project_created_by')
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='project_updated_by')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title


class Announcement(models.Model):
    title = models.CharField(
        max_length=100, help_text="Title of the announcement")
    sub_title = models.CharField(
        max_length=100, help_text="Subtitle of the announcement")
    description = models.TextField(help_text="Description of the announcement")
    icon_name = models.CharField(
        max_length=100, help_text="Bootstrap icon class name (e.g., bi-people")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='announcement_created_by')
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='announcement_updated_by')

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    title = models.CharField(
        max_length=100, help_text="Title of the about us section")
    description_1 = models.TextField(
        help_text="Description of the about us section")
    description_2 = models.TextField(
        help_text="Description of the about us section")
    bullet_points = models.CharField(
        max_length=255, help_text="Comma separated list of bullet points")
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='about_created_by')
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='about_updated_by')

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"

    def __str__(self):
        return self.title


class NumberStatistic(models.Model):
    title = models.CharField(
        max_length=100, help_text="Title for the statistic (e.g., Users, Projects)")
    value = models.PositiveIntegerField(help_text="Value of the statistic")
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='number_created_by')
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='number_updated_by')

    class Meta:
        verbose_name = "Numbers"
        verbose_name_plural = "Numbers"

    def __str__(self):
        return f"{self.title}: {self.value}"


class FAQ(models.Model):
    question = models.CharField(
        max_length=300, help_text="The frequently asked question")
    answer = models.TextField(help_text="Answer to the question")
    order = models.PositiveIntegerField(
        default=0, help_text="Display order of the FAQ")
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='faq_created_by')
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='faq_updated_by')

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        ordering = ['order']

    def __str__(self):
        return self.question


class ContactUs(models.Model):
    title = models.CharField(
        max_length=100, help_text="Title of the contact us section")
    address = models.CharField(max_length=200, help_text="Address")
    email = models.EmailField(help_text="Email address")
    phone = models.CharField(max_length=10, help_text="Phone number")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='contact_created_by')
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='contact_updated_by')

    def __str__(self):
        return f"{self.email} - {self.phone}"

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"
