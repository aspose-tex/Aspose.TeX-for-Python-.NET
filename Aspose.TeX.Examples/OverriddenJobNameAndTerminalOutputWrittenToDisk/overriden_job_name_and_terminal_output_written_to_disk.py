from aspose.tex import *
from aspose.tex.io import *
from aspose.tex.presentation.xps import *
from util import Util


# Using file system directories for input and output, outputting to XPS device, overriding the job name,
# writing terminal output to disk.
class OverriddenJobNameAndTerminalOutputWrittenToDisk:
    @staticmethod
    def run():
        # ExStart:OverrideJobName-WriteTerminalOutputToFileSystem
        # Create conversion options for default ObjectTeX format upon ObjectTeX engine extension.
        options = TeXOptions.console_app_options(TeXConfig.object_tex())
        # Specify a job name. Otherwise, the first argument of the TeXJob constructor will be taken as a job name.
        options.job_name = "overridden-job-name"
        # Specify a file system working directory for the input.
        options.input_working_directory = InputFileSystemDirectory(Util.input_directory)
        # Specify a file system working directory for the output.
        options.output_working_directory = OutputFileSystemDirectory(Util.output_directory)
        # Specify that the terminal output must be written to a file in the output working directory.
        # The file name is <job_name>.trm.
        options.terminal_out = OutputFileTerminal(options.output_working_directory)
        
        # Run the job.
        job = TeXJob("hello-world", XpsDevice(), options)
        job.run()
        # ExEnd:OverrideJobName-WriteTerminalOutputToFileSystem
