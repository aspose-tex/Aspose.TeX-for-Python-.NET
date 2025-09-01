from aspose.tex import *
from aspose.tex.io import *
from aspose.tex.presentation.pdf import *
from util import Util
from os import path


# Using ZIP directories for input and output, outputting to PDF device, writing terminal output to console.
class ZipFileInputOutputAndPdfOutput:
    @staticmethod
    def run():
        # ExStart:TakeInputFromZip-WriteOutputToZip
        # Open the stream on the ZIP archive that will serve as the input working directory.
        with open(path.join(Util.input_directory, "zip-in.zip"), "rb") as in_zip_stream:
            # Open the stream on the ZIP archive that will serve as the output working directory.
            with open(path.join(Util.output_directory, "zip-pdf-out.zip"), "wb") as out_zip_stream:
                # Create conversion options for default ObjectTeX format upon ObjectTeX engine extension.
                options = TeXOptions.console_app_options(TeXConfig.object_tex())
                # Specify a ZIP archive working directory for the input. You can also specify a path inside the archive.
                options.input_working_directory = InputZipDirectory(in_zip_stream, "in")
                # Specify a ZIP archive working directory for the output.
                output_directory = OutputZipDirectory(out_zip_stream)
                options.output_working_directory = output_directory
                # Specify the console as the output terminal.
                options.terminal_out = OutputConsoleTerminal()  # Default value. Arbitrary assignment.
                
                # Define the saving options.
                options.save_options = PdfSaveOptions()
                # Run the job.
                job = TeXJob("hello-world", PdfDevice(), options)
                job.run()
                
                # For further output to look fine. 
                options.terminal_out.writer.write_line()
                
                # Finalize output ZIP archive.
                output_directory.finish()
        # ExEnd:TakeInputFromZip-WriteOutputToZip
