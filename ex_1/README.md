# Ex1

邮件加密发送和接收

## 1. 使用OpenSSL生成私钥、公钥

```bash
openssl genrsa -out priv.key
```

## 2. 使用OpenSSL生成CA证书

```bash
openssl req -new -x509 -key priv.key -out ca.crt
```

## 3. 通过CA申请收发邮件证书

```bash
openssl req -new -key priv.key -out send.pem
openssl req -new -key priv.key -out recv.pem
openssl x509 -req -in send.pem -CA ca.crt -CAkey priv.key -CAcreateserial -out send.cer
openssl x509 -req -in recv.pem -CA ca.crt -CAkey priv.key -CAcreateserial -out recv.cer
```
（cer文件是outlook需要，而下面的crt是另外生成的）

## 4. 导出pfx格式发件证书

```bash
openssl pkcs12 -export -clcerts -in send.crt -inkey priv.key -out send.pfx
```


## 5. 在Outlook登录发件账号

![p1](doc/p1.png)

## 6. 添加收件联系人及其证书

![p2](doc/p2.png)
![p3](doc/p3.png)

## 7. 安装pfx证书及发送邮件

![p4](doc/p4.png)
![p5](doc/p5.png)
![p6](doc/p6.png)

到这里，邮件的加密签名发送就完成了。
## 8.一点补充

一个菜鸡，参考本作业，但踩了点坑，直接无脑抄上面代码并不能直接完成此次实验。直接贴我生成的顺序，能够然后琢磨一下，生成的证书是可以直接导入到outlook中的。
```bash
openssl genrsa -out priv.key
openssl req -new -x509 -key priv.key -out ca.crt

openssl genrsa -out alice.key
openssl req -new -key priv.key -out alicecsr.pem
openssl genrsa -out bob.key
openssl req -new -key priv.key -out bobcsr.pem

openssl x509 -req -in alicecsr.pem -CA ca.crt -CAkey priv.key -CAcreateserial -out alicecert.crt
openssl x509 -req -in bobcsr.pem -CA ca.crt -CAkey priv.key -CAcreateserial -out bobcert.crt

openssl x509 -req -in alicecsr.pem -CA ca.crt -CAkey priv.key -CAcreateserial -out alicecert.cer
openssl x509 -req -in bobcsr.pem -CA ca.crt -CAkey priv.key -CAcreateserial -out bobcert.cer
openssl pkcs12 -export -clcerts -in alicecert.crt -inkey priv.key -out alicepfx.pfx
openssl pkcs12 -export -clcerts -in bobcert.crt -inkey priv.key -out bobpfx.pfx
```
大致是，先创建一个CA证书机构然后安装，最好选择下成为“受信任的更证书颁发”，然后alice(也就是user1)，和bob(user2)分别“被”这个ca机构颁发了证书。
其中，提示输入YOUR NAME or Email Adress时，注意别输重复了，要输入user1的邮箱还是user2的邮箱。
不是很清楚具体用法，深入了解请查询openssl相关内容。
