import argparse
import dpapi


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-auto', '--auto', action='store_true')
    parser.add_argument('-p', '--password', type=str, help='user logon password')
    parser.add_argument('-mk', '--masterKey', type=str, default=None, help='master key file path')
    parser.add_argument('-sid', '--userSid', type=str, default=None, help='user sid value')
    parser.add_argument('-dc', '--decrypt', type=str, default=None, help='credentials file path to '
                                                                         'be decrypted')
    dpapi.exec(parser)


if __name__ == '__main__':
    main()
