import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from xml.dom import minidom

def generate_flood_warning_cap():
    """Generate a flood warning in CAP format"""
    
    # Create root alert element
    alert = ET.Element('alert')
    alert.set('xmlns', 'urn:oasis:names:tc:emergency:cap:1.2')
    
    # Identifier
    identifier = ET.SubElement(alert, 'identifier')
    identifier.text = f'flood-warning-{datetime.now().strftime("%Y%m%d%H%M%S")}'
    
    # Sender
    sender = ET.SubElement(alert, 'sender')
    sender.text = 'anaespinolar@gmail.com'
    
    # Sent
    sent = ET.SubElement(alert, 'sent')
    sent.text = datetime.now().isoformat() + 'Z'
    
    # Status
    status = ET.SubElement(alert, 'status')
    status.text = 'Actual'
    
    # Message Type
    msg_type = ET.SubElement(alert, 'msgType')
    msg_type.text = 'Alert'
    
    # Scope
    scope = ET.SubElement(alert, 'scope')
    scope.text = 'Public'
    
    # Info element
    info = ET.SubElement(alert, 'info')
    
    # Language
    language = ET.SubElement(info, 'language')
    language.text = 'en-US'
    
    # Category
    category = ET.SubElement(info, 'category')
    category.text = 'Met'
    
    # Event
    event = ET.SubElement(info, 'event')
    event.text = 'Flood Warning'
    
    # Urgency
    urgency = ET.SubElement(info, 'urgency')
    urgency.text = 'Immediate'
    
    # Severity
    severity = ET.SubElement(info, 'severity')
    severity.text = 'Severe'
    
    # Certainty
    certainty = ET.SubElement(info, 'certainty')
    certainty.text = 'Observed'
    
    # Effective
    effective = ET.SubElement(info, 'effective')
    effective.text = datetime.now().isoformat() + 'Z'
    
    # Expires
    expires = ET.SubElement(info, 'expires')
    expires.text = (datetime.now() + timedelta(hours=24)).isoformat() + 'Z'
    
    # Headline
    headline = ET.SubElement(info, 'headline')
    headline.text = 'FLOOD WARNING ISSUED'
    
    # Description
    description = ET.SubElement(info, 'description')
    description.text = 'A Flood Warning means that flooding is imminent or occurring. Move to higher ground immediately.'
    
    # Instruction
    instruction = ET.SubElement(info, 'instruction')
    instruction.text = 'Do not attempt to drive through flooded areas. Turn around and find alternate routes.'
    
    # Area
    area = ET.SubElement(info, 'area')
    
    # Area Description
    area_desc = ET.SubElement(area, 'areaDesc')
    area_desc.text = 'Flood Zone A - Downtown District'
    
    # Polygon (example coordinates)
    polygon = ET.SubElement(area, 'polygon')
    polygon.text = '39.75,-104.99 39.75,-104.98 39.76,-104.98 39.76,-104.99 39.75,-104.99'
    
    # Pretty print XML
    xml_str = minidom.parseString(ET.tostring(alert)).toprettyxml(indent="  ")
    
    return xml_str

# Generate and save the flood warning
if __name__ == '__main__':
    cap_warning = generate_flood_warning_cap()
    print(cap_warning)
    
    # Save to file
    with open('flood_warning.xml', 'w') as f:
        f.write(cap_warning)
    
    print("\n✓ Flood warning saved to flood_warning.xml")