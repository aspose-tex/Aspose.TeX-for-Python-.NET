from aspose.tex import *
from aspose.tex.io import *
from util import Util


# Creating a custom TeX format file.
class CustomTeXFormatFileCreation:
    @staticmethod
    def run():
        # ExStart:CreateCustomTeXFormatFile
        # Create TeX engine options for no format upon ObjectTeX engine extension.
        options = TeXOptions.console_app_options(TeXConfig.object_ini_tex)
        # Specify a file system working directory for the input.
        options.input_working_directory = InputFileSystemDirectory(Util.input_directory)
        # Specify a file system working directory for the output.
        options.output_working_directory = OutputFileSystemDirectory(Util.output_directory)
        
        # Run format creation.
        TeXJob.create_format("customtex", options)
        
        # For further output to look fine.
        options.terminal_out.writer.write_line()
        # ExEnd:CreateCustomTeXFormatFile
