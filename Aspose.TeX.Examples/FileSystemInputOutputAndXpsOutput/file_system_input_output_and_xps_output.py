from aspose.tex import *
from aspose.tex.io import *
from aspose.tex.presentation.xps import *
from util import Util


# Using file system directories for input and output, outputting to XPS device, writing terminal output to console.
class FileSystemInputOutputAndXpsOutput:
    @staticmethod
    def run():
        # ExStart:TakeInputFromFileSystem-WriteOutputToFileSystem-WriteTerminalOutputToConsole
        # Create conversion options for default ObjectTeX format upon ObjectTeX engine extension.
        options = TeXOptions.console_app_options(TeXConfig.object_tex())
        # Specify a file system working directory for the input.
        options.input_working_directory = InputFileSystemDirectory(Util.input_directory)
        # Specify a file system working directory for the output.
        options.output_working_directory = OutputFileSystemDirectory(Util.output_directory)
        # Specify the console as the output terminal.
        options.terminal_out = OutputConsoleTerminal()  # Default value. Arbitrary assignment.
        # Specify a memory terminal as output terminal, if you don't want the terminal output to be written to the console.
        # options.TerminalOut = new OutputMemoryTerminal();
        # Run the job.
        job = TeXJob("hello-world", XpsDevice(), options)
        job.run()
        
        # For further output to look fine.
        options.terminal_out.writer.write_line()  # The same as print()
        # ExEnd:TakeInputFromFileSystem-WriteOutputToFileSystem-WriteTerminalOutputToConsole
