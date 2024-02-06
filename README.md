# Python API to TypeSet TeX Files

<!-- ![Version 24.1.0](https://img.shields.io/badge/nuget-v24.1.0-blue) ![Nuget](https://img.shields.io/nuget/dt/Aspose.TeX) -->

[![banner](https://raw.githubusercontent.com/Aspose/aspose.github.io/master/img/banners/aspose_tex-for-net-banner.png)](https://releases.aspose.com/tex/python-net/)

[Product Page](https://products.aspose.com/tex/python-net/) | [Docs](https://docs.aspose.com/tex/python-net/) | [Demos](https://products.aspose.app/tex/family) | [API Reference](https://reference.aspose.com/tex/python-net/) | [Examples](https://github.com/aspose-tex/Aspose.TeX-for-Python-.NET) | [Blog](https://blog.aspose.com/category/tex/) | [Search](https://search.aspose.com/) | [Free Support](https://forum.aspose.com/c/tex) | [Temporary License](https://purchase.aspose.com/temporary-license/)

[Aspose.TeX for Python via .NET](https://products.aspose.com/tex/python-net/) is a library that provides a TeX engine extension called ObjectTeX. It can be used to typeset documents described by TeX files. "Object" means that intermediary typesetting result is a specific object model which then can be uniformly converted into a number of end formats.

## TypeSetting File Processing Features
- Typesetting of TeX files
- Create custom TeX formats
- Provide input data in various ways
- Fetch output data in various ways

## Supported Input Formats

TeX

## Save TeX As

XPS, PDF, JPEG, PNG, TIFF and BMP

## Supported Embedded Fonts for Typesetting

cmbsy10, cmbx10, cmbx5, cmbx6, cmbx7, cmbx8, cmbx9, cmcsc10, cmdunh10, cmex10, cmmi10, cmmi5, cmmi6, cmm7, cmmi8, cmmi9, cmmib10, cmr10, cmr5, cmr6, cmr7, cmr8, cmr9, cmsl10, cmsl8, cmsl9, cmsltt10, cmss10, cmssbx10, cmssi10, cmssq8, cmssqi8, cmsy10, cmsy5, cmsy6, cmsy7, cmsy8, cmsy9, cmti10, cmti7, cmti8, cmti9, cmtt10, cmtt8, cmtt9, cmu10

## Supported Platforms

You can use Aspose.TeX for Python via .NET to build any type of a 32-bit or 64-bit Python application for Windows. Python 3.5 or later is supported.

## Use Python to Obtain Typeset Document from `XPS` Device

You can execute the below code snippet to see how Aspose.TeX API performs against your own samples or check the [GitHub Repository](https://github.com/aspose-tex/Aspose.TeX-for-Python-.NET) for other common usage scenarios.

```python
from aspose.tex import *
from aspose.tex.io import *
from aspose.tex.presentation.image import *
from os import path

options = TeXOptions.console_app_options(TeXConfig.object_tex())
options.job_name = "sample2-1";
options.input_working_directory = InputFileSystemDirectory(_inputDirectory)
options.output_working_directory = OutputFileSystemDirectory(_outputDirectory)
options.terminal_out = OutputFileTerminal(options.output_working_directory)

with open(path.join(_outputDirectory, options.JobName + ".xps")) as stream:
    TeXJob("hello-world", new XpsDevice(stream), options).run()

options.terminal_out.writer.write_line()
```

[Product Page](https://products.aspose.com/tex/python-net/) | [Docs](https://docs.aspose.com/tex/python-net/) | [Demos](https://products.aspose.app/tex/family) | [API Reference](https://reference.aspose.com/tex/python-net/) | [Examples](https://github.com/aspose-tex/Aspose.TeX-for-Python-.NET) | [Blog](https://blog.aspose.com/category/tex/) | [Search](https://search.aspose.com/) | [Free Support](https://forum.aspose.com/c/tex) | [Temporary License](https://purchase.aspose.com/temporary-license/)