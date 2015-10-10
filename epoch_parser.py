from datetime import datetime
import commands
import string

query = commands.getoutput("pbpaste")

xml_string = "<?xml version=\"1.0\"?>\n<items>\n"

try:
    date = datetime.utcfromtimestamp(query/1000).isoformat() + 'Z'
    date_xml = string.Template("""\t<item uid=\"${date}\" arg=\"${date}\">
                <title>${date}</title>
                <subtitle>Press ENTER to copy \"${date}\" to clipboard</subtitle>
                <icon>icon.png</icon>
                </item>\n""").substitute(locals())
    xml_string += date_xml
except Exception, e:
    none_xml = """\t<item uid=\"none\" arg=\"none\">
                <title>No Suggestions</title>
                <subtitle>Copy valid epoch and type epoch to see output</subtitle>
                <icon>icon.png</icon>
                </item>\n"""
    xml_string += none_xml
finally:
    xml_string += "</items>"
    print xml_string
