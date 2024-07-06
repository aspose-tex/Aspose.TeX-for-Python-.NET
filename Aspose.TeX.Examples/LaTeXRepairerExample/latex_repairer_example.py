from aspose.tex.features import *
from aspose.tex.io import *
from util import Util
from os import path


class LaTeXRepairerExample:
    @staticmethod
    def run():
        # ExStart:Features-LaTeXRepairer
        # Create repair options.
        options = LaTeXRepairerOptions()
        # Specify a file system working directory for the output.
        options.output_working_directory = OutputFileSystemDirectory(Util.output_directory)
        # Specify a file system working directory for the required input.
        # The directory containing packages may be located anywhere.
        options.required_input_directory = InputFileSystemDirectory(path.join(Util.input_directory, "packages"))
        # Run the repair process.
        LaTeXRepairer(path.join(Util.input_directory, "invalid-latex.tex"), options).run()
        # ExEnd:Features-LaTeXRepairer
