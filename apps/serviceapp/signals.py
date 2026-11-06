import os
from django.core.mail import EmailMessage
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from .models import (
    Quote, QuoteItem, Contact, Invoice, QuoteRequest, 
    EmailMessageTemplate, MyCompany
)


# ===============================================================
# 🧾 When a user submits a Quote Request
# ===============================================================
@receiver(post_save, sender=QuoteRequest)
def quote_request_recieved_alter(sender, instance, created, **kwargs):
    if created:
        # ✅ Send confirmation email to the user
        template = EmailMessageTemplate.objects.filter(type="init", is_active=True).first()
        mail = EmailMessage(
            subject=template.subject if template else "Quote Request Received",
            body=template.body if template else "We have received your quote request. We will get back to you soon. Thanks!",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[instance.email],
        )
        mail.send(fail_silently=False)

        # ✅ Notify company dynamically (from MyCompany.email)
        company = MyCompany.objects.first()
        if company and company.email:
            admin_subject = f"New Quote Request from {instance.name}"
            admin_body = (
                f"A new quote request has been submitted.\n\n"
                f"Name: {instance.name}\n"
                f"Email: {instance.email}\n"
                f"Phone: {instance.phone or 'N/A'}\n"
                f"City: {instance.city or 'N/A'}\n"
                f"Address: {instance.address or 'N/A'}\n"
                f"Message:\n{instance.message or 'No message provided.'}\n\n"
                f"Please log in to your admin panel to view and reply."
            )
            admin_mail = EmailMessage(
                subject=admin_subject,
                body=admin_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[company.email],  # 👈 Dynamic company email
            )
            admin_mail.send(fail_silently=False)


# ===============================================================
# 📩 When user fills Contact form
# ===============================================================
@receiver(post_save, sender=Contact)
def contact_message_notify(sender, instance, created, **kwargs):
    if created:
        # ✅ Notify company (dynamic MyCompany.email)
        company = MyCompany.objects.first()
        if company and company.email:
            admin_subject = f"New Contact Message from {instance.first_name}"
            admin_body = (
                f"You've received a new message via the contact form.\n\n"
                f"Name: {instance.first_name} {instance.last_name or ''}\n"
                f"Email: {instance.email}\n"
                f"Phone: {instance.phone or 'N/A'}\n"
                f"Subject: {instance.subject or 'N/A'}\n"
                f"Message:\n{instance.message or 'No message provided.'}\n\n"
                f"Please check your admin panel for details."
            )
            admin_mail = EmailMessage(
                subject=admin_subject,
                body=admin_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[company.email],  # 👈 Dynamic company email
            )
            admin_mail.send(fail_silently=False)

    # ✅ clear cache for unread count
    cache.delete("unread_message_count")



# ===============================================================
# 🧾 QuoteItem Save → Regenerate PDF + Send Quote Email to User
# ===============================================================
@receiver(post_save, sender=QuoteItem)
def regenerate_docs_on_item_save(sender, instance, **kwargs):
    quote = instance.quote
    if quote.items.exists():
        quote.generate_quote()
        quote.refresh_from_db()

        if quote.status == "replied" and not quote.mail_sent:
            template = EmailMessageTemplate.objects.filter(type="quote", is_active=True).first()
            email = EmailMessage(
                subject=template.subject if template else "Your quote is ready",
                body=template.body if template else "Your quote is ready. Please find the attached PDF.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[quote.quote_request.email],
            )

            if quote.quotation_file and hasattr(quote.quotation_file, "path"):
                file_path = quote.quotation_file.path
                if os.path.exists(file_path):
                    email.attach_file(file_path)

            email.send(fail_silently=False)
            quote.mail_sent = True
            quote.save(update_fields=["mail_sent"])


# ===============================================================
# 🧾 Handle Quote status changes (send invoice etc.)
# ===============================================================
@receiver(post_save, sender=Quote)
def handle_quote_status(sender, instance, **kwargs):
    if instance.quote_request and instance.status == "replied":
        instance.quote_request.status = "replied"
        instance.quote_request.save(update_fields=["status"])

        if instance.items.exists() and not instance.mail_sent:
            instance.generate_quote()
            instance.refresh_from_db()
            template = EmailMessageTemplate.objects.filter(type="quote", is_active=True).first()
            email = EmailMessage(
                subject=template.subject if template else "Your quote is ready",
                body=template.body if template else "Your quote is ready. Please find the attached PDF.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[instance.quote_request.email],
            )

            if instance.quotation_file and hasattr(instance.quotation_file, "path"):
                file_path = instance.quotation_file.path
                if os.path.exists(file_path):
                    email.attach_file(file_path)

            email.send(fail_silently=False)
            instance.mail_sent = True
            instance.save(update_fields=["mail_sent"])

    elif instance.quote_request and instance.status == "rejected":
        instance.quote_request.status = "rejected"
        instance.quote_request.save(update_fields=["status"])

    elif instance.quote_request and instance.status == "completed":
        instance.quote_request.status = "completed"
        instance.quote_request.save(update_fields=["status"])

        if instance.items.exists():
            invoice, created = Invoice.objects.get_or_create(quote=instance)
            invoice.generate_invoice()

            template = EmailMessageTemplate.objects.filter(type="invoice", is_active=True).first()
            email = EmailMessage(
                subject=template.subject if template else "Your invoice is ready",
                body=template.body if template else "Your invoice is ready. Please find the attached PDF.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[instance.quote_request.email],
            )

            if invoice.invoice_file and hasattr(invoice.invoice_file, "path"):
                file_path = invoice.invoice_file.path
                if os.path.exists(file_path):
                    email.attach_file(file_path)

            email.send(fail_silently=False)



# ===============================================================
# 🧾 Handle invoice creation event
# ===============================================================
@receiver(post_save, sender=Invoice)
def handle_invoice_status(sender, instance, created, **kwargs):
    if created:
        instance.refresh_from_db()
        instance.generate_invoice()
        instance.quote.status = "completed"
        instance.quote.save(update_fields=["status"])
