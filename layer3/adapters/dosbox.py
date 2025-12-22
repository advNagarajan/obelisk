from layer3.adapters.base import EmulatorAdapter
from layer3.launchplan import LaunchPlan
from layer3.canonical import CanonicalMachine

class DOSBoxAdapter(EmulatorAdapter):

    def synthesize(
        self,
        machine: CanonicalMachine,
        entry_point: str,
        mode: str = "strict"
    ) -> LaunchPlan:

        conf_path = f"generated_dosbox_{mode}.conf"

        with open(conf_path, "w") as f:
            # ---- CPU ----
            f.write("[cpu]\n")
            f.write(f"cputype={machine.cpu}\n")

            if mode == "strict":
                f.write("core=normal\n")
                f.write("cycles=3000\n")
            else:
                f.write("core=auto\n")
                f.write("cycles=auto\n")

            f.write("\n")

            # ---- Memory ----
            f.write("[memory]\n")
            f.write(f"memsize={machine.memory_mb}\n\n")

            # ---- Graphics ----
            f.write("[dosbox]\n")
            if mode == "strict":
                f.write("machine=vga\n")
            else:
                f.write("machine=svga_s3\n")
            f.write("\n")

            # ---- Sound ----
            f.write("[sblaster]\n")
            if machine.sound and mode == "lenient":
                f.write("sbtype=sb16\n")
            else:
                f.write("sbtype=none\n")

        return LaunchPlan(
            emulator="dosbox",
            config_path=conf_path,
            entry_point=entry_point,
            timeout=20,
            confidence=0.6,
            mode=mode
        )
