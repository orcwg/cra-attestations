#!/usr/bin/env python3
"""Validate the example instance against the schema, and prove the schema refuses.

A schema that accepts its own example says nothing. Each negative case below is a
form a tick box cannot refuse and this schema does, so the run prints what the
schema buys rather than only that it parses.

Run: python3 validate.py
"""

from __future__ import annotations

import copy
import json
import pathlib
import sys

try:
    from jsonschema import Draft202012Validator
except ImportError:  # pragma: no cover - dependency reported, never guessed
    sys.stderr.write("jsonschema is not installed; install it to run this check\n")
    raise SystemExit(2)

HERE = pathlib.Path(__file__).parent
SCHEMA = json.loads((HERE / "template-lite.schema.json").read_text())
EXAMPLE = json.loads((HERE / "template-lite.example.json").read_text())

NEGATIVES: list[tuple[str, str]] = [
    (
        "an evidenced MUST answered met with no artefact",
        "controls/GV.01: drop evidence_url",
    ),
    (
        "a conditional item that does not apply yet answered met",
        "controls/QA.05: applies false, status met",
    ),
    (
        "a should-or-explain item answered not_met with no reason",
        "controls/LE.02: drop explanation",
    ),
    (
        "QA.01 answered met without saying whether checksums are present",
        "controls/QA.01: drop checksums_present",
    ),
    (
        "an item omitted from the form altogether",
        "controls: delete VM.02",
    ),
    (
        "a security contact claimed met with nobody to write to",
        "controls/VM.01: drop reporting_contact",
    ),
]


def mutate(case: int) -> dict:
    d = copy.deepcopy(EXAMPLE)
    if case == 0:
        del d["controls"]["GV.01"]["evidence_url"]
    elif case == 1:
        d["controls"]["QA.05"]["applies"] = False
    elif case == 2:
        del d["controls"]["LE.02"]["explanation"]
    elif case == 3:
        del d["controls"]["QA.01"]["checksums_present"]
    elif case == 4:
        del d["controls"]["VM.02"]
    elif case == 5:
        del d["controls"]["VM.01"]["reporting_contact"]
    return d


def main() -> int:
    Draft202012Validator.check_schema(SCHEMA)
    validator = Draft202012Validator(SCHEMA)

    errors = sorted(validator.iter_errors(EXAMPLE), key=lambda e: e.json_path)
    if errors:
        print("FAIL: the example does not validate")
        for e in errors:
            print(f"  {e.json_path}: {e.message}")
        return 1
    print("PASS: the example validates")

    failures = 0
    for i, (what, how) in enumerate(NEGATIVES):
        found = list(validator.iter_errors(mutate(i)))
        if found:
            print(f"PASS: refused  {what}  [{how}]")
        else:
            print(f"FAIL: accepted {what}  [{how}]")
            failures += 1

    print(f"\n{len(NEGATIVES) - failures} of {len(NEGATIVES)} negative cases refused")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
