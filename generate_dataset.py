import pandas as pd
import numpy as np
from config import *

# Générer les timestamps
timestamps = pd.date_range(start=START_DATE, periods=24 * DURATION_DAYS, freq=FREQUENCY)

vm_list = [f"vm_{i}" for i in range(TOTAL_VMS)]
vm_host_map = {vm: np.random.randint(0, N_HOSTS) for vm in vm_list}
vm_records, host_records = [], []

for ts in timestamps:
    host_usage = {h: {"cpu": 0, "ram": 0, "n_vms": 0} for h in range(N_HOSTS)}

    for vm in vm_list:
        host = vm_host_map[vm]
        cpu = round(np.clip(np.random.normal(VM_CPU_MEAN, VM_CPU_STD), 0.5, 6.0), 2)
        ram = round(np.clip(np.random.normal(VM_RAM_MEAN, VM_RAM_STD), 1, 12), 2)
        status = np.random.choice(list(STATUS_PROBS.keys()), p=list(STATUS_PROBS.values()))

        if status != 'off':
            host_usage[host]["cpu"] += cpu
            host_usage[host]["ram"] += ram
            host_usage[host]["n_vms"] += 1

        vm_records.append({
            "timestamp": ts, "vm_id": vm, "host_id": host,
            "cpu_demand": cpu, "ram_demand": ram, "status": status
        })

    for host in range(N_HOSTS):
        cpu_used = host_usage[host]["cpu"]
        usage_ratio = cpu_used / CPU_CAPACITY
        power = POWER_IDLE + (POWER_FULL - POWER_IDLE) * usage_ratio
        host_records.append({
            "timestamp": ts, "host_id": host, "n_vms": host_usage[host]["n_vms"],
            "cpu_used": round(cpu_used, 2), "ram_used": round(host_usage[host]["ram"], 2),
            "cpu_capacity": CPU_CAPACITY, "ram_capacity": RAM_CAPACITY,
            "power_consumed": round(power, 2)
        })

# Sauvegarde
pd.DataFrame(vm_records).to_csv("data/vms_dataset.csv", index=False)
pd.DataFrame(host_records).to_csv("data/hosts_dataset.csv", index=False)

print("✅ Données générées dans le dossier /data/")
