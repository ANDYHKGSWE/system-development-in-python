import psutil
from .status import SystemStatus

def get_system_status() -> SystemStatus:
    cpu = int(psutil.cpu_percent(interval=0.1))
    vm = psutil.virtual_memory()
    du = psutil.disk_usage("/")
    return SystemStatus(
        cpu_pct=cpu,
        mem_pct=int(vm.percent),
        mem_used_gb=round(vm.used / (1024**3), 1),
        mem_total_gb=round(vm.total / (1024**3), 1),
        disk_pct=int(du.percent),
        disk_used_gb=round(du.used / (1024**3), 1),
        disk_total_gb=round(du.total / (1024**3), 1),
    )