from aspose.tex.plugins import *
from util import Util
from aspose.pydrawing import Color
from os import path


class PngMathRendererPlugin:
    @staticmethod
    def run():
        # ExStart:Plugins-MathRenderer-Png
        template = 'Without_License'
        out_template1 = f'{template}{1}'
        output_file_name1 = path.join(Util.output_directory, f'{out_template1}.png')

        out_template2 = f'{template}{2}'
        output_file_name2 = path.join(Util.output_directory, f'{out_template2}.png')

        renderer = MathRendererPlugin()
        options = PngMathRendererPluginOptions()
        options.background_color = Color.yellow
        options.text_color = Color.blue
        options.resolution = 300
        options.margin = 10
        options.add_input_data_source(StringDataSource(r'''\begin{align*}
x ^ 2 + y ^ 2 &= 1 \\
y &= \sqrt{ 1 - x ^ 2 }
\end{ align *}'''))
        options.add_input_data_source(StringDataSource(r'''\lim_{N \to \infty} \sum_{k=1}^N f(t_k) \Delta t'''))

        with open(output_file_name1, "wb") as stream1:
            with open(output_file_name2, "wb") as stream2:
                options.add_output_data_target(StreamDataSource(stream1))
                options.add_output_data_target(StreamDataSource(stream2))
                result = renderer.process(options)
        # ExEnd:Plugins-MathRenderer-Png

