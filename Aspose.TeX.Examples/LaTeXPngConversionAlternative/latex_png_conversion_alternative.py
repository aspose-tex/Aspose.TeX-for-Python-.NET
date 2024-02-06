from aspose.tex import *
from aspose.tex.io import *
from aspose.tex.presentation.image import *
from util import Util
from os import path


class LaTeXPngConversionAlternative:
    @staticmethod
    def run():
        # ExStart:Conversion-LaTeXToPng-Alternative
        # Create conversion options for Object LaTeX format upon Object TeX engine extension.
        options = TeXOptions.console_app_options(TeXConfig.object_latex)
        # Specify a file system working directory for the output.
        options.output_working_directory = OutputFileSystemDirectory(Util.output_directory)
        # Initialize the options for saving in PNG format.
        so = PngSaveOptions()
        so.device_writes_images = False  # Run LaTeX to PNG conversion.
        options.save_options = so
        device = ImageDevice(True)
        TeXJob(path.join(Util.input_directory, "hello-world.ltx"), device, options).run()
        
        # Save pages file by file.
        for i in range(len(device.result)):
            with open(path.join(Util.output_directory, f"page-{(i + 1)}" + ".png"), "wb") as fs:
                fs.write(device.result[i][0:0+len(device.result[i])])
        # ExEnd:Conversion-LaTeXToPng-Alternative
