# Secure Data Transmission in Wireless Sensor Networks using VAWGAN and NPOA

## Overview

This project is a Flask-based web application that demonstrates secure and efficient data transmission in Wireless Sensor Networks (WSNs). It integrates malicious node detection, optimal routing, and secure message transmission using encryption and hashing techniques.

The system simulates a wireless sensor network where nodes are created, malicious nodes are identified using a VAWGAN-based detection approach, an optimal communication path is selected using the NPOA routing algorithm, and data is securely transmitted between nodes.

---

## Features

- User Authentication
- Wireless Sensor Network Creation
- Malicious Node Detection (VAWGAN)
- Optimal Route Selection (NPOA)
- Secure Message Encryption & Decryption
- SHA-256 Hash Generation
- Secure Data Transmission
- Performance Evaluation
  - Detection Accuracy
  - False Positive Rate
  - Detection Time
  - Energy Consumption
  - Transmission Delay
  - Throughput
  - Packet Delivery Ratio (PDR)

---

## Project Structure

```
my project/
│
├── algorithms/
│   ├── npoa.py
│   ├── routing.py
│   ├── security.py
│   └── vawgan.py
│
├── database/
│   └── db.py
│
├── dataset/
│
├── models/
│
├── static/
│   ├── css/
│   └── js/
│
├── templates/
│   ├── about.html
│   ├── dashboard.html
│   ├── detection.html
│   ├── index.html
│   ├── login.html
│   ├── network.html
│   ├── result.html
│   ├── routing.html
│   └── transmission.html
│
├── database.db
├── app.py
└── README.md
```

---

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript

---

## Algorithms Used

### VAWGAN
Variational Adversarial Wasserstein Generative Adversarial Network (VAWGAN) is used to identify malicious nodes within the wireless sensor network. The algorithm evaluates node behavior and provides detection metrics such as:

- Detection Accuracy
- False Positive Rate
- Detection Time

### NPOA
Nature-inspired Path Optimization Algorithm (NPOA) is used to determine the optimal routing path between sensor nodes while minimizing energy consumption and communication delay.

Performance Metrics:

- Energy Consumption
- Transmission Delay
- Throughput
- Packet Delivery Ratio (PDR)

### Security Module

The security module provides:

- XOR-based Encryption
- XOR-based Decryption
- SHA-256 Hash Generation
- Secure Transmission Status

---

## Application Workflow

1. User Login
2. Create Wireless Sensor Network
3. Detect Malicious Nodes using VAWGAN
4. Select Optimal Route using NPOA
5. Encrypt Message
6. Generate SHA-256 Hash
7. Secure Data Transmission
8. Display Performance Results

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd my-project
```

### Install Dependencies

```bash
pip install flask
```

### Run the Application

```bash
python app.py
```

The application will start at:

```
http://127.0.0.1:5000/
```

---

## Default Login

```
Username: admin
Password: admin
```

*(Use the default credentials configured in the database.)*

---

## Modules

### Home
Displays the project homepage.

### Login
Authenticates the user.

### Dashboard
Provides access to all project functionalities.

### Network
Creates and stores sensor nodes.

### Detection
Detects malicious nodes using the VAWGAN algorithm.

### Routing
Finds the optimal communication path using NPOA.

### Transmission
Encrypts messages, decrypts them, generates SHA-256 hashes, and simulates secure communication.

### Results
Displays overall network performance metrics.

### About
Provides project information.

---

## Performance Metrics

The application evaluates:

- Detection Accuracy
- False Positive Rate
- Detection Time
- Average Energy Consumption
- Transmission Delay
- Throughput
- Packet Delivery Ratio (PDR)

---

## Future Enhancements

- Real-time sensor integration
- Deep learning-based intrusion detection
- Advanced AES/RSA encryption
- Cloud database support
- Graphical network visualization
- Performance comparison with additional routing algorithms

---

## Author

**Ajay Masabattula**

---

## License

This project is developed for educational and research purposes.
