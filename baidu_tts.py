from aip import AipSpeech

# python 3
# pip install baidu-aip

class TTS:
    def baidutts(self, text):
        """ 你的 APPID AK SK """
        APP_ID = '15014704'
        API_KEY = 'ybTeHM8ol4khsjk9lNVKSDyc'
        SECRET_KEY = 'CmhXByl3XuNnjIlOgnK3ps1MTV5S4g0d'

        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

        result = client.synthesis(text, 'zh', 1, {
            'vol': 5,   # 音量 0-9
            'per': 4,   # 度丫丫
            'spd': 3,   # 语速
            'pit': 2    # 音调
        })

        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            text = text.split('/')[-1]
            text = text.split(' ')[-1]
            with open(f'mp3/auido_{text}.mp3', 'wb') as f:
                f.write(result)
        elif isinstance(result, dict):
            pass
            # if result.err_no == 500:
            #     print("不支持的输入")
            # elif result.err_no == 501:
            #     print("输入参数不正确")
            # elif result.err_no == 502:
            #     print("token 验证失败")
            # elif result.err_no == 503:
            #     print("合成后端错误")
            # else:
            #     pass
