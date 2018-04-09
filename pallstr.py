# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 17:27:33 2018

@author: rajashekhar
"""

class stl:
    
    def str1(self,a):
        b=""
        c=""
        
      
        k=len(a)-1
        i=0
        
        while k>=0:
            if (a[i]>='a' and a[i]<='z') or (a[i]>='A' and a[i]<='Z') or (a[i]>='0' and a[i]<='9'):
                b=a[i]+b
                c=a[i]+c
            k-=1
            i+=1
            
        print("value of b is= "+b)
        """
        k=len(a)-1
        while k>=0:
            if (a[k]>='a' and a[k]<='z') or (a[k]>='A' and a[k]<='Z') or (a[k]>='0' and a[k]<='9'):
                c=a[k]+c
            k-=1
            
            """
        print("value of c is= "+c)
        
        if c.lower()==b.lower():
            print("pallindrone")
        else:
            print("not pallindrone")
            
    
        

            
        
ob=stl()
ob.str1("A man, a plan, a canal: Panama")
#ob.str1("2nitin2")
