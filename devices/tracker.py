import threading
import time

_devices = {}
_lock = threading.Lock()

def update_device(device_id: str):
    with _lock:
        _devices[device_id] = time.time()

def get_active_devices():
    """
    Return dict of device_id -> last_seen timestamp
    Only devices seen within last hour considered active.
    """
    cutoff = time.time() - 3600
    with _lock:
        active = {k: v for k, v in _devices.items() if v >= cutoff}
    return active
