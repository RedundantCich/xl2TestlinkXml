import xml.etree.cElementTree as ET


def create_name_sub_parent(cell_value, section_name, parent):
    added_element = ET.SubElement(parent, section_name, name = cell_value)
    return added_element


def create_text_child(cell_value, section_name, parent):
    ET.SubElement(parent, section_name).text = str(cell_value)


def create_simple_child(parent, section_name):
    added_element = ET.SubElement(parent, section_name)
    return added_element
