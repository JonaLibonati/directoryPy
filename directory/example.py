import directory

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

if __name__ == '__main__':
    main()