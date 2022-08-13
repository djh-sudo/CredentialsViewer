#pragma once
#include <string>
#include <vector>
#include "MasterKey.h"
#include "Credentials.h"


class CredentialsViewer {

public:

	bool Init(const void const* memory, int szMemory, std::string psw, std::string sid) {
		bool flag = false;
		do {
			flag = m_credential.Init(memory, szMemory);
			if (flag == false) {
				break;
			}
			m_masterKey.SetParameter(psw, sid);
		} while (false);
		return flag;
	}

	bool Decrypt(const void const * memory, int szMemory) {
		bool flag = false;
		DWORD szBlob = 0, szCred = 0, acc = 0, szUsername = 0, szCredentialBlob = 0;
		std::vector<char>blob;

		do {
			flag = m_masterKey.Decrypt(memory, szMemory);
			if (flag == false) {
				break;
			}

			flag = m_credential.Decrypt(m_masterKey.GetMasterKey().data(), m_masterKey.GetMasterKey().size());
			if (flag == false) {
				break;
			}
			m_description = m_credential.GetDescription();
			szBlob = m_credential.GetBlob().size();
			blob.resize(szBlob);
			memcpy(blob.data(), m_credential.GetBlob().data(), szBlob);
			szCred = ((P_CRED_BLOB)(blob.data()))->credSize;
			if (szCred + 4 != szBlob) {
				break;
			}

			flag = ConvertTime(&(((P_CRED_BLOB)blob.data())->LastWritten));
			if (flag == false) {
				break;
			}

			acc = ((P_CRED_BLOB)blob.data())->dwTargetName;
			m_targetName.resize(acc);
			memcpy((char*)m_targetName.c_str(), blob.data() + 52, acc);

			acc += *(PWORD)(blob.data() + 52 + acc);
			acc += *(PWORD)(blob.data() + 56 + acc);
			acc += *(PWORD)(blob.data() + 60 + acc);

			szUsername = *(PWORD)(blob.data() + 64 + acc);
			m_usename.resize(szUsername);
			memcpy((char *)m_usename.data(), (blob.data() + 68 + acc), szUsername);
			acc += szUsername;

			szCredentialBlob = *(PWORD)(blob.data() + 68 + acc);
			m_credentialBlob.resize(szCredentialBlob);
			memcpy((char *)m_credentialBlob.data(), blob.data() + 72 + acc, szCredentialBlob);
			acc += szCredentialBlob;
			if (acc + 72 != szCred) {
				break;
			}
			flag = true;
		} while (false);

		return flag;
	}

	std::string GetGUID() {
		return m_credential.GetGUID();
	}

	std::wstring GetUserName() {
		return m_usename;
	}

	std::string GetCredBlob() {
		return m_credentialBlob;
	}

	std::wstring GetTargetName() {
		return m_targetName;
	}

	std::string GetLastWritten() {
		return m_lastWritten;
	}

	std::wstring GetDescription() {
		return m_description;
	}

	CredentialsViewer() = default;

	~CredentialsViewer() = default;


private:
	MasterKey m_masterKey;
	Credentials m_credential;
	// output information
	std::wstring m_usename;
	std::string m_credentialBlob;
	std::wstring m_targetName;
	std::string m_lastWritten;
	std::wstring m_description;

	bool ConvertTime(FILETIME* fileTime) {
		bool flag = false;
		FILETIME localTime[sizeof(FILETIME)] = { 0 };
		SYSTEMTIME sysTime;
		char timeStamp[32] = { 0 };
		do {
			flag = FileTimeToLocalFileTime(fileTime, localTime);
			if (flag == false) {
				break;
			}
			flag = FileTimeToSystemTime(localTime, &sysTime);
			if (flag == false) {
				break;
			}
			sprintf(timeStamp, "%04d/%02d/%02d %02d:%02d:%02d",
				sysTime.wYear, sysTime.wMonth, sysTime.wDay,
				sysTime.wHour, sysTime.wMinute, sysTime.wSecond);
			m_lastWritten = std::string(timeStamp);

		} while (false);

		return flag;
	}
};