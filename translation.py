import requests  #  实现发送数据给服务器  pip install requests
import hashlib, time, random


def md5(word):
    word = word.encode()
    # 加密之前先进行编码一下
    result = hashlib.md5(word)
    return result.hexdigest()

def youdao(word):
    '''
    这个函数用来实现发送请求（发送翻译的内容）得到翻译的数据
    :return: None
    '''
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    t = md5(
        "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36")
    r = str(int(time.time() * 1000))
    i = r + str(random.randint(0, 9))
    # 字典类型
    words = {
            'i': word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': i,
            'sign': md5("fanyideskweb" + word + i + "n%A-rKaT5fb[Gy?;N5@Tj"),
            'ts': r,
            'bv': t,
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
    }
    # 加请求头 让服务器认识我们
    headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-2089593706@10.108.160.17; OUTFOX_SEARCH_USER_ID_NCOO=903955928.3679626; JSESSIONID=aaat2xDAKcfki5vrlJ--w; ___rl__test__cookies=1580542988571',
            'Host': 'fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
    }
    result = requests.post(url, data=words, headers=headers)
    print(result.text)  # 文本的结果


if __name__ == '__main__':
    a = input('进入翻译软件请按y，退出请按其它任意键 :')
    while a == 'y':
        word = input("请输入需要翻译的词汇/句子：")
        youdao(word)
        a = input('继续翻译请按y，退出请按其它任意键 :')
    print('谢谢使用')
    b = input()


