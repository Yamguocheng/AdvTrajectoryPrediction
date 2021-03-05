import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from prediction.TrafficPredict import TrafficPredictInterface
from prediction.evaluate import *
from prediction.visualize import *

if __name__ == "__main__":
    api = TrafficPredictInterface("apolloscape", 4, 6)
    ade, fde = evaluate_error(api)
    draw_error_distribution(ade, fde, "error.png")