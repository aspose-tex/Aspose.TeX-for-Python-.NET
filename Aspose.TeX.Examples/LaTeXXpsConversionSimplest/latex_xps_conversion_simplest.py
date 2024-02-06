from aspose.tex import *
from aspose.tex.io import *
from aspose.tex.presentation.xps import *
from util import Util
from os import path
from datetime import datetime
from io import BytesIO


class LaTeXXpsConversionSimplest:
    @staticmethod
    def run():
        # ExStart:Conversion-LaTeXToXps-Simplest
        # Create conversion options for Object LaTeX format upon Object TeX engine extension.
        options = TeXOptions.console_app_options(TeXConfig.object_latex)
        options.input_working_directory = InputFileSystemDirectory(Util.input_directory)
        
        # ExStart:Conversion-InteractionMode
        # Set interaction mode.
        options.interaction = Interaction.NONSTOP_MODE
        # ExEnd:Conversion-InteractionMode
        
        # ExStart:Conversion-JobName
        # Set the job name.
        # options.job_name = "my-job-name"
        # ExEnd:Conversion-JobName
        
        # ExStart:Conversion-DateTime
        # Force the TeX engine to output the specified date in the title.
        # options.date_time = datetime(2022, 12, 18)
        # ExEnd:Conversion-DateTime
        
        # ExStart:Conversion-IgnoreMissingPackages
        # Set to true to make the engine skip missing packages (when your file references one) without errors.
        # options.ignore_missing_packages = True
        # ExEnd:Conversion-IgnoreMissingPackages
        
        # ExStart:Conversion-NoLigatures
        # Set to true to make the engine not construct ligatures where normally it would.
        # options.no_ligatures = True
        # ExEnd:AConversion-NoLigatures
        
        # ExStart:Conversion-Repeat
        # Ask the engine to repeat the job.
        # options.repeat = True
        # ExEnd:Conversion-Repeat
        
        # Specify a file system working directory for the output.
        options.output_working_directory = OutputFileSystemDirectory(Util.output_directory)
        
        # Initialize the options for saving in XPS format.
        so = XpsSaveOptions()
        options.save_options = so  # Default value. Arbitrary assignment.
        
        # ExStart:Conversion-RasterizeFormulas
        # Set to true if you want math formulas to be converted to raster images.
        # so.rasterize_formulas = True
        # ExEnd:Conversion-RasterizeFormulas
        
        # ExStart:Conversion-RasterizeIncludedGraphics
        # Set to true if you want included graphics (if it contains vector elements) to be converted to raster images.
        # so.rasterize_included_graphics = True
        # ExEnd:Conversion-RasterizeIncludedGraphics
        
        # ExStart:Conversion-SubsetFonts
        # Set to true to make the device subset fonts used in the document.
        # so.subset_fonts = True
        # ExEnd:Conversion-SubsetFonts
        
        # Run LaTeX to XPS conversion.
        TeXJob(path.join(Util.input_directory, "sample.ltx"), XpsDevice(), options).run()
        
        # ExStart:Conversion-InputStream
        # Run LaTeX to XPS conversion.
        # TeXJob(BytesIO(r"\documentclass{article} \begin{document} Hello, World! \end{document}".encode("ascii")),
        #       XpsDevice(), options).run()
        # ExEnd:Conversion-InputStream
        
        # ExStart:Conversion-MainInputTerminal
        # Run LaTeX to XPS conversion. When prompted, enter the /-separated path to the LaTeX file.
        # TeXJob(XpsDevice(), options).run()
        # ExEnd:Conversion-MainInputTerminal
        
        # ExEnd:Conversion-LaTeXToXps-Simplest
