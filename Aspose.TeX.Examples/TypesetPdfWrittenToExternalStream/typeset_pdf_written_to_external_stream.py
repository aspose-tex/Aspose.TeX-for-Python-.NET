from aspose.tex import *
from aspose.tex.io import *
from aspose.tex.presentation.pdf import *
from util import Util
from os import path


# Alternative way to obtain typeset document from PDF device.
class TypesetPdfWrittenToExternalStream:
    @staticmethod
    def run():
        # ExStart:WriteOutputPdfToExternalStream
        # Open a stream on a ZIP archive that will serve as the input working directory.
        with open(path.join(Util.input_directory, "zip-in.zip"), "rb") as in_zip_stream:
            # Open a stream on a ZIP archive that will serve as the output working directory.
            with open(path.join(Util.output_directory, "typeset-pdf-to-external-stream.zip"), "wb") as out_zip_stream:
                # Create conversion options for default ObjectTeX format upon ObjectTeX engine extension.
                options = TeXOptions.console_app_options(TeXConfig.object_tex())
                # Specify a job name.
                options.job_name = "typeset-pdf-to-external-stream"  # does NOT define the name of the output PDF.
                # Specify a ZIP archive working directory for the input. You can also specify a path inside the archive.
                options.input_working_directory = InputZipDirectory(in_zip_stream, "in")
                # Specify a ZIP archive working directory for the output.
                options.output_working_directory = OutputZipDirectory(out_zip_stream)
                # Specify that the terminal output must be written to a file in the output working directory.
                # The file name is <job_name>.trm.
                options.terminal_out = OutputFileTerminal(options.output_working_directory)
                
                # Define the saving options.
                options.save_options = PdfSaveOptions()
                # Open a stream to write the output PDF to.
                # 1) A file somewhere on a local file system.
                with open(path.join(Util.output_directory, "file-name.pdf"), "wb") as stream:
                # 2) A file in the output ZIP. A weird feature that extends flexibility :)
                # with options.output_working_directory.get_output_file("file-name.pdf").stream as stream:  # writing PDF to the same ZIP
                    TeXJob("hello-world", PdfDevice(stream), options).run()
                
                # Finalize output ZIP archive.
                options.output_working_directory.finish()
        # ExEnd:WriteOutputPdfToExternalStream
