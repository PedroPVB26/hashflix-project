from django.apps import AppConfig
import os

class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'


    if os.getenv("DATABASE_URL"):
        def ready(self):
            from .models import Usuario
            import os

            email = os.getenv("EMAIL_ADMIN")
            senha = os.getenv("SENHA_ADMIN")

            usuarios = Usuario.objects.filter(email=email)

            if not usuarios:
                Usuario.objects.create_superuser(username="a", email=email, password=senha,
                                                 is_active=True, is_staff=True)