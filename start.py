def interpreter_version_check():
    import sys
    if sys.version_info.major != 3:
        print('Python3 is required')
        sys.exit()

if __name__ == '__main__':
    interpreter_version_check()
    import main
    main.main()