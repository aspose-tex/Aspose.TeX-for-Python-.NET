from aspose.tex import License
from util import Util


class LoadLicenseFromStream:
    @staticmethod
    def run():
        # ExStart:LoadLicenseFromStream
        # Initialize license object.
        license = License()
        # Load license in FileStream.
        with open(Util.license_path, "rb") as my_stream:
            # Set license.
            license.set_license(my_stream)
        print('License set successfully.')
        # ExEnd:LoadLicenseFromStream
