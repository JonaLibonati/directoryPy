import directory
import asyncio

def main():

    #REPLACE WITH A VALID DIRECTORY PATH
    dir = directory.Directory('/Users/jonathanlibonati/Canvas')

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

    dir = directory.Directory('/Users/jonathanlibonati/exampleDir')
    dir.tree(0)
    dir.tree(1)
    dir.tree()

    print(dir.files)
    print(dir.directories)

    print(dir.data())

""" async def dos():
    file = directory.File('/Users/jonathanlibonati/exampleFile.txt')
    dir = directory.Directory('/Users/jonathanlibonati/desktop')

    copied_file = await file.copy(dir)

    print(copied_file.data()) """

if __name__ == '__main__':
    main()
    #asyncio.run(dos())