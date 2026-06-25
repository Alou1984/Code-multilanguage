from __future__ import annotations

import json
from pathlib import Path


class SentLinksState:
    def __init__(self, path: str | Path = "data/sent_links.json") -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.sent: set[str] = set()
        if self.path.exists():
            try:
                self.sent = set(json.loads(self.path.read_text(encoding="utf-8")))
            except json.JSONDecodeError:
                self.sent = set()

    def is_new(self, url: str) -> bool:
        return url not in self.sent

    def mark_many(self, urls: list[str]) -> None:
        self.sent.update(urls)

    def save(self) -> None:
        self.path.write_text(
            json.dumps(sorted(self.sent), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
