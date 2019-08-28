import json
import glob
import xml.etree.ElementTree as ET


path_to_json_files = "PATH_TO_FILES"
read_files = sorted(glob.glob(path_to_json_files + "*.json"))
print(read_files)
# Read all json files from folder and merge to one list
groups = []
for file in read_files:
    with open(file, 'r') as json_file:
        parsed = json.load(json_file)
        for i in parsed['jobContent']:
            groups.append(i)
print(groups)

# Open json with names of test cases
with open('report_links.json', 'r') as json_links:
    links = json.load(json_links)

Number = 0
Errors = 0
Passed = 0

# Create report
report = ET.Element('body')

header = ET.SubElement(report, "h1", attrib={"style": "color: #5e9ca0;"})
header.text = "AUTOTEST REPORT"

for i in groups:
    if i["ScenarioResult"] != "PASS":
        Errors += 1
    else:
        Passed += 1

# Draw table
header = ET.SubElement(report, "h3", attrib={"style": "color: #5e9ca0;"})
header.text = "Summary:"
table = ET.SubElement(report, "table", attrib={"style": "border: 1px solid black;", "cellspacing": "0"})
tablerow = ET.SubElement(table, "tr", attrib={"style": "background-color: grey;"})
tabledata = ET.SubElement(tablerow, "td", attrib={"style": "font-weight: bold;"})
tabledata.text = "Passed"
tabledata = ET.SubElement(tablerow, "td", attrib={"style": "font-weight: bold;"})
tabledata.text = "Failed"
tablerow = ET.SubElement(table, "tr")
tabledata = ET.SubElement(tablerow, "td")
tabledata.text = str(Passed)
tabledata = ET.SubElement(tablerow, "td")
tabledata.text = str(Errors)
br = ET.SubElement(report, 'br')
table = ET.SubElement(report, "table", attrib={"style": "border: 1px solid black;", "cellspacing": "0"})
tablerow = ET.SubElement(table, "tr", attrib={"style": "background-color: grey;"})
tabledata = ET.SubElement(tablerow, "td", attrib={"style": "font-weight: bold;"})
tabledata.text = "Num"
tabledata = ET.SubElement(tablerow, "td", attrib={"style": "font-weight: bold;"})
tabledata.text = "Group"
tabledata = ET.SubElement(tablerow, "td", attrib={"style": "font-weight: bold;"})
tabledata.text = "Name"
tabledata = ET.SubElement(tablerow, "td", attrib={"style": "font-weight: bold;"})
tabledata.text = "Status"
tabledata = ET.SubElement(tablerow, "td", attrib={"style": "font-weight: bold;"})
tabledata.text = "Description"

# Fill table
for i in groups:
    Number += 1
    tablerow = ET.SubElement(table, "tr", attrib={"style": "background-color: yellowgreen;" if i["ScenarioResult"] == "PASS" else "background-color: lightcoral;"})
    tabledata = ET.SubElement(tablerow, "td")
    tabledata.text = str(Number)
    tabledata = ET.SubElement(tablerow, "td")
    tabledata.text = i["HighGrpName"]
    tabledata = ET.SubElement(tablerow, "td")
    tablelink = ET.SubElement(tabledata, "a", attrib={"href": links[i["ScenarioName"]]["link"]})
    tablelink.text = i["ScenarioName"]
    tabledata = ET.SubElement(tablerow, "td")
    tabledata.text = i["ScenarioResult"]
    tabledata = ET.SubElement(tablerow, "td")
    tabledata.text = i["ScenarioReason"]
    print(str(Number) + ". " + i["HighGrpName"] + " - " + i["ScenarioName"] + " - " + i["ScenarioResult"] + " : " + i["ScenarioReason"])


# Save report file
fnm = "report.html"
print("Saving report file: " + fnm)
ET.ElementTree(report).write(fnm)

# Mark job fail in case of Errors
if Errors > 0:
    raise ValueError("Errors count:" + str(Errors))
