import httpx
from app.clients.service_discovery_client import ServiceDiscoveryClient
from app.core.settings import settings


class ConfigClient:
    def __init__(self):
        self.discovery = ServiceDiscoveryClient()

    def _get_base_url(self) -> str:
        # 1️⃣ Try discovery first
        discovered = self.discovery.get_service_url(
            "rootlender-config-service"
        )
        if discovered:
            return discovered

        # 2️⃣ Fallback (safe default)
        return "http://127.0.0.1:8000"

    def get_health(self) -> dict | None:
        base_url = self._get_base_url()
        try:
            with httpx.Client(timeout=5.0) as client:
                resp = client.get(f"{base_url}/health")
                resp.raise_for_status()
                return resp.json()
        except Exception:
            return None
