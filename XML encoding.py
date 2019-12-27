class XMLTag ():

    def __init__(tagName=None, tagCode=None, attribute=[], children=[]):
        self.tagName=tagName
        self.tagCode=tagCode
        self.attribute=attribute
        self.children=children
    
class XMLAttribute():

    def __init__(attributeName=None, attributeCode=None, value=None):
        self.attributeName=attributeName
        self.attributeCode=attributeCode
        self.attributeValue=value

class encodeXML():

    def __init__(root=None, encoded=''):
        self.root=root
        self.encoded=encoded
    
    def encodeRoot(self, root):

        if root!=None:

            encodeTag(root.tagCode)
            for attribute in self.attribute:
                self.encodeAttribute(attribute)

            for children in root.children:
                self.encodeRoot(children)
        
            self.encoded+=' 0'
        
        return
    
    def encodeTag(self, tagCode):

        self.encoded+= ' '+str(tagCode)
        return
    
    def encodeAttribute(self, attribute):

        if attribute.attributeName!=None:

            self.encode+= ' '+str(attribute.attributeCode)
            self.encode+= ' '+str(attribute.value)
        
        return
        
    def XMLtoString(self):

        if self.root!=None:
            self.encodeRoot()

        return


        

