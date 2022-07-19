import utils
import dpapi
from FileFormat import *


def GetLocalCredential(password: str) -> [(DPAPI_ENCRYPTED_CRED, CRED_BLOB)]:
    res = []
    cred_files = utils.TryGetUserCredentials()
    sid_file = utils.TryGetMasterKeyFile()
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
