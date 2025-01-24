from django.core.management.base import BaseCommand

from mint_landing.models import (
    FAQ,
    AboutUs,
    Announcement,
    GDOPModule,
    PDFResource,
    TeamMember,
)


class Command(BaseCommand):
    help = "Seed the database with initial data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")
        self.create_gdop_components()
        self.create_announcements()
        self.create_about_us()
        self.create_faqs()
        self.create_pdf_resources()
        self.create_team_members()
        self.stdout.write("Seeding complete.")

    def create_gdop_components(self):
        components = [
            {
                "title": "Visitors Management System",
                "subtitle": "Simplify managing visitors.",
                "description": "Simplify and secure the process of managing visitor interactions and records.The system ensures a smooth and efficient experience for both visitors and administrators by automating check-ins, maintaining accurate records, and enhancing on-site security.",
                "key_advantages": "Improved Security,Time Saving,Efficient Tracking,Enhanced Organization,Real-Time Updates",
                "icon_name": "bi-people",
                "is_active": True,
            },
            {
                "title": "Document Management System (DMS)",
                "subtitle": "A cloud-based document management",
                "description": "A cloud-based document storage and management system with secure access and sharing capabilities.Rollout of the DMS across multiple government offices using an in-house developed SaaS model to standardize document handling processes.",
                "key_advantages": "Improved Security,Time Saving,Efficient Tracking,Enhanced Organization,Real-Time Updates",
                "icon_name": "bi-file-earmark-text",
                "is_active": True,
            },
            {
                "title": "Planning, Monitoring and Reporting System",
                "subtitle": "System for strategic planning and reporting.",
                "description": "A system for strategic planning, monitoring, and reporting that integrates various government departments and agencies. Automate and streamline processes for managing, analyzing, and communicating strategic plans and performance metrics.",
                "key_advantages": "Improved Security,Time Saving,Efficient Tracking,Enhanced Organization,Real-Time Updates",
                "icon_name": "bi-bar-chart",
                "is_active": False,
            },
            {
                "title": "Transport Management System",
                "subtitle": "System for managing transport logistics",
                "description": "A system for managing transport logistics that includes sourcing, procurement, delivery, and inventory management. Implement a centralized transport management system to streamline transport operations, optimize resources, and enhance efficiency.",
                "key_advantages": "Improved Security,Time Saving,Efficient Tracking,Enhanced Organization,Real-Time Updates",
                "icon_name": "bi-truck",
                "is_active": False,
            },
            {
                "title": "Call Center System",
                "subtitle": "Centralized customer service",
                "description": "A centralized customer service system that enables easy communication, tracking, and resolution of customer inquiries. Implement a robust call center system to streamline customer service operations, optimize resources, and enhance efficiency.",
                "key_advantages": "Improved Security,Time Saving,Efficient Tracking,Enhanced Organization,Real-Time Updates",
                "icon_name": "bi-telephone",
                "is_active": False,
            },
        ]
        for component in components:
            GDOPModule.objects.get_or_create(
                title=component["title"],
                subtitle=component["subtitle"],
                description=component["description"],
                key_advantages=component["key_advantages"],
                icon_name=component["icon_name"],
                is_active=component["is_active"],
            )
            self.stdout.write(f'Component "{component["title"]}" created.')

    def create_announcements(self):
        Announcement.objects.get_or_create(
            title="User Training Session",
            sub_title="Upcoming Training on Platform Features",
            description="Join us for a comprehensive training session on how to maximize your use of the platform. Date: March 20th at 2:00 PM.",
            icon_name="bi-journal-bookmark",
        )
        self.stdout.write("Announcements created.")

    def create_about_us(self):
        AboutUs.objects.get_or_create(
            title="Empowering Ethiopia through innovation and technology for a prosperous and inclusive future.",
            description_1="The Ministry of Innovation and Technology is at the forefront of driving Ethiopia's transformation into a digital economy. By fostering innovation and building local capacity, we aim to create jobs, enhance the country’s competitiveness, and inspire limitless imagination.",
            description_2="We work to create plans for digital growth and support local talent to ensure technology and innovation drive Ethiopia's success. With a focus on hard work, creativity, and a passion for learning, we aim to make a positive impact on society.",
            bullet_points="Leading Ethiopia's digital transformation for sustainable growth., Promoting research and innovation to drive impactful solutions., Building a strong foundation for future generations.",
        )
        self.stdout.write("About Us created.")

    def create_faqs(self):
        faqs = [
            {
                "question": "How do I access the platform?",
                "answer": "You can access the platform through the internal intranet  link provided by the IT department.",
                "order": 1,
            },
            {
                "question": "Can I use the platform on any device?",
                "answer": "Yes, it is accessible on all devices connected to the ministry’s intranet. For the best experience, use a modern browser like Chrome or Edge.",
                "order": 2,
            },
            {
                "question": "Can I access the platform remotely?",
                "answer": "No, the platform is restricted to the ministry’s internal network and can only be accessed on-premises.",
                "order": 3,
            },
            {
                "question": "How do I find an older document?",
                "answer": "Use the search feature and apply filters like date, department, or document type to locate older files.",
                "order": 4,
            },
            {
                "question": "What if I cannot open a document?",
                "answer": "Check your permissions for the document. If you are authorized and still face issues, report it to IT support.",
                "order": 5,
            },
            {
                "question": "What should I do if a contact’s information is outdated?",
                "answer": "You can update the details if you have editing  permissions. Otherwise, notify the responsible department.",
                "order": 6,
            },
            {
                "question": "What should I do if the platform isn’t loading?",
                "answer": "Check your network connection and ensure you are connected to the ministry’s intranet. If the issue persists, contact IT support.",
                "order": 7,
            },
            {
                "question": "How do I report a bug or error in the system?",
                "answer": "Use the 'Report Issue' option in the 'Contact Us' section and provide detailed information about the issue, including screenshots if possible.",
                "order": 8,
            },
            {
                "question": "Is there a way to recover deleted data?",
                "answer": "Yes, contact the IT team immediately. Data recovery may be possible depending on the system's backup policies.",
                "order": 9,
            },
        ]

        for faq in faqs:
            FAQ.objects.get_or_create(
                question=faq["question"], answer=faq["answer"], order=faq["order"]
            )
            self.stdout.write(f'FAQ "{faq["question"]}" created.')

    def create_pdf_resources(self):
        resources = [
            {
                "icon_name": "file-earmark-text",
                "title": "Visitor Form",
                "description": "For first-time visitors to fill out necessary details.",
            },
            {
                "icon_name": "book",
                "title": "Employee Manual",
                "description": "Policies, rules, and guidelines for employees.",
            },
            {
                "icon_name": "file-earmark-spreadsheet",
                "title": "Budget Template",
                "description": "Use this template to prepare budgets effectively.",
            },
            {
                "icon_name": "calendar-check",
                "title": "Event Checklist",
                "description": "A step-by-step checklist for organizing events.",
            },
            {
                "icon_name": "clipboard",
                "title": "Meeting Minutes",
                "description": "Template for recording meeting minutes professionally.",
            },
            {
                "icon_name": "envelope",
                "title": "Official Letterhead",
                "description": "Preformatted letterhead for official communication.",
            },
        ]

        for resource in resources:
            PDFResource.objects.create(**resource)

        print("Successfully seeded PDF resources")

    def create_team_members(self):
        TeamMember.objects.get_or_create(
            name="John Doe",
            role="Project Manager",
            project=GDOPModule.objects.get_or_create(
                title="Test",
                subtitle="Test",
                icon_name="bi-people",
                is_active=False,
            )[0],
        )
