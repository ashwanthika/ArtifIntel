import sys
from copy import deepcopy


class burglary_earthquake_alarm(object):
    def __init__(self):
        self.dictionary={'Burg':0.001, 'Ear' :0.002,'Alar_Burg_Ear' :0.95,'Alar_Burg_not_Ear' :0.94,'Alar_not_Burg_Ear' :0.29,'Alar_not_Burg_not_Ear' :0.001,'JC_Alar' : 0.90,'JC_not_Alar' : 0.05,'MC_Alar' :0.70,'MC_not_Alar' : 0.01}
    
    
    def Compute_from_global(self, values_present, Truth_Values):
        b = e = a = j = m = 0.0
        #print(Truth_Values)
        
        if Truth_Values['e'] == 1:
            e = self.dictionary['Ear']
        elif Truth_Values['e'] == 0:
            e = 1 - self.dictionary['Ear']
            
            
        if Truth_Values['b'] == 1:
            b=self.dictionary['Burg']
        elif Truth_Values['b'] == 0:
            b = 1 - self.dictionary['Burg']
            
        if Truth_Values['a'] == 0:
            if Truth_Values['b'] == 1 and Truth_Values['e'] == 1:
                a = 1 - self.dictionary['Alar_Burg_Ear']
            elif Truth_Values['b'] == 1 and Truth_Values['e'] == 0:
                a = 1 - self.dictionary['Alar_Burg_not_Ear']
            elif Truth_Values['b'] == 0 and Truth_Values['e'] == 1:
                a = 1 - self.dictionary['Alar_not_Burg_Ear']
            elif Truth_Values['b'] == 0 and Truth_Values['e'] == 0:
                a = 1 - self.dictionary['Alar_not_Burg_not_Ear']
        elif Truth_Values['a'] == 1:
            if Truth_Values['b'] == 1 and Truth_Values['e'] == 1:
                a = self.dictionary['Alar_Burg_Ear']
            elif Truth_Values['b'] == 1 and Truth_Values['e'] == 0:
                a = self.dictionary['Alar_Burg_not_Ear']
            elif Truth_Values['b'] == 0 and Truth_Values['e'] == 1:
                a = self.dictionary['Alar_not_Burg_Ear']
            elif Truth_Values['b'] == 0 and Truth_Values['e'] == 0:
                a = self.dictionary['Alar_not_Burg_not_Ear']
          
        if Truth_Values['m'] == 1:
            if Truth_Values['a'] == 1:
                m = self.dictionary['MC_Alar']
            elif Truth_Values['a'] == 0:
                m = self.dictionary['MC_not_Alar']
        elif Truth_Values['m'] == 0:
            if Truth_Values['a'] == 1:
                m = 1 - self.dictionary['MC_Alar']
            elif Truth_Values['a'] == 0:
                m = 1 - self.dictionary['MC_not_Alar']
                
                
        if Truth_Values['j'] == 1:
            if Truth_Values['a'] == 1:
                j = self.dictionary['JC_Alar']
            elif Truth_Values['a'] == 0:
                j = self.dictionary['JC_not_Alar']
        elif Truth_Values['j'] == 0:
            if Truth_Values['a'] == 1:
                j = 1 - self.dictionary['JC_Alar']
            elif Truth_Values['a'] == 0:
                j = 1 - self.dictionary['JC_not_Alar']
        return (b * e * a * j * m)
            

    def Append_Hidden_var(self, neumerator, Denominator, truthval):
        All_var = ['B', 'E', 'A', 'J', 'M']
        temp_all_var= ['B', 'E', 'A', 'J', 'M']
        Hidden_var_neum = []
        Hidden_var_Deno = []
        flag = 0
        for items in temp_all_var:
            if items not in neumerator:
               Hidden_var_neum.append(items)
            if items not in Denominator:
                Hidden_var_Deno.append(items)
            #flag = flag + 1
        #print(Hidden_var_neum)
        #print(Hidden_var_Deno)
        Total_Neum = self.Total_prob(neumerator, truthval, Hidden_var_neum)
        if len(Denominator) >= 1:
            Total_Deno = self.Total_prob(Denominator, truthval, Hidden_var_Deno)
            print("Probablity of ( %s given %s) is = %2.12f" % (neumerator, Denominator, (Total_Neum / Total_Deno)))
        else:
            print("Probablity of( %s ) is = %2.12f" % (neumerator, Total_Neum))
            
    
    def Find_c1_c2(self, argv, truthval, length_of_args_input, C1, C2, given):
        #flag = 1
        elements_array=['B','E','A','J','M']
        for flag in range(1,length_of_args_input):
            for i in elements_array:
                post=i.lower()
                #print(flag)
                if argv[flag][0] == 'g':
                    given = True
                elif argv[flag][0] == i:
                    if not given:
                        if argv[flag][1] == 't':
                            truthval[i.lower()] = 1
                        C1.append(i)         
                    elif given:
                        if argv[flag][1] == 't':
                            truthval[i.lower()] = 1
                        C1.append(i)
                        C2.append(i)

    def Set_val(self, truthval, items, Boolean_Val):
        if Boolean_Val == True:
            truthval[items.lower()] = 1
        else:
            truthval[items.lower()] = 0
        return truthval
        
    def Total_prob(self, values_present, truthval, missingElements):
        total = 0.0
        if len(values_present) == 5:
            total = self.Compute_from_global(values_present, truthval)
        else:
            items = missingElements.pop()
            pending_missing_elements = deepcopy(missingElements)
            #print("pending_missing_elements", pending_missing_elements)
            pending_missing_elements1 = deepcopy(missingElements)
            #print("pending_missing_elements copy", pending_missing_elements1)
            values_present1 = deepcopy(values_present)
            values_present2 = deepcopy(values_present)
            values_present1.append(items)
            values_present2.append(items)
            total = self.Total_prob(values_present1, self.Set_val(truthval, items, True), pending_missing_elements) + self.Total_prob(values_present2, self.Set_val(truthval, items, False), pending_missing_elements1)
        return total

    
def main(argv):
    if len(argv) > 6:
        sys.exit(0)
    #print(argv  )    
    C1 = []
    C2 = []
    truthVal = {'b': 0, 'e': 0, 'a': 0, 'j': 0, 'm': 0}
    given = False
    length_of_args_input = len(argv)
    a = burglary_earthquake_alarm()
    a.Find_c1_c2(argv, truthVal, length_of_args_input, C1, C2, given)
    #print(C1)
    #print(C2)
    a.Append_Hidden_var(C1, C2, truthVal)


if __name__ == '__main__':
    main(sys.argv)
