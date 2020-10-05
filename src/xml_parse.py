import xml.etree.ElementTree as ET

from config import SECURITIES_FILES, HISTORY_FILES


security_rows = []
allowed_secids = set()

for securities_file in SECURITIES_FILES:
    try:
        tree = ET.parse(securities_file)
        root = tree.getroot()
        rows = root.find(".//*[@id='securities']").find("rows")
    except Exception:
        rows = None
    if not rows:
        continue
    for row in rows.iter():
        if row.attrib == {}:
            continue
        security_rows.append(row.attrib)
        allowed_secids.add(row.attrib.get("secid"))


history_rows = []

for history_file in HISTORY_FILES:
    try:
        tree = ET.parse(history_file)
        root = tree.getroot()
        rows = root.find(".//*[@id='history']").find("rows")
    except Exception:
        rows = None
    if not rows:
        continue
    for row in rows.iter():
        if row.attrib == {}:
            continue
        if row.attrib.get("SECID") in allowed_secids:
            history_rows.append(row.attrib)
