from django.apps import AppConfig


class FacedetectionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "facedetection"

    def ready(self):
        try:
            from django.urls import include, path
            from horilla.urls import urlpatterns
            urlpatterns.append(
                path("api/facedetection/", include("facedetection.urls")),
            )
        except ImportError:
            # Ignore import errors to allow server to start
            pass
        super().ready()
