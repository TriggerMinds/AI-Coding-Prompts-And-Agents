#!/usr/bin/env python3
"""Register a new prompt in index.json with validation and metadata handling."""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REQUIRED_FIELDS = ["id", "name", "type", "version", "description"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Register a new prompt in index.json")
    parser.add_argument("--index", default="index.json", help="Pad naar index.json (standaard: index.json)")
    parser.add_argument("--id", required=True, help="Unieke identifier voor de prompt")
    parser.add_argument("--name", required=True, help="Naam van de prompt")
    parser.add_argument("--type", required=True, help="Type prompt (bijv. task, system, agent)")
    parser.add_argument("--version", required=True, help="Versienummer voor de prompt")
    parser.add_argument("--description", required=True, help="Korte beschrijving van de prompt")
    parser.add_argument(
        "--tags",
        nargs="*",
        default=None,
        help="Optionele lijst met tags. Meerdere tags scheiden met een spatie."
    )
    return parser.parse_args()


def load_index(path: Path) -> dict:
    if not path.exists():
        return {"prompts": []}
    try:
        with path.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Fout: bestaande index.json bevat ongeldige JSON: {exc}")
    if "prompts" not in data or not isinstance(data["prompts"], list):
        raise SystemExit("Fout: index.json mist een geldige 'prompts'-lijst.")
    return data


def validate_fields(args: argparse.Namespace) -> None:
    missing = [field for field in REQUIRED_FIELDS if not getattr(args, field)]
    if missing:
        raise SystemExit(f"Fout: verplichte velden ontbreken: {', '.join(missing)}")


def check_duplicates(prompts: list[dict], prompt_id: str) -> None:
    for entry in prompts:
        if entry.get("id") == prompt_id:
            raise SystemExit(f"Fout: prompt met id '{prompt_id}' bestaat al.")


def build_entry(args: argparse.Namespace) -> dict:
    timestamp = datetime.now(timezone.utc).isoformat()
    return {
        "id": args.id,
        "name": args.name,
        "type": args.type,
        "version": args.version,
        "description": args.description,
        "tags": args.tags if args.tags is not None else [],
        "created": timestamp,
        "updated": timestamp,
    }


def write_index(path: Path, data: dict) -> None:
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    with tmp_path.open("w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    # Validate JSON by reading it back in
    with tmp_path.open("r", encoding="utf-8") as fh:
        json.load(fh)
    tmp_path.replace(path)


def main() -> None:
    args = parse_args()
    index_path = Path(args.index)

    validate_fields(args)
    data = load_index(index_path)
    prompts = data.setdefault("prompts", [])

    check_duplicates(prompts, args.id)
    entry = build_entry(args)
    prompts.append(entry)

    write_index(index_path, data)
    print(f"Prompt '{args.id}' succesvol geregistreerd in {index_path}.")


if __name__ == "__main__":
    try:
        main()
    except SystemExit as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)
