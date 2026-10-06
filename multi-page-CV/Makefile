# Name of your main LaTeX file (without extension)
MAIN=zaferopoulos_cv_multipage

# Tables generated from ../bibs/*.bib by ../generate_tex_tables.py
TABLES=../tex/publications.tex ../tex/conferences.tex ../tex/students.tex ../tex/teaching.tex

# Default target
all: $(MAIN).pdf

# Rule to generate the PDF
$(MAIN).pdf: $(MAIN).tex $(TABLES)
	latexmk -outdir=build -pdf $(MAIN).tex
	cp build/$(MAIN).pdf .

# Regenerate all tables when a .bib file or the script changes (the script expects the repo root as cwd)
$(TABLES) &: $(wildcard ../bibs/*.bib) ../generate_tex_tables.py
	cd .. && python generate_tex_tables.py

# Clean up LaTeX build files
clean:
	latexmk -C