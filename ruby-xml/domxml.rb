require 'rexml/document'
include REXML
 
xmlfile = File.new("starwars.xml")
xmldoc = Document.new(xmlfile)
 
#get root element
root = xmldoc.root
puts "Root element : " + root.attributes["category"]
 
#get power title
xmldoc.elements.each("collection/power"){ 
   |e| puts "Power Title : " + e.attributes["title"] 
}
#get power type
xmldoc.elements.each("collection/power/type") {
   |e| puts "Power Type : " + e.text 
}
 
#get description
xmldoc.elements.each("collection/power/description") {
   |e| puts "Power Description : " + e.text 
}