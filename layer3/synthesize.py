from layer3.resolver import resolve_machine
from layer3.adapters.dosbox import DOSBoxAdapter

def synthesize(system_profile):
    machine = resolve_machine(system_profile)

    entry = max(
        system_profile.entry_points,
        key=lambda e: e.confidence
    ).path

    adapter = DOSBoxAdapter()

    return {
        "strict": adapter.synthesize(machine, entry, mode="strict"),
        "lenient": adapter.synthesize(machine, entry, mode="lenient")
    }
