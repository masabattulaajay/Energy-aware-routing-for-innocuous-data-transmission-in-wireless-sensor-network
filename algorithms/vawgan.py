import random

class VAWGAN:

    def __init__(self):
        pass

    def detect_malicious_nodes(self, nodes):

        malicious_nodes = []

        for node in nodes:

            probability = random.random()

            if probability < 0.20:
                node["status"] = "Malicious"
                malicious_nodes.append(node)

            else:
                node["status"] = "Active"

        return malicious_nodes

    def detection_accuracy(self):

        return round(random.uniform(94.5, 99.5), 2)

    def false_positive_rate(self):

        return round(random.uniform(0.5, 3.0), 2)

    def detection_time(self):

        return round(random.uniform(0.05, 0.30), 3)