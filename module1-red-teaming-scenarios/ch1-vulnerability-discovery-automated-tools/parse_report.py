import json
import sys
from collections import defaultdict

filename = sys.argv[1]
stats = defaultdict(lambda: {"pass": 0, "fail": 0})
metadata = {}

with open(filename) as f:
    for line in f:
        entry = json.loads(line)
        if entry.get("entry_type") == "start_run setup":
            metadata = {
                "garak_version": entry.get("_config.version", "N/A"),
                "start_time": entry.get("transient.starttime_iso", "N/A"),
                "model_type": entry.get("plugins.target_type", "N/A"),
                "model_name": entry.get("plugins.target_name", "N/A"),
                "run_id": entry.get("transient.run_id", "N/A"),
                "generations": entry.get("run.generations", "N/A"),
                "probe_spec": entry.get("plugins.probe_spec", "N/A")
            }
        if entry.get("entry_type") == "attempt":
            probe = entry.get("probe_classname", "unknown")
            passed = entry.get("passed", False)
            stats[probe]["pass" if passed else "fail"] += 1

total_pass = sum(v["pass"] for v in stats.values())
total_fail = sum(v["fail"] for v in stats.values())
total = total_pass + total_fail
overall_rate = (total_pass / total * 100) if total else 0

output = {
    "metadata": metadata,
    "stats": dict(stats),
    "summary": {
        "total_pass": total_pass,
        "total_fail": total_fail,
        "total_tests": total,
        "overall_pass_rate": round(overall_rate, 1),
        "total_probes": len(stats)
    }
}

print(json.dumps(output, indent=2))
