DOT_FILES := $(wildcard dot/*.dot)
SVG_FILES := $(patsubst dot/%.dot, img/%.svg, $(DOT_FILES))

.PHONY: all force

# Default: only compile Graphviz .dot files newer than .svg output
all: $(SVG_FILES)

# Convert with dot:
img/%.svg: dot/%.dot
	@mkdir -p img
	dot -Tsvg $< -o $@

# Rebuild ALL from .dot
force:
	@touch $(DOT_FILES)
	@$(MAKE) -s all
