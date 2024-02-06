from aspose.tex import *
from aspose.tex.io import *
from aspose.tex.presentation.svg import *
from util import Util
from os import path


class LaTeXSvgConversionSimplest:
    @staticmethod
    def run():
        # ExStart:Conversion-LaTeXToSvg-Simplest
        # Create conversion options for Object LaTeX format upon Object TeX engine extension.
        options = TeXOptions.console_app_options(TeXConfig.object_latex)
        # Specify a file system working directory for the output.
        options.output_working_directory = OutputFileSystemDirectory(Util.output_directory)
        # Initialize the options for saving in SVG format.
        options.save_options = SvgSaveOptions()
        # Run LaTeX to SVG conversion.
        TeXJob(path.join(Util.input_directory, "hello-world.ltx"), SvgDevice(), options).run()
        # ExEnd:Conversion-LaTeXToSvg-Simplest
