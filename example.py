
# IMPORT directory.py
import src.directoryPy.directory as directory
import asyncio

def main():

    # REPLACE WITH A VALID DIRECTORY PATH
    # mac
    #dir = directory.Directory('/Users/jonathanlibonati/Desktop')
    # windows
    dir = directory.Directory('C:/Users/inter/Desktop/exampleDir')

    print(dir.path)
    print('')
    print(dir.data())
    print('')
    print(dir.directories)
    print('')

    for i, file in enumerate(dir.filesList()):
        print('')
        print(f'--File Path {i}: {file.path}')
        print(f'--File Dir Path {i}: {file.dirpath}')
        print(f'--File Name {i}: {file.name}')
        print(f'--File Type {i}: {file.extension}')
        print(f'--File Data {i}: {file.data()}')

    dir.tree(1)
    print('====================================')
    dir.tree(2)
    print('====================================')
    dir.tree(2)
    print('====================================')
    dir.tree()
    print('====================================')

    dir.findDirs([])

if __name__ == '__main__':
    main()