import pathlib, json
from jinja2 import Environment, FileSystemLoader

def generate(context, template_name,template_dir,output_path):
    env = Environment(loader  = FileSystemLoader(str(template_dir)))
    template = env.get_template(template_name)    
    rendered = template.render(context)
    print(rendered)


