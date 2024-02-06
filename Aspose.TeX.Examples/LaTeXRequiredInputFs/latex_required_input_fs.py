from aspose.tex import *
from aspose.tex.io import *
from aspose.tex.presentation.image import *
from util import Util
from os import path


class LaTeXRequiredInputFs:
    @staticmethod
    def run():
        # ExStart:Conversion-RequiredInput-FileSystem
        # Create conversion options for Object LaTeX format upon Object TeX engine extension.
        options = TeXOptions.console_app_options(TeXConfig.object_latex)
        # Specify a file system working directory for the output.
        options.output_working_directory = OutputFileSystemDirectory(Util.output_directory)
        # Specify a file system working directory for the required input.
        # The directory containing packages may be located anywhere.
        options.required_input_directory = InputFileSystemDirectory(path.join(Util.input_directory, "packages"))
        # Initialize the options for saving in PNG format.
        options.save_options = PngSaveOptions()
        # Run LaTeX to PNG conversion.
        TeXJob(path.join(Util.input_directory, "required-input-fs.tex"), ImageDevice(True), options).run()
        # ExEnd:Conversion-RequiredInput-FileSystem
