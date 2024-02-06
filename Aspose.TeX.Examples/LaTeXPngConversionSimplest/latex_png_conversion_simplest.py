from aspose.tex import *
from aspose.tex.io import *
from aspose.tex.presentation.image import *
from util import Util
from os import path


class LaTeXPngConversionSimplest:
    @staticmethod
    def run():
        # ExStart:Conversion-LaTeXToPng-Simplest
        # Create conversion options for Object LaTeX format upon Object TeX engine extension.
        options = TeXOptions.console_app_options(TeXConfig.object_latex)
        # Specify a file system working directory for the output.
        options.output_working_directory = OutputFileSystemDirectory(Util.output_directory)
        # Initialize the options for saving in PNG format.
        options.save_options = PngSaveOptions()
        
        # ExStart:Conversion-LaTeXToJpeg
        # Initialize the options for saving in JPEG format.
        # options.save_options = JpegSaveOptions()
        # ExEnd:Conversion-LaTeXToJpeg
        
        # ExStart:Conversion-LaTeXToTiff
        # Initialize the options for saving in TIFF format.
        # options.save_options = TiffSaveOptions()
        # ExEnd:Conversion-LaTeXToTiff
        
        # ExStart:Conversion-LaTeXToBmp
        # Initialize the options for saving in BMP format.
        # options.save_options = BmpSaveOptions()
        # ExEnd:Conversion-LaTeXToBmp
        
        # Run LaTeX to PNG conversion.
        TeXJob(path.join(Util.input_directory, "hello-world.ltx"), ImageDevice(True), options).run()
        # ExEnd:Conversion-LaTeXToPng-Simplest
