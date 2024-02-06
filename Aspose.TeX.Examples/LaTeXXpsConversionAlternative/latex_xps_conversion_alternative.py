from aspose.tex import *
from aspose.tex.io import *
from aspose.tex.presentation.xps import *
from util import Util
from os import path


class LaTeXXpsConversionAlternative:
    @staticmethod
    def run():
        # ExStart:Conversion-LaTeXToXps-Alternative
        # Create the stream to write the XPS file to.
        with open(path.join(Util.output_directory, "any-name.xps"), "wb") as xps_stream:
            # Create conversion options for Object LaTeX format upon Object TeX engine extension.
            options = TeXOptions.console_app_options(TeXConfig.object_latex)
            # Specify a file system working directory for the output.
            options.output_working_directory = OutputFileSystemDirectory(Util.output_directory)
            # Initialize the options for saving in XPS format.
            options.save_options = XpsSaveOptions()  # Default value. Arbitrary assignment.
            # Run LaTeX to XPS conversion.
            TeXJob(path.join(Util.input_directory, "hello-world.ltx"), XpsDevice(xps_stream), options).run()
        # ExEnd:Conversion-LaTeXToXps-Alternative
