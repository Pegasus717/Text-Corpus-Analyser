from pathlib import Path


def read_text_file(path: str) -> str:
    p = Path(path)
    if p.suffix == ".gz":
        return gzip.decompress(p.read_bytes()).decode("utf-8")
    return p.read_text(encoding="utf-8")
