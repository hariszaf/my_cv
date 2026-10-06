#!/usr/bin/env bash
# Build a cover letter: compile main.tex with the given letter as its body.
# Usage: ./build-letter.sh inrae2026.tex   -> inrae2026.pdf
# Env var: ENGINE (pdf | xelatex | lualatex, default pdf)
set -euo pipefail

letter_path=${1:?Usage: $0 <letter.tex>}
[[ -f $letter_path ]] || { echo "Error: '$letter_path' not found" >&2; exit 1; }
letter=$(basename "$letter_path" .tex)

cd "$(dirname "$0")"
latexmk -"${ENGINE:-pdf}" -interaction=nonstopmode -halt-on-error \
        -outdir=build -jobname="$letter" \
        -usepretex="\\def\\letterbody{$letter}" main.tex
cp "build/$letter.pdf" .
echo "Built $letter.pdf"
