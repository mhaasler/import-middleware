project_name = "shop_data_import"
base_directory = f""

import os  # Modul für Dateioperationen
import shutil  # Modul für das Erstellen von ZIP-Dateien

# Funktion zur Erstellung der notwendigen Dateien in jeder Crate
def initialize_crate(crate_name, base_dir):
    src_dir = os.path.join(base_dir, crate_name, "src")
    os.makedirs(src_dir, exist_ok=True)

    # lib.rs erstellen
    lib_rs_path = os.path.join(src_dir, "lib.rs")
    with open(lib_rs_path, "w") as f:
        f.write(f"// Placeholder for the {crate_name} module\n\n")
        f.write(f"pub fn {crate_name}_info() -> &'static str {{\n")
        f.write(f'    "{crate_name.capitalize()} module is working!"\n')
        f.write("}\n")

    # Cargo.toml erstellen oder anpassen
    cargo_toml_path = os.path.join(base_dir, crate_name, "Cargo.toml")
    if not os.path.exists(cargo_toml_path):
        with open(cargo_toml_path, "w") as f:
            f.write(f"""\
[package]
name = "{crate_name}"
version = "0.1.0"
edition = "2021"

[dependencies]
""")


# Liste der Crates
crates = ["api", "storage", "queue", "processor", "exporter", "monitoring", "cli", "common"]

# Initialisierung jeder Crate
for crate in crates:
    initialize_crate(crate, base_directory)

# Workspace Cargo.toml anpassen
workspace_cargo_toml = os.path.join(base_directory, "Cargo.toml")
with open(workspace_cargo_toml, "w") as f:
    f.write("[workspace]\nmembers = [\n")
    for crate in crates:
        f.write(f'    "{crate}",\n')
    f.write("]\n")

print("Initialization complete!")
