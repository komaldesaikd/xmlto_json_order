import xmltodict
import json
import pandas as pd
df=pd.DataFrame(columns=['Name','Street','City','PostalCode','IsAttending','Order'])

def jsonreqgen(xmlstr,v_res_data):
    v_nm=[]
    v_street=[]
    v_city=[]
    v_postalcode=[]
    v_attending=[]
    v_order=[]  
    with open(xmlstr, encoding='utf8') as xmlfile:
             obj=xmltodict.parse(xmlfile.read())             
             v_emp=json.dumps(obj)             
             for i in (obj['Employees']['Employee']):                
                v_nm.append(i["Name"])
                v_attending.append(i["IsAttending"])                
                v_order.append(str(i["Order"]))
                v_address= (i["Address"])
                v_street.append(v_address['Street'])
                v_city.append(v_address['City'])
                v_postalcode.append(v_address['PostalCode'])                
             df['Name']= v_nm
             df['Street']=v_street
             df['City']=v_city
             df['PostalCode']=v_postalcode
             df['IsAttending']=v_attending
             df['Order']=v_order             
             ord_sub=[]              
             ord1=[]                                            
             for index, row in df.iterrows(): 
               cust=dict()   
               add_sub={}
               cust_sub={}              
               final_dic={}           
               cust_sub["name"]=row["Name"]
               add_sub["street"]=row["Street"]
               add_sub["city"]=row["City"]
               add_sub["postal_code"]=row["PostalCode"]
               cust_sub["address"]=(add_sub)                                     
               v_od=row["Order"].split(',')               
               v_od=[i.split('x') for i in v_od]               
               v_od=dict(v_od)                              
               item_list=[]  
               for item,value in v_od.items():
                 items_sub={}                
                 for dish in  v_res_data['dishes']:                   
                   if(value.strip()==dish['name']):                                                 
                    items_sub["id"]=dish['id']
                 items_sub["amount"]=int(item)
                 item_list.append(items_sub)               
               cust={"customer":cust_sub,
               "items":item_list}                              
               ord1.append(cust)
             final_dic['orders'] =ord1 
             return final_dic

               


               
