from dataclasses import dataclass

#definierar en datastruktur -> sparar och skickar vidare systemets status (CPU, Minne, Disk) på ett snyggt och organiserat sätt. T.ex. Monitor och Service kan skapa ett systemstatus-objekt och använda det utan att hålla kolla på massa lösa variabler.

@dataclass
class SystemStatus:
  cpu_pct: int
  mem_pct: int
  mem_used_gb: float
  mem_total_gb: float
  disk_pct: int
  disk_used_gb: float
  disk_total_gb: float
