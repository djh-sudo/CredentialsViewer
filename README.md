# Windows  CredentialViewer

`cpp`分支是`C++`实现版本。用户需要指定`sid`和`win logon`登录密码即可解密凭证文件。

其中主密钥文件通常在`Protect`文件夹中，同时这个文件夹的子文件夹`S-1-5-*`也表明了`sid`。

```bash
C:\Users\{username}\AppData\Roaming\Microsoft\Protect
```

凭证文件通常在`Credentials`文件夹中

```bash
C:/Users/Administrator/AppData/Roaming/Microsoft/Credentials
```

示例程序见[`main`](https://github.com/djh-sudo/CredentialsViewer/blob/cpp/CredentialsViewer/main.cpp)。

## Other

解密依赖于第三方库`openssl`，需简单配置环境。