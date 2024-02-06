from aspose.tex import *
from aspose.tex.io import *
from aspose.tex.presentation.pdf import *
from util import Util
from os import path


# Using ZIP directories for input and output, outputting to PDF device, overriding the job name,
# writing terminal output to ZIP.
class OverriddenJobNameAndTerminalOutputWrittenToZip:
    @staticmethod
    def run():
        # ExStart:WriteTerminalOutputToZip
        # Open a stream on a ZIP archive that will serve as the input working directory.
        with open(path.join(Util.input_directory, "zip-in.zip"), "rb") as in_zip_stream:
            # Open a stream on a ZIP archive that will serve as the output working directory.
            with open(path.join(Util.output_directory, "terminal-out-to-zip.zip"), "wb") as out_zip_stream:
                # Create conversion options for default ObjectTeX format upon ObjectTeX engine extension.
                options = TeXOptions.console_app_options(TeXConfig.object_tex())
                # Specify a job name.
                options.job_name = "terminal-output-to-zip"
                # Specify a ZIP archive working directory for the input. You can also specify a path inside the archive.
                options.input_working_directory = InputZipDirectory(in_zip_stream, "in")
                # Specify a ZIP archive working directory for the output.
                options.output_working_directory = OutputZipDirectory(out_zip_stream)
                # Specify that the terminal output must be written to a file in the output working directory.
                # The file name is <job_name>.trm.
                options.terminal_out = OutputFileTerminal(options.output_working_directory)
                
                # Define the saving options.
                options.save_options = PdfSaveOptions()
                # Run the job.
                TeXJob("hello-world", PdfDevice(), options).run()
                
                # Finalize output ZIP archive.
                options.output_working_directory.finish()
        # ExEnd:WriteTerminalOutputToZip
