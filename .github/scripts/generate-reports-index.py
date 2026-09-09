"""Generate the GitHub Pages landing page for the Release Radar reports."""

from __future__ import annotations

import html
import re
from pathlib import Path
from urllib.parse import quote


REPORTS_DIRECTORY = Path("reports")
OUTPUT_FILE = REPORTS_DIRECTORY / "index.html"
TITLE_PATTERN = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)


def report_title(report: Path) -> str:
    """Return the document title, falling back to a readable file name."""
    match = TITLE_PATTERN.search(report.read_text(encoding="utf-8", errors="replace"))
    if match:
        return re.sub(r"\s+", " ", html.unescape(match.group(1))).strip()
    return report.stem.replace("-", " ").title()


def main() -> None:
    reports = sorted(
      (report for report in REPORTS_DIRECTORY.rglob("*.html") if report != OUTPUT_FILE),
      key=lambda report: report.relative_to(REPORTS_DIRECTORY).as_posix().lower(),
      reverse=True,
    )
    entries = "\n".join(
      f'      <li><a href="{quote(report.relative_to(REPORTS_DIRECTORY).as_posix())}">{html.escape(report_title(report))}</a></li>'
        for report in reports
    ) or "      <li class=\"empty\">No reports have been published yet.</li>"

    OUTPUT_FILE.write_text(
        f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Release Radar reports</title>
  <style>
    :root {{ color-scheme: light dark; font-family: Inter, system-ui, sans-serif; }}
    body {{ background: #f8fafc; color: #172033; margin: 0; }}
    main {{ margin: 0 auto; max-width: 760px; padding: 5rem 1.5rem; }}
    h1 {{ font-size: clamp(2rem, 6vw, 3.25rem); letter-spacing: -.04em; margin: 0; }}
    p {{ color: #526078; font-size: 1.1rem; margin: .75rem 0 2.5rem; }}
    ul {{ display: grid; gap: .75rem; list-style: none; margin: 0; padding: 0; }}
    a {{ background: #fff; border: 1px solid #dce3ee; border-radius: .75rem; color: #185adb; display: block; font-weight: 650; padding: 1rem 1.25rem; text-decoration: none; transition: border-color .15s, transform .15s; }}
    a:hover {{ border-color: #185adb; transform: translateY(-2px); }}
    .empty {{ color: #526078; padding: 1rem 0; }}
    @media (prefers-color-scheme: dark) {{ body {{ background: #101827; color: #edf2ff; }} p, .empty {{ color: #aebbd0; }} a {{ background: #182236; border-color: #31415d; color: #91b7ff; }} }}
  </style>
</head>
<body>
  <main>
    <h1>Release Radar</h1>
    <p>Published release reports</p>
    <ul>
{entries}
    </ul>
  </main>
</body>
</html>
""",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()