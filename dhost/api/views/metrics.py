from datetime import timedelta

from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from prometheus_client import CollectorRegistry, Gauge, Info, generate_latest
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from dhost.api.permissions import IsSuperUser
from dhost.api.renderers import PlainTextRenderer
from dhost.utils import get_version

User = get_user_model()


def metrics():
    registry = CollectorRegistry()

    # general infos
    info = Info(
        "dhost",
        "Dhost System Information",
        registry=registry,
    )
    info.info({"version": get_version(), "debug": str(settings.DEBUG)})

    # users
    user_count = Gauge(
        "dhost_users_total",
        "Number of users",
        ["activity"],
        registry=registry,
    )

    # all users
    total_users = User.objects.count()
    user_count.labels(activity="all").set(total_users)

    # daily users
    last_24h = now() - timedelta(hours=24)
    daily_users = User.objects.filter(last_login__gte=last_24h).count()
    user_count.labels(activity="daily").set(daily_users)

    # monthly users
    last_30d = now() - timedelta(days=30)
    monthly_users = User.objects.filter(last_login__gte=last_30d).count()
    user_count.labels(activity="monthly").set(monthly_users)

    # sessions
    if "django.contrib.sessions" in settings.INSTALLED_APPS:
        from django.contrib.sessions.models import Session

        user_sessions = Gauge(
            "dhost_sessions_total",
            "Number of sessions",
            ["type"],
            registry=registry,
        )

        # all sessions
        total_sessions = Session.objects.count()
        user_sessions.labels(type="all").set(total_sessions)

        # valid sessions
        valid_sessions = Session.objects.filter(expire_date__gte=now()).count()
        user_sessions.labels(type="valid").set(valid_sessions)

        # expired sessions
        expired_sessions = total_sessions - valid_sessions
        user_sessions.labels(type="expired").set(expired_sessions)

    return generate_latest(registry=registry)


class APIMetricsView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsSuperUser,)
    renderer_classes = (PlainTextRenderer,)

    def get(self, request, format=None):
        metrics_response = metrics().decode("UTF-8")
        return Response(metrics_response)
