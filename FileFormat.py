import os


class GUID:
    def __init__(self):
        self.Data1 = ''             # 4 bytes
        self.Data2 = ''             # 2 bytes
        self.Data3 = ''             # 2 bytes
        self.Data4 = ''             # 8 bytes


class DPAPI_MASTERKEY:
    def __init__(self):
        self.dwVersion = ''         # 4 bytes
        self.salt = ''              # 16 bytes
        self.rounds = ''            # 4 bytes
        self.algHash = ''           # 4 bytes
        self.algCrypt = ''          # 4 bytes
        self.pbKey = ''             # not fixed
        self._dwKeyLen = ''         # not exist
        self._masterkey = ''        # not exist

    def info(self):
        print('** Master Key')
        print('dwVersion:', self.dwVersion)
        print('salt:', self.salt)
        print('rounds:', self.rounds)
        print('algHash:', self.algHash)
        print('algCrypt:', self.algCrypt)
        print('pbKey:', self.pbKey)


class DPAPI_MASTERKEY_DOMAINKEY:
    def __init__(self):
        self.dwVersion = ''         # 4 bytes
        self.dwSecrete = ''         # 4 bytes
        self.dwAccesscheckLen = ''  # 4 bytes
        self.guidMasterKey = ''     # 16 bytes
        self.pbSecrete = ''         # not fixed
        self.pbAccesscheck = ''     # not fixed

    def info(self):
        # TODO
        pass


class DPAPI_MASTERKEY_CREDHIST:
    def __init__(self):
        self.dwVersion = ''         # 4 bytes
        self.guid = GUID()          # 16 bytes
        self._guid = ''            # not exist

    def info(self):
        print('** Credentials Info:')
        print('dwVersion:', self.dwVersion)
        print('guid:', self._guid)


class DPAPI_MASTERKEYS:
    def __init__(self):
        self._full_path = ''        # not exist
        self.valid = False          # not exist

        self.dwVersion = ''         # 4 bytes
        
        self.unk0 = ''              # 4 bytes
        self.unk1 = ''              # 4 bytes
        
        self.szGuid = ''            # 36 * 2 bytes
        
        self.unk2 = ''              # 4 bytes
        self.unk3 = ''              # 4 byte
        
        self.dwFlags = ''           # 4 bytes
        
        self.dwMasterKeyLen = ''    # 8 bytes
        self.dwBackupKeyLen = ''    # 8 bytes
        self.dwCreHistLen = ''      # 8 bytes
        self.dwDomainKeyLen = ''    # 8 bytes
        
        self.MasterKey = DPAPI_MASTERKEY()
        self.BackKey = DPAPI_MASTERKEY()
        self.CredHist = DPAPI_MASTERKEY_CREDHIST()
        self.DomainKey = DPAPI_MASTERKEY_DOMAINKEY()

    def info(self):
        print('** Master Keys **')
        print('dwVersion:', self.dwVersion)
        print('szGuid:', self.szGuid)
        print('dwFlags:', self.dwFlags)
        print('dwMasterKeyLen:', self.dwMasterKeyLen)
        print('dwBackupKeyLen:', self.dwBackupKeyLen)
        print('dwCreHistLen:', self.dwCreHistLen)
        print('dwDomainKeyLen', self.dwDomainKeyLen)
        self.MasterKey.info()
        self.BackKey.info()
        self.CredHist.info()

    def save(self, save_path):
        save_name = os.path.join(save_path, 'masterKey.csv')
        assert os.path.exists(save_name), 'save file missing!'
        with open(save_name, 'a', encoding='utf-8') as f:
            f.write(self._full_path.split('/')[-1])
            f.write(',')
            f.write(self.szGuid)
            f.write(',')
            f.write(str(self.dwFlags))
            f.write(',')
            f.write(str(self.dwMasterKeyLen))
            f.write(',')
            f.write(str(self.dwBackupKeyLen))
            f.write(',')
            f.write(self.MasterKey.salt)
            f.write(',')
            f.write(str(self.MasterKey.rounds))
            f.write(',')
            f.write(str(self.MasterKey.algHash))
            f.write(',')
            f.write(str(self.MasterKey.algCrypt))
            f.write(',')
            f.write(self.MasterKey.pbKey)
            f.write(',')
            f.write(self.MasterKey._masterkey)
            f.write(',')
            f.write(self._full_path)
            f.write('\n')
            f.close()


class DPAPI_ENCRYPTED_CRED:
    def __init__(self):
        self._full_path = ''        # not fixed
        self.version = ''           # 4 bytes
        self.blockSize = ''         # 4 bytes
        self.unk = ''               # 4 bytes
        self.blob = DPAPI_BLOB()    # not fixed

    def save(self, save_path):
        save_name = os.path.join(save_path, 'credentials.csv')
        assert os.path.exists(save_name), 'save file missing!'
        with open(save_name, 'a', encoding='utf-8') as f:
            f.write(self.blob._guidMasterKey)
            f.write(',')
            f.write(str(self.blob.algCrypt))
            f.write(',')
            f.write(str(self.blob.dwAlgCryptLen))
            f.write(',')
            f.write(self.blob.pbSalt)
            f.write(',')
            f.write(str(self.blob.algHash))
            f.write(',')
            f.write(str(self.blob.dwAlgHashLen))
            f.write(',')
            f.write(self.blob.pbData)
            f.write(',')
            f.write(self._full_path)
            f.write(',')
        f.close()


class DPAPI_BLOB:
    def __init__(self):
        self.dwVersion = ''             # 4 bytes
        self.guidProvider = GUID()      # 16 bytes
        self._guidProvider = ''         # not exist
        self.dwMasterKeyVersion = ''    # 4 bytes
        self.guidMasterKey = GUID()     # 16 bytes
        self._guidMasterKey = ''        # not exist
        self.dwFlags = ''               # 4 bytes

        self.dwDescriptionLen = ''      # 4 bytes
        self.szDescription = ''         # not fixed

        self.algCrypt = ''              # 4 byte
        self.dwAlgCryptLen = ''         # 4 bytes

        self.dwSaltLen = ''             # 4 bytes
        self.pbSalt = ''                # not fixed

        self.dwHmacKeyLen = ''          # 4 bytes
        self.pbHmackKey = ''            # not fixed

        self.algHash = ''               # 4 byte
        self.dwAlgHashLen = ''          # 4 bytes

        self.dwHmac2KeyLen = ''         # 4 bytes
        self.pbHmack2Key = ''           # not fixed

        self.dwDataLen = ''             # 4 byte
        self.pbData = ''                # not fixed

        self.dwSignLen = ''             # 4 bytes
        self.pbSign = ''                # not fixed

    def info(self):
        print('** BLOB **')
        print('dwVersion:', self.dwVersion)
        print('guidProvider:', self._guidProvider)
        print('dwMasterKeyVersion:', self.dwMasterKeyVersion)
        print('guidMasterKey:', self._guidMasterKey)
        print('dwFlags:', self.dwFlags)
        print('dwDescriptionLen', self.dwDescriptionLen)
        print('szDescription:', self.szDescription)
        print('algCrypt', self.algCrypt)
        print('dwAlgCryptLen:', self.dwAlgCryptLen)
        print('dwSaltLen:', self.dwSaltLen)
        print('pbSalt:', self.pbSalt)
        print('dwHmacKeyLen:', self.dwHmacKeyLen)
        print('pbHmackKey:', self.pbHmackKey)
        print('algHash:', self.algHash)
        print('dwAlgHashLen:', self.dwAlgHashLen)
        print('dwHmac2KeyLen:', self.dwHmac2KeyLen)
        print('pbHmack2Key:', self.pbHmack2Key)
        print('dwDataLen:', self.dwDataLen)
        print('pbData:', self.pbData)
        print('dwSignLen:', self.dwSignLen)
        print('pbSign', self.pbSign)


class FILE_TIME:
    def __init__(self):
        self.dwLowDateTime = ''         # 4 bytes
        self.dwHighDateTime = ''        # 4 bytes
        self._file_time = ''            # not exist


class CRED_BLOB:
    def __init__(self):
        self.credFlags = ''             # 4 bytes
        self.credSize = ''              # 4 bytes
        self.credUnk0 = ''              # 4 bytes

        self.Type = ''                  # 4 bytes
        self.Flags = ''                 # 4 bytes
        self.LastWritten = FILE_TIME()  # 8 bytes
        self.unkFlagsOrSize = ''        # 4 bytes
        self.Persist = ''               # 4 bytes
        self.AttributeCount = ''        # 4 bytes
        self.unk0 = ''                  # 4 bytes
        self.unk1 = ''                  # 4 bytes

        self.dwTargetName = ''          # 4 bytes
        self.TargetName = ''            # not fixed
        self.dwTargetAlias = ''         # 4 bytes
        self.TargetAlias = ''           # not fixed

        self.dwComment = ''             # 4 bytes
        self.Comment = ''               # not fixed

        self.dwUnkData = ''             # 4 bytes
        self.UnkData = ''               # not fixed

        self.dwUserName = ''            # 4 bytes
        self.UserName = ''              # not fixed

        self.CredentialBlobSize = ''    # 4 bytes
        self.CredentialBlob = ''        # not fixed

        self.Attributes = ''            # not fixed[ignore]

    def info(self):
        print('** Credentials **')
        print('credFlags:', self.credFlags)
        print('credSize:', self.credSize)
        print('credUnk0:', self.credUnk0)
        print('Type:', self.Type)
        print('Flags:', self.Flags)
        print('LastWritten:', self.LastWritten._file_time)
        print('unkFlagsOrSize:', self.unkFlagsOrSize)
        print('Persist:', self.Persist)
        print('AttributeCount:', self.AttributeCount)
        print('unk0:', self.unk0)
        print('unk1:', self.unk1)
        print('TargetName:', self.TargetName)
        print('TargetAlias:', self.TargetAlias)
        print('Comment:', self.Comment)
        print('UnkData:', self.UnkData)
        print('UserName:', self.UserName)
        print('CredentialBlob:', self.CredentialBlob)

    def save(self, save_path):
        save_name = os.path.join(save_path, 'credentials.csv')
        assert os.path.exists(save_name), 'save file missing!'
        with open(save_name, 'a', encoding='utf-8') as f:
            f.write(self.LastWritten._file_time)
            f.write(',')
            f.write(str(self.credSize))
            f.write(',')
            f.write(self.TargetName)
            f.write(',')
            f.write(self.UserName)
            f.write(',')
            f.write(self.CredentialBlob)
            f.write('\n')
        f.close()

