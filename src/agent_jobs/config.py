from __future__ import annotations

from pathlib import Path
from typing import Any
import yaml


def load_config(path: str | Path = "config.yml") -> dict[str, Any]:
    config_path = Path(path)
    if not config_path.exists():
        raise FileNotFoundError(f"Fichier de configuration introuvable: {config_path}")
    with config_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)
