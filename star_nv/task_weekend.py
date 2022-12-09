def fun_1(str):
    # import pdb;pdb.set_trace()
    dict_1={}
    for i in str:
        key=dict_1.keys()
        print(key)
        if i in dict_1:
            dict_1[i]+=1
        else:
            dict_1[i]=1
    return dict_1
print(fun_1("helloworld"))

def fun_2(str2):
    s1=""
    if len(str2)<2:
        return ""
    else:
        s1=str2[0:2]+str2[-2:]
        return s1
print(fun_2("he")) 

def fun_3(str3):
    chr=str3[2]
    str3=str3.replace(chr,'$')
    s3=chr+str3[1:]
    return s3
print(fun_3("helloworld"))

class list():
    li=[]
    def append(self,num):
        self.li.append(num)
        return None
    
    def Pop(self,num):
        ab=self.pop()
        return ab
obj1=list
print(obj1([1,2,4,5]))
        
             
                

        
        
        
            
    