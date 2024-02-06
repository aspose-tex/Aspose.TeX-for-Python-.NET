from aspose.tex import Metered


class SetMeteredLicense:
    @staticmethod
    def run():
        # ExStart:SetMeteredLicense
        # Set metered public and private keys.
        Metered().set_metered_key('<type public key here>', '<type private key here>')
        print('License set successfully.')
        # ExEnd:SetMeteredLicense
