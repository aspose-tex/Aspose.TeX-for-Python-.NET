from aspose.tex import *
from aspose.tex.io import *
from aspose.tex.presentation.pdf import *
from util import Util
from os import path


class LaTeXPdfConversionSimplest:
    @staticmethod
    def run():
        # ExStart:Conversion-LaTeXToPdf-Simplest
        # Create conversion options for Object LaTeX format upon Object TeX engine extension.
        options = TeXOptions.console_app_options(TeXConfig.object_latex)
        # Specify a file system working directory for the output.
        options.output_working_directory = OutputFileSystemDirectory(Util.output_directory)
        # Initialize the options for saving in PDF format.
        options.save_options = PdfSaveOptions()
        # Run LaTeX to PDF conversion.
        TeXJob(path.join(Util.input_directory, "hello-world.ltx"), PdfDevice(), options).run()
        # ExEnd:Conversion-LaTeXToPdf-Simplest
