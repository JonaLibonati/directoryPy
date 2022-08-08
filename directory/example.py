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
    """ dir.newFile('exampleFile1.txt')
    dir.newFile('exampleFile2.txt') """
    dir.newDir('subExampledir1')
    dir.newDir('subExampledir2')
    #file_1 = dir.files['exampleFile1.txt']
    #file_2 = dir.files['exampleFile2.txt']
    #dir.removeFiles(file_1, file_2)
    #sub_dir_1 = dir.directories['subExampledir1']
    #sub_dir_2 = dir.directories['subExampledir2']
    dir.empty()
    print(dir.directories)
    print(dir.files)
    dir.tree(1)


    """ print(dir.files)
    print(dir.directories)

    print(dir.data()) """

""" async def dos():
    file = directory.File('/Users/jonathanlibonati/exampleFile.txt')
    dir = directory.Directory('/Users/jonathanlibonati/desktop')

    copied_file = await file.copy(dir)

    print(copied_file.data()) """

if __name__ == '__main__':
    main()
    #asyncio.run(dos())