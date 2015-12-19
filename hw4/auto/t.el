(TeX-add-style-hook
 "t"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8x") ("babel" "hebrew" "english")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "amsmath"
    "inputenc"
    "babel"
    "tikz"
    "dsfont")))

