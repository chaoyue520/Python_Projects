##直接跳过错误行 PASS

id_miwen=[]
for id_i in data_set['id_initial']:
    try:
        url = ''接口URL''
        req = urllib2.Request(url)
        res_data = urllib2.urlopen(req)
        json_str = res_data.read()
        json_obj = json.loads(json_str)
        id_miwen.append(json_obj['idNo'])
    except Exception as e:
        pass
    continue

## 当报错的时候执行
id_miwen=[]
for id_i in data_set['id_initial']:
    try:
        url = ''接口URL''
        req = urllib2.Request(url)
        res_data = urllib2.urlopen(req)
        json_str = res_data.read()
        json_obj = json.loads(json_str)
    except Exception as e:
        id_miwen.append(0)
    else :
        id_miwen.append(json_obj['idNo'])
