def longestCommonPrefix(strs):
    temp_string=""
    out_string =""
    for i in range(len(strs)):
        ch_str = strs[i]
        if i==0:
            out_string=ch_str
        else:
            if len(ch_str) <= len(out_string):
                for k in range(len(ch_str)):
                    if ch_str[k] == out_string[k]:
                        temp_string += ch_str[k]
                    else:
                        break
                out_string = temp_string
                temp_string =""
            else:
                for k in range(len(out_string)):
                    if out_string[k] == ch_str[k]:
                        temp_string += out_string[k]
                    else:
                        break
                out_string = temp_string
                temp_string =""

    return out_string
strs = ["dog","racer","caow"]
print(longestCommonPrefix(strs))

#strs = ["flower", "flow", "flight"]
#strs.sort()  # Now: ["flight", "flow", "flower"]

#first = strs[0]  # "flight"
#last = strs[-1]  # "flower"

#i = 0
#while i < len(first) and i < len(last) and first[i] == last[i]:
#    i += 1

#print(first[:i])  # Output: "fl"

                


                    
        
