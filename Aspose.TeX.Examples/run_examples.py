from aspose.tex import License
from LoadLicenseFromFile.load_license_from_file import *
from LoadLicenseFromStream.load_license_from_stream import *
from SetMeteredLicense.set_metered_license import *
from FileSystemInputOutputAndXpsOutput.file_system_input_output_and_xps_output import *
from OverriddenJobNameAndTerminalOutputWrittenToDisk.overriden_job_name_and_terminal_output_written_to_disk import *
from TypesetXpsWrittenToExternalStream.typeset_xps_written_to_external_stream import *
from ZipFileInputOutputAndPdfOutput.zip_file_input_ouput_and_pdf_output import *
from OverriddenJobNameAndTerminalOutputWrittenToZip.overriden_job_name_and_terminal_output_written_to_zip import *
from TypesetPdfWrittenToExternalStream.typeset_pdf_written_to_external_stream import *
from StreamInputImageOutputAndTerminalInput.stream_input_image_output_and_terminal_input import *
from CustomTeXFormatFileCreation.custom_tex_format_file_creation import *
from TypesetWithCustomTeXFormat.typeset_with_custom_tex_format import *
from LaTeXPngConversionSimplest.latex_png_conversion_simplest import *
from LaTeXPngConversionAlternative.latex_png_conversion_alternative import *
from LaTeXPdfConversionSimplest.latex_pdf_conversion_simplest import *
from LaTeXPdfConversionAlternative.latex_pdf_conversion_alternative import *
from LaTeXXpsConversionSimplest.latex_xps_conversion_simplest import *
from LaTeXXpsConversionAlternative.latex_xps_conversion_alternative import *
from LaTeXSvgConversionSimplest.latex_svg_conversion_simplest import *
from LaTeXRequiredInputFs.latex_required_input_fs import *
from LaTeXRequiredInputZip.latex_required_input_zip import *
from PngLaTeXFigureRenderer.png_latex_figure_renderer import *
from SvgLaTeXMathRenderer.svg_latex_math_renderer import *
from PngLaTeXMathRenderer.png_latex_math_renderer import *
from SvgLaTeXFigureRenderer.svg_latex_figure_renderer import *
from PngMathRendererPlugin.png_math_renderer_plugin import *
from util import *

# class RunExamples:
# @staticmethod


def main():
    print("Open RunExamples.cs. \nIn Main() method uncomment the example that you want to run.")
    print("=====================================================")

    # Instantiate an instance of license and set the license file through its path
    License().set_license(Util.license_path)

    # Uncomment the example that you want to run.

    # =====================================================
    # =====================================================
    #  Typeset a TeX file
    # =====================================================
    # =====================================================

    # LoadLicenseFromFile.run()

    # LoadLicenseFromStream.run()

    # SetMeteredLicense.run()

    FileSystemInputOutputAndXpsOutput.run()

    # OverriddenJobNameAndTerminalOutputWrittenToDisk.run()

    # TypesetXpsWrittenToExternalStream.run()

    # ZipFileInputOutputAndPdfOutput.run()

    # OverriddenJobNameAndTerminalOutputWrittenToZip.run()

    # TypesetPdfWrittenToExternalStream.run()

    # StreamInputImageOutputAndTerminalInput.run()

    # CustomTeXFormatFileCreation.run()

    # TypesetWithCustomTeXFormat.run()

    # =====================================================
    # =====================================================
    #  Typeset a LaTeX file
    # =====================================================
    # =====================================================

    # LaTeXPngConversionSimplest.run()
    # LaTeXPngConversionAlternative.run()

    # LaTeXPdfConversionSimplest.run()
    # LaTeXPdfConversionAlternative.run()

    # LaTeXXpsConversionSimplest.run()
    # LaTeXXpsConversionAlternative.run()

    # LaTeXSvgConversionSimplest.run()

    # LaTeXRequiredInputFs.run()

    # LaTeXRequiredInputZip.run()

    # =====================================================
    # =====================================================
    #  Rendering LaTeX math formulas
    # =====================================================
    # =====================================================

    # PngLaTeXMathRenderer.run()

    # SvgLaTeXMathRenderer.run()

    # =====================================================
    # =====================================================
    #  Rendering LaTeX graphic figures
    # =====================================================
    # =====================================================

    # PngLaTeXFigureRenderer.run()

    # SvgLaTeXFigureRenderer.run()

    # =====================================================
    # =====================================================
    #  Plugins
    # =====================================================
    # =====================================================

    # PngMathRendererPlugin.run()


if __name__ == '__main__':
    main()
