#include <cstdlib>
#include <iostream>
#include <string>
#include "MasterKey.h"
#include "Credentials.h"


using namespace std;
#define MAX_LEN 4096
/*
* User protect directory
* C:\Users\Administrator\AppData\Roaming\Microsoft\Protect
* Credentials file directory
* C:/Users/Administrator/AppData/Roaming/Microsoft/Credentials
*/

bool Init(char *buffer, int&szBuffer, string path) {
	bool flag = false;
	do {
		if (buffer == NULL) {
			break;
		}
		FILE* fp = fopen(path.c_str(), "rb");
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

	return flag;
}

int main() {
	/*
	* test demo
	*/
	char * buffer = new char[MAX_LEN];
	char* key = new char[MAX_LEN];
	int szBuffer = 0, szKey = 0;;
	bool flag = false;
	memset(buffer, 0, MAX_LEN);
	string sid = "******";
	string passsword = "******";
	MasterKey mKey;
	Credentials credentials;

	do {
		// credential File
		flag = Init(buffer, szBuffer, "../test/694A68E201EB5A1142AE8ACFB8BEA4AC");
		if (flag == false) {
			break;
		}
		flag = credentials.Init(buffer, szBuffer);
		if (flag == false) {
			break;
		}
		std::string guid = credentials.GetGUID();
		flag = Init(key, szKey, "../test/" + guid);
		if (flag == false) {
			break;
		}
		mKey.SetParameter(passsword, sid);
		flag = mKey.Decrypt(key, szKey);
		if (flag == false) {
			break;
		}

		credentials.Decrypt(mKey.GetMasterKey().data(), mKey.GetMasterKey().size());
	
	} while (false);

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