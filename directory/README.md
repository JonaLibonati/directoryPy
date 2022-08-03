# Directory.py
This library is useful for working with structure of files and directories, facilitating the tasks related with those structures, such as getting information, copying, renaming and creating files and directories.

## Class File(path: str)
This class creates a File object using a relative or absolute path.
When __File('<new file's path>')__ is instantiated, If the file does not exist, an empty file is created.  

```file = File('jonathanlibonati/exampleFile.txt')```

### path
Contains the absolute path as string.  
```
print(file.path)

Result:
/Users/jonathanlibonati/exampleFile.txt
```

### dirpath
Contains the absolute path as string of the directory where the file is located.  
```
print(file.dirpath)

Result:
/Users/jonathanlibonati
```

### name
Contains the file name as string without the extension.  
```
print(file.name)

Result:
exampleFile
```

### extension
Contains the file extension as string.  
```
print(file.extension)

Result:
.txt
```
