# Directory.py
This library is useful for working with structure of files and directories, facilitating the tasks related with those structures, such as getting information, copying, renaming and creating files and directories.

## Class File(path: str)
This class creates a File object using a relative or absolute path.
When __File('<new file's path>')__ is instantiated, If the file does not exist, an empty file is created.

  __path__
    Contains the absolute path.
  __dirpath__
    Contains the absolute path of the directory where the file is located.
  __name__
    Contains the file name without the extension.
  __extension__
    Contains the file extension.