def get_suffix(filename,has_dot=False):
    pos=filename.rfind('.')
    if 0<pos<len(filename)-1:
        index=pos if has_dot else pos+1
        return filename[index:]
        print(filename[pos:])
    else:
       return''
#test
print(get_suffix('Exercise-04-祝薇.ipynb'))
