#include <cstdlib>
#include <iostream>
#include <string>
#include "Analyse.h"


using namespace std;
#define MAX_LEN 4096
/*
* User protect directory
* C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Protect
* Credentials file directory
* C:/Users/%USERNAME%/AppData/Roaming/Microsoft/Credentials
*/

bool Init(char *buffer, int&szBuffer, string path) {
	bool flag = false;
	FILE* fp = NULL;
	do {
		if (buffer == NULL) {
			break;
		}
		fp = fopen(path.c_str(), "rb");
		if (fp == NULL) {
			break;
		}
		fseek(fp, 0, SEEK_END);
		szBuffer = ftell(fp);
		fseek(fp, 0, SEEK_SET);
		flag = (fread(buffer, szBuffer, 1, fp) >= 0);
		if (szBuffer <= 0) {
			break;
		}

	} while (false);
	if (fp) {
		fclose(fp);
		fp = NULL;
	}
	
	return flag;
}

int main() {
	/*
	* test demo
	*/
	char * buffer = new char[MAX_LEN];
	char * key = new char[MAX_LEN];
	int szBuffer = 0, szKey = 0;
	bool flag = false;
	memset(buffer, 0, MAX_LEN);
	memset(key, 0, MAX_LEN);

	string sid = "S-1-5-21-2300453706-2493150108-2793419970-500";
	string passsword = "123456";

	CredentialsViewer viewer;

	do {
		// credential File
		flag = Init(buffer, szBuffer, "../test/138FE05C05C8EACA25971A8C1AA90D72");
		if (flag == false) {
			break;
		}
		// step 1 Initial
		flag = viewer.Init(buffer, szBuffer, passsword, sid);
		if (flag == false) {
			break;
		}

		std::string guid = viewer.GetGUID();
		flag = Init(key, szKey, "C:/Users/Administrator/AppData/Roaming/Microsoft/Protect/" + sid + "/" + guid);
		if (flag == false) {
			break;
		}

		// Step 2 Decrypt
		flag = viewer.Decrypt(key, szKey);
		if (flag == false) {
			break;
		}

	} while (false);

	wcout.imbue(locale("chs"));
	cout << "Analysis result: " << endl;
	wcout << L"Description" << viewer.GetDescription() << endl;
	wcout << "User name: " << viewer.GetTargetName() << endl;
	wcout << L"Target Name: " << viewer.GetUserName() << endl;
	cout << "Last written time: " << viewer.GetLastWritten() << endl;
	cout << "Credential Blob: " << viewer.GetCredBlob() << endl;
	
	/*
	* Ending ...
	*/
	if (buffer != NULL) {
		delete[] buffer;
		buffer = NULL;
	}
	if (key != NULL) {
		delete[] key;
		key = NULL;
	}

	system("pause");
	return 0;
}