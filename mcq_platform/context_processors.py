from django.conf import settings


def whatsapp_number(request):
    """
    Make WhatsApp contact number available in all templates
    """
    # Clean number for WhatsApp link (remove + and spaces)
    clean_number = settings.WHATSAPP_CONTACT_NUMBER.replace('+', '').replace(' ', '').replace('-', '')
    
    return {
        'WHATSAPP_NUMBER': settings.WHATSAPP_CONTACT_NUMBER,
        'WHATSAPP_LINK': f"https://wa.me/{clean_number}",
    }
