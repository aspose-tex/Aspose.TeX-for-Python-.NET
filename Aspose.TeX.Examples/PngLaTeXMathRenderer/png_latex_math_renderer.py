from aspose.tex.features import *
from aspose.pydrawing import Color
from util import Util
from io import BytesIO
from os import path


class PngLaTeXMathRenderer:
    @staticmethod
    def run():
        # ExStart:Features-PngLaTeXMathRendering
        # Create rendering options setting the image resolution to 150 dpi.
        options = PngMathRendererOptions() 
        options.resolution = 150             # Specify the preamble.
        options.preamble = r"""\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{color}"""
        # Specify the scaling factor 300%.
        options.scale = 3000
        # Specify the foreground color.
        options.text_color = Color.black
        # Specify the background color.
        options.background_color = Color.white
        # Specify the output stream for the log file.
        options.log_stream = BytesIO()
        # Specify whether to show the terminal output on the console or not.
        options.show_terminal = True

        # Create the output stream for the formula image.
        with open(path.join(Util.output_directory, "math-formula.png"), "wb") as stream:
            # Run rendering.
            size = PngMathRenderer().render(r"""\begin{equation*}
e^x = x^{\color{red}0} + x^{\color{red}1} + \frac{x^{\color{red}2}}{2} + \frac{x^{\color{red}3}}{6} + \cdots = \sum_{n\geq 0} \frac{x^{\color{red}n}}{n!}
\end{equation*}""", stream, options)
        
        # Show other results.
        print(options.error_report)
        print()
        print(f"Size: {size.width}x{size.height}")
        # ExEnd:Features-PngLaTeXMathRendering
