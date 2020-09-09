require 'rexml/document'
include REXML
 
xmlfile = File.new("starwars.xml")
xmldoc = Document.new(xmlfile)

#the first power
power = XPath.first(xmldoc, "//power")
p power
 
#print power type
XPath.each(xmldoc, "//type") { |e| puts e.text }
 
#get all power format
names = XPath.match(xmldoc, "//format").map {|x| x.text }
p names