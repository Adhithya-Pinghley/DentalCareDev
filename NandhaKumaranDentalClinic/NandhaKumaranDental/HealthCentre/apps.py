from django.apps import AppConfig
import threading
# from .views import whatsappNotification

class HealthcentreConfig(AppConfig):
    name = 'HealthCentre'

    def ready(self):
        # thread = threading.Thread(target= whatsappNotification)
        # thread.daemon = True
        # thread.start()
        pass
