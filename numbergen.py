from flask import Flask, request, jsonify
import requests
import concurrent.futures
app=Flask(__name__)
def getData(url):
    response = requests.get(url, timeout=500)
    if response.status_code == 200:
        data = response.json()
        return data.get("numbers", [])
    return []

@app.route('/numbers',methods=['GET'])
def fun():
    urls=request.args.getlist('url')
    num=[]
    for i in urls:
        lst=getData(i)
        for j in lst:
            num.append(j)
    res=sorted(list(set(num)))
    return jsonify({"numbers": res})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8081)