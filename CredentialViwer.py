import argparse
import dpapi
import utils


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-skey', '--searchKey', action='store_true', help='search the master key')
    parser.add_argument('-scred', '--searchCred', action='store_true', help='Search the credentials file')
    # dpapi
    parser.add_argument('-auto', '--auto', action='store_true')
    parser.add_argument('-p', '--password', type=str, help='user logon password')
    parser.add_argument('-mk', '--masterKey', type=str, default=None, help='master key file path')
    parser.add_argument('-sid', '--userSid', type=str, default=None, help='user sid value')
    parser.add_argument('-dc', '--decrypt', type=str, default=None, help='credentials file path to '
                                                                         'be decrypted')
    utils.exec(parser)
    dpapi.exec(parser)
    # args = parser.parse_args()
    # print(args.auto)
    # demo
    # password = '123456'
    # SID = 'S-1-5-21-2300453706-2493150108-2793419970-500'
    # master_key = dpapi.GetMasterKey('./demo3/cdadc9c2-a3e5-4abe-b184-e69949c18d05', password, SID)
    # dpapi.GetCredentials('./demo3/6FD3FB652B5A61B4225D169E4B4565AA', master_key)


if __name__ == '__main__':
    main()
