import random


class Routing:

    def __init__(self):
        self.nodes = []


    # Generate Sensor Nodes
    def create_network(self, total_nodes):

        self.nodes = []

        for i in range(1, total_nodes + 1):

            node = {
                "id": i,
                "energy": random.randint(60, 100),
                "x": random.randint(10, 500),
                "y": random.randint(10, 500),
                "status": "Active"
            }

            self.nodes.append(node)

        return self.nodes


    # Display Network
    def get_nodes(self):

        return self.nodes


    # Source Node
    def source_node(self):

        if len(self.nodes) > 0:
            return self.nodes[0]

        return None


    # Destination Node
    def destination_node(self):

        if len(self.nodes) > 0:
            return self.nodes[-1]

        return None


    # Count Active Nodes
    def active_nodes(self):

        count = 0

        for node in self.nodes:

            if node["status"] == "Active":
                count += 1

        return count


    # Count Malicious Nodes
    def malicious_nodes(self):

        count = 0

        for node in self.nodes:

            if node["status"] == "Malicious":
                count += 1

        return count


    # Average Energy
    def average_energy(self):

        total = 0

        for node in self.nodes:
            total += node["energy"]

        if len(self.nodes) == 0:
            return 0

        return round(total / len(self.nodes), 2)