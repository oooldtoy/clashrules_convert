from flask import Flask,request,send_file
from wakeonlan import send_magic_packet
from pathlib import Path
import os.path,time
import convert,conf

app = Flask(__name__)

@app.route('/')
def hello_world():
    if request.method == 'GET':
        print(1)
    return 'hello world'


#-----------------------------------------#

@app.route('/clash_convert/<group_name>/')
def clash_convert(group_name):
    print(group_name)
    convert_file = Path('convert_rules/'+str(group_name.split(',')) + '.yaml')
    if convert_file.is_file():
        edittime = os.path.getmtime(convert_file)#获取文件修改时间
        if time.time()-edittime > 120:#运行间隔
            try:
                convert.run(group_name.split(','))
            except:
                return '转换失败'
            return send_file('convert_rules/'+str(group_name.split(',')) + '.yaml',as_attachment=True)
        else:
            return send_file('convert_rules/'+str(group_name.split(',')) + '.yaml',as_attachment=True)
    else:
        try:
            convert.run(group_name.split(','))
        except:
            return '转换失败'
        return send_file('convert_rules/'+str(group_name.split(',')) + '.yaml', as_attachment=True)

#-----------------------------------------#


if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)

