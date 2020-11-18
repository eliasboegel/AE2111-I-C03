temperatures = {"reference": 288.15, "min": 200, "max": 350} # Values are placeholders. Put in the actual ones

info_fastener = {"E": 2000000, "diameter": 0.01, "alpha": 0.05} # Also placeholders

alpha_clamped_part = 0.08 # Another placeholder...

phi = 0 # And another one

F_T_max = (alpha_clamped_part - info_fastener["alpha"]) * (temperatures["max"] - temperatures["reference"]) * info_fastener["E"] * info_fastener["diameter"] ** 2 / 4 * (1 - phi)
F_T_min = (alpha_clamped_part - info_fastener["alpha"]) * (temperatures["min"] - temperatures["reference"]) * info_fastener["E"] * info_fastener["diameter"] ** 2 / 4 * (1 - phi)

print("F_T_max:", F_T_max, "\nF_T_min:", F_T_min)