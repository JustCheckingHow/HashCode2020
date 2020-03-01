import comet_ml
from algo import NaiveAlgo, save_output
from parser_books import parse_data

import glob
import sys 
import os 


fname = sys.argv[1]
clf = NaiveAlgo()
save_folder = 'data'
fname = glob.glob(f"{save_folder}/*.txt")[0].replace('\\', '/')
# We only need to specify the algorithm and hyperparameters to use:
config = {
    # We pick the Bayes algorithm:
    "algorithm": "bayes",

    # Declare your hyperparameters in the Vizier-inspired format:
    "parameters": {
        "_number_of_scans_power": {
            "type": "float",
            "min": 0.1,
            "max": 6
        },
        '_mapped_power': {
            'type': 'float',
            'min': 0.1,
            'max': 6,
        },
        '_signup_power': {
            'type': 'float',
            'min': 0.1,
            'max': 6,
        },
    },

    # Declare what we will be optimizing, and how:
    "spec": {
        "filename": fname,
        "metric": "score",
        "objective": "maximise",
    },
}

# Next, create an optimizer, passing in the config:
opt = comet_ml.Optimizer(config,
                         api_key=os.environ['API_KEY'],
                         project_name="optimizer-search-GH2020")

# define fit function here!

libs, books_values, days = parse_data(fname)

parameters = {
    '_number_of_scans_power': 1,
    '_mapped_power': 1,
    '_signup_power': 1,
}

# Finally, get experiments, and train your models:
for experiment in opt.get_experiments():
    # Test the model
    params = {}
    for p in ['_number_of_scans_power', '_mapped_power', 
             '_signup_power']:
        params[p] = experiment.get_parameter(p)
    max_libs, _, score = clf.fit([[libs, books_values, days],
                                  list(params.keys()),
                                  list(params.values())])
    experiment.log_metric("score", score)
