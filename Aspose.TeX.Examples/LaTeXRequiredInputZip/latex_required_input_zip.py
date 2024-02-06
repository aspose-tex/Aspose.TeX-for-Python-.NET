from aspose.tex import *
from aspose.tex.io import *
from aspose.tex.presentation.image import *
from util import Util
from os import path


class LaTeXRequiredInputZip:
    @staticmethod
    def run():
        # ExStart:Conversion-RequiredInput-Zip
        # Create conversion options for Object LaTeX format upon Object TeX engine extension.
        options = TeXOptions.console_app_options(TeXConfig.object_latex)
        # Specify a file system working directory for the output.
        options.output_working_directory = OutputFileSystemDirectory(Util.output_directory)
        # Initialize the options for saving in PNG format.
        options.save_options = PngSaveOptions()
        # Create a file stream for the ZIP archive containing the required package.
        # The ZIP archive may be located anywhere.
        with open(path.join(Util.input_directory, "packages\\pgfplots.zip"), "rb") as zip_stream:
            # Specify a ZIP working directory for the required input.
            options.required_input_directory = InputZipDirectory(zip_stream, "")
            
            # Run LaTeX to PNG conversion.
            TeXJob(path.join(Util.input_directory, "required-input-zip.tex"), ImageDevice(True), options).run()
        # ExEnd:Conversion-RequiredInput-Zip
