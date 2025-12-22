from abc import ABC, abstractmethod
from layer3.canonical import CanonicalMachine
from layer3.launchplan import LaunchPlan

class EmulatorAdapter(ABC):

    @abstractmethod
    def synthesize(
        self,
        machine: CanonicalMachine,
        entry_point: str,
        mode: str            # "strict" | "lenient"
    ) -> LaunchPlan:
        pass
