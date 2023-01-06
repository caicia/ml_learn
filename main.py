import json
import time

import urllib3

import pandas as pd


def fiddler(df, couponId):
    http = urllib3.PoolManager()

    # Name
    r = http.request(
        'GET',
        'https://user.qihepay.com/api/nologin/sb/queryMchActive?couponId={}'.format(couponId),
        headers={
            'Cookie': 'acw_tc=0bdd26e216652838191886116e00f931019a08406743eafc027e8f520de70f; Hm_lvt_1e57fd5c1f8122d4ab62e054269b39fc=1665283821; Hm_lpvt_1e57fd5c1f8122d4ab62e054269b39fc=1665283841',
            'Host': 'user.qihepay.com',
            'Referer': 'https://user.qihepay.com/pages/blindBox/business?couponId=17',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
        }
    )

    data = json.loads(r.data)
    activeName = data['data']['activeName']

    # first
    r1 = http.request(
        'GET',
        'https://user.qihepay.com/api/nologin/sb/queryMchList?mchName=&mchType=&limit=10&couponId={}'.format(couponId),
        headers={
            'Cookie': 'acw_tc=0bdd26e216652838191886116e00f931019a08406743eafc027e8f520de70f; Hm_lvt_1e57fd5c1f8122d4ab62e054269b39fc=1665283821; Hm_lpvt_1e57fd5c1f8122d4ab62e054269b39fc=1665283841',
            'Host': 'user.qihepay.com',
            'Referer': 'https://user.qihepay.com/pages/blindBox/business?couponId={}'.format(couponId),
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
        }
    )

    data1 = json.loads(r1.data)
    time.sleep(30)
    # second

    r2 = http.request(
        'GET',
        'https://user.qihepay.com/api/nologin/sb/queryMchList?mchName=&mchType=&limit={}&couponId={}'.format(data1['count'] + 1, couponId),
        headers={
            'Cookie': 'acw_tc=0bdd26e216652838191886116e00f931019a08406743eafc027e8f520de70f; Hm_lvt_1e57fd5c1f8122d4ab62e054269b39fc=1665283821; Hm_lpvt_1e57fd5c1f8122d4ab62e054269b39fc=1665283841',
            'Host': 'user.qihepay.com',
            'Referer': 'https://user.qihepay.com/pages/blindBox/business?couponId={}'.format(couponId),
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
        }
    )

    data2 = json.loads(r2.data)
    for one in data2['data']:
        dict_ = {'activeName': activeName, 'mchShotName': one['mchShotName'], 'mchName': one['mchName'],
                 'mchType': one['mchType'], 'servicePhone': one['servicePhone'], 'mchAddr': one['mchAddr']}
        df_tmp = pd.DataFrame(dict_, index=[0])
        df = pd.concat([df, df_tmp], ignore_index=True)

    time.sleep(30)

    return df


if __name__ == '__main__':
    df = pd.DataFrame()
    list_ = [17, 18, 2, 12, 16, 14, 8, 10, 9]
    for i in list_:
        print(i)
        df = fiddler(df, i)
    df.to_excel('./闪支付消费券-20221021.xlsx')
