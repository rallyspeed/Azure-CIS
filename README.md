# Azure-CIS
Automate Azure subscription check against CIS Benchmark
Output will create a report in HTML format including Azure Subscription name and timestamp

## Prerequisites
Azure CLI 2.0, python3

## Installation
- `git clone https://github.com/rallyspeed/Azure-CIS.git`

## Usage
- `python3 azure-cis.py`

## To do
 - PowerShell Checks
 - Some CLI checks
 - Launch reports for all available subscriptions (instead of one at at time) --> Done

 
 ## Notes
  - It might take a while to run (pending on the number of resources within the Azure Subscription), so be patient.
