import pathlib, json
from jinja2 import Environment, FileSystemLoader

from flamapy.metamodels.fm_metamodel.transformations import UVLReader
#from flamapy.metamodels.pysat_metamodel.transformations import FmToPysat
#from flamapy.metamodels.bdd_metamodel.transformations import FmToBDD
#from flamapy.metamodels.pysat_metamodel.operations import PySATProducts
#from flamapy.metamodels.bdd_metamodel.operations import BDDProducts
from flamapy.metamodels.fm_metamodel.operations import FMEstimatedProductsNumber
import random


import pattern_generator

base_dir = pathlib.Path(__file__).parent

#C:\usj\tfm_tools\patterns\behavioral\strategy\configurations\strategy.json
general_group = "behavioral" # behavioral | creational | structural
pattern = "strategy" # singleton | strategy | adapter | factory_method
configuration_path = "configurations"
template_path = "templates"

template_dir = base_dir / "patterns" / general_group / pattern / template_path
json_configuration_dir =  base_dir / "patterns" / general_group / pattern / configuration_path  # base_dir / "patterns/creational/singleton/configurations"


config_name = "strategy.json"
template_name = "strategy.swift.j2"


#print(base_dir)
#print(template_dir)
#print(json_configuration_dir)

configuration = json_configuration_dir / config_name

fm = load_feature_model("singleton_pattern.uvl")
#config = get_random_configuration(fm)
#features_dict = configuration_to_dict(config, fm)

json_config = json.loads(configuration.read_text(encoding="utf-8"))
#print(json_config)
#print(template_name)
#print(json_configuration_dir / config_name)

"""
features = {
    "Class Name": "ConfigManager", 
    "Initialization": "Lazy",
    "Access Method": "getInstance()",
    "Thread Safety": True
}
"""

features = {
    "Context Class Name": "PaymentProcessor",
    "Strategy Interface Name": "PaymentStrategy", 
    "Strategy Interface": "Interface",
    "Strategy Selection": "Factory Method",
    "Number of Strategies": 3,
    "Strategy Caching": True,
    "Default Strategy": True
}

context = {
"features": features
}

pattern_generator.generate(context,template_name,template_dir,"hol")


def load_feature_model(uvl_file_path):
    """Carga un feature model desde un archivo UVL"""
    fm = UVLReader(uvl_file_path).transform()
    return fm