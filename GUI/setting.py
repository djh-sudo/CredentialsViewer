import utils
import dpapi
import pickle
from FileFormat import *


def GetLocalCredential(password: str) -> [(DPAPI_ENCRYPTED_CRED, CRED_BLOB)]:
    res = []
    cred_files, cred_path = utils.TryGetUserCredentials()
    sid_file, sid_path = utils.TryGetMasterKeyFile()
    if cred_files:
        pass

    cache_sid_file = dpapi.HandleSIDFile(sid_file)
    for file in cred_files:
        enc_cred, cred = dpapi.GetCredentials(file, flag=False)
        guid = enc_cred.blob._guidMasterKey
        index, sid = dpapi.Search(cache_sid_file, guid)
        if sid:
            master_key = dpapi.GetMasterKey(sid_file[sid][index], password, sid, False)
            enc_cred, cred = dpapi.GetCredentials(file, master_key, False)
        res.append((enc_cred, cred))
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
