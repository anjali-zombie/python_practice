def substring(heystack,needle):
    needle_len =len(needle)
    heystack_len =len(heystack)
    for i in range(heystack_len - needle_len + 1):
        match =True
        for j in range(len(needle)):
            if heystack[i+j] != needle[j]:
                match = False
                break
        if match:
            return i
    return -1

heystack="sadbutsad"
needle="sad"
print(substring(heystack,needle))
#most simple way to thid program is by using find function which goes like 
#heystack.find(needle) 
#which will return first index of this substring
