#V1.0

from layer1.ingest import ingest
from dataclasses import asdict
import json

artifact = ingest("input/DoomTest2")
artifact_dict = asdict(artifact)
with open("artifact_descriptor.txt", "w", encoding="utf-8") as f:
    json.dump(artifact_dict, f, indent=2)

print("Artifact descriptor written to artifact_descriptor.txt")

#V2.0
from layer2.analyze import analyze

profile = analyze(artifact)
output = json.dumps(asdict(profile), indent=2)

with open("artifact_profile.txt", "w", encoding="utf-8") as f:
    f.write(output)
print("Possible configuration written to artifact_profile.txt")

print(output)

# V3.0 – Layer 3 (Configuration Synthesis)

from layer3.synthesize import synthesize

plans = synthesize(profile)

layer3_output = {
    mode: asdict(plan)
    for mode, plan in plans.items()
}

with open("artifact_launch_plans.txt", "w", encoding="utf-8") as f:
    json.dump(layer3_output, f, indent=2)

print("Launch plans written to artifact_launch_plans.txt")

print("\n=== Layer 3 Launch Plans ===")
print(json.dumps(layer3_output, indent=2))