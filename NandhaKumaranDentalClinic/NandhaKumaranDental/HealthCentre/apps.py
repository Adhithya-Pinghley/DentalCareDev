from django.apps import AppConfig
import threading
# from .views import whatsappNotification

class HealthcentreConfig(AppConfig):
    name = 'HealthCentre'

    def ready(self):
        # thread = threading.Thread(target= whatsappNotification)
        # thread.daemon = True
        # thread.start()
        from django.db.models.signals import post_migrate
        from django.dispatch import receiver

        @receiver(post_migrate)
        def startwp(sender, **kwargs):
            if sender.name == 'HealthCentre':
                from .views import wp
                wp() 
        # startwp()
        # from .views import openWhatsapp
        # openWhatsapp()
