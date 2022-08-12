#pragma once
#include <string>
#include <vector>
#include <Windows.h>

/*
* This header file is about DPAPI BLOB
* Keywords: CREDENTIALS
* Also See
* https://github.com/gentilkiwi/mimikatz
*/


typedef struct _DPAPI_BLOB {
	/* Off[DEC]  Description */
	/* acc is unfixed length accumulated! */
	/*   00   */ DWORD dwVersion;
	/*   04   */ GUID guidProvider;
	/*   20   */ DWORD dwMasterKeyVersion;
	/*   24   */ GUID guidMasterKey;
	/*   40   */ DWORD dwFlags;
	/*   44   */ DWORD dwDescriptionLen;
	/* acc+48 */ WCHAR szDescription[ANYSIZE_ARRAY];
	/* acc+48 */ ALG_ID algCrypt;
	/* acc+52 */ DWORD dwAlgCryptLen;
	/* acc+56 */ DWORD dwSaltLen;
	/* acc+60 */ BYTE pbSalt[ANYSIZE_ARRAY];
	/* acc+60 */ DWORD dwHmacKeyLen;
	/* acc+64 */ BYTE pbHmackKey[ANYSIZE_ARRAY];
	/* acc+64 */ ALG_ID algHash;
	/* acc+68 */ DWORD dwAlgHashLen;
	/* acc+72 */ DWORD dwHmac2KeyLen;
	/* acc+76 */ BYTE pbHmack2Key[ANYSIZE_ARRAY];
	/* acc+76 */ DWORD dwDataLen;
	/* acc+80 */ BYTE pbData[ANYSIZE_ARRAY];
	/* acc+80 */ DWORD dwSignLen;
	/* acc+84 */ BYTE pbSign[ANYSIZE_ARRAY];
} DPAPI_BLOB, * P_DPAPI_BLOB;

typedef struct _KULL_M_CRED_ATTRIBUTE {
	/* Off[DEC] Description */
	DWORD Flags;

	DWORD dwKeyword;
	LPWSTR Keyword;

	DWORD ValueSize;
	LPBYTE Value;
} KULL_M_CRED_ATTRIBUTE, * PKULL_M_CRED_ATTRIBUTE;

typedef struct _KULL_M_CRED_BLOB {
	DWORD	credFlags;
	DWORD	credSize;
	DWORD	credUnk0;

	DWORD Type;
	DWORD Flags;
	FILETIME LastWritten;
	DWORD	unkFlagsOrSize;
	DWORD	Persist;
	DWORD	AttributeCount;
	DWORD	unk0;
	DWORD	unk1;

	DWORD	dwTargetName;
	LPWSTR	TargetName;

	DWORD	dwTargetAlias;
	LPWSTR	TargetAlias;

	DWORD	dwComment;
	LPWSTR	Comment;

	DWORD	dwUnkData;
	LPWSTR	UnkData;

	DWORD	dwUserName;
	LPWSTR	UserName;

	DWORD	CredentialBlobSize;
	LPBYTE	CredentialBlob;

	PKULL_M_CRED_ATTRIBUTE* Attributes;

} KULL_M_CRED_BLOB, * PKULL_M_CRED_BLOB;

class Credentials {

public:

	bool Init(const void* memory, int szMemory) {
		bool flag = false;
		
		do {

		} while (false);

		return flag;
	}

	bool Decrypt(const void* memory, int szMemory) {
		bool flag = false;
		do {
			

		} while (false);

		return flag;
	}

	std::string GetGUID() {
		return "";
	}

private:
	
	std::vector<char>m_encBlob;
	std::vector<char>m_blob;
	
	std::vector<char>m_salt;
	GUID m_mKeyGuid;
	
};