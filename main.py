from flask import Flask, abort, render_template
from jinja2 import Environment, FileSystemLoader
import os, markdown

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
root_directory = "try_project"
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
    
    end_list = [] + (full_end_list)
    for i in range(0, len(end_list)):
        a = end_list[i].rfind("/")
        if i != -1:
            end_list[i] = end_list[i][a+1:]
    
    
    return full_end_list, end_list


@app.route('/')
def index():
    names = get_all_files(os.listdir(f"markdown/files"), [])[0]
    
    return render_template('index.html', files=names)


@app.route('/<filename>')
def sigle_page(filename):
    files, names = get_all_files(os.listdir(f"markdown/files"), [])
    t = False
    for file in files:
            if file.find(filename) != -1:
                file_path = file
                t = True
                break

    if t:
        content = markdown.markdown(open(f"markdown/files/" + file_path).read())
        with open(f"templates/content.html", mode="w") as content_file:
            content_file.write(content)
        #html = Environment(loader=FileSystemLoader("templates/")).get_template("single.html")
        #print(html)
        print(content)
        return render_template('single.html', files=names)
    else:
        return abort(404)


app.run()