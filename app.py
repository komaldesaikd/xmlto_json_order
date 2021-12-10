from flask import Flask, request, render_template,redirect
import xmltodict
import pandas as pd
import ordercreate 
import json
  
app = Flask(__name__) #creating the Flask class object   
v_res_data=''
v_req_json=''
var_list = []
vd_req_json={}  
xmlpath='employee_orders.xml'


@app.route('/')
def home():
    return ('WELCOME')

@app.route('/nourish.me/api/v1/')
def nourishme():
    return ('WELCOME to nourish')    

@app.route('/nourish.me/api/v1/menu', methods=['GET','POST']) #decorator drfines the   
def nourish_menu():        
        if request.method=='POST':
            v_res_data=request.form['jtext']   
            if(v_res_data):
                try: 
                    v_res_data=json.loads(v_res_data)        
                    var_list.append(v_res_data)                           
                    v_req_json=ordercreate.jsonreqgen(xmlpath,v_res_data)                        
                    vd_req_json['json']=v_req_json
                    return redirect('/nourish.me/api/v1/bulk/order')
                except Exception as e:
                        print('There is issue in input data!!!')                
                    
            else:
                print('No input Data!!!')        
        return render_template('menu.html')

@app.route('/nourish.me/api/v1/bulk/order',methods=['GET','POST']) #decorator drfines the   
def bulk_order():        
    if (request.method=='POST'):
        if(len(var_list)>0):
            v_res_data=var_list.pop()                     
            v_req_json=vd_req_json['json']        
            return render_template('order.html', v_req_json=v_req_json) 
        else:
            print('json list is empty!!!')    
    return render_template('order.html')    

if __name__ =='__main__':  
    app.run()