import os


def main():
    print('hello from main')
    os.environ['CONTINUE_PROCESSING'] = 'True'
    if bool(os.environ['CONTINUE_PROCESSING']):
        print(os.environ['LOGNAME'])


if __name__ == '__main__':
    main()
