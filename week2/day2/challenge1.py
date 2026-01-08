MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''   

code =MATRIX_STR.split('\n')
decode_message =""
for col in range(3):
    for row in code:
        if len(row) > col :
           items = row[col] 
           if items.isalnum() :
            decode_message += items 
           else:
             if decode_message and decode_message[-1] != " " :
               decode_message += " "
print(decode_message.strip())
