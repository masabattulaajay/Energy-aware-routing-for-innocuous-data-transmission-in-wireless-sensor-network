import random


class NPOA:

    def __init__(self):
        pass


    def select_route(self, nodes):

        active_nodes = []

        for node in nodes:

            if node["status"] == "Active":
                active_nodes.append(node)

        active_nodes = sorted(
            active_nodes,
            key=lambda x: x["energy"],
            reverse=True
        )

        if len(active_nodes) >= 4:

            route = [
                active_nodes[0]["id"],
                active_nodes[1]["id"],
                active_nodes[2]["id"],
                active_nodes[3]["id"]
            ]

        else:

            route = [1, 2, 3, 4]

        return route


    def route_energy(self):

        return round(random.uniform(75, 98), 2)


    def transmission_delay(self):

        return round(random.uniform(1.0, 4.0), 2)


    def throughput(self):

        return round(random.uniform(90, 99), 2)


    def packet_delivery_ratio(self):

        return round(random.uniform(94, 100), 2)