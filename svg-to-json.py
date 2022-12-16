import os
import sys
import json

from glob import glob
from xml.dom import minidom


def parse(svg_file):
    dom = minidom.parse(svg_file)
    svg = dom.getElementsByTagName('svg')[0]
    paths = dom.getElementsByTagName('path')
    output = {'viewBox': get_attribute_value(svg, 'viewBox'), 'height': get_attribute_value(svg, 'height'),
              'width': get_attribute_value(svg, 'width'), 'fill': get_attribute_value(svg, 'fill'), 'objects': []}

    for node in paths:
        output['objects'].append({
            'd': get_attribute_value(node, 'd'),
            'attributes': {
                'fill': get_attribute_value(node, 'fill'),
                'stroke': get_attribute_value(node, 'stroke'),
                'strokeWidth': get_attribute_value(node, 'stroke-width'),
                'strokeLinecap': get_attribute_value(node, 'stroke-linecap'),
                'strokeLinejoin': get_attribute_value(node, 'stroke-linejoin')
            }
        })

    return output


def get_attribute_value(element, attribute):
    node = element.getAttributeNode(attribute)
    if node:
        return str(node.nodeValue)
    return


def main():
    if len(sys.argv) < 2:
        print(u'Usage: python svg-to-json.py [input] [output]')
        return

    output = {}
    files = [y for x in os.walk(sys.argv[1]) for y in glob(os.path.join(x[0], '*.svg'))]

    for file in files:
        output[os.path.splitext(os.path.basename(file))[0]] = parse(file)

    with open(sys.argv[2], "w") as outfile:
        outfile.write(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
