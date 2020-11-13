import re
import unidecode


class BusinessCleaner:
    def __init__(self, paragraphs):
        self.paragraphs = paragraphs
        self.regexs = [
            r"(^|\s)[0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]*(\)|.-|\s-)",
            # empieza con 1) o cualquier numero
            r"^\s*[0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]*.-",
            # igual a la de arriba pero si tiene algun espacio al principio
            r"^consiga|^consigna:|consigna",
            r"grafique",
            r"^$",  # string vacio
            r"^\s$",  # solo un espacio
            r"hernan borre",
            r"alejandro prince",
            r"^curso|alumno|profesor|legajo|ayudante",
            r"^trabajo practico",
            r"^fecha de entrega",
            r"\[pic\]",
            r"universidad tecnologica nacional|utn|frba|facultad regional buenos aires|ingenieria en sistemas de informacion|ingenieria en sistemas",
            r"Ingenieria en Sistemas de Informacion",
        ]

    def invalid_paragraph(self, paragraph):
        for regex in self.regexs:
            if re.search(regex, unidecode.unidecode(paragraph.lower())):  # minuscula y sin tildes
                return True
        return False

    def preprocess(self):
        return '\n'.join([paragraph for paragraph in self.paragraphs if not self.invalid_paragraph(paragraph)])
