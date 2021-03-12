# Modern_ShowInterfaceStatus

A pyATS script using Genie and Jinaj2 templates to create business-ready human readable reports
## Simply a better way to run the show interfaces status command on IOS-XE Devices

Install pyATS

```console
pip install pyats[full]
```
Update the testbed file to reflect your devices. The example uses a 3850. 

Here are the pyATS documentation guides on Testbed files and Device Connectivity:

Testbed and Topology Information: https://pubhub.devnetcloud.com/media/pyats/docs/topology/index.html

Device Connection: https://pubhub.devnetcloud.com/media/pyats-getting-started/docs/quickstart/manageconnections.html

Testbed File Example: https://pubhub.devnetcloud.com/media/pyats/docs/topology/example.html

Device Connections: https://developer.cisco.com/docs/pyats/#!connection-to-devices

Secret Strings (how I encrypted the enable secret in my testbed file): https://pubhub.devnetcloud.com/media/pyats/docs/utilities/secret_strings.html

Ensure SSH connectivity and run the pyATS job

```console
pyats run job Modern_Show_Interface_Status_job.py --testbed-file ../testbed/
```

Review your output files. You should have 3 files in the output folder:

show_int_status_csv.csv
show_int_status_md.md
show_int_status_html.html

I hope you enjoyed my first Python code!
