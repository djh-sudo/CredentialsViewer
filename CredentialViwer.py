import dpapi


def main():
    # demo
    password = '123456'
    SID = 'S-1-5-21-2300453706-2493150108-2793419970-500'
    master_key = dpapi.GetMasterKey('./demo3/cdadc9c2-a3e5-4abe-b184-e69949c18d05', password, SID)
    dpapi.GetCredentials('./demo3/6FD3FB652B5A61B4225D169E4B4565AA', master_key)


if __name__ == '__main__':
    main()
