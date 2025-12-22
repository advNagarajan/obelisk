from dataclasses import dataclass

@dataclass
class LaunchPlan:
    emulator: str
    config_path: str
    entry_point: str
    timeout: int
    confidence: float
    mode: str             # "strict" | "lenient"
