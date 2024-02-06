import os


class Util:
	base_path: str = os.path.abspath(os.getcwd())
	input_directory: str = os.path.join(base_path, 'input')
	output_directory: str = os.path.join(base_path, 'output')
	license_path: str = os.path.join(base_path, 'License', 'Aspose.TeX.Product.Family.lic')
