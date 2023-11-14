from django.apps import AppConfig

class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'


    def ready(self):
        import os
        if os.getenv("DATABASE_URL"):
            email = os.getenv("EMAIL_ADMIN")
            senha = os.getenv("SENHA_ADMIN")

            from filme.models import Usuario
            usuario = Usuario.objects.filter(email=email).first()

            if not usuario:
                Usuario.objects.create_superuser(username="admin", email=email, password=senha,
                                                 is_active=True, is_staff=True)