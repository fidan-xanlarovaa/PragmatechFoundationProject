'''if __name__ == '__main__':
    s = input()
list_numalp=[]
list_num=[]
list_alpha=[]
list_lower=[]
list_upper=[]
for i in range (len(s)):
        numalp=s[i].isalnum()
        list_numalp.append(numalp)
        
        num=s[i].isdigit()
        list_num.append(num)
        
        alpha=s[i].isalpha()
        list_alpha.append(alpha)
        
        lower=s[i].islower()
        list_lower.append(lower)
        upper=s[i].isupper()
        list_upper.append(upper)
        
if "True" in list_numalp:
    print("True")
else:
    print("False")

if "True" in list_alpha:
    print("True")
else:
    print("False")

if "True" in list_num:
    print("True")
else:
    print("False")

if "True" in list_lower:
    print("True")
else:
    print("False")

if "True" in list_upper:
    print("True")
else:
    print("False")'''

list1=[{'Ad': 'dggsd', 'Soyad': 'ddfgf', 'Tam_ad': 'a a', 'email': 'gfdgdf', 'maas': 20},{'Ad': 'dggsd', 'Soyad': 'ddfgf', 'Tam_ad': 'dggsd ddfgf', 'email': 'gfdgdf', 'maas': 15}]
list2=[]
for i in list1:
    list2.append(i['maas'])
maxi=max(list2)
index=list2.index(maxi)
max_user=list1[index]
print(max_user['Tam_ad'])


