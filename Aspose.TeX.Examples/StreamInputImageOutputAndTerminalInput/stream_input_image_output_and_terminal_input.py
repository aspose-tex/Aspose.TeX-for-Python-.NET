from aspose.tex import *
from aspose.tex.io import *
from aspose.tex.presentation.image import *
from util import Util
from io import BytesIO
from os import path


# Taking TeX input from a stream, using file system directory for output, outputting to image device,
# writing terminal output to console, taking online input from console.
class StreamInputImageOutputAndTerminalInput:
    @staticmethod
    def run():
        # ExStart:TakeMainInputFromStream-AuxFromFileSystem-TakeTerminalInputFromConsole-AlternativeImagesStorage
        # Create conversion options for default ObjectTeX format upon ObjectTeX engine extension.
        options = TeXOptions.console_app_options(TeXConfig.object_tex())
        # Specify a job name.
        options.job_name = "stream-in-image-out"
        # Specify a file system working directory for the input.
        options.input_working_directory = InputFileSystemDirectory(Util.input_directory)
        # Specify a file system working directory for the output.
        options.output_working_directory = OutputFileSystemDirectory(Util.output_directory)
        # Specify the console as the input terminal.
        options.terminal_in = InputConsoleTerminal()  # Default value. Arbitrary assignment.
        # Specify the console as the output terminal.
        options.terminal_out = OutputConsoleTerminal()  # Default value. Arbitrary assignment.
        
        # Define the saving options.
        so = PngSaveOptions()
        options.save_options = so
        so.resolution = 300             # Create the image device.
        device = ImageDevice(True)
        # Run the job.
        job = TeXJob(BytesIO("\\hrule height 10pt width 95pt\\vskip10pt\\hrule height 5pt".encode('ascii')), device, options)
        job.run()
        
        # When the console prompts the input, type "ABC", press Enter, then type "\end" and press Enter again.
        
        # For further output to look fine. 
        options.terminal_out.writer.write_line()
        
        # You can alternatively get images in form of array of byte arrays.
        # The first index for the page number (0-based, of course).
        result = device.result
        # with open(path.join(Util.output_directory, 'image.png'), 'wb') as stream:
        #    stream.write(result[0])
        # ExEnd:TakeMainInputFromStream-AuxFromFileSystem-TakeTerminalInputFromConsole-AlternativeImagesStorage
