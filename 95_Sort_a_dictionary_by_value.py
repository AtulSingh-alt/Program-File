# Sort a dictionary by value
mark= {"Jahn":43, "Lisa":56,"sid":48}
sv=sorted(mark.items(),key= lambda x:x[1])
print(sv)