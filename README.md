# JIRA Release Note Generator

## Overview
The JIRA Release Note Generator is a Python tool designed to automatically fetch issue data from JIRA using the REST API, populate a custom release note template, and export the generated release note in both JSON and PDF formats. This tool aims to streamline the process of creating release notes for software releases, making it efficient and standardized.

## Features
- Fetches data from JIRA projects using the JIRA REST API.
- Populates a customizable release note template.
- Exports release notes in both JSON and PDF formats.

## Prerequisites
- Python 3.x
- Access to a JIRA account with API permissions.
- `requests` library for Python.
- `reportlab` library for PDF generation in Python.

## Installation
Clone the repository and install the required Python libraries.

```bash
git clone [repository-url]
cd [repository-directory]
pip install requests
pip install reportlab

```


## Configuration
Before running the tool, configure your JIRA API credentials and project details in the script.

## Customization
- Modify the ReleaseNoteTemplate class to fit the structure of your release notes.
- Adjust the JIRA API data fetching and processing to suit your specific project needs.

