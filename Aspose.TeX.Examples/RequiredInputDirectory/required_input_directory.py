from aspose.tex.io import *
import io

# ExStart:Conversion-RequiredInputDirectory
# This is an implementation of IInputWorkingDirectory that is suitable for the TeX job's RequiredInputDirectory option
# in case required input contains fonts provided by external packages.
# The class additionally implements IFileCollector, which provides access to file collections by extension.
# This is necessary to load external font maps, which are files (outside TeX syntax) that map TeX's
# internal font names to file names of physical fonts.
class RequiredInputDirectory(IInputWorkingDirectory, IFileCollector):
    def __init__(self):
        self._file_names =
        {}
        pass
    
    
    # This method should preliminarily be called for each file entry that is supposed to be located inside
    # the required input directory. Inside is an example of how the dictionary of file names could be organized
    # for easy collection of file names by extension.
    # Here fileName is a full file name. This can be a file path on a file system, a URL, or whatever else (theoretically).
    def store_file_name(self, file_name):
        extension = Path.GetExtension(file_name)
        name = Path.GetFileNameWithoutExtension(file_name)
        
        files = None
        if not extension in self._file_names and ((files := self._file_names[extension]) or True):
            self._file_names.append(extension, files = {})
        
        files[name] = file_name
    
    # The IInputWorkingDirectory implementation.
    def get_file(self, file_name, full_name, search_subdirectories = False):
        full_name[0] = file_name
        return None # Here we actually return a stream for the file requested by its name.
    
    # Here is how we gather file collections by extension.
    def get_file_names_by_extension(self, extension, path = None):
        files = None
        if not extension in self._file_names and ((files := self._file_names[extension]) or True):
            return ['' for _ in range(0)]
        
        return list(list(files.Values))
    
    def dispose(self):
        self._file_names.clear()
