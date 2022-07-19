import utils
import dpapi
import pickle
from FileFormat import *


def GetLocalCredential(password: str) -> [(DPAPI_ENCRYPTED_CRED, CRED_BLOB)]:
    cred_files, cred_path = utils.TryGetUserCredentials()
    sid_file, sid_path = utils.TryGetMasterKeyFile()
    if cred_files and sid_file:
        Save(cred_path, 'cred_path')
        Save(sid_path, 'sid_path')
        Save(cred_files, 'cred_files')
        Save(sid_file, 'sid_file')
    cache_sid_file = dpapi.HandleSIDFile(sid_file)
    if cache_sid_file:
        Save(cache_sid_file, 'cache_sid_file')

    return GetCredentials(password, cred_files, sid_file, cache_sid_file)


def GetCredentials(password: str, cred_files: list, sid_file, cache_sid_file):
    res = []
    for file in cred_files:
        enc_cred, cred, raw = dpapi.GetCredentials(file, flag=False)
        guid = enc_cred.blob._guidMasterKey
        index, sid = dpapi.Search(cache_sid_file, guid)
        if sid:
            master_key = dpapi.GetMasterKey(sid_file[sid][index], password, sid, False)
            enc_cred, cred, raw = dpapi.GetCredentials(file, master_key, False)
        res.append((enc_cred, cred, raw))
    return res


def Save(obj: object, name: str):
    save_file = name
    tmp = './cache'
    if not os.path.exists(tmp):
        os.mkdir(tmp)
    file = open(os.path.join(tmp, save_file), 'wb')
    pickle.dump(obj, file)
    file.close()


def Load(name: str):
    path = f'./cache/{name}'
    if not os.path.exists(path):
        print('no config file found!')
        return None
    else:
        file = open(path, 'rb')
        obj = pickle.load(file)
        file.close()
        return obj


def ToASCII(letter_list: list):
    res = ''
    for letter in letter_list:
        val = int(letter, 16)
        if 0x20 <= val <= 0x7e:
            res += chr(val)
        else:
            res += '.'
    return res
