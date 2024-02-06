from aspose.tex import *
from aspose.tex.io import *
from aspose.tex.presentation.xps import *
from aspose.tex.resourceproviders import FormatProvider
from util import Util
from io import BytesIO


# Typesetting a TeX file using a custom TeX format.
class TypesetWithCustomTeXFormat:
    @staticmethod
    def run():
        # ExStart:TypesetWithCustomTeXFormat
        # Create the format provider using the file system input working directory.
        # We use the project output directory as our custom format file is supposed to be located there.
        with FormatProvider(InputFileSystemDirectory(Util.output_directory), "customtex") as format_provider:
            # Create conversion options for a custom format upon ObjectTeX engine extension.
            options = TeXOptions.console_app_options(TeXConfig.object_tex(format_provider))
            options.job_name = "typeset-with-custom-format"
            # Specify the input working directory. This is not required here as we are providing the main input as a stream.
            # But it is required when the main input has dependencies (e.g. images).
            options.input_working_directory = InputFileSystemDirectory(Util.input_directory)
            # Specify a file system working directory for the output.
            options.output_working_directory = OutputFileSystemDirectory(Util.output_directory)
            
            # Run the job.
            TeXJob(BytesIO("Congratulations! You have successfully typeset this text with your own TeX format!\\end".encode('ascii')),
                   XpsDevice(), options).run()
            
            # For further output to look fine.
            options.terminal_out.writer.write_line()
        # ExEnd:TypesetWithCustomTeXFormat
