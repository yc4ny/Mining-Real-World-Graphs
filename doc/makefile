MAIN= paper
TEXPARTS= 	$(MAIN).tex 		\
		000abstract.tex		\
		010intro.tex 		\
		020survey.tex 		\
		030method.tex 		\
		040experiments.tex 	\
		050conclusions.tex 	\
		099appendix.tex 		

BIBPARTS= BIB/*.bib
FIGPARTS= FIG/*.pdf FIG/*.png
STYPARTS= mdwlist.sty
ALL= makefile  $(TEXPARTS) $(BIBPARTS) $(FIGPARTS) $(STYPARTS) README 

$(MAIN).pdf: $(MAIN).tex
	pdflatex $(MAIN).tex
	bibtex $(MAIN)
	pdflatex $(MAIN).tex
	pdflatex $(MAIN).tex

clean:
	\rm -f *.dvi *.bbl *.aux *.log *.blg *.toc

spotless: clean
	\rm -f $(MAIN).ps $(MAIN).pdf
	\rm -rf TST
	\rm -f all.tar


all.tar:
	tar cvfh all.tar makefile $(MAIN).tex $(TEXPARTS) $(BIBPARTS) \
	$(FIGPARTS) README 

