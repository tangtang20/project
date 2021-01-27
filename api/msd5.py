import hashlib
#哈希加密，单向加密通道，只能加密，不能解密
msd='守护最可爱的糖糖'
data='世界上最可恶的黄琴'
msd5=hashlib.md5(msd.encode(encoding='utf-8')).hexdigest()
da=hashlib.md5(data.encode(encoding='utf-8')).hexdigest()
print(msd5)
print(da)
