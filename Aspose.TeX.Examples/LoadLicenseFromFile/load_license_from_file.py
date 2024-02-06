from aspose.tex import License
from util import Util


class LoadLicenseFromFile:
    @staticmethod
    def run():
        # ExStart:LoadLicenseFromFile
        # Initialize license object.
        license = License()
        # Set license.
        license.set_license(Util.license_path)
        print('License set successfully.')
        # ExEnd:LoadLicenseFromFile
