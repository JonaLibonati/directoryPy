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

### data()
Return a dictionary with the dirpath, path, name and extension.
```
data = file.data()
print(data)

Result:
{
    'dirpath': '/Users/jonathanlibonati',
    'path': '/Users/jonathanlibonati/exampleFile.txt',
    'name': 'exampleFile',
    'extension': '.txt'
}
```

### rename(name: str)
Renames the file and returns self. This method uses os.rename() function for renaming the file.
```
data = file.rename('new_name').data()
print(data)

Result:
{
    'dirpath': '/Users/jonathanlibonati',
    'path': '/Users/jonathanlibonati/new_name.txt',
    'name': 'new_name',
    'extension': '.txt'
}
```

### copy(dir: Directory) - asynchronous
Copies the file to an especific directory an returns the copied file object. The parameter is an Directory object.
It is an asynchronous method, therefore it is "awaitable" and uses asyncio.

For further information about Directory class, please search the information in this Readme.
```
import asyncio

async def main():
    file = File('jonathanlibonati/exampleFile.txt')
    dir = Directory('/Users/jonathanlibonati/desktop')

    copied_file = await file.copy(dir)

    print(copied_file.data())

asyncio.run(main())

Result:
{
    'dirpath': '/Users/jonathanlibonati/desktop',
    'path': '/Users/jonathanlibonati/desktop/exampleFile.txt',
    'name': 'exampleFile',
    'extension': '.txt'
}
```

## Class Directory(path: str)
This class creates a Directory object using a relative or absolute path. When __Directory('<new directory's path>')__ is instantiated, If the directory does not exist, an empty directory is created. if the directory already exists, all files and folders inside the directory are created and saved in Directory().file and Directory().directories properties.

Folder used as example:
```
🛣️ /Users/jonathanlibonati/exampleDir

📁 exampleDir
|
|-- 📄 exampleFile1.txt
|-- 📄 exampleFile2.txt
|
|-- 📁 subExampledir2
|   |
|   |-- 📄 subExampleFile2.txt
|
|-- 📁 subExampledir1
    |
    |-- 📄 subExampleFile1.txt
```

```dir = Directory('/Users/jonathanlibonati/exampleDir')```

### path
Contains the absolute path as string.
```
print(dir.path)

Result:
/Users/jonathanlibonati/exampleDir
```

### name
Contains the directory name as string.
```
print(dir.name)

Result:
exampleDir
```

### files
Contains a dictionary with the Files objects which are inside the directory.
```
print(dir.files)

Result:
{
'exampleFile1.txt': <File object 'exampleFile1'>,
'exampleFile2.txt': <File object 'exampleFile2'>
}
```

### fileslist()
Returns a list with the Files objects which are inside the directory.
```
print(dir.fileslist())

Result:
[<File object 'exampleFile1'>, <File object 'exampleFile2'>]
```

### directories
Contains a dictionary with the Directory objects which are inside the directory.
```
print(dir.directories)

Result:
{
'subExampledir1': <Directory object 'subExampledir1'>,
'subExampledir2': <Directory object 'subExampledir2'>
}
```

### dirlist()
Returns a list with the Directory objects which are inside the directory.
```
print(dir.fileslist())

Result:
[<Directory object 'subExampledir1'>, <Directory object 'subExampledir2'>]
```

### tree(levels: int)
Prints on the terminal the tree of files and direcoties. The levels parameter indicates how deep to print.
```
dir.tree(0)

Result:
🛣️ /Users/jonathanlibonati/exampleDir

📁 exampleDir
```
```
dir.tree(1)

Result:
🛣️ /Users/jonathanlibonati/exampleDir

📁 exampleDir
|
|-- 📄 exampleFile1.txt
|-- 📄 exampleFile2.txt
|
|-- 📁 subExampledir2
|
|-- 📁 subExampledir1
```
```
dir.tree()

Result:
🛣️ /Users/jonathanlibonati/exampleDir

📁 exampleDir
|
|-- 📄 exampleFile1.txt
|-- 📄 exampleFile2.txt
|
|-- 📁 subExampledir2
|   |
|   |-- 📄 subExampleFile2.txt
|
|-- 📁 subExampledir1
    |
    |-- 📄 subExampleFile1.txt
```
### data()
Return a dictionary with the information of root directory and all the files and directories inside.
```
data = dir.data()
print(data)

Result:
{
    'selfData': {
        'path': '/Users/jonathanlibonati/exampleDir',
        'name': 'exampleDir'},
    'contentData': {
        'exampleFile1_file': {
            'dirpath': '/Users/jonathanlibonati/exampleDir',
            'path': '/Users/jonathanlibonati/exampleDir/exampleFile1.txt',
            'name': 'exampleFile1',
            'extension': '.txt'},
        'exampleFile2_file': {
            'dirpath': '/Users/jonathanlibonati/exampleDir',
            'path': '/Users/jonathanlibonati/exampleDir/exampleFile2.txt',
            'name': 'exampleFile2',
            'extension': '.txt'},
        'subExampledir2_dir': {
            'selfData': {
                'path': '/Users/jonathanlibonati/exampleDir/subExampledir2',
                'name': 'subExampledir2'},
            'contentData': {
                'subExampleFile2_file': {
                    'dirpath': '/Users/jonathanlibonati/exampleDir/subExampledir2',
                    'path': '/Users/jonathanlibonati/exampleDir/subExampledir2/subExampleFile2.txt',
                    'name': 'subExampleFile2',
                    'extension': '.txt'
                }
            }
        },
        'subExampledir1_dir': {
            'selfData': {
                'path': '/Users/jonathanlibonati/exampleDir/subExampledir1',
                'name': 'subExampledir1'},
            'contentData': {
                'subExampleFile1_file': {
                    'dirpath': '/Users/jonathanlibonati/exampleDir/subExampledir1',
                    'path': '/Users/jonathanlibonati/exampleDir/subExampledir1/subExampleFile1.txt',
                    'name': 'subExampleFile1',
                    'extension': '.txt'
                }
            }
        }
    }
}
```

### selfData()
Return a dictionary with the information of root directory.
```
{
   'path': '/Users/jonathanlibonati/exampleDir',
   'name': 'exampleDir'
}
```

### contentData()
Return a dictionary with the information of all the files and directories inside.
```
data = dir.contentData()
print(data)

Result:
{
    'exampleFile1_file': {
        'dirpath': '/Users/jonathanlibonati/exampleDir',
        'path': '/Users/jonathanlibonati/exampleDir/exampleFile1.txt',
        'name': 'exampleFile1',
        'extension': '.txt'},
    'exampleFile2_file': {
        'dirpath': '/Users/jonathanlibonati/exampleDir',
        'path': '/Users/jonathanlibonati/exampleDir/exampleFile2.txt',
        'name': 'exampleFile2',
        'extension': '.txt'},
    'subExampledir2_dir': {
        'selfData': {
            'path': '/Users/jonathanlibonati/exampleDir/subExampledir2',
            'name': 'subExampledir2'},
        'contentData': {
            'subExampleFile2_file': {
                'dirpath': '/Users/jonathanlibonati/exampleDir/subExampledir2',
                'path': '/Users/jonathanlibonati/exampleDir/subExampledir2/subExampleFile2.txt',
                'name': 'subExampleFile2',
                'extension': '.txt'
            }
        }
    },
    'subExampledir1_dir': {
        'selfData': {
            'path': '/Users/jonathanlibonati/exampleDir/subExampledir1',
            'name': 'subExampledir1'},
        'contentData': {
            'subExampleFile1_file': {
                'dirpath': '/Users/jonathanlibonati/exampleDir/subExampledir1',
                'path': '/Users/jonathanlibonati/exampleDir/subExampledir1/subExampleFile1.txt',
                'name': 'subExampleFile1',
                'extension': '.txt'
            }
        }
    }
}
```

### newDir(name: str)

### removeFile(file: File)

### removeFiles(*args: File)

### removeAllFiles()

### removeDir(dir: Directory)

### removeDirs(*args: Directory)

### removeAllDirs()

### empty()

### addFiles(*args: File) - asynchronous

### addDirectories(*args: Directory) - asynchronous

### copyFilesTo(dir: Directory) - asynchronous

### copyDirsTo(dir: Directory) - asynchronous

### copy(self, dir: Directory) - asynchronous