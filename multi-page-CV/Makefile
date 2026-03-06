# Name of your main LaTeX file (without extension)
MAIN=zaferopoulos_cv_multipage

# Default target
all: $(MAIN).pdf

# Rule to generate the PDF
$(MAIN).pdf: $(MAIN).tex publications.tex
	latexmk -pdf $(MAIN).tex

# Rule to generate publications.tex from .bib
publications.tex: publications.bib generate_publications.py
	python generate_publications.py

# Clean up LaTeX build files
clean:
	latexmk -C
# 	rm -f publications.tex
