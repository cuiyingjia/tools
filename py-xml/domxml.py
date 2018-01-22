from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("starwars.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
   print ("Root element : %s" % collection.getAttribute("shelf"))

powers = collection.getElementsByTagName("power")

for power in powers:
   print ("*****Power*****")
   if power.hasAttribute("title"):
      print ("Title: %s" % power.getAttribute("title"))

   type = power.getElementsByTagName('type')[0]
   print ("Type: %s" % type.childNodes[0].data)
   format = power.getElementsByTagName('format')[0]
   print ("Format: %s" % format.childNodes[0].data)
   rating = power.getElementsByTagName('rating')[0]
   print ("Rating: %s" % rating.childNodes[0].data)
   description = power.getElementsByTagName('description')[0]
   print ("Description: %s" % description.childNodes[0].data)