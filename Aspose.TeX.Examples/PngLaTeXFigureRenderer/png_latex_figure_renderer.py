from aspose.tex.features import *
from aspose.pydrawing import Color
from aspose.tex.io import *
from aspose.tex.presentation.xps import *
from util import Util
from io import BytesIO
from os import path


class PngLaTeXFigureRenderer:
    @staticmethod
    def run():
        # ExStart:Features-PngLaTeXFigureRendering
        # Create rendering options setting the image resolution to 150 dpi.
        options = PngFigureRendererOptions() 
        options.resolution = 150
        # Specify the preamble.
        options.preamble = r"\usepackage{pict2e}"
        # Specify the scaling factor 300%.
        options.scale = 3000
        # Specify the background color.
        options.background_color = Color.white
        # Specify the output stream for the log file.
        options.log_stream = BytesIO()
        # Specify whether to show the terminal output on the console or not.
        options.show_terminal = True

        # Create the output stream for the figure image.
        with open(path.join(Util.output_directory, "text-and-formula.png"), "wb") as stream:
            # Run rendering.
            size = PngFigureRenderer().render(r"""\setlength{\unitlength}{0.8cm}
\begin{picture}(6,5)
\thicklines
\put(1,0.5){\line(2,1){3}} \put(4,2){\line(-2,1){2}} \put(2,3){\line(-2,-5){1}} \put(0.7,0.3){$A$} \put(4.05,1.9){$B$} \put(1.7,2.95){$C$}
\put(3.1,2.5){$a$} \put(1.3,1.7){$b$} \put(2.5,1.05){$c$} \put(0.3,4){$F=\sqrt{s(s-a)(s-b)(s-c)}$} \put(3.5,0.4){$\displaystyle s:=\frac{a+b+c}{2}$}
\end{picture}""", stream, options)
        
        # Show other results.
        print(options.error_report)
        print()
        print(f"Size: {size.width}x{size.height}")
        # ExEnd:Features-PngLaTeXFigureRendering
