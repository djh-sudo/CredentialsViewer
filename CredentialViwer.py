import argparse
import dpapi
import utils

# demo command
'''
    [1] python CredentialViwer.py -skey
    [2] python CredentialViwer.py -scred
    [3] python CredentialViwer.py -p 123456 -auto
    [4] python CredentialViwer.py -p 123456 -mk ./demo1/*-db97-*-868d-* -sid S-1-5-21-*-*-*-500
    [5] python CredentialViwer.py -p 123456 -mk ./demo1/*-db97-*-868d-* -sid S-1-5-21-*-*-*-500 
     -dc ./demo1/9EB88D43D3*******6BE1D953BA87AE

'''


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-skey', '--searchKey', action='store_true', help='search the master key')
    parser.add_argument('-scred', '--searchCred', action='store_true', help='Search the credentials file')
    parser.add_argument('-show', '--showInfo', action='store_true', help='output information')
    # dpapi
    parser.add_argument('-auto', '--auto', action='store_true')
    parser.add_argument('-p', '--password', type=str, help='user logon password')
    parser.add_argument('-mk', '--masterKey', type=str, default=None, help='master key file path')
    parser.add_argument('-sid', '--userSid', type=str, default=None, help='user sid value')
    parser.add_argument('-dc', '--decrypt', type=str, default=None, help='credentials file path to '
                                                                         'be decrypted')
    parser.add_argument('-save', '--savePath', type=str, default=None, help='information save path')

    utils.exec(parser)
    dpapi.exec(parser)


if __name__ == '__main__':
    main()
