import os

def build_simple():
    f = open("simple_all.html", "w")
    str = "<body><div class='mainco'>"
    for filename in os.scandir("simple"):
        str += "<div class='f7card'>"
        str+= f"<a href='/templates?type={filename.path.split('/')[0]}&id={filename.path.split('/')[1].split('.')[0]}'>{filename.path}</a>"
        if filename.is_file():
            print(filename.path)
            g = open(filename.path, "r")
            re = g.read()
            str += re
        str += "</div>"
    str += "</div></body>"
    
    f.write(str)       
            
build_simple()
    