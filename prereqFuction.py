def corses(prereqs_courses1):
    listComb = []
    
    for rows in prereqs_courses1:
        if listComb == []:
            listComb = rows
        else:
            if rows[0] in listComb:
                idx = listComb.index(rows[0])
                listComb.insert(idx+1, rows[1])
            elif rows[1] in listComb:
                idx = listComb.index(rows[1])
                if idx == 0:
                    listComb.insert(0, rows[0])
   
            else:
                listComb.extend(rows)   
    
    val = len(listComb)
    if val % 2 == 0:
      div = int(val/2) 
      div = div - 1
    else:
      div = int((val-1)/2)
    return listComb[div]                    
            


    
prereqs_courses1 = [
    ["Algorithms", "Foundations of Computer Science"],
    ["Data Structures", "Algorithms"],
    ["Foundations of Computer Science", "Logic"],
    ["Logic", "Compilers"],
    ["Compilers", "Distributed Systems"],
    ["hhsdhasgdhsaghd", "Data Structures"]
]
print(corses(prereqs_courses1))