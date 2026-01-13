import os
import httpx

def register_service():
    registry_url = os.getenv("SERVICE_REGISTRY_URL", "").strip()
    service_name = os.getenv("SERVICE_NAME", "").strip()
    port = os.getenv("PORT", "").strip()
    environment = os.getenv("ENVIRONMENT", "local").strip()

    if not registry_url or not service_name or not port:
        return

    payload = {
        "service_name": service_name,
        "port": int(port),
        "environment": environment,
        "health_url": f"http://127.0.0.1:{port}/health"
    }

    try:
        with httpx.Client(timeout=2.0) as client:
            client.post(f"{registry_url}/register", json=payload)
    except Exception:
        # Fail-open: never block startup
        pass
