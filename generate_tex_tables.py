#!/usr/bin/env python
import re
import bibtexparser
# pip install pylatexenc
from pylatexenc.latexencode import unicode_to_latex


# ----
# Publications
# ----

# Load your .bib file
with open("bibs/my_publications.bib") as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Sort by year (descending)
entries = sorted(bib_database.entries, key=lambda e: e.get('year', '0000'), reverse=True)

with open("tex/publications.tex", "w") as out:
    for e in entries:
        # title   = e.get('title', '').replace('{', '').replace('}', '')
        text   = e.get('title', '').replace('{', '').replace('}', '')
        title = unicode_to_latex(text)

        authors = e.get('author', '')
        journal = e.get('journal', e.get('booktitle', ''))
        doi     = e.get('doi', '')
        year    = e.get('year', '')

        if "Zafeiropoulos, Haris" in authors:
            authors = authors.replace(
                "Zafeiropoulos, Haris",
                r"\textbf{Zafeiropoulos, Haris}"
            )
        elif "Zafeiropoulos, H" in authors:
            authors = authors.replace(
                "Zafeiropoulos, H",
                r"\textbf{Zafeiropoulos, H}"
            )
        parts = [a.strip() for a in authors.split(" and ")]
        if len(parts) > 1:
            authors = ", ".join(parts[:-1]) + " and " + parts[-1]

        # Write formatted \cvpubitem lines with clickable DOI links
        out.write(
            f"    \\cvpubitem{{{title}}}{{{authors}}}{{{journal}, DOI: \\href{{https://doi.org/{doi}}}{{{doi}}}}}{{{year}}}\n"
        )

# ----
# Students
# ----

with open("bibs/my_students.bib") as bibtex_file:
    bib_students = bibtexparser.load(bibtex_file)

# Sort by year (descending)
students = sorted(bib_students.entries, key=lambda e: e.get('year', '0000'), reverse=True)

with open("tex/students.tex", "w", encoding="utf-8") as f:
    for s in students:
        link_tex = s['link'] if s['link'] else "{}"
        desc = s['level'] + " @ " + s['school'] if 'school' in s else s['level']
        f.write(
            f"\\cvitem{{{s['year']}}}{{{s['student']}, {s['level']}}}\n"
            f"{{{link_tex}}}\n"
            f"{{\"{s['title']}\"}}\n"
            f"{{}}\n\\\\\n\n"
        )

# ----
# Conferences
# ----


# Load your .bib file
with open("bibs/my_conferences.bib") as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Sort by year (descending)
conferences = sorted(bib_database.entries, key=lambda e: e.get('year', '0000'), reverse=True)

with open("tex/conferences.tex", "w") as out:
    for entry in sorted(bib_database.entries, key=lambda e: e.get("year", ""), reverse=True):
        entry_id = entry.get("ID", "")
        year     = entry.get("year", "")
        # title    = entry.get("title", "").replace("&", "\&")
        text = entry.get("title", "")
        # title = re.sub(r'(?<!\\)&', r'\&', text)
        title = unicode_to_latex(text)
        url      = entry.get("link", "")
        # note     = entry.get("note", "").replace("&", "\&")
        text = entry.get("note", "")
        # note = re.sub(r'(?<!\\)&', r'\&', text)
        note = unicode_to_latex(text)

        # Build the LaTeX line
        out.write(f"    \\cvitem{{{year}}}{{{title}}}{{\\href{{{url}}}{{{entry_id}}}}}{{{note}}}{{}}\\\\\n\n")


# ----
# Teaching
# ----

with open("bibs/my_teaching.bib") as bib_file:
    bib_database = bibtexparser.load(bib_file)

lectures = sorted(bib_database.entries, key=lambda e: e.get('year', '0000'), reverse=True)

with open("tex/teaching.tex", "w") as out:
    for e in lectures:
        year    = e.get('year', '')
        title   = e.get('title', '').replace('{', '').replace('}', '')
        url     = e.get('url', '')
        urldesc = e.get('urldesc', '')
        note    = e.get('note', '')

        if url and urldesc:
            link = f"\\href{{{url}}}{{{urldesc}}}"
        elif url:
            link = f"\\href{{{url}}}{{link}}"
        else:
            link = ""

        out.write(
            f"    \\cvitem{{{year}}}{{{title}}}{{{link}}}{{{note}}}{{}}\\\\\n"
        )


# ----
# Workshops - summer schools
# ----

with open("bibs/my_workshops.bib") as bib_file:
    bib_database = bibtexparser.load(bib_file)

workshops = sorted(bib_database.entries, key=lambda e: e.get('year', '0000'), reverse=True)
