# directory.py
This library is useful for working with structure of files and directories, facilitating the tasks related with those structures, such as getting information, copying, renaming and creating files and directories.

__Installing:__

```
pip install directoryPy
```

__Importing:__

```
from directoryPy import directory
```

## Class File(path: str)
This class creates a File object using a relative or absolute path.
When __File('<new file's path>')__ is instantiated, If the file does not exist, an empty file is created.

```
file = File('jonathanlibonati/exampleFile.txt')
```

### path
Contains the absolute path as string.
```
print(file.path)
```
```
Result:
/Users/jonathanlibonati/exampleFile.txt
```

### dirpath
Contains the absolute path as string of the directory where the file is located.
```
print(file.dirpath)
```
```
Result:
/Users/jonathanlibonati
```

### name
Contains the file name as string without the extension.
```
print(file.name)
```
```
Result:
exampleFile
```

### extension
Contains the file extension as string.
```
print(file.extension)
```
```
Result:
.txt
```

### data()
Return a dictionary with the dirpath, path, name and extension.
```
data = file.data()
print(data)
```
```
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
```
```
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
```
```
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
??????? /Users/jonathanlibonati/exampleDir

???? exampleDir
|
|-- ???? exampleFile1.txt
|-- ???? exampleFile2.txt
|
|-- ???? subExampledir2
|   |
|   |-- ???? subExampleFile2.txt
|
|-- ???? subExampledir1
    |
    |-- ???? subExampleFile1.txt
```

```dir = Directory('/Users/jonathanlibonati/exampleDir')```

### path
Contains the absolute path as string.
```
print(dir.path)
```
```
Result:
/Users/jonathanlibonati/exampleDir
```

### name
Contains the directory name as string.
```
print(dir.name)
```
```
Result:
exampleDir
```

### files
Contains a dictionary with the Files objects which are inside the directory.
```
print(dir.files)
```
```
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
```
```
Result:
[<File object 'exampleFile1'>, <File object 'exampleFile2'>]
```

### directories
Contains a dictionary with the Directory objects which are inside the directory.
```
print(dir.directories)
```
```
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
```
```
Result:
[<Directory object 'subExampledir1'>, <Directory object 'subExampledir2'>]
```

### tree(levels: int)
Prints on the terminal the tree of files and directories. The levels parameter indicates how deep to print.
```
dir.tree(0)
```
```
Result:
??????? /Users/jonathanlibonati/exampleDir

???? exampleDir
```
```
dir.tree(1)
```
```
Result:
??????? /Users/jonathanlibonati/exampleDir

???? exampleDir
|
|-- ???? exampleFile1.txt
|-- ???? exampleFile2.txt
|
|-- ???? subExampledir2
|
|-- ???? subExampledir1
```
```
dir.tree()
```
```
Result:
??????? /Users/jonathanlibonati/exampleDir

???? exampleDir
|
|-- ???? exampleFile1.txt
|-- ???? exampleFile2.txt
|
|-- ???? subExampledir2
|   |
|   |-- ???? subExampleFile2.txt
|
|-- ???? subExampledir1
    |
    |-- ???? subExampleFile1.txt
```
### data()
Return a dictionary with the information of root directory and all the files and directories inside.
```
data = dir.data()

print(data)
```
```
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
data = dir.selfData()

print(data)
```
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
```
```
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
Creates and returns a new directory inside the root directory. If the directory exists already, a FileExistsError is raised.
```
dir.newDir('subExampledir3')

dir.tree(1)
```
```
Result:
??????? /Users/jonathanlibonati/exampleDir

???? exampleDir
|
|-- ???? exampleFile1.txt
|-- ???? exampleFile2.txt
|
|-- ???? subExampledir2
|
|-- ???? subExampledir1
|
|-- ???? subExampledir3
```

### newFile(name: str)
Creates and returns a new empty file inside the root directory. If the file exists already, a FileExistsError is raised.
```
dir.newFile('exampleFile3.txt')

dir.tree(1)
```
```
Result:
??????? /Users/jonathanlibonati/exampleDir

???? exampleDir
|
|-- ???? exampleFile1.txt
|-- ???? exampleFile2.txt
|-- ???? exampleFile3.txt
|
|-- ???? subExampledir2
|
|-- ???? subExampledir1
```

### removeFile(file: File)
Removes an existing file inside the root directory.
```
file_1 = dir.files['exampleFile1.txt']

dir.removeFile(file_1)
```
```
Result:
??????? /Users/jonathanlibonati/exampleDir

???? exampleDir
|
|-- ???? exampleFile2.txt
|
|-- ???? subExampledir2
|
|-- ???? subExampledir1
```

### removeFiles(*args: File)
Removes multiple existing files inside the root directory.
```
file_1 = dir.files['exampleFile1.txt']
file_2 = dir.files['exampleFile2.txt']

dir.removeFiles(file_1, file_2)

dir.tree(1)
```
```
Result:
??????? /Users/jonathanlibonati/exampleDir

???? exampleDir
|
|-- ???? subExampledir2
|
|-- ???? subExampledir1
```

### removeAllFiles()
Removes all files inside the root directory.
```
dir.removeAllFiles()

print(dir.files)
dir.tree(1)
```
```
Result:
{}

??????? /Users/jonathanlibonati/exampleDir

???? exampleDir
|
|-- ???? subExampledir2
|
|-- ???? subExampledir1
```

### removeDir(dir: Directory)
Removes an existing directory inside the root directory.
```
sub_dir_1 = dir.directories['subExampledir1']

dir.removeDir(sub_dir_1)

dir.tree(1)
```
```
Result:
??????? /Users/jonathanlibonati/exampleDir

???? exampleDir
|
|-- ???? exampleFile1.txt
|-- ???? exampleFile2.txt
|
|-- ???? subExampledir2
```
### removeDirs(*args: Directory)
Removes multiple existing directories inside the root directory.
```
sub_dir_1 = dir.directories['subExampledir1']
sub_dir_2 = dir.directories['subExampledir2']

dir.removeDirs(sub_dir_1, sub_dir_2)

dir.tree(1)
```
```
Result:
??????? /Users/jonathanlibonati/exampleDir

???? exampleDir
|
|-- ???? exampleFile1.txt
|-- ???? exampleFile2.txt
```

### removeAllDirs()
Removes all directories inside the root directory.
```
dir.removeAllDirs()

print(dir.directories)
dir.tree(1)
```
```
Result:
{}

??????? /Users/jonathanlibonati/exampleDir

???? exampleDir
|
|-- ???? exampleFile1.txt
|-- ???? exampleFile2.txt
```

### empty()
Removes all directories and files inside the root directory.
```
dir.empty()

print(dir.directories)
print(dir.files)
dir.tree(1)
```
```
Result:
{}
{}

??????? /Users/jonathanlibonati/exampleDir

???? exampleDir
```

### addFiles(*args: File) - asynchronous
Adds files to the root directory and returns it. It is an asynchronous method, therefore it is "awaitable" and uses asyncio.
```
import asyncio

async def main():
    dir = Directory('/Users/jonathanlibonati/exampleDir')

    file_a = File('/Users/jonathanlibonati/file_a.txt')
    file_b = File('/Users/jonathanlibonati/file_b.txt')

    await dir.addFiles(file_a, file_b)

    dir.tree(1)

asyncio.run(main())
```
```
Result:
??????? /Users/jonathanlibonati/exampleDir

???? exampleDir
|
|-- ???? exampleFile1.txt
|-- ???? exampleFile2.txt
|-- ???? file_a.txt
|-- ???? file_b.txt
|
|-- ???? subExampledir2
|
|-- ???? subExampledir1
```

### addDirectories(*args: Directory) - asynchronous
Adds directories to the root directory and returns it. It is an asynchronous method, therefore it is "awaitable" and uses asyncio.
```
import asyncio

async def main():
    dir = Directory('/Users/jonathanlibonati/exampleDir')

    dir_a = Directory('/Users/jonathanlibonati/dir_a')
    dir_b = Directory('/Users/jonathanlibonati/dir_b')

    await dir.addDirectories(dir_a, dir_b)

    dir.tree(1)

asyncio.run(main())
```
```
Result:
??????? /Users/jonathanlibonati/exampleDir

???? exampleDir
|
|-- ???? exampleFile1.txt
|-- ???? exampleFile2.txt
|
|-- ???? subExampledir2
|
|-- ???? subExampledir1
|
|-- ???? dir_a
|
|-- ???? dir_b
```

### copyFilesTo(dir: Directory) - asynchronous
Copies the files of the root directory to other directory. It is an asynchronous method, therefore it is "awaitable" and uses asyncio.
```
import asyncio

async def main():
    dir = Directory('/Users/jonathanlibonati/exampleDir')
    dir_a = Directory('/Users/jonathanlibonati/dir_a')

    await dir.copyFilesTo(dir_a)

    dir_a.tree(1)

asyncio.run(main())
```
```
Result:
??????? /Users/jonathanlibonati/dir_a

???? dir_a
|
|-- ???? exampleFile1.txt
|-- ???? exampleFile2.txt
```

### copyDirsTo(dir: Directory) - asynchronous
Copies the directories of the root directory to other directory. It is an asynchronous method, therefore it is "awaitable" and uses asyncio.
```
import asyncio

async def main():
    dir = Directory('/Users/jonathanlibonati/exampleDir')
    dir_a = Directory('/Users/jonathanlibonati/dir_a')

    await dir.copyDirsTo(dir_a)

    dir_a.tree()

asyncio.run(main())
```
```
Result:
??????? /Users/jonathanlibonati/dir_a

???? dir_a
|
|-- ???? subExampledir2
|   |
|   |-- ???? subExampleFile2.txt
|
|-- ???? subExampledir1
    |
    |-- ???? subExampleFile1.txt
```

### copyAllTo(self, dir: Directory) - asynchronous
Copies the files and directories of the root directory to other directory. It is an asynchronous method, therefore it is "awaitable" and uses asyncio.
```
import asyncio

async def main():
    dir = Directory('/Users/jonathanlibonati/exampleDir')
    dir_a = Directory('/Users/jonathanlibonati/dir_a')

    await dir.copyAllTo(dir_a)

    dir_a.tree()

asyncio.run(main())
```
```
Result:
??????? /Users/jonathanlibonati/dir_a

???? dir_a
|
|-- ???? exampleFile1.txt
|-- ???? exampleFile2.txt
|
|-- ???? subExampledir2
|   |
|   |-- ???? subExampleFile2.txt
|
|-- ???? subExampledir1
    |
    |-- ???? subExampleFile1.txt
```

### copy(self, dir: Directory) - asynchronous
Copies the root directory to other directory. It is an asynchronous method, therefore it is "awaitable" and uses asyncio.
```
import asyncio

async def main():
    dir = Directory('/Users/jonathanlibonati/exampleDir')
    dir_a = Directory('/Users/jonathanlibonati/dir_a')

    await dir.copy(dir_a)

    dir_a.tree()

asyncio.run(main())
```
```
Result:
??????? /Users/jonathanlibonati/dir_a

???? dir_a
|
|-- ???? exampleDir
    |
    |-- ???? exampleFile1.txt
    |-- ???? exampleFile2.txt
    |
    |-- ???? subExampledir2
    |   |
    |   |-- ???? subExampleFile2.txt
    |
    |-- ???? subExampledir1
        |
        |-- ???? subExampleFile1.txt
```

### findDirs([name_1, name_2 ...], deepLevel = -1):
Finds and returns a list of dirs which match with the list of names passed as parameter. By default, the searching is made on all the tree but the scope of the search can be set by the deepLevel parameter.

```
dir_matches_list = dir.findDirs(["subExampledir1"])

    for dir in dir_matches_list:
        dir.tree()
        print('====================================')
```
```
Result:
??????? /Users/jonathanlibonati/Desktop/exampleDir/subExampledir1

???? subExampledir1
|
|-- ???? subExampleFile1.txt

====================================

??????? /Users/jonathanlibonati/Desktop/exampleDir/subExampledir2

???? subExampledir2
|
|-- ???? subExampleFile2.txt

====================================
```

### findFilesByName([name_1, name_2 ...], deepLevel = -1):
Finds and returns a list of Files which match with the list of names passed as parameter. By default, the searching is made on all the tree but but the scope of the search can be set by the deepLevel parameter.

```
files_matches_list = dir.findFilesByName(["subExampleFile1"])

    for file in files_matches_list:
        print('')
        print(f'--File Path: {file.path}')
        print(f'--File Dir Path: {file.dirpath}')
        print(f'--File Name: {file.name}')
        print(f'--File Type: {file.extension}')
        print(f'--File Data: {file.data()}')
        print('====================================')
```
```
Result:
--File Path: /Users/jonathanlibonati/Desktop/exampleDir/subExampledir1/subExampleFile1.txt
--File Dir Path: /Users/jonathanlibonati/Desktop/exampleDir/subExampledir1
--File Name: subExampleFile1
--File Type: .txt
--File Data: {'dirpath': '/Users/jonathanlibonati/Desktop/exampleDir/subExampledir1', 'path': '/Users/jonathanlibonati/Desktop/exampleDir/subExampledir1/subExampleFile1.txt', 'name': 'subExampleFile1', 'extension': '.txt'}
```

### findFilesByExtension([extension_1, extension_2 ...], deepLevel = -1):
Finds and returns a list of Files which match with the list of extensions passed as parameter. By default, the searching is made on all the tree but but the scope of the search can be set by the deepLevel parameter.

```
files_matches_list = dir.findFilesByExtension([".txt"])

    for file in files_matches_list:
        print('')
        print(f'--File Path: {file.path}')
        print(f'--File Dir Path: {file.dirpath}')
        print(f'--File Name: {file.name}')
        print(f'--File Type: {file.extension}')
        print('====================================')
```
```
Result:
--File Path: /Users/jonathanlibonati/Desktop/exampleDir/exampleFile1.txt
--File Dir Path: /Users/jonathanlibonati/Desktop/exampleDir
--File Name: exampleFile1
--File Type: .txt
====================================

--File Path: /Users/jonathanlibonati/Desktop/exampleDir/exampleFile2.txt
--File Dir Path: /Users/jonathanlibonati/Desktop/exampleDir
--File Name: exampleFile2
--File Type: .txt
====================================

--File Path: /Users/jonathanlibonati/Desktop/exampleDir/subExampledir1/subExampleFile1.txt
--File Dir Path: /Users/jonathanlibonati/Desktop/exampleDir/subExampledir1
--File Name: subExampleFile1
--File Type: .txt
====================================

--File Path: /Users/jonathanlibonati/Desktop/exampleDir/subExampledir2/subExampleFile2.txt
--File Dir Path: /Users/jonathanlibonati/Desktop/exampleDir/subExampledir2
--File Name: subExampleFile2
--File Type: .txt
====================================
```



