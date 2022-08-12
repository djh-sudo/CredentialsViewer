#include <cstdlib>
#include <iostream>
#include <string>
#include "MasterKey.h"


using namespace std;
#define MAX_LEN 2048
/*
* User protect directory
* C:\Users\Administrator\AppData\Roaming\Microsoft\Protect
* Credentials file directory
* C:/Users/Administrator/AppData/Roaming/Microsoft/Credentials
*/

bool Init(char *buffer, int&szBuffer) {
	bool flag = false;
	do {
		if (buffer == NULL) {
			break;
		}
		FILE* fp = fopen("../test/71739bfb-e3f1-4c2b-ab20-05b9655543b4", "rb");
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
	int szBuffer = 0;
	bool flag = false;
	memset(buffer, 0, MAX_LEN);
	string sid = "S-1-5-21-2300453706-2493150108-2793419970-500";
	string passsword = "123456";
	MasterKey mKey;
	do {
		flag = Init(buffer, szBuffer);
		if (flag == false) {
			break;
		}
		mKey.SetParameter(passsword, sid);
		flag = mKey.Decrypt(buffer, szBuffer);
		if (flag == false) {
			break;
		}
	
	} while (false);

	if (buffer != NULL) {
		delete[] buffer;
		buffer = NULL;
	}
	system("pause");
	return 0;
}