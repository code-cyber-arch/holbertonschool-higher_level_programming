#!/usr/bin/python3
"""serialization and deserialization using XML as
    an alternative format to JSON"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")

    def add_elements(parent, dic):
        for key, value in dic.items():
            child = ET.SubElement(parent, key)
            if isinstance(value, dict):
                add_elements(child, value)
            else:
                child.text = str(value)

    add_elements(root, dictionary)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    def elements_to_dict(element):
        dic = {}
        for child in element:
            if len(child) > 0:
                dic[child.tag] = elements_to_dict(child)
            else:
                dic[child.tag] = child.text
        return dic

    dictionary = elements_to_dict(root)

    return dictionary
