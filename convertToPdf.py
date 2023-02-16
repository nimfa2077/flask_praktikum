import pdfkit
import os
import markdown

def get_all_files(start_list, full_end_list):
    folder_list = []
    new_start_list = []
    for i in range(0, len(start_list)):
        if os.path.isdir("markdown/files/" + start_list[i]):
            folder_list.append(start_list[i])
        else:
            full_end_list.append(start_list[i])
    if folder_list:
        for folder in folder_list:
            dir = os.listdir("markdown/files/" + folder)
            for i in range(0,len(dir)):
                dir[i] = folder + "/" + dir[i]
            new_start_list += dir
        get_all_files(new_start_list, full_end_list)
    
    html_string = ""
    full_end_list.sort()
    for file in full_end_list:
        if file != "tag1.md":
            html_string += f"<h1>{file[:-3]}</h1>" + markdown.markdown(open("markdown/files/" + file).read())
        else:
            html_string += f"<h1>{file[:-3]}</h1>" + markdown.markdown(open("markdown/files/" + file).read().replace("static/pic/0602.png", "https://illiat.de/static/pic/0602.png"))
            print(html_string)
    return full_end_list, html_string

def convert(filePath):
    _, html = get_all_files(os.listdir("markdown/files"), [])

    pdfkit.from_string(html, filePath, {"enable-local-file-access": ""})

if __name__ == "__main__":
    convert()
