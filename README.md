# Virtual Machines (VMs)

A study and implementation of Virtual Machine concepts, virtualization architecture, and hypervisor technologies in the context of Operating Systems.

## Overview

Virtual Machines (VMs) enable multiple independent computing environments to operate on a single physical system. Each virtual machine provides an isolated environment with its own operating system, virtual hardware, and applications.

This project explores the architecture, operational principles, resource management mechanisms, and relationship between virtual machines and hypervisors. It also includes a Python-based application structure with static resources, templates, and database storage.

## Project Purpose

The purpose of this project is to develop an understanding of virtualization technology and its role in modern operating systems. It focuses on how virtual machines abstract physical hardware, how hypervisors manage virtual computing environments, and how system resources are allocated to independent virtual machines.

The project also organizes the related concepts and application resources into a structured repository for learning, reference, and further development.

## GitHub Repository

**Repository:** [Virtual Machines and Hypervisors](https://github.com/chatzz06/virtual-machines-and-hyperviser)

Access the source code, application files, templates, and supporting resources through the repository.

## Project Structure

```text
virtual-machines-and-hyperviser/
│
├── Templates/          # HTML templates for the application
│
├── static/             # Static assets such as CSS, JavaScript, and images
│
├── app.py               # Python application entry point
│
├── database.db          # SQLite database
│
├── requirements.txt     # Python dependencies
│
└── README.md             # Project documentation
```

## Core Concepts

### 1. Virtual Machine Architecture

A virtual machine uses a software-defined hardware environment that emulates the essential components of a physical computer.

- **Host Machine:** Provides the physical hardware resources.
- **Hypervisor:** Creates and manages virtual machines.
- **Virtual Hardware:** Provides virtualized CPU, memory, storage, and networking.
- **Guest Operating System:** Runs inside the virtual machine.
- **Applications:** Execute within the guest operating system.

### 2. Virtualization Mechanism

Virtualization abstracts physical hardware and presents it as virtual resources. The hypervisor manages virtual machine execution and coordinates access to the underlying infrastructure.

Each virtual machine maintains its own operating system environment while sharing the host machine's physical resources through the virtualization layer.

### 3. Types of Virtual Machines

**System Virtual Machines**

Provide a complete virtual hardware environment capable of running an independent operating system.

**Process Virtual Machines**

Provide a runtime environment for executing individual programs. The Java Virtual Machine (JVM) is a common example.

### 4. Hypervisor Architecture

Hypervisors are classified into two primary categories:

- **Type 1 — Bare-Metal Hypervisor:** Runs directly on physical hardware.
- **Type 2 — Hosted Hypervisor:** Runs as an application on an existing host operating system.

### 5. Resource Allocation and Management

Virtual machines use resources assigned from the host system. The main resource management components include:

- CPU virtualization
- Memory virtualization
- Storage virtualization
- Network virtualization
- Virtual machine isolation

### 6. Virtual Machine Lifecycle

The typical lifecycle of a virtual machine includes:

1. Creation and configuration
2. Resource provisioning
3. Operating system installation and startup
4. Application execution
5. Suspension or shutdown
6. Maintenance and configuration updates

## Technologies and Tools

- **Python** — Application logic
- **HTML and CSS** — Web interface and presentation, where implemented
- **SQLite** — Database storage
- **Flask** — Web application framework, if used in `app.py`
- **Virtualization Concepts** — Virtual machines, hypervisors, and resource management

## Getting Started

### Prerequisites

- Python 3.x
- Git
- A code editor such as Visual Studio Code

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/chatzz06/virtual-machines-and-hyperviser.git
```

**2. Navigate to the project directory**

```bash
cd virtual-machines-and-hyperviser
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the application**

```bash
python app.py
```

If the application uses Flask's development server, open the local URL displayed in the terminal, commonly `http://127.0.0.1:5000/`.

## Learning Outcomes

- Understanding virtual machine architecture and virtualization principles.
- Identifying the roles of host systems, guest operating systems, and hypervisors.
- Exploring virtual resource allocation and isolation.
- Understanding the organization of a Python-based web application.
- Learning how application templates, static resources, and database files fit into a project structure.

## Conclusion

Virtual machines are an important component of modern computing, providing a way to run independent operating system environments on shared physical hardware. Understanding their architecture, hypervisors, and resource management mechanisms establishes a foundation for further study of operating systems, cloud infrastructure, and virtualization technologies.

---

**Domain:** Operating Systems | Virtualization | Python Application Development
