from django.core.management.base import BaseCommand
from mint_landing.models import FAQ, AboutUs, Announcement, Figure, GDOPComponent, HeroSection, Resource


class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')
        self.create_hero_section()
        self.create_gdop_components()
        self.create_announcements()
        self.create_about_us()
        self.create_figures()
        self.create_faqs()
        self.create_resources()
        self.stdout.write('Seeding complete.')

    def create_hero_section(self):
        HeroSection.objects.get_or_create(
            title="Government Digital Office Platforms Portal (GDOP)",
            subtitle="A paperless back office system automation. Modern Office | Automated Process | Digital Services",
            button_text="Learn More"
        )
        self.stdout.write('Hero Section created.')

    def create_gdop_components(self):
        components = [
            {
                "title": "Visitors Management System",
                "subtitle": (
                    "Simplify and secure the process of managing visitor interactions and records."
                    "The system ensures a smooth and efficient experience for both visitors and administrators by automating check-ins, maintaining accurate records, and enhancing on-site security."
                ),
                "icon_name": "bi-people",
                "is_active": True,
            },
            {
                "title": "Document Management System (DMS)",
                "subtitle": (
                    "A cloud-based document storage and management system with secure access and sharing capabilities."
                    "Rollout of the DMS across multiple government offices using an in-house developed SaaS model to standardize document handling processes."
                ),
                "icon_name": "bi-file-earmark-text",
                "is_active": True,
            },
            {
                "title": "Planning, Monitoring and Reporting System",
                "subtitle": (
                    "Development of a comprehensive system for strategic planning, resource allocation, performance tracking, and reporting."
                    "Enhance the effectiveness, efficiency, and accuracy of data collection, analysis, and reporting processes."
                ),
                "icon_name": "bi-bar-chart",
                "is_active": False,
            },
            {
                "title": "Transport Management System",
                "subtitle": (
                    "An in-house developed system for managing transport logistics, vehicle scheduling, fleet tracking, and maintenance."
                    "Automation of transport-related processes to improve cost-efficiency and reduce downtime."
                ),
                "icon_name": "bi-truck",
                "is_active": False,
            },
            {
                "title": "Call Center System",
                "subtitle": (
                    "Streamline a centralized customer service center by utilizing state-of-the-art customer success digital tools."
                    "Implementation of a centralized Call Center to manage communications, service requests, and feedback from both internal staff and external stakeholders."
                ),
                "icon_name": "bi-telephone",
                "is_active": False,
            },
        ]
        for component in components:
            GDOPComponent.objects.get_or_create(
                title=component["title"],
                subtitle=component["subtitle"],
                icon_name=component["icon_name"],
                is_active=component["is_active"],
            )
            self.stdout.write(f'Component "{component["title"]}" created.')

    def create_announcements(self):
        Announcement.objects.get_or_create(
            title="User Training Session",
            sub_title="Upcoming Training on Platform Features",
            description="Join us for a comprehensive training session on how to maximize your use of the platform. Date: March 20th at 2:00 PM.",
            icon_name="bi-journal-bookmark"
        )
        self.stdout.write('Announcements created.')

    def create_about_us(self):
        AboutUs.objects.get_or_create(
            title="Empowering Ethiopia through innovation and technology for a prosperous and inclusive future.",
            description_1="The Ministry of Innovation and Technology is at the forefront of driving Ethiopia's transformation into a digital economy. By fostering innovation and building local capacity, we aim to create jobs, enhance the country’s competitiveness, and inspire limitless imagination.",
            description_2="We work to create plans for digital growth and support local talent to ensure technology and innovation drive Ethiopia's success. With a focus on hard work, creativity, and a passion for learning, we aim to make a positive impact on society.",
            bullet_points="Leading Ethiopia's digital transformation for sustainable growth., Promoting research and innovation to drive impactful solutions., Building a strong foundation for future generations."
        )
        self.stdout.write('About Us created.')

    def create_figures(self):
        figures = [
            {
                "title": "Institutions Supported",
                "value": 132
            },
            {
                "title": "Projects",
                "value": 521
            },
            {
                "title": "Mentorship Hours",
                "value": 1453
            },
            {
                "title": "Workers",
                "value": 52
            }
        ]
        for figure in figures:
            Figure.objects.get_or_create(
                title=figure["title"],
                value=figure['value']
            )
            self.stdout.write(f'Figure {figure['title']} created.')

    def create_faqs(self):
        faqs = [
            {
                "question": "How do I access the platform?",
                "answer": "You can access the platform through the internal intranet  link provided by the IT department.",
                "order": 1
            },
            {
                "question": "Can I use the platform on any device?",
                "answer": "Yes, it is accessible on all devices connected to the ministry’s intranet. For the best experience, use a modern browser like Chrome or Edge.",
                "order": 2
            },
            {
                "question": "Can I access the platform remotely?",
                "answer": "No, the platform is restricted to the ministry’s internal network and can only be accessed on-premises.",
                "order": 3
            },
            {
                "question": "How do I find an older document?",
                "answer": "Use the search feature and apply filters like date, department, or document type to locate older files.",
                "order": 4
            },
            {
                "question": "What if I cannot open a document?",
                "answer": "Check your permissions for the document. If you are authorized and still face issues, report it to IT support.",
                "order": 5
            },
            {
                "question": "What should I do if a contact’s information is outdated?",
                "answer": "You can update the details if you have editing  permissions. Otherwise, notify the responsible department.",
                "order": 6
            },
            {
                "question": "What should I do if the platform isn’t loading?",
                "answer": "Check your network connection and ensure you are connected to the ministry’s intranet. If the issue persists, contact IT support.",
                "order": 7
            },
            {
                "question": "How do I report a bug or error in the system?",
                "answer": "Use the 'Report Issue' option in the 'Contact Us' section and provide detailed information about the issue, including screenshots if possible.",
                "order": 8
            },
            {
                "question": "Is there a way to recover deleted data?",
                "answer": "Yes, contact the IT team immediately. Data recovery may be possible depending on the system's backup policies.",
                "order": 9
            },
        ]

        for faq in faqs:
            FAQ.objects.get_or_create(
                question=faq["question"],
                answer=faq["answer"],
                order=faq['order']
            )
            self.stdout.write(f'FAQ "{faq["question"]}" created.')

    def create_resources(self):
        Resource.objects.get_or_create(
            title="The government merged the former...",
            address="Lisie G/Mariam Street",
            email="contact@mint.gov.et",
            phone="0118132192"
        )
        self.stdout.write('Resources created.')
