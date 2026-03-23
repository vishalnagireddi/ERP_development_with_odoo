# ERP Development with Odoo – Custom Modules Collection

## Overview

This repository contains a collection of custom-developed modules built on the Odoo ERP framework. Each module addresses specific business requirements such as CRM analytics, task management, project handling, and external tool integration.

The project demonstrates practical experience in designing, developing, and organizing multiple Odoo modules within a single scalable repository.

## Modules Included

### CRM and Analytics

* **crm_dashboard**
  Provides visual dashboards for CRM data including leads and sales performance.

* **crm_dashboard_for_sales_person**
  Focuses on salesperson-level analytics and performance tracking.

* **crm_stages**
  Customization of CRM stages to enhance pipeline management.

### Project and Task Management

* **custom_project**
  Extends project management features in Odoo.

* **custom_project_form**
  Custom forms and UI enhancements for project handling.

* **custom_tasks**
  Task-level customization including tracking and workflow improvements.

### Integrations

* **orangescrum_odoo_integration**
  Integration between Odoo and Orangescrum for project and task synchronization.

### Supporting Files

* **suspect_prospect_ratio (JS & HTML)**
  Implements logic and UI for analyzing conversion ratios.

* **ratio (Text file)**
  Contains reference or calculation-related data.

## Key Features

* Modular Odoo development structure
* CRM analytics and dashboard visualization
* Salesperson performance tracking
* Project and task management customization
* External tool integration (Orangescrum)
* Backend and frontend customization using Odoo framework
  
## Technology Stack

* Odoo Framework
* Python
* XML (Views and UI Definitions)
* JavaScript
* PostgreSQL

## Project Structure

```id="qz1x9c"
.
├── crm_dashboard/
├── crm_dashboard_for_sales_person/
├── crm_stages/
├── custom_project/
├── custom_project_form/
├── custom_tasks/
├── orangescrum_odoo_integration/
├── static_files/
└── supporting_files/
```

## Installation and Setup

### Clone Repository

```id="1j5n2d"
git clone https://github.com/vishalnagireddi/ERP_development_with_odoo.git
```

### Add Modules to Odoo Addons Path

```id="f7m3sk"
cp -r <repository_folder> /path/to/odoo/addons/
```

### Update Apps List

* Open Odoo
* Navigate to Apps
* Click "Update Apps List"

### Install Modules

* Search for each module by name
* Install based on requirements

## Use Cases

* ERP customization and learning
* CRM analytics implementation
* Project and task workflow optimization
* Integration of external project management tools
* Academic and portfolio demonstration

## Learning Outcomes

* Multi-module Odoo development
* Understanding of Odoo architecture and customization
* Backend (Python) and frontend (XML/JS) integration
* Real-world ERP use case implementation

## Author

Vishal Nagireddi

