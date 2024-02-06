from aspose.tex import *
from aspose.tex.io import *
from aspose.tex.presentation.xps import *
from util import Util
from os import path


# Alternative way to obtain typeset document from XPS device.
class TypesetXpsWrittenToExternalStream:
    @staticmethod
    def run():
        # ExStart:WriteOutputXpsToExternalStream
        # Create conversion options for default ObjectTeX format upon ObjectTeX engine extension.
        options = TeXOptions.console_app_options(TeXConfig.object_tex())
        # Specify a job name.
        options.job_name = "external-file-stream"
        # Specify a file system working directory the for input.
        options.input_working_directory = InputFileSystemDirectory(Util.input_directory)
        # Specify a file system working directory the for output.
        options.output_working_directory = OutputFileSystemDirectory(Util.output_directory)
        # Specify that the terminal output must be written to a file in the output working directory.
        # The file name is <job_name>.trm.
        options.terminal_out = OutputFileTerminal(options.output_working_directory)
        
        # Open the stream to write typeset XPS document. The file name is not necessarily the same as the job name.
        with open(path.join(Util.output_directory, options.job_name + ".xps"), "wb") as stream:
            # Run the job.
            TeXJob("hello-world", XpsDevice(stream), options).run()
        # ExEnd:WriteOutputXpsToExternalStream
