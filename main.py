import kivy
from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout 
from kivy.properties import StringProperty,BooleanProperty,ObjectProperty,NumericProperty 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.bubble import Bubble
from kivy.uix.popup import Popup
from kivymd.uix.label import MDLabel
from kivy.uix.progressbar import ProgressBar
from kivy.uix.button import Button
from time import sleep
from kivy.uix.scrollview import ScrollView
import docx


class gri(GridLayout):
    pass

class button(Button):
    pass



class myexample(GridLayout ):

    doc = docx.Document('docx\\somto.docx')
    content = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    
    #file=open("C:\\Users\\Nnonyelume\\Desktop\\clone\\R@1n.txt")
    #content=file.read()
    #file.close()



    '''box_=BoxLayout(orientation="vertical")
    #pro_=ProgressBar(value=val,max=100)
    butt_=Button(text="cancel",size=("40dp","40dp"),)
    label_=Label(text="your popup")
    box_.add_widget(label_)
    box_.add_widget(butt_)
    popup_=Popup(title='Test popup', 
    content=box_,auto_dismiss=False,size_hint=(None,None),size=(400,100))
    butt_.bind(on_press=popup_.dismiss) 
    def testing(self):
        self.popup_.open()'''
    
        
        

    def count(self):
        pass
        
        
            

class myapp(MDApp):
    
    def build (self):
        
        return myexample()
       #pass
    
if __name__=='__main__':
    
    myapp().run()

    print (type(StringProperty()))






