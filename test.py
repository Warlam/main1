from kivy.app import App
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup


Bool = False
Bool1 = False

Window.clearcolor = (.33, .3, .3, 1)

class Tab1(TabbedPanel):
    pass


place = 0
placei = 0
class MyApp(App):

    def build(self):
        self.itog1 = 0
        self.itog2 = 0
        self.itog3 = 0
        self.itog4 = 0
        self.itog5 = 0
        self.itog6 = 0
        self.itog7 = 0
        self.itog8 = 0
        self.itog9 = 0
        self.itog10 = 0
        self.itog11 = 0
        self.itog12 = 0
        self.itog13 = 0
        self.itog14 = 0
        self.itog15 = 0
        self.itog16 = 0
        self.itogbool1 = True
        self.itogbool2 = True
        self.itogbool3 = True
        self.itogbool4 = True
        self.itogbool5 = True
        self.itogbool6 = True
        self.itogbool7 = True
        self.itogbool8 = True
        self.itogbool9 = True
        self.itogbool10 = True
        self.itogbool11 = True
        self.itogbool12= True
        self.itogbool13 = True
        self.itogbool14 = True
        self.itogbool15 = True
        self.itogbool16 = True

        #Ползунок(комнаты)
        g1 = GridLayout(cols=1, size_hint = (1,1), size_hint_y=None, spacing=1)
        #кнопки
        btn = Button(text='Комната 1', size_hint_y=None, height=40, on_press = self.btn1)
        g1.add_widget(btn)
        btn = Button(text='Комната 2', size_hint_y=None, height=40, on_press=self.btn2)
        g1.add_widget(btn)
        btn = Button(text='Комната 3', size_hint_y=None, height=40, on_press=self.btn3)
        g1.add_widget(btn)
        btn = Button(text='Комната 4', size_hint_y=None, height=40, on_press=self.btn4)
        g1.add_widget(btn)
        btn = Button(text='Комната 5', size_hint_y=None, height=40, on_press=self.btn5)
        g1.add_widget(btn)
        btn = Button(text='Комната 6', size_hint_y=None, height=40, on_press=self.btn6)
        g1.add_widget(btn)
        btn = Button(text='Комната 7', size_hint_y=None, height=40, on_press=self.btn7)
        g1.add_widget(btn)
        btn = Button(text='Комната 8', size_hint_y=None, height=40, on_press=self.btn8)
        g1.add_widget(btn)
        btn = Button(text='Комната 9', size_hint_y=None, height=40, on_press=self.btn9)
        g1.add_widget(btn)
        btn = Button(text='Комната 10', size_hint_y=None, height=40, on_press=self.btn10)
        g1.add_widget(btn)
        btn = Button(text='Комната 11', size_hint_y=None, height=40, on_press=self.btn11)
        g1.add_widget(btn)
        btn = Button(text='Комната 12', size_hint_y=None, height=40, on_press=self.btn12)
        g1.add_widget(btn)
        btn = Button(text='Комната 13', size_hint_y=None, height=40, on_press=self.btn13)
        g1.add_widget(btn)
        btn = Button(text='Комната 14', size_hint_y=None, height=40, on_press=self.btn14)
        g1.add_widget(btn)
        btn = Button(text="Баня", size_hint_y=None, height=40, on_press=self.btn15)
        g1.add_widget(btn)
        btn = Button(text="Дом", size_hint_y=None, height=40, on_press=self.btn16)
        g1.add_widget(btn)

        #popup

        bxl4 = BoxLayout(orientation = 'vertical')
        scrl3 = ScrollView(size_hint=(1, .9))
        bxl5 = BoxLayout(orientation = 'horizontal', size_hint=(1, .1))
        self.txt1 = TextInput(text='', multiline=False)
        self.txt2 = TextInput(text='', multiline=False)
        bxl5.add_widget(Label(text = 'Название:'))
        bxl5.add_widget(self.txt1)
        bxl5.add_widget(Label(text='Стоимость:'))
        bxl5.add_widget(self.txt2)
        btn = Button(text='Добавить позицию')
        btn.bind(on_press = self.menuadd)
        bxl5.add_widget(btn)
        #popup gl
        self.gl5 = GridLayout(cols=2, size_hint = (1,1), row_force_default=True,size_hint_y=None, row_default_height=40, spacing = 1)
        self.gl5.bind(minimum_height=self.gl5.setter('height'))
        scrl3.add_widget(self.gl5)
        bxl4.add_widget(scrl3)
        bxl4.add_widget(bxl5)
        self.popup = Popup(title='Меню',content=bxl4, size_hint=(None, None), size=(700, 400))
        f = open('menu.txt', 'a+')
        f.close()
        f = open('menu.txt', 'r')
        a = f.read()
        s = a.split()
        n = 0
        for word in s:
            n = n + 1
        for i in range(0, n, 2):
            self.gl5.add_widget(Label(text=s[i]))
            self.gl5.add_widget(Label(text=s[i+1]+'руб'))
        f.close()


        btn = Button(text="Меню", size_hint_y=None, height=40, on_press=self.popup1)
        btn.bind(on_press = self.btn1 )
        g1.add_widget(btn)
        g1.bind(minimum_height=g1.setter('height'))
        b1 = (ScrollView(size_hint=(.1, 1), size=(Window.width, Window.height)))
        b1.add_widget(g1)
        self.general=BoxLayout()
        self.general.add_widget(b1)
        return self.general

    def obnovit1(self,instance):
        self.itog1 = 0
        f = open('chet1.txt', 'r')
        a = f.read()
        s = a.split()
        n = 0
        for word in s:
            n = n+1
        f.close()
        f = open('chet1.txt', 'w')
        f.close()
        self.txtbx.text = '0 руб'
        for i in range(0,n):
            self.gl6.remove_widget(self.gl6.children[0])

    def obnovit2(self,instance):
        self.itog2 = 0
        f = open('chet2.txt', 'r')
        a = f.read()
        s = a.split()
        n = 0
        for word in s:
            n = n+1
        f.close()
        f = open('chet2.txt', 'w')
        f.close()
        self.txtbx1.text = '0 руб'
        for i in range(0,n):
            self.gl7.remove_widget(self.gl7.children[0])

    def obnovit3(self,instance):
        self.itog3 = 0
        f = open('chet3.txt', 'r')
        a = f.read()
        s = a.split()
        n = 0
        for word in s:
            n = n+1
        f.close()
        f = open('chet3.txt', 'w')
        f.close()
        self.txtbx3.text = '0 руб'
        for i in range(0,n):
            self.gl8.remove_widget(self.gl8.children[0])

    def obnovit4(self,instance):
        self.itog4 = 0
        f = open('chet4.txt', 'r')
        a = f.read()
        s = a.split()
        n = 0
        for word in s:
            n = n+1
        f.close()
        f = open('chet4.txt', 'w')
        f.close()
        self.txtbx4.text = '0 руб'
        for i in range(0,n):
            self.gl9.remove_widget(self.gl9.children[0])

    def obnovit5(self,instance):
        self.itog5 = 0
        f = open('chet5.txt', 'r')
        a = f.read()
        s = a.split()
        n = 0
        for word in s:
            n = n+1
        f.close()
        f = open('chet5.txt', 'w')
        f.close()
        self.txtbx5.text = '0 руб'
        for i in range(0,n):
            self.gl10.remove_widget(self.gl10.children[0])

    def obnovit6(self,instance):
        self.itog6 = 0
        f = open('chet6.txt', 'r')
        a = f.read()
        s = a.split()
        n = 0
        for word in s:
            n = n+1
        f.close()
        f = open('chet6.txt', 'w')
        f.close()
        self.txtbx6.text = '0 руб'
        for i in range(0,n):
            self.gl11.remove_widget(self.gl11.children[0])

    def obnovit7(self,instance):
        self.itog7 = 0
        f = open('chet7.txt', 'r')
        a = f.read()
        s = a.split()
        n = 0
        for word in s:
            n = n+1
        f.close()
        f = open('chet7.txt', 'w')
        f.close()
        self.txtbx7.text = '0 руб'
        for i in range(0,n):
            self.gl12.remove_widget(self.gl12.children[0])

    def obnovit8(self,instance):
        self.itog8 = 0
        f = open('chet8.txt', 'r')
        a = f.read()
        s = a.split()
        n = 0
        for word in s:
            n = n+1
        f.close()
        f = open('chet8.txt', 'w')
        f.close()
        self.txtbx8.text = '0 руб'
        for i in range(0,n):
            self.gl13.remove_widget(self.gl13.children[0])

    def obnovit9(self,instance):
        self.itog9 = 0
        f = open('chet9.txt', 'r')
        a = f.read()
        s = a.split()
        n = 0
        for word in s:
            n = n+1
        f.close()
        f = open('chet9.txt', 'w')
        f.close()
        self.txtbx9.text = '0 руб'
        for i in range(0,n):
            self.gl14.remove_widget(self.gl14.children[0])

    def obnovit10(self,instance):
        self.itog10 = 0
        f = open('chet10.txt', 'r')
        a = f.read()
        s = a.split()
        n = 0
        for word in s:
            n = n+1
        f.close()
        f = open('chet10.txt', 'w')
        f.close()
        self.txtbx10.text = '0 руб'
        for i in range(0,n):
            self.gl15.remove_widget(self.gl15.children[0])

    def obnovit11(self,instance):
        self.itog11 = 0
        f = open('chet1.txt', 'r')
        a = f.read()
        s = a.split()
        n = 0
        for word in s:
            n = n+1
        f.close()
        f = open('chet11.txt', 'w')
        f.close()
        self.txtbx11.text = '0 руб'
        for i in range(0,n):
            self.gl16.remove_widget(self.gl16.children[0])

    def obnovit12(self,instance):
        self.itog12 = 0
        f = open('chet12.txt', 'r')
        a = f.read()
        s = a.split()
        n = 0
        for word in s:
            n = n+1
        f.close()
        f = open('chet12.txt', 'w')
        f.close()
        self.txtbx12.text = '0 руб'
        for i in range(0,n):
            self.gl17.remove_widget(self.gl17.children[0])

    def obnovit13(self,instance):
        self.itog13 = 0
        f = open('chet13.txt', 'r')
        a = f.read()
        s = a.split()
        n = 0
        for word in s:
            n = n+1
        f.close()
        f = open('chet13.txt', 'w')
        f.close()
        self.txtbx13.text = '0 руб'
        for i in range(0,n):
            self.gl18.remove_widget(self.gl18.children[0])

    def obnovit14(self,instance):
        self.itog1 = 0
        f = open('chet14.txt', 'r')
        a = f.read()
        s = a.split()
        n = 0
        for word in s:
            n = n+1
        f.close()
        f = open('chet14.txt', 'w')
        f.close()
        self.txtbx14.text = '0 руб'
        for i in range(0,n):
            self.gl19.remove_widget(self.gl19.children[0])

    def obnovit15(self,instance):
        self.itog15 = 0
        f = open('chet15.txt', 'r')
        a = f.read()
        s = a.split()
        n = 0
        for word in s:
            n = n+1
        f.close()
        f = open('chet15.txt', 'w')
        f.close()
        self.txtbx15.text = '0 руб'
        for i in range(0,n):
            self.gl20.remove_widget(self.gl20.children[0])

    def obnovit16(self,instance):
        self.itog16 = 0
        f = open('chet16.txt', 'r')
        a = f.read()
        s = a.split()
        n = 0
        for word in s:
            n = n+1
        f.close()
        f = open('chet16.txt', 'w')
        f.close()
        self.txtbx16.text = '0 руб'
        for i in range(0,n):
            self.gl21.remove_widget(self.gl21.children[0])

    def ti1_1_action(self,instance):
        f = open('pas1.txt', 'w+')
        f.write(str(self.ti1_1.text))
        f.close()

    def ti1_2_action(self,instance):
        f = open('predopl1.txt', 'w+')
        f.write(str(self.ti1_2.text))
        f.close()

    def ti2_1_action(self,instance):
        f = open('pas2.txt', 'w+')
        f.write(str(self.ti2_1.text))
        f.close()

    def ti2_2_action(self,instance):
        f = open('predopl2.txt', 'w+')
        f.write(str(self.ti2_2.text))
        f.close()

    def ti3_1_action(self,instance):
        f = open('pas3.txt', 'w+')
        f.write(str(self.ti3_1.text))
        f.close()

    def ti3_2_action(self,instance):
        f = open('predopl3.txt', 'w+')
        f.write(str(self.ti3_2.text))
        f.close()

    def ti4_1_action(self,instance):
        f = open('pas4.txt', 'w+')
        f.write(str(self.ti4_1.text))
        f.close()

    def ti4_2_action(self,instance):
        f = open('predopl4.txt', 'w+')
        f.write(str(self.ti4_2.text))
        f.close()

    def ti5_1_action(self,instance):
        f = open('pas5.txt', 'w+')
        f.write(str(self.ti5_1.text))
        f.close()

    def ti5_2_action(self,instance):
        f = open('predopl5.txt', 'w+')
        f.write(str(self.ti5_2.text))
        f.close()

    def ti6_1_action(self,instance):
        f = open('pas6.txt', 'w+')
        f.write(str(self.ti6_1.text))
        f.close()

    def ti6_2_action(self,instance):
        f = open('predopl6.txt', 'w+')
        f.write(str(self.ti6_2.text))
        f.close()

    def ti7_1_action(self,instance):
        f = open('pas7.txt', 'w+')
        f.write(str(self.ti7_1.text))
        f.close()

    def ti7_2_action(self,instance):
        f = open('predopl7.txt', 'w+')
        f.write(str(self.ti7_2.text))
        f.close()

    def ti8_1_action(self,instance):
        f = open('pas8.txt', 'w+')
        f.write(str(self.ti8_1.text))
        f.close()

    def ti8_2_action(self,instance):
        f = open('predopl8.txt', 'w+')
        f.write(str(self.ti8_2.text))
        f.close()

    def ti9_1_action(self,instance):
        f = open('pas9.txt', 'w+')
        f.write(str(self.ti9_1.text))
        f.close()

    def ti9_2_action(self,instance):
        f = open('predopl9.txt', 'w+')
        f.write(str(self.ti9_2.text))
        f.close()

    def ti10_1_action(self,instance):
        f = open('pas10.txt', 'w+')
        f.write(str(self.ti10_1.text))
        f.close()

    def ti10_2_action(self,instance):
        f = open('predopl10.txt', 'w+')
        f.write(str(self.ti10_2.text))
        f.close()

    def ti11_1_action(self,instance):
        f = open('pas11.txt', 'w+')
        f.write(str(self.ti11_1.text))
        f.close()

    def ti11_2_action(self,instance):
        f = open('predopl11.txt', 'w+')
        f.write(str(self.ti11_2.text))
        f.close()

    def ti12_1_action(self,instance):
        f = open('pas12.txt', 'w+')
        f.write(str(self.ti12_1.text))
        f.close()

    def ti12_2_action(self,instance):
        f = open('predopl12.txt', 'w+')
        f.write(str(self.ti12_2.text))
        f.close()

    def ti13_1_action(self,instance):
        f = open('pas13.txt', 'w+')
        f.write(str(self.ti13_1.text))
        f.close()

    def ti13_2_action(self,instance):
        f = open('predopl13.txt', 'w+')
        f.write(str(self.ti13_2.text))
        f.close()

    def ti14_1_action(self,instance):
        f = open('pas14.txt', 'w+')
        f.write(str(self.ti14_1.text))
        f.close()

    def ti14_2_action(self,instance):
        f = open('predopl14.txt', 'w+')
        f.write(str(self.ti14_2.text))
        f.close()

    def ti15_1_action(self,instance):
        f = open('pas15.txt', 'w+')
        f.write(str(self.ti15_1.text))
        f.close()

    def ti15_2_action(self,instance):
        f = open('predopl15.txt', 'w+')
        f.write(str(self.ti15_2.text))
        f.close()

    def ti16_1_action(self,instance):
        f = open('pas16.txt', 'w+')
        f.write(str(self.ti16_1.text))
        f.close()

    def ti16_2_action(self,instance):
        f = open('predopl16.txt', 'w+')
        f.write(str(self.ti16_2.text))
        f.close()

    def menuadd(self, instance):
        text = self.txt1.text
        text1 = self.txt2.text
        f = open('menu.txt', 'a+')
        f.write(str(text)+' '+str(text1)+ '\n')
        f.close()
        self.gl5.add_widget(Label(text=text))
        self.gl5.add_widget(Label(text=text1+'руб'))
        btn = Button(text=text, size_hint_y=None, height=35)
        btn.bind(on_release=lambda btn: self.dd1.select(btn.text))
        self.dd1.add_widget(btn)

    def dobavitvschet1(self,instance):
        text = self.lblnazvanie.text
        f = open('menu.txt','r')
        a = f.read()
        s = a.split()
        n=0
        for word in s:
            n = n+1

        for i in range(0,n):
            if s[i] == text:
                cena = s[i+1]

        f.close()
        self.gl6.add_widget(Label(text=text))
        self.gl6.add_widget(Label(text=cena+' руб'))
        self.itog1 = int(self.itog1) + int(cena)
        self.txtbx.text = str(self.itog1)+' руб'
        f = open('chet1.txt', 'a+')
        f.write(text +' '+ cena + '\n')

    def dobavitvschet2(self,instance):
        text = self.lblnazvanie.text
        f = open('menu.txt','r')
        a = f.read()
        s = a.split()
        n=0
        for word in s:
            n = n+1

        for i in range(0,n):
            if s[i] == text:
                cena = s[i+1]

        f.close()
        self.gl7.add_widget(Label(text=text))
        self.gl7.add_widget(Label(text=cena+' руб'))
        self.itog2 = int(self.itog2) + int(cena)
        self.txtbx1.text = str(self.itog2)+' руб'
        f = open('chet2.txt', 'a+')
        f.write(text +' '+ cena + '\n')

    def dobavitvschet3(self,instance):
        text = self.lblnazvanie.text
        f = open('menu.txt','r')
        a = f.read()
        s = a.split()
        n=0
        for word in s:
            n = n+1

        for i in range(0,n):
            if s[i] == text:
                cena = s[i+1]

        f.close()
        self.gl8.add_widget(Label(text=text))
        self.gl8.add_widget(Label(text=cena+' руб'))
        self.itog3 = int(self.itog3) + int(cena)
        self.txtbx3.text = str(self.itog3)+' руб'
        f = open('chet3.txt', 'a+')
        f.write(text +' '+ cena + '\n')

    def dobavitvschet4(self,instance):
        text = self.lblnazvanie.text
        f = open('menu.txt','r')
        a = f.read()
        s = a.split()
        n=0
        for word in s:
            n = n+1

        for i in range(0,n):
            if s[i] == text:
                cena = s[i+1]

        f.close()
        self.gl9.add_widget(Label(text=text))
        self.gl9.add_widget(Label(text=cena+' руб'))
        self.itog4 = int(self.itog4) + int(cena)
        self.txtbx4.text = str(self.itog4)+' руб'
        f = open('chet4.txt', 'a+')
        f.write(text +' '+ cena + '\n')

    def dobavitvschet5(self,instance):
        text = self.lblnazvanie.text
        f = open('menu.txt','r')
        a = f.read()
        s = a.split()
        n=0
        for word in s:
            n = n+1

        for i in range(0,n):
            if s[i] == text:
                cena = s[i+1]

        f.close()
        self.gl10.add_widget(Label(text=text))
        self.gl10.add_widget(Label(text=cena+' руб'))
        self.itog5 = int(self.itog5) + int(cena)
        self.txtbx5.text = str(self.itog5)+' руб'
        f = open('chet5.txt', 'a+')
        f.write(text +' '+ cena + '\n')

    def dobavitvschet6(self,instance):
        text = self.lblnazvanie.text
        f = open('menu.txt','r')
        a = f.read()
        s = a.split()
        n=0
        for word in s:
            n = n+1

        for i in range(0,n):
            if s[i] == text:
                cena = s[i+1]

        f.close()
        self.gl11.add_widget(Label(text=text))
        self.gl11.add_widget(Label(text=cena+' руб'))
        self.itog6 = int(self.itog6) + int(cena)
        self.txtbx6.text = str(self.itog6)+' руб'
        f = open('chet6.txt', 'a+')
        f.write(text +' '+ cena + '\n')

    def dobavitvschet7(self,instance):
        text = self.lblnazvanie.text
        f = open('menu.txt','r')
        a = f.read()
        s = a.split()
        n=0
        for word in s:
            n = n+1

        for i in range(0,n):
            if s[i] == text:
                cena = s[i+1]

        f.close()
        self.gl12.add_widget(Label(text=text))
        self.gl12.add_widget(Label(text=cena+' руб'))
        self.itog7 = int(self.itog7) + int(cena)
        self.txtbx7.text = str(self.itog7)+' руб'
        f = open('chet7.txt', 'a+')
        f.write(text +' '+ cena + '\n')

    def dobavitvschet8(self,instance):
        text = self.lblnazvanie.text
        f = open('menu.txt','r')
        a = f.read()
        s = a.split()
        n=0
        for word in s:
            n = n+1

        for i in range(0,n):
            if s[i] == text:
                cena = s[i+1]

        f.close()
        self.gl13.add_widget(Label(text=text))
        self.gl13.add_widget(Label(text=cena+' руб'))
        self.itog8 = int(self.itog8) + int(cena)
        self.txtbx8.text = str(self.itog8)+' руб'
        f = open('chet8.txt', 'a+')
        f.write(text +' '+ cena + '\n')

    def dobavitvschet9(self,instance):
        text = self.lblnazvanie.text
        f = open('menu.txt','r')
        a = f.read()
        s = a.split()
        n=0
        for word in s:
            n = n+1

        for i in range(0,n):
            if s[i] == text:
                cena = s[i+1]

        f.close()
        self.gl14.add_widget(Label(text=text))
        self.gl14.add_widget(Label(text=cena+' руб'))
        self.itog9 = int(self.itog9) + int(cena)
        self.txtbx9.text = str(self.itog9)+' руб'
        f = open('chet9.txt', 'a+')
        f.write(text +' '+ cena + '\n')

    def dobavitvschet10(self,instance):
        text = self.lblnazvanie.text
        f = open('menu.txt','r')
        a = f.read()
        s = a.split()
        n=0
        for word in s:
            n = n+1

        for i in range(0,n):
            if s[i] == text:
                cena = s[i+1]

        f.close()
        self.gl15.add_widget(Label(text=text))
        self.gl15.add_widget(Label(text=cena+' руб'))
        self.itog10 = int(self.itog10) + int(cena)
        self.txtbx10.text = str(self.itog10)+' руб'
        f = open('chet10.txt', 'a+')
        f.write(text +' '+ cena + '\n')

    def dobavitvschet11(self,instance):
        text = self.lblnazvanie.text
        f = open('menu.txt','r')
        a = f.read()
        s = a.split()
        n=0
        for word in s:
            n = n+1

        for i in range(0,n):
            if s[i] == text:
                cena = s[i+1]

        f.close()
        self.gl16.add_widget(Label(text=text))
        self.gl16.add_widget(Label(text=cena+' руб'))
        self.itog11 = int(self.itog11) + int(cena)
        self.txtbx11.text = str(self.itog11)+' руб'
        f = open('chet11.txt', 'a+')
        f.write(text +' '+ cena + '\n')


    def dobavitvschet12(self,instance):
        text = self.lblnazvanie.text
        f = open('menu.txt','r')
        a = f.read()
        s = a.split()
        n=0
        for word in s:
            n = n+1

        for i in range(0,n):
            if s[i] == text:
                cena = s[i+1]

        f.close()
        self.gl17.add_widget(Label(text=text))
        self.gl17.add_widget(Label(text=cena+' руб'))
        self.itog12 = int(self.itog12) + int(cena)
        self.txtbx12.text = str(self.itog12)+' руб'
        f = open('chet12.txt', 'a+')
        f.write(text +' '+ cena + '\n')


    def dobavitvschet13(self,instance):
        text = self.lblnazvanie.text
        f = open('menu.txt','r')
        a = f.read()
        s = a.split()
        n=0
        for word in s:
            n = n+1

        for i in range(0,n):
            if s[i] == text:
                cena = s[i+1]

        f.close()
        self.gl18.add_widget(Label(text=text))
        self.gl18.add_widget(Label(text=cena+' руб'))
        self.itog13 = int(self.itog13) + int(cena)
        self.txtbx13.text = str(self.itog13)+' руб'
        f = open('chet13.txt', 'a+')
        f.write(text +' '+ cena + '\n')


    def dobavitvschet14(self,instance):
        text = self.lblnazvanie.text
        f = open('menu.txt','r')
        a = f.read()
        s = a.split()
        n=0
        for word in s:
            n = n+1

        for i in range(0,n):
            if s[i] == text:
                cena = s[i+1]

        f.close()
        self.gl19.add_widget(Label(text=text))
        self.gl19.add_widget(Label(text=cena+' руб'))
        self.itog14 = int(self.itog14) + int(cena)
        self.txtbx14.text = str(self.itog14)+' руб'
        f = open('chet14.txt', 'a+')
        f.write(text +' '+ cena + '\n')


    def dobavitvschet15(self,instance):
        text = self.lblnazvanie.text
        f = open('menu.txt','r')
        a = f.read()
        s = a.split()
        n=0
        for word in s:
            n = n+1

        for i in range(0,n):
            if s[i] == text:
                cena = s[i+1]

        f.close()
        self.gl20.add_widget(Label(text=text))
        self.gl20.add_widget(Label(text=cena+' руб'))
        self.itog15 = int(self.itog15) + int(cena)
        self.txtbx15.text = str(self.itog15)+' руб'
        f = open('chet15.txt', 'a+')
        f.write(text +' '+ cena + '\n')


    def dobavitvschet16(self,instance):
        text = self.lblnazvanie.text
        f = open('menu.txt','r')
        a = f.read()
        s = a.split()
        n=0
        for word in s:
            n = n+1

        for i in range(0,n):
            if s[i] == text:
                cena = s[i+1]

        f.close()
        self.gl21.add_widget(Label(text=text))
        self.gl21.add_widget(Label(text=cena+' руб'))
        self.itog16 = int(self.itog16) + int(cena)
        self.txtbx16.text = str(self.itog16)+' руб'
        f = open('chet16.txt', 'a+')
        f.write(text +' '+ cena + '\n')


    def popup1(self,instance):
        self.popup.open()

    def zaezdTIA1_1_1(self, instance):
        text = self.zaezdTI1_1_1.text
        f = open('zaezdTI1_1_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA1_1_2(self, instance):
        text = self.zaezdTI1_1_2.text
        f = open('zaezdTI1_1_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA1_1_3(self, instance):
        text = self.zaezdTI1_1_3.text
        f = open('zaezdTI1_1_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA1_2_1(self, instance):
        text = self.zaezdTI1_2_1.text
        f = open('zaezdTI1_2_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA1_2_2(self, instance):
        text = self.zaezdTI1_2_2.text
        f = open('zaezdTI1_2_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA1_2_3(self, instance):
        text = self.zaezdTI1_2_3.text
        f = open('zaezdTI1_2_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA1_3_1(self, instance):
        text = self.zaezdTI1_3_1.text
        f = open('zaezdTI1_3_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA1_3_2(self, instance):
        text = self.zaezdTI1_3_2.text
        f = open('zaezdTI1_3_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA1_3_3(self, instance):
        text = self.zaezdTI1_3_3.text
        f = open('zaezdTI1_3_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA2_1_1(self, instance):
        text = self.zaezdTI2_1_1.text
        f = open('zaezdTI2_1_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA2_1_2(self, instance):
        text = self.zaezdTI2_1_2.text
        f = open('zaezdTI2_1_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA2_1_3(self, instance):
        text = self.zaezdTI2_1_3.text
        f = open('zaezdTI2_1_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA2_2_1(self, instance):
        text = self.zaezdTI2_2_1.text
        f = open('zaezdTI2_2_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA2_2_2(self, instance):
        text = self.zaezdTI2_2_2.text
        f = open('zaezdTI2_2_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA2_2_3(self, instance):
        text = self.zaezdTI2_2_3.text
        f = open('zaezdTI2_2_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA2_3_1(self, instance):
        text = self.zaezdTI2_3_1.text
        f = open('zaezdTI2_3_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA2_3_2(self, instance):
        text = self.zaezdTI2_3_2.text
        f = open('zaezdTI2_3_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA2_3_3(self, instance):
        text = self.zaezdTI2_3_3.text
        f = open('zaezdTI2_3_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA3_1_1(self, instance):
        text = self.zaezdTI3_1_1.text
        f = open('zaezdTI3_1_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA3_1_2(self, instance):
        text = self.zaezdTI3_1_2.text
        f = open('zaezdTI3_1_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA3_1_3(self, instance):
        text = self.zaezdTI3_1_3.text
        f = open('zaezdTI3_1_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA3_2_1(self, instance):
        text = self.zaezdTI3_2_1.text
        f = open('zaezdTI3_2_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA3_2_2(self, instance):
        text = self.zaezdTI3_2_2.text
        f = open('zaezdTI3_2_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA3_2_3(self, instance):
        text = self.zaezdTI3_2_3.text
        f = open('zaezdTI3_2_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA3_3_1(self, instance):
        text = self.zaezdTI3_3_1.text
        f = open('zaezdTI3_3_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA3_3_2(self, instance):
        text = self.zaezdTI3_3_2.text
        f = open('zaezdTI3_3_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA3_3_3(self, instance):
        text = self.zaezdTI3_3_3.text
        f = open('zaezdTI3_3_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA4_1_1(self, instance):
        text = self.zaezdTI4_1_1.text
        f = open('zaezdTI4_1_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA4_1_2(self, instance):
        text = self.zaezdTI4_1_2.text
        f = open('zaezdTI4_1_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA4_1_3(self, instance):
        text = self.zaezdTI4_1_3.text
        f = open('zaezdTI4_1_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA4_2_1(self, instance):
        text = self.zaezdTI4_2_1.text
        f = open('zaezdTI4_2_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA4_2_2(self, instance):
        text = self.zaezdTI4_2_2.text
        f = open('zaezdTI4_2_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA4_2_3(self, instance):
        text = self.zaezdTI4_2_3.text
        f = open('zaezdTI4_2_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA4_3_1(self, instance):
        text = self.zaezdTI4_3_1.text
        f = open('zaezdTI4_3_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA4_3_2(self, instance):
        text = self.zaezdTI4_3_2.text
        f = open('zaezdTI4_3_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA4_3_3(self, instance):
        text = self.zaezdTI4_3_3.text
        f = open('zaezdTI4_3_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA5_1_1(self, instance):
        text = self.zaezdTI5_1_1.text
        f = open('zaezdTI5_1_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA5_1_2(self, instance):
        text = self.zaezdTI5_1_2.text
        f = open('zaezdTI5_1_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA5_1_3(self, instance):
        text = self.zaezdTI5_1_3.text
        f = open('zaezdTI5_1_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA5_2_1(self, instance):
        text = self.zaezdTI5_2_1.text
        f = open('zaezdTI5_2_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA5_2_2(self, instance):
        text = self.zaezdTI5_2_2.text
        f = open('zaezdTI5_2_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA5_2_3(self, instance):
        text = self.zaezdTI5_2_3.text
        f = open('zaezdTI5_2_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA5_3_1(self, instance):
        text = self.zaezdTI5_3_1.text
        f = open('zaezdTI5_3_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA5_3_2(self, instance):
        text = self.zaezdTI5_3_2.text
        f = open('zaezdTI5_3_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA5_3_3(self, instance):
        text = self.zaezdTI5_3_3.text
        f = open('zaezdTI5_3_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA6_1_1(self, instance):
        text = self.zaezdTI6_1_1.text
        f = open('zaezdTI6_1_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA6_1_2(self, instance):
        text = self.zaezdTI6_1_2.text
        f = open('zaezdTI6_1_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA6_1_3(self, instance):
        text = self.zaezdTI6_1_3.text
        f = open('zaezdTI6_1_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA6_2_1(self, instance):
        text = self.zaezdTI6_2_1.text
        f = open('zaezdTI6_2_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA6_2_2(self, instance):
        text = self.zaezdTI6_2_2.text
        f = open('zaezdTI6_2_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA6_2_3(self, instance):
        text = self.zaezdTI6_2_3.text
        f = open('zaezdTI6_2_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA6_3_1(self, instance):
        text = self.zaezdTI6_3_1.text
        f = open('zaezdTI6_3_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA6_3_2(self, instance):
        text = self.zaezdTI6_3_2.text
        f = open('zaezdTI6_3_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA6_3_3(self, instance):
        text = self.zaezdTI6_3_3.text
        f = open('zaezdTI6_3_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA7_1_1(self, instance):
        text = self.zaezdTI7_1_1.text
        f = open('zaezdTI7_1_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA7_1_2(self, instance):
        text = self.zaezdTI7_1_2.text
        f = open('zaezdTI7_1_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA7_1_3(self, instance):
        text = self.zaezdTI7_1_3.text
        f = open('zaezdTI7_1_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA7_2_1(self, instance):
        text = self.zaezdTI7_2_1.text
        f = open('zaezdTI7_2_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA7_2_2(self, instance):
        text = self.zaezdTI7_2_2.text
        f = open('zaezdTI7_2_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA7_2_3(self, instance):
        text = self.zaezdTI7_2_3.text
        f = open('zaezdTI7_2_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA7_3_1(self, instance):
        text = self.zaezdTI7_3_1.text
        f = open('zaezdTI7_3_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA7_3_2(self, instance):
        text = self.zaezdTI7_3_2.text
        f = open('zaezdTI7_3_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA7_3_3(self, instance):
        text = self.zaezdTI7_3_3.text
        f = open('zaezdTI7_3_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA8_1_1(self, instance):
        text = self.zaezdTI8_1_1.text
        f = open('zaezdTI8_1_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA8_1_2(self, instance):
        text = self.zaezdTI8_1_2.text
        f = open('zaezdTI8_1_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA8_1_3(self, instance):
        text = self.zaezdTI8_1_3.text
        f = open('zaezdTI8_1_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA8_2_1(self, instance):
        text = self.zaezdTI8_2_1.text
        f = open('zaezdTI8_2_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA8_2_2(self, instance):
        text = self.zaezdTI8_2_2.text
        f = open('zaezdTI8_2_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA8_2_3(self, instance):
        text = self.zaezdTI8_2_3.text
        f = open('zaezdTI8_2_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA8_3_1(self, instance):
        text = self.zaezdTI8_3_1.text
        f = open('zaezdTI8_3_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA8_3_2(self, instance):
        text = self.zaezdTI8_3_2.text
        f = open('zaezdTI8_3_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA8_3_3(self, instance):
        text = self.zaezdTI8_3_3.text
        f = open('zaezdTI8_3_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA9_1_1(self, instance):
        text = self.zaezdTI9_1_1.text
        f = open('zaezdTI9_1_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA9_1_2(self, instance):
        text = self.zaezdTI9_1_2.text
        f = open('zaezdTI9_1_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA9_1_3(self, instance):
        text = self.zaezdTI9_1_3.text
        f = open('zaezdTI9_1_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA9_2_1(self, instance):
        text = self.zaezdTI9_2_1.text
        f = open('zaezdTI9_2_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA9_2_2(self, instance):
        text = self.zaezdTI9_2_2.text
        f = open('zaezdTI9_2_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA9_2_3(self, instance):
        text = self.zaezdTI9_2_3.text
        f = open('zaezdTI9_2_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA9_3_1(self, instance):
        text = self.zaezdTI9_3_1.text
        f = open('zaezdTI9_3_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA9_3_2(self, instance):
        text = self.zaezdTI9_3_2.text
        f = open('zaezdTI9_3_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA9_3_3(self, instance):
        text = self.zaezdTI9_3_3.text
        f = open('zaezdTI9_3_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA10_1_1(self, instance):
        text = self.zaezdTI10_1_1.text
        f = open('zaezdTI10_1_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA10_1_2(self, instance):
        text = self.zaezdTI10_1_2.text
        f = open('zaezdTI10_1_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA10_1_3(self, instance):
        text = self.zaezdTI10_1_3.text
        f = open('zaezdTI10_1_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA10_2_1(self, instance):
        text = self.zaezdTI10_2_1.text
        f = open('zaezdTI10_2_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA10_2_2(self, instance):
        text = self.zaezdTI10_2_2.text
        f = open('zaezdTI10_2_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA10_2_3(self, instance):
        text = self.zaezdTI10_2_3.text
        f = open('zaezdTI10_2_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA10_3_1(self, instance):
        text = self.zaezdTI10_3_1.text
        f = open('zaezdTI10_3_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA10_3_2(self, instance):
        text = self.zaezdTI10_3_2.text
        f = open('zaezdTI10_3_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA10_3_3(self, instance):
        text = self.zaezdTI10_3_3.text
        f = open('zaezdTI10_3_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA11_1_1(self, instance):
        text = self.zaezdTI11_1_1.text
        f = open('zaezdTI11_1_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA11_1_2(self, instance):
        text = self.zaezdTI11_1_2.text
        f = open('zaezdTI11_1_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA11_1_3(self, instance):
        text = self.zaezdTI11_1_3.text
        f = open('zaezdTI11_1_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA11_2_1(self, instance):
        text = self.zaezdTI11_2_1.text
        f = open('zaezdTI11_2_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA11_2_2(self, instance):
        text = self.zaezdTI11_2_2.text
        f = open('zaezdTI11_2_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA11_2_3(self, instance):
        text = self.zaezdTI11_2_3.text
        f = open('zaezdTI11_2_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA11_3_1(self, instance):
        text = self.zaezdTI11_3_1.text
        f = open('zaezdTI11_3_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA11_3_2(self, instance):
        text = self.zaezdTI11_3_2.text
        f = open('zaezdTI11_3_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA11_3_3(self, instance):
        text = self.zaezdTI11_3_3.text
        f = open('zaezdTI11_3_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA12_1_1(self, instance):
        text = self.zaezdTI12_1_1.text
        f = open('zaezdTI12_1_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA12_1_2(self, instance):
        text = self.zaezdTI12_1_2.text
        f = open('zaezdTI12_1_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA12_1_3(self, instance):
        text = self.zaezdTI12_1_3.text
        f = open('zaezdTI12_1_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA12_2_1(self, instance):
        text = self.zaezdTI12_2_1.text
        f = open('zaezdTI12_2_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA12_2_2(self, instance):
        text = self.zaezdTI12_2_2.text
        f = open('zaezdTI12_2_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA12_2_3(self, instance):
        text = self.zaezdTI12_2_3.text
        f = open('zaezdTI12_2_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA12_3_1(self, instance):
        text = self.zaezdTI12_3_1.text
        f = open('zaezdTI12_3_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA12_3_2(self, instance):
        text = self.zaezdTI12_3_2.text
        f = open('zaezdTI12_3_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA12_3_3(self, instance):
        text = self.zaezdTI12_3_3.text
        f = open('zaezdTI12_3_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA13_1_1(self, instance):
        text = self.zaezdTI13_1_1.text
        f = open('zaezdTI13_1_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA13_1_2(self, instance):
        text = self.zaezdTI13_1_2.text
        f = open('zaezdTI13_1_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA13_1_3(self, instance):
        text = self.zaezdTI13_1_3.text
        f = open('zaezdTI13_1_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA13_2_1(self, instance):
        text = self.zaezdTI13_2_1.text
        f = open('zaezdTI13_2_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA13_2_2(self, instance):
        text = self.zaezdTI13_2_2.text
        f = open('zaezdTI13_2_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA13_2_3(self, instance):
        text = self.zaezdTI13_2_3.text
        f = open('zaezdTI13_2_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA13_3_1(self, instance):
        text = self.zaezdTI13_3_1.text
        f = open('zaezdTI13_3_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA13_3_2(self, instance):
        text = self.zaezdTI13_3_2.text
        f = open('zaezdTI13_3_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA13_3_3(self, instance):
        text = self.zaezdTI13_3_3.text
        f = open('zaezdTI13_3_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA14_1_1(self, instance):
        text = self.zaezdTI14_1_1.text
        f = open('zaezdTI14_1_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA14_1_2(self, instance):
        text = self.zaezdTI14_1_2.text
        f = open('zaezdTI14_1_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA14_1_3(self, instance):
        text = self.zaezdTI14_1_3.text
        f = open('zaezdTI14_1_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA14_2_1(self, instance):
        text = self.zaezdTI14_2_1.text
        f = open('zaezdTI14_2_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA14_2_2(self, instance):
        text = self.zaezdTI14_2_2.text
        f = open('zaezdTI14_2_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA14_2_3(self, instance):
        text = self.zaezdTI14_2_3.text
        f = open('zaezdTI14_2_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA14_3_1(self, instance):
        text = self.zaezdTI14_3_1.text
        f = open('zaezdTI14_3_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA14_3_2(self, instance):
        text = self.zaezdTI14_3_2.text
        f = open('zaezdTI14_3_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA14_3_3(self, instance):
        text = self.zaezdTI14_3_3.text
        f = open('zaezdTI14_3_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA15_1_1(self, instance):
        text = self.zaezdTI15_1_1.text
        f = open('zaezdTI15_1_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA15_1_2(self, instance):
        text = self.zaezdTI15_1_2.text
        f = open('zaezdTI15_1_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA15_1_3(self, instance):
        text = self.zaezdTI15_1_3.text
        f = open('zaezdTI15_1_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA15_2_1(self, instance):
        text = self.zaezdTI15_2_1.text
        f = open('zaezdTI15_2_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA15_2_2(self, instance):
        text = self.zaezdTI15_2_2.text
        f = open('zaezdTI15_2_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA15_2_3(self, instance):
        text = self.zaezdTI15_2_3.text
        f = open('zaezdTI15_2_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA15_3_1(self, instance):
        text = self.zaezdTI15_3_1.text
        f = open('zaezdTI15_3_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA15_3_2(self, instance):
        text = self.zaezdTI15_3_2.text
        f = open('zaezdTI15_3_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA15_3_3(self, instance):
        text = self.zaezdTI15_3_3.text
        f = open('zaezdTI15_3_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA16_1_1(self, instance):
        text = self.zaezdTI16_1_1.text
        f = open('zaezdTI16_1_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA16_1_2(self, instance):
        text = self.zaezdTI16_1_2.text
        f = open('zaezdTI16_1_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA16_1_3(self, instance):
        text = self.zaezdTI16_1_3.text
        f = open('zaezdTI16_1_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA16_2_1(self, instance):
        text = self.zaezdTI16_2_1.text
        f = open('zaezdTI16_2_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA16_2_2(self, instance):
        text = self.zaezdTI16_2_2.text
        f = open('zaezdTI16_2_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA16_2_3(self, instance):
        text = self.zaezdTI16_2_3.text
        f = open('zaezdTI16_2_3.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA16_3_1(self, instance):
        text = self.zaezdTI16_3_1.text
        f = open('zaezdTI16_3_1.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA16_3_2(self, instance):
        text = self.zaezdTI16_3_2.text
        f = open('zaezdTI16_3_2.txt', 'w+')
        f.write(text)
        f.close()

    def zaezdTIA16_3_3(self, instance):
        text = self.zaezdTI16_3_3.text
        f = open('zaezdTI16_3_3.txt', 'w+')
        f.write(text)
        f.close()

    def btn1(self, instance):
        global Bool

        def on_checkbox_active_1(checkbox, value):
            f = open('cb1_1.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_2(checkbox, value):
            f = open('cb1_2.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_3(checkbox, value):
            f = open('cb1_3.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_4(checkbox, value):
            f = open('cb1_4.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_5(checkbox, value):
            f = open('cb1_5.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_6(checkbox, value):
            f = open('cb1_6.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()


        global Bool1
        if not Bool1:
            self.tb1 = TabbedPanel()
            self.tb1.do_default_tab = False

        #Заезды

            th1 = TabbedPanelHeader(text = 'Заезды')
            blo1 = BoxLayout(orientation='vertical')
            gl1 = GridLayout(cols = 1, size_hint = (1,1), row_force_default=True, row_default_height=35)
            bl0 = BoxLayout()
            bl0.add_widget(Label(text='С'))
            self.zaezdTI1_1_1 = TextInput(text='', multiline=False)
            self.zaezdTI1_1_1.bind(on_text_validate=self.zaezdTIA1_1_1)
            f = open('zaezdTI1_1_1.txt', 'a+')
            f.close()
            f = open('zaezdTI1_1_1.txt', 'r')
            a = f.read()
            self.zaezdTI1_1_1.text = a
            f.close()
            bl0.add_widget(self.zaezdTI1_1_1)
            bl0.add_widget(Label(text='по'))
            self.zaezdTI1_1_2 = TextInput(text='', multiline=False)
            self.zaezdTI1_1_2.bind(on_text_validate=self.zaezdTIA1_1_2)
            f = open('zaezdTI1_1_2.txt', 'a+')
            f.close()
            f = open('zaezdTI1_1_2.txt', 'r')
            a = f.read()
            self.zaezdTI1_1_2.text = a
            f.close()
            bl0.add_widget(self.zaezdTI1_1_2)
            bl0.add_widget(Label(text='ФИО:'))
            self.zaezdTI1_1_3 = TextInput(text='', multiline=False)
            self.zaezdTI1_1_3.bind(on_text_validate=self.zaezdTIA1_1_3)
            f = open('zaezdTI1_1_3.txt', 'a+')
            f.close()
            f = open('zaezdTI1_1_3.txt', 'r')
            a = f.read()
            self.zaezdTI1_1_3.text = a
            f.close()
            bl0.add_widget(self.zaezdTI1_1_3)
            gl1.add_widget(bl0)

            bl1 = BoxLayout()
            bl1.add_widget(Label(text='С'))
            self.zaezdTI1_2_1 = TextInput(text='', multiline=False)
            self.zaezdTI1_2_1.bind(on_text_validate=self.zaezdTIA1_2_1)
            f = open('zaezdTI1_2_1.txt', 'a+')
            f.close()
            f = open('zaezdTI1_2_1.txt', 'r')
            a = f.read()
            self.zaezdTI1_2_1.text = a
            f.close()
            bl1.add_widget(self.zaezdTI1_2_1)
            bl1.add_widget(Label(text='по'))
            self.zaezdTI1_2_2 = TextInput(text='', multiline=False)
            self.zaezdTI1_2_2.bind(on_text_validate=self.zaezdTIA1_2_2)
            f = open('zaezdTI1_2_2.txt', 'a+')
            f.close()
            f = open('zaezdTI1_2_2.txt', 'r')
            a = f.read()
            self.zaezdTI1_2_2.text = a
            f.close()
            bl1.add_widget(self.zaezdTI1_2_2)
            bl1.add_widget(Label(text='ФИО:'))
            self.zaezdTI1_2_3 = TextInput(text='', multiline=False)
            self.zaezdTI1_2_3.bind(on_text_validate=self.zaezdTIA1_2_3)
            f = open('zaezdTI1_2_3.txt', 'a+')
            f.close()
            f = open('zaezdTI1_2_3.txt', 'r')
            a = f.read()
            self.zaezdTI1_2_3.text = a
            f.close()
            bl1.add_widget(self.zaezdTI1_2_3)
            gl1.add_widget(bl1)

            bl2 = BoxLayout()
            bl2.add_widget(Label(text='С'))
            self.zaezdTI1_3_1 = TextInput(text='', multiline=False)
            self.zaezdTI1_3_1.bind(on_text_validate=self.zaezdTIA1_3_1)
            f = open('zaezdTI1_3_1.txt', 'a+')
            f.close()
            f = open('zaezdTI1_3_1.txt', 'r')
            a = f.read()
            self.zaezdTI1_3_1.text = a
            f.close()
            bl2.add_widget(self.zaezdTI1_3_1)
            bl2.add_widget(Label(text='по'))
            self.zaezdTI1_3_2 = TextInput(text='', multiline=False)
            self.zaezdTI1_3_2.bind(on_text_validate=self.zaezdTIA1_3_2)
            f = open('zaezdTI1_3_2.txt', 'a+')
            f.close()
            f = open('zaezdTI1_3_2.txt', 'r')
            a = f.read()
            self.zaezdTI1_3_2.text = a
            f.close()
            bl2.add_widget(self.zaezdTI1_3_2)
            bl2.add_widget(Label(text='ФИО:'))
            self.zaezdTI1_3_3 = TextInput(text='', multiline=False)
            self.zaezdTI1_3_3.bind(on_text_validate=self.zaezdTIA1_3_3)
            f = open('zaezdTI1_3_3.txt', 'a+')
            f.close()
            f = open('zaezdTI1_3_3.txt', 'r')
            a = f.read()
            self.zaezdTI1_3_3.text = a
            f.close()
            bl2.add_widget(self.zaezdTI1_3_3)
            gl1.add_widget(bl2)

            th1.content = gl1

            #Сведения
            th2 = TabbedPanelHeader(text = 'Сведения')
            blo2=BoxLayout(orientation = 'vertical')
            gl2 = GridLayout(cols=4, size_hint=(1, .2), row_force_default=True, row_default_height=35)

            gl2.add_widget(Label(text = 'Паспорт:'))
            f = open("pas1.txt", 'a+')
            f.close()
            f = open("pas1.txt", 'r')
            a = f.read()
            self.ti1_1 = TextInput(multiline=False)
            self.ti1_1.text = a
            self.ti1_1.bind(on_text_validate = self.ti1_1_action)
            f.close()
            gl2.add_widget(self.ti1_1)
            gl2.add_widget(Label(text='Предоплата букинг'))
            cb1 = CheckBox()
            f = open('cb1_1.txt', 'a+')
            f.close()
            f = open('cb1_1.txt','r')
            a = f.read()
            cb1.bind(active=on_checkbox_active_1)
            cb1.bind(disabled=on_checkbox_active_1)
            if a == 'true':
                cb1.trigger_action()
            f.close()
            gl2.add_widget(cb1)
            gl2.add_widget(Label(text='Предоплата:'))
            f = open('predopl1.txt', 'a+')
            f.close()
            f = open('predopl1.txt', 'r')
            a = f.read()
            self.ti1_2 = TextInput(multiline=False)
            self.ti1_2.text = a
            self.ti1_2.bind(on_text_validate=self.ti1_2_action)
            gl2.add_widget(self.ti1_2)
            f.close()
            gl2.add_widget(Label(text='Собака'))
            f = open('cb1_2.txt', 'a+')
            f.close()
            f = open('cb1_2.txt', 'r')
            a = f.read()
            cb2 = CheckBox()
            cb2.bind(active=on_checkbox_active_2)
            cb2.bind(disabled=on_checkbox_active_2)
            if a == 'true':
                cb2.trigger_action()
            f.close()
            gl2.add_widget(cb2)
            gl2.add_widget(Label(text='Ранний заезд'))
            f = open('cb1_3.txt', 'a+')
            f.close()
            f = open('cb1_3.txt', 'r')
            a = f.read()
            cb3 = CheckBox()
            cb3.bind(active=on_checkbox_active_3)
            cb3.bind(disabled=on_checkbox_active_3)
            if a == 'true':
                cb3.trigger_action()
            f.close()
            gl2.add_widget(cb3)
            gl2.add_widget(Label(text='Поздний выезд'))
            f = open('cb1_4.txt', 'a+')
            f.close()
            f = open('cb1_4.txt', 'r')
            a = f.read()
            cb4 = CheckBox()
            cb4.bind(active=on_checkbox_active_4)
            cb4.bind(disabled=on_checkbox_active_4)
            if a == 'true':
                cb4.trigger_action()
            f.close()
            gl2.add_widget(cb4)
            gl2.add_widget(Label(text='Доп. кровать'))
            f = open('cb1_5.txt', 'a+')
            f.close()
            f = open('cb1_5.txt', 'r')
            a = f.read()
            cb5 = CheckBox()
            cb5.bind(active=on_checkbox_active_5)
            cb5.bind(disabled=on_checkbox_active_5)
            if a == 'true':
                cb5.trigger_action()
            f.close()
            gl2.add_widget(cb5)
            gl2.add_widget(Label(text='Выходные'))
            f = open('cb1_6.txt', 'a+')
            f.close()
            f = open('cb1_6.txt', 'r')
            a = f.read()
            cb6 = CheckBox()
            cb6.bind(active=on_checkbox_active_6)
            cb6.bind(disabled=on_checkbox_active_6)
            if a == 'true':
                cb6.trigger_action()
            f.close()
            gl2.add_widget(cb6)

            #dropdown
            self.dd1 = DropDown()
            self.lblnazvanie = Label(text ='')
            mainbutton = Button(text='Меню')
            mainbutton.bind(on_release=self.dd1.open)
            self.dd1.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
            self.dd1.bind(on_select=lambda instance, x: setattr(self.lblnazvanie,'text', x))
            f = open('menu.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n=n+1
            for i in range(0,n,2):
                btn = Button(text=s[i], size_hint_y=None, height=35)
                btn.bind(on_release=lambda btn: self.dd1.select(btn.text))
                self.dd1.add_widget(btn)
            f.close()

            blo2.add_widget(gl2)
            gl3 = GridLayout(cols=2, size_hint=(1, .5), row_force_default=True, row_default_height=35)
            gl3.add_widget(mainbutton)
            btn8 = Button(text='Добавить в счет',on_press = self.dobavitvschet1)

            gl3.add_widget(btn8)
            blo2.add_widget(gl3)
            th2.content = blo2
            th3 = TabbedPanelHeader(text = 'Счет')


            #счет

            bxl1 = BoxLayout(orientation = 'vertical')
            scrl1 = ScrollView(size_hint=(1, .95))
            self.gl6 = GridLayout(cols=2, size_hint = (1,1), row_force_default=True,size_hint_y=None, row_default_height=40, spacing = 1)

            self.gl6.bind(minimum_height=self.gl6.setter('height'))
            scrl1.add_widget(self.gl6)
            bxl1.add_widget(scrl1)
            bxl2 = BoxLayout(orientation = 'horizontal', size_hint=(1, .05))
            bxl2.add_widget(Label(text = 'Итог :'))
            self.txtbx = TextInput(text=str(self.itog1)+' руб', multiline = False, halign = 'center')
            bxl2.add_widget(self.txtbx)
            btn = Button(text='Обновить', on_press=self.obnovit1)
            bxl2.add_widget(btn)
            bxl1.add_widget(bxl2)
            th3.content = bxl1
            f = open('chet1.txt', 'a+')
            f.close()
            f = open('chet1.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n = n + 1
            for i in range(0,n,2):
                self.gl6.add_widget(Label(text=s[i]))
                self.gl6.add_widget(Label(text=s[i+1] + ' руб'))
                if self.itogbool1:
                    self.itog1 = self.itog1 + int(s[i+1])
            f.close()
            self.itogbool1 = False
            self.txtbx.text = str(self.itog1) + ' руб'

            self.tb1.add_widget(th1)
            self.tb1.add_widget(th2)
            self.tb1.add_widget(th3)
        if not Bool:
            self.general.add_widget(self.tb1)
            Bool = True
        else:
            self.general.remove_widget(self.general.children[0])
            self.general.add_widget(self.tb1)

    def btn2(self, instance):
        global Bool

        def on_checkbox_active_1(checkbox, value):
            f = open('cb2_1.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_2(checkbox, value):
            f = open('cb2_2.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_3(checkbox, value):
            f = open('cb2_3.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_4(checkbox, value):
            f = open('cb2_4.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_5(checkbox, value):
            f = open('cb2_5.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_6(checkbox, value):
            f = open('cb2_6.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()


        global Bool1
        if not Bool1:
            self.tb2 = TabbedPanel()
            self.tb2.do_default_tab = False

        #Заезды

            th1 = TabbedPanelHeader(text = 'Заезды')
            blo1 = BoxLayout(orientation='vertical')
            gl1 = GridLayout(cols = 1, size_hint = (1,1), row_force_default=True, row_default_height=35)
            bl0 = BoxLayout()
            bl0.add_widget(Label(text='С'))
            self.zaezdTI2_1_1 = TextInput(text='', multiline=False)
            self.zaezdTI2_1_1.bind(on_text_validate=self.zaezdTIA2_1_1)
            f = open('zaezdTI2_1_1.txt', 'a+')
            f.close()
            f = open('zaezdTI2_1_1.txt', 'r')
            a = f.read()
            self.zaezdTI2_1_1.text = a
            f.close()
            bl0.add_widget(self.zaezdTI2_1_1)
            bl0.add_widget(Label(text='по'))
            self.zaezdTI2_1_2 = TextInput(text='', multiline=False)
            self.zaezdTI2_1_2.bind(on_text_validate=self.zaezdTIA2_1_2)
            f = open('zaezdTI2_1_2.txt', 'a+')
            f.close()
            f = open('zaezdTI2_1_2.txt', 'r')
            a = f.read()
            self.zaezdTI2_1_2.text = a
            f.close()
            bl0.add_widget(self.zaezdTI2_1_2)
            bl0.add_widget(Label(text='ФИО:'))
            self.zaezdTI2_1_3 = TextInput(text='', multiline=False)
            self.zaezdTI2_1_3.bind(on_text_validate=self.zaezdTIA2_1_3)
            f = open('zaezdTI2_1_3.txt', 'a+')
            f.close()
            f = open('zaezdTI2_1_3.txt', 'r')
            a = f.read()
            self.zaezdTI2_1_3.text = a
            f.close()
            bl0.add_widget(self.zaezdTI2_1_3)
            gl1.add_widget(bl0)

            bl1 = BoxLayout()
            bl1.add_widget(Label(text='С'))
            self.zaezdTI2_2_1 = TextInput(text='', multiline=False)
            self.zaezdTI2_2_1.bind(on_text_validate=self.zaezdTIA2_2_1)
            f = open('zaezdTI2_2_1.txt', 'a+')
            f.close()
            f = open('zaezdTI2_2_1.txt', 'r')
            a = f.read()
            self.zaezdTI2_2_1.text = a
            f.close()
            bl1.add_widget(self.zaezdTI2_2_1)
            bl1.add_widget(Label(text='по'))
            self.zaezdTI2_2_2 = TextInput(text='', multiline=False)
            self.zaezdTI2_2_2.bind(on_text_validate=self.zaezdTIA2_2_2)
            f = open('zaezdTI2_2_2.txt', 'a+')
            f.close()
            f = open('zaezdTI2_2_2.txt', 'r')
            a = f.read()
            self.zaezdTI2_2_2.text = a
            f.close()
            bl1.add_widget(self.zaezdTI2_2_2)
            bl1.add_widget(Label(text='ФИО:'))
            self.zaezdTI2_2_3 = TextInput(text='', multiline=False)
            self.zaezdTI2_2_3.bind(on_text_validate=self.zaezdTIA2_2_3)
            f = open('zaezdTI2_2_3.txt', 'a+')
            f.close()
            f = open('zaezdTI2_2_3.txt', 'r')
            a = f.read()
            self.zaezdTI2_2_3.text = a
            f.close()
            bl1.add_widget(self.zaezdTI2_2_3)
            gl1.add_widget(bl1)

            bl2 = BoxLayout()
            bl2.add_widget(Label(text='С'))
            self.zaezdTI2_3_1 = TextInput(text='', multiline=False)
            self.zaezdTI2_3_1.bind(on_text_validate=self.zaezdTIA2_3_1)
            f = open('zaezdTI2_3_1.txt', 'a+')
            f.close()
            f = open('zaezdTI2_3_1.txt', 'r')
            a = f.read()
            self.zaezdTI2_3_1.text = a
            f.close()
            bl2.add_widget(self.zaezdTI2_3_1)
            bl2.add_widget(Label(text='по'))
            self.zaezdTI2_3_2 = TextInput(text='', multiline=False)
            self.zaezdTI2_3_2.bind(on_text_validate=self.zaezdTIA2_3_2)
            f = open('zaezdTI2_3_2.txt', 'a+')
            f.close()
            f = open('zaezdTI2_3_2.txt', 'r')
            a = f.read()
            self.zaezdTI2_3_2.text = a
            f.close()
            bl2.add_widget(self.zaezdTI2_3_2)
            bl2.add_widget(Label(text='ФИО:'))
            self.zaezdTI2_3_3 = TextInput(text='', multiline=False)
            self.zaezdTI2_3_3.bind(on_text_validate=self.zaezdTIA2_3_3)
            f = open('zaezdTI2_3_3.txt', 'a+')
            f.close()
            f = open('zaezdTI2_3_3.txt', 'r')
            a = f.read()
            self.zaezdTI2_3_3.text = a
            f.close()
            bl2.add_widget(self.zaezdTI2_3_3)
            gl1.add_widget(bl2)

            th1.content = gl1

            #Сведения
            th2 = TabbedPanelHeader(text = 'Сведения')
            blo2=BoxLayout(orientation = 'vertical')
            gl2 = GridLayout(cols=4, size_hint=(1, .2), row_force_default=True, row_default_height=35)

            gl2.add_widget(Label(text = 'Паспорт:'))
            f = open("pas2.txt", 'a+')
            f.close()
            f = open("pas2.txt", 'r')
            a = f.read()
            self.ti2_1 = TextInput(multiline=False)
            self.ti2_1.text = a
            self.ti2_1.bind(on_text_validate = self.ti2_1_action)
            f.close()
            gl2.add_widget(self.ti2_1)
            gl2.add_widget(Label(text='Предоплата букинг'))
            cb1 = CheckBox()
            f = open('cb2_1.txt', 'a+')
            f.close()
            f = open('cb2_1.txt','r')
            a = f.read()
            cb1.bind(active=on_checkbox_active_1)
            cb1.bind(disabled=on_checkbox_active_1)
            if a == 'true':
                cb1.trigger_action()
            f.close()
            gl2.add_widget(cb1)
            gl2.add_widget(Label(text='Предоплата:'))
            f = open('predopl2.txt', 'a+')
            f.close()
            f = open('predopl2.txt', 'r')
            a = f.read()
            self.ti2_2 = TextInput(multiline=False)
            self.ti2_2.text = a
            self.ti2_2.bind(on_text_validate=self.ti2_2_action)
            gl2.add_widget(self.ti2_2)
            f.close()
            gl2.add_widget(Label(text='Собака'))
            f = open('cb2_2.txt', 'a+')
            f.close()
            f = open('cb2_2.txt', 'r')
            a = f.read()
            cb2 = CheckBox()
            cb2.bind(active=on_checkbox_active_2)
            cb2.bind(disabled=on_checkbox_active_2)
            if a == 'true':
                cb2.trigger_action()
            f.close()
            gl2.add_widget(cb2)
            gl2.add_widget(Label(text='Ранний заезд'))
            f = open('cb2_3.txt', 'a+')
            f.close()
            f = open('cb2_3.txt', 'r')
            a = f.read()
            cb3 = CheckBox()
            cb3.bind(active=on_checkbox_active_3)
            cb3.bind(disabled=on_checkbox_active_3)
            if a == 'true':
                cb3.trigger_action()
            f.close()
            gl2.add_widget(cb3)
            gl2.add_widget(Label(text='Поздний выезд'))
            f = open('cb2_4.txt', 'a+')
            f.close()
            f = open('cb2_4.txt', 'r')
            a = f.read()
            cb4 = CheckBox()
            cb4.bind(active=on_checkbox_active_4)
            cb4.bind(disabled=on_checkbox_active_4)
            if a == 'true':
                cb4.trigger_action()
            f.close()
            gl2.add_widget(cb4)
            gl2.add_widget(Label(text='Доп. кровать'))
            f = open('cb2_5.txt', 'a+')
            f.close()
            f = open('cb2_5.txt', 'r')
            a = f.read()
            cb5 = CheckBox()
            cb5.bind(active=on_checkbox_active_5)
            cb5.bind(disabled=on_checkbox_active_5)
            if a == 'true':
                cb5.trigger_action()
            f.close()
            gl2.add_widget(cb5)
            gl2.add_widget(Label(text='Выходные'))
            f = open('cb2_6.txt', 'a+')
            f.close()
            f = open('cb2_6.txt', 'r')
            a = f.read()
            cb6 = CheckBox()
            cb6.bind(active=on_checkbox_active_6)
            cb6.bind(disabled=on_checkbox_active_6)
            if a == 'true':
                cb6.trigger_action()
            f.close()
            gl2.add_widget(cb6)

            #dropdown
            self.dd1 = DropDown()
            self.lblnazvanie = Label(text ='')
            mainbutton = Button(text='Меню')
            mainbutton.bind(on_release=self.dd1.open)
            self.dd1.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
            self.dd1.bind(on_select=lambda instance, x: setattr(self.lblnazvanie,'text', x))
            f = open('menu.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n=n+1
            for i in range(0,n,2):
                btn = Button(text=s[i], size_hint_y=None, height=35)
                btn.bind(on_release=lambda btn: self.dd1.select(btn.text))
                self.dd1.add_widget(btn)
            f.close()

            blo2.add_widget(gl2)
            gl3 = GridLayout(cols=2, size_hint=(1, .5), row_force_default=True, row_default_height=35)
            gl3.add_widget(mainbutton)
            btn8 = Button(text='Добавить в счет',on_press = self.dobavitvschet2)

            gl3.add_widget(btn8)
            blo2.add_widget(gl3)
            th2.content = blo2
            th3 = TabbedPanelHeader(text = 'Счет')


            #счет

            bxl1 = BoxLayout(orientation = 'vertical')
            scrl1 = ScrollView(size_hint=(1, .95))
            self.gl7 = GridLayout(cols=2, size_hint = (1,1), row_force_default=True,size_hint_y=None, row_default_height=40, spacing = 1)

            self.gl7.bind(minimum_height=self.gl7.setter('height'))
            scrl1.add_widget(self.gl7)
            bxl1.add_widget(scrl1)
            bxl2 = BoxLayout(orientation = 'horizontal', size_hint=(1, .05))
            bxl2.add_widget(Label(text = 'Итог :'))
            self.txtbx1 = TextInput(text=str(self.itog2)+' руб', multiline = False, halign = 'center')
            bxl2.add_widget(self.txtbx1)
            btn = Button(text='Обновить', on_press=self.obnovit2)
            bxl2.add_widget(btn)
            bxl1.add_widget(bxl2)
            th3.content = bxl1
            f = open('chet2.txt','a+')
            f.close()
            f = open('chet2.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n = n + 1
            for i in range(0,n,2):
                self.gl7.add_widget(Label(text=s[i]))
                self.gl7.add_widget(Label(text=s[i+1] + ' руб'))
                if self.itogbool2:
                    self.itog2 = self.itog2 + int(s[i+1])
            f.close()
            self.itogbool2 = False
            self.txtbx1.text = str(self.itog2) + ' руб'

            self.tb2.add_widget(th1)
            self.tb2.add_widget(th2)
            self.tb2.add_widget(th3)
        if not Bool:
            self.general.add_widget(self.tb2)
            Bool = True
        else:
            self.general.remove_widget(self.general.children[0])
            self.general.add_widget(self.tb2)

    def btn3(self, instance):
        global Bool

        def on_checkbox_active_1(checkbox, value):
            f = open('cb3_1.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_2(checkbox, value):
            f = open('cb3_2.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_3(checkbox, value):
            f = open('cb3_3.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_4(checkbox, value):
            f = open('cb3_4.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_5(checkbox, value):
            f = open('cb3_5.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_6(checkbox, value):
            f = open('cb3_6.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()


        global Bool1
        if not Bool1:
            self.tb3 = TabbedPanel()
            self.tb3.do_default_tab = False

        #Заезды

            th1 = TabbedPanelHeader(text = 'Заезды')
            blo1 = BoxLayout(orientation='vertical')
            gl1 = GridLayout(cols = 1, size_hint = (1,1), row_force_default=True, row_default_height=35)
            bl0 = BoxLayout()
            bl0.add_widget(Label(text='С'))
            self.zaezdTI3_1_1 = TextInput(text='', multiline=False)
            self.zaezdTI3_1_1.bind(on_text_validate=self.zaezdTIA3_1_1)
            f = open('zaezdTI3_1_1.txt', 'a+')
            f.close()
            f = open('zaezdTI3_1_1.txt', 'r')
            a = f.read()
            self.zaezdTI3_1_1.text = a
            f.close()
            bl0.add_widget(self.zaezdTI3_1_1)
            bl0.add_widget(Label(text='по'))
            self.zaezdTI3_1_2 = TextInput(text='', multiline=False)
            self.zaezdTI3_1_2.bind(on_text_validate=self.zaezdTIA3_1_2)
            f = open('zaezdTI3_1_2.txt', 'a+')
            f.close()
            f = open('zaezdTI3_1_2.txt', 'r')
            a = f.read()
            self.zaezdTI3_1_2.text = a
            f.close()
            bl0.add_widget(self.zaezdTI3_1_2)
            bl0.add_widget(Label(text='ФИО:'))
            self.zaezdTI3_1_3 = TextInput(text='', multiline=False)
            self.zaezdTI3_1_3.bind(on_text_validate=self.zaezdTIA3_1_3)
            f = open('zaezdTI3_1_3.txt', 'a+')
            f.close()
            f = open('zaezdTI3_1_3.txt', 'r')
            a = f.read()
            self.zaezdTI3_1_3.text = a
            f.close()
            bl0.add_widget(self.zaezdTI3_1_3)
            gl1.add_widget(bl0)

            bl1 = BoxLayout()
            bl1.add_widget(Label(text='С'))
            self.zaezdTI3_2_1 = TextInput(text='', multiline=False)
            self.zaezdTI3_2_1.bind(on_text_validate=self.zaezdTIA3_2_1)
            f = open('zaezdTI3_2_1.txt', 'a+')
            f.close()
            f = open('zaezdTI3_2_1.txt', 'r')
            a = f.read()
            self.zaezdTI3_2_1.text = a
            f.close()
            bl1.add_widget(self.zaezdTI3_2_1)
            bl1.add_widget(Label(text='по'))
            self.zaezdTI3_2_2 = TextInput(text='', multiline=False)
            self.zaezdTI3_2_2.bind(on_text_validate=self.zaezdTIA3_2_2)
            f = open('zaezdTI3_2_2.txt', 'a+')
            f.close()
            f = open('zaezdTI3_2_2.txt', 'r')
            a = f.read()
            self.zaezdTI3_2_2.text = a
            f.close()
            bl1.add_widget(self.zaezdTI3_2_2)
            bl1.add_widget(Label(text='ФИО:'))
            self.zaezdTI3_2_3 = TextInput(text='', multiline=False)
            self.zaezdTI3_2_3.bind(on_text_validate=self.zaezdTIA3_2_3)
            f = open('zaezdTI3_2_3.txt', 'a+')
            f.close()
            f = open('zaezdTI3_2_3.txt', 'r')
            a = f.read()
            self.zaezdTI3_2_3.text = a
            f.close()
            bl1.add_widget(self.zaezdTI3_2_3)
            gl1.add_widget(bl1)

            bl2 = BoxLayout()
            bl2.add_widget(Label(text='С'))
            self.zaezdTI3_3_1 = TextInput(text='', multiline=False)
            self.zaezdTI3_3_1.bind(on_text_validate=self.zaezdTIA3_3_1)
            f = open('zaezdTI3_3_1.txt', 'a+')
            f.close()
            f = open('zaezdTI3_3_1.txt', 'r')
            a = f.read()
            self.zaezdTI3_3_1.text = a
            f.close()
            bl2.add_widget(self.zaezdTI3_3_1)
            bl2.add_widget(Label(text='по'))
            self.zaezdTI3_3_2 = TextInput(text='', multiline=False)
            self.zaezdTI3_3_2.bind(on_text_validate=self.zaezdTIA3_3_2)
            f = open('zaezdTI3_3_2.txt', 'a+')
            f.close()
            f = open('zaezdTI3_3_2.txt', 'r')
            a = f.read()
            self.zaezdTI3_3_2.text = a
            f.close()
            bl2.add_widget(self.zaezdTI3_3_2)
            bl2.add_widget(Label(text='ФИО:'))
            self.zaezdTI3_3_3 = TextInput(text='', multiline=False)
            self.zaezdTI3_3_3.bind(on_text_validate=self.zaezdTIA3_3_3)
            f = open('zaezdTI3_3_3.txt', 'a+')
            f.close()
            f = open('zaezdTI3_3_3.txt', 'r')
            a = f.read()
            self.zaezdTI3_3_3.text = a
            f.close()
            bl2.add_widget(self.zaezdTI3_3_3)
            gl1.add_widget(bl2)

            th1.content = gl1

            #Сведения
            th2 = TabbedPanelHeader(text = 'Сведения')
            blo2=BoxLayout(orientation = 'vertical')
            gl2 = GridLayout(cols=4, size_hint=(1, .2), row_force_default=True, row_default_height=35)

            gl2.add_widget(Label(text = 'Паспорт:'))
            f = open("pas3.txt", 'a+')
            f.close()
            f = open("pas3.txt", 'r')
            a = f.read()
            self.ti3_1 = TextInput(multiline=False)
            self.ti3_1.text = a
            self.ti3_1.bind(on_text_validate = self.ti3_1_action)
            f.close()
            gl2.add_widget(self.ti3_1)
            gl2.add_widget(Label(text='Предоплата букинг'))
            cb1 = CheckBox()
            f = open('cb3_1.txt', 'a+')
            f.close()
            f = open('cb3_1.txt','r')
            a = f.read()
            cb1.bind(active=on_checkbox_active_1)
            cb1.bind(disabled=on_checkbox_active_1)
            if a == 'true':
                cb1.trigger_action()
            f.close()
            gl2.add_widget(cb1)
            gl2.add_widget(Label(text='Предоплата:'))
            f = open('predopl3.txt', 'a+')
            f.close()
            f = open('predopl3.txt', 'r')
            a = f.read()
            self.ti3_2 = TextInput(multiline=False)
            self.ti3_2.text = a
            self.ti3_2.bind(on_text_validate=self.ti3_2_action)
            gl2.add_widget(self.ti3_2)
            f.close()
            gl2.add_widget(Label(text='Собака'))
            f = open('cb3_2.txt', 'a+')
            f.close()
            f = open('cb3_2.txt', 'r')
            a = f.read()
            cb2 = CheckBox()
            cb2.bind(active=on_checkbox_active_2)
            cb2.bind(disabled=on_checkbox_active_2)
            if a == 'true':
                cb2.trigger_action()
            f.close()
            gl2.add_widget(cb2)
            gl2.add_widget(Label(text='Ранний заезд'))
            f = open('cb3_3.txt', 'a+')
            f.close()
            f = open('cb3_3.txt', 'r')
            a = f.read()
            cb3 = CheckBox()
            cb3.bind(active=on_checkbox_active_3)
            cb3.bind(disabled=on_checkbox_active_3)
            if a == 'true':
                cb3.trigger_action()
            f.close()
            gl2.add_widget(cb3)
            gl2.add_widget(Label(text='Поздний выезд'))
            f = open('cb3_4.txt', 'a+')
            f.close()
            f = open('cb3_4.txt', 'r')
            a = f.read()
            cb4 = CheckBox()
            cb4.bind(active=on_checkbox_active_4)
            cb4.bind(disabled=on_checkbox_active_4)
            if a == 'true':
                cb4.trigger_action()
            f.close()
            gl2.add_widget(cb4)
            gl2.add_widget(Label(text='Доп. кровать'))
            f = open('cb3_5.txt', 'a+')
            f.close()
            f = open('cb3_5.txt', 'r')
            a = f.read()
            cb5 = CheckBox()
            cb5.bind(active=on_checkbox_active_5)
            cb5.bind(disabled=on_checkbox_active_5)
            if a == 'true':
                cb5.trigger_action()
            f.close()
            gl2.add_widget(cb5)
            gl2.add_widget(Label(text='Выходные'))
            f = open('cb3_6.txt', 'a+')
            f.close()
            f = open('cb3_6.txt', 'r')
            a = f.read()
            cb6 = CheckBox()
            cb6.bind(active=on_checkbox_active_6)
            cb6.bind(disabled=on_checkbox_active_6)
            if a == 'true':
                cb6.trigger_action()
            f.close()
            gl2.add_widget(cb6)

            #dropdown
            self.dd1 = DropDown()
            self.lblnazvanie = Label(text ='')
            mainbutton = Button(text='Меню')
            mainbutton.bind(on_release=self.dd1.open)
            self.dd1.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
            self.dd1.bind(on_select=lambda instance, x: setattr(self.lblnazvanie,'text', x))
            f = open('menu.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n=n+1
            for i in range(0,n,2):
                btn = Button(text=s[i], size_hint_y=None, height=35)
                btn.bind(on_release=lambda btn: self.dd1.select(btn.text))
                self.dd1.add_widget(btn)
            f.close()

            blo2.add_widget(gl2)
            gl3 = GridLayout(cols=2, size_hint=(1, .5), row_force_default=True, row_default_height=35)
            gl3.add_widget(mainbutton)
            btn8 = Button(text='Добавить в счет',on_press = self.dobavitvschet3)

            gl3.add_widget(btn8)
            blo2.add_widget(gl3)
            th2.content = blo2
            th3 = TabbedPanelHeader(text = 'Счет')


            #счет

            bxl1 = BoxLayout(orientation = 'vertical')
            scrl1 = ScrollView(size_hint=(1, .95))
            self.gl8 = GridLayout(cols=2, size_hint = (1,1), row_force_default=True,size_hint_y=None, row_default_height=40, spacing = 1)

            self.gl8.bind(minimum_height=self.gl8.setter('height'))
            scrl1.add_widget(self.gl8)
            bxl1.add_widget(scrl1)
            bxl2 = BoxLayout(orientation = 'horizontal', size_hint=(1, .05))
            bxl2.add_widget(Label(text = 'Итог :'))
            self.txtbx3 = TextInput(text=str(self.itog3)+' руб', multiline = False, halign = 'center')
            bxl2.add_widget(self.txtbx3)
            btn = Button(text = 'Обновить', on_press = self.obnovit3)
            bxl2.add_widget(btn)
            bxl1.add_widget(bxl2)
            th3.content = bxl1
            f = open('chet3.txt','a+')
            f.close()
            f = open('chet3.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n = n + 1
            for i in range(0,n,2):
                self.gl8.add_widget(Label(text=s[i]))
                self.gl8.add_widget(Label(text=s[i+1] + ' руб'))
                if self.itogbool3:
                    self.itog3 = self.itog3 + int(s[i+1])
            f.close()
            self.itogbool3 = False
            self.txtbx3.text = str(self.itog3) + ' руб'

            self.tb3.add_widget(th1)
            self.tb3.add_widget(th2)
            self.tb3.add_widget(th3)
        if not Bool:
            self.general.add_widget(self.tb3)
            Bool = True
        else:
            self.general.remove_widget(self.general.children[0])
            self.general.add_widget(self.tb3)


    def btn4(self, instance):
        global Bool

        def on_checkbox_active_1(checkbox, value):
            f = open('cb4_1.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_2(checkbox, value):
            f = open('cb4_2.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_3(checkbox, value):
            f = open('cb4_3.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_4(checkbox, value):
            f = open('cb4_4.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_5(checkbox, value):
            f = open('cb4_5.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_6(checkbox, value):
            f = open('cb4_6.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()


        global Bool1
        if not Bool1:
            self.tb4 = TabbedPanel()
            self.tb4.do_default_tab = False

        #Заезды

            th1 = TabbedPanelHeader(text = 'Заезды')
            blo1 = BoxLayout(orientation='vertical')
            gl1 = GridLayout(cols = 1, size_hint = (1,1), row_force_default=True, row_default_height=35)
            bl0 = BoxLayout()
            bl0.add_widget(Label(text='С'))
            self.zaezdTI4_1_1 = TextInput(text='', multiline=False)
            self.zaezdTI4_1_1.bind(on_text_validate=self.zaezdTIA4_1_1)
            f = open('zaezdTI4_1_1.txt', 'a+')
            f.close()
            f = open('zaezdTI4_1_1.txt', 'r')
            a = f.read()
            self.zaezdTI4_1_1.text = a
            f.close()
            bl0.add_widget(self.zaezdTI4_1_1)
            bl0.add_widget(Label(text='по'))
            self.zaezdTI4_1_2 = TextInput(text='', multiline=False)
            self.zaezdTI4_1_2.bind(on_text_validate=self.zaezdTIA4_1_2)
            f = open('zaezdTI4_1_2.txt', 'a+')
            f.close()
            f = open('zaezdTI4_1_2.txt', 'r')
            a = f.read()
            self.zaezdTI4_1_2.text = a
            f.close()
            bl0.add_widget(self.zaezdTI4_1_2)
            bl0.add_widget(Label(text='ФИО:'))
            self.zaezdTI4_1_3 = TextInput(text='', multiline=False)
            self.zaezdTI4_1_3.bind(on_text_validate=self.zaezdTIA4_1_3)
            f = open('zaezdTI4_1_3.txt', 'a+')
            f.close()
            f = open('zaezdTI4_1_3.txt', 'r')
            a = f.read()
            self.zaezdTI4_1_3.text = a
            f.close()
            bl0.add_widget(self.zaezdTI4_1_3)
            gl1.add_widget(bl0)

            bl1 = BoxLayout()
            bl1.add_widget(Label(text='С'))
            self.zaezdTI4_2_1 = TextInput(text='', multiline=False)
            self.zaezdTI4_2_1.bind(on_text_validate=self.zaezdTIA4_2_1)
            f = open('zaezdTI4_2_1.txt', 'a+')
            f.close()
            f = open('zaezdTI4_2_1.txt', 'r')
            a = f.read()
            self.zaezdTI4_2_1.text = a
            f.close()
            bl1.add_widget(self.zaezdTI4_2_1)
            bl1.add_widget(Label(text='по'))
            self.zaezdTI4_2_2 = TextInput(text='', multiline=False)
            self.zaezdTI4_2_2.bind(on_text_validate=self.zaezdTIA4_2_2)
            f = open('zaezdTI4_2_2.txt', 'a+')
            f.close()
            f = open('zaezdTI4_2_2.txt', 'r')
            a = f.read()
            self.zaezdTI4_2_2.text = a
            f.close()
            bl1.add_widget(self.zaezdTI4_2_2)
            bl1.add_widget(Label(text='ФИО:'))
            self.zaezdTI4_2_3 = TextInput(text='', multiline=False)
            self.zaezdTI4_2_3.bind(on_text_validate=self.zaezdTIA4_2_3)
            f = open('zaezdTI4_2_3.txt', 'a+')
            f.close()
            f = open('zaezdTI4_2_3.txt', 'r')
            a = f.read()
            self.zaezdTI4_2_3.text = a
            f.close()
            bl1.add_widget(self.zaezdTI4_2_3)
            gl1.add_widget(bl1)

            bl2 = BoxLayout()
            bl2.add_widget(Label(text='С'))
            self.zaezdTI4_3_1 = TextInput(text='', multiline=False)
            self.zaezdTI4_3_1.bind(on_text_validate=self.zaezdTIA4_3_1)
            f = open('zaezdTI4_3_1.txt', 'a+')
            f.close()
            f = open('zaezdTI4_3_1.txt', 'r')
            a = f.read()
            self.zaezdTI4_3_1.text = a
            f.close()
            bl2.add_widget(self.zaezdTI4_3_1)
            bl2.add_widget(Label(text='по'))
            self.zaezdTI4_3_2 = TextInput(text='', multiline=False)
            self.zaezdTI4_3_2.bind(on_text_validate=self.zaezdTIA4_3_2)
            f = open('zaezdTI4_3_2.txt', 'a+')
            f.close()
            f = open('zaezdTI4_3_2.txt', 'r')
            a = f.read()
            self.zaezdTI4_3_2.text = a
            f.close()
            bl2.add_widget(self.zaezdTI4_3_2)
            bl2.add_widget(Label(text='ФИО:'))
            self.zaezdTI4_3_3 = TextInput(text='', multiline=False)
            self.zaezdTI4_3_3.bind(on_text_validate=self.zaezdTIA4_3_3)
            f = open('zaezdTI4_3_3.txt', 'a+')
            f.close()
            f = open('zaezdTI4_3_3.txt', 'r')
            a = f.read()
            self.zaezdTI4_3_3.text = a
            f.close()
            bl2.add_widget(self.zaezdTI4_3_3)
            gl1.add_widget(bl2)

            th1.content = gl1

            #Сведения
            th2 = TabbedPanelHeader(text = 'Сведения')
            blo2=BoxLayout(orientation = 'vertical')
            gl2 = GridLayout(cols=4, size_hint=(1, .2), row_force_default=True, row_default_height=35)

            gl2.add_widget(Label(text = 'Паспорт:'))
            f = open("pas4.txt", 'a+')
            f.close()
            f = open("pas4.txt", 'r')
            a = f.read()
            self.ti4_1 = TextInput(multiline=False)
            self.ti4_1.text = a
            self.ti4_1.bind(on_text_validate = self.ti4_1_action)
            f.close()
            gl2.add_widget(self.ti4_1)
            gl2.add_widget(Label(text='Предоплата букинг'))
            cb1 = CheckBox()
            f = open('cb4_1.txt', 'a+')
            f.close()
            f = open('cb4_1.txt','r')
            a = f.read()
            cb1.bind(active=on_checkbox_active_1)
            cb1.bind(disabled=on_checkbox_active_1)
            if a == 'true':
                cb1.trigger_action()
            f.close()
            gl2.add_widget(cb1)
            gl2.add_widget(Label(text='Предоплата:'))
            f = open('predopl4.txt', 'a+')
            f.close()
            f = open('predopl4.txt', 'r')
            a = f.read()
            self.ti4_2 = TextInput(multiline=False)
            self.ti4_2.text = a
            self.ti4_2.bind(on_text_validate=self.ti4_2_action)
            gl2.add_widget(self.ti4_2)
            f.close()
            gl2.add_widget(Label(text='Собака'))
            f = open('cb4_2.txt', 'a+')
            f.close()
            f = open('cb4_2.txt', 'r')
            a = f.read()
            cb2 = CheckBox()
            cb2.bind(active=on_checkbox_active_2)
            cb2.bind(disabled=on_checkbox_active_2)
            if a == 'true':
                cb2.trigger_action()
            f.close()
            gl2.add_widget(cb2)
            gl2.add_widget(Label(text='Ранний заезд'))
            f = open('cb4_3.txt', 'a+')
            f.close()
            f = open('cb4_3.txt', 'r')
            a = f.read()
            cb3 = CheckBox()
            cb3.bind(active=on_checkbox_active_3)
            cb3.bind(disabled=on_checkbox_active_3)
            if a == 'true':
                cb3.trigger_action()
            f.close()
            gl2.add_widget(cb3)
            gl2.add_widget(Label(text='Поздний выезд'))
            f = open('cb4_4.txt', 'a+')
            f.close()
            f = open('cb4_4.txt', 'r')
            a = f.read()
            cb4 = CheckBox()
            cb4.bind(active=on_checkbox_active_4)
            cb4.bind(disabled=on_checkbox_active_4)
            if a == 'true':
                cb4.trigger_action()
            f.close()
            gl2.add_widget(cb4)
            gl2.add_widget(Label(text='Доп. кровать'))
            f = open('cb4_5.txt', 'a+')
            f.close()
            f = open('cb4_5.txt', 'r')
            a = f.read()
            cb5 = CheckBox()
            cb5.bind(active=on_checkbox_active_5)
            cb5.bind(disabled=on_checkbox_active_5)
            if a == 'true':
                cb5.trigger_action()
            f.close()
            gl2.add_widget(cb5)
            gl2.add_widget(Label(text='Выходные'))
            f = open('cb4_6.txt', 'a+')
            f.close()
            f = open('cb4_6.txt', 'r')
            a = f.read()
            cb6 = CheckBox()
            cb6.bind(active=on_checkbox_active_6)
            cb6.bind(disabled=on_checkbox_active_6)
            if a == 'true':
                cb6.trigger_action()
            f.close()
            gl2.add_widget(cb6)

            #dropdown
            self.dd1 = DropDown()
            self.lblnazvanie = Label(text ='')
            mainbutton = Button(text='Меню')
            mainbutton.bind(on_release=self.dd1.open)
            self.dd1.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
            self.dd1.bind(on_select=lambda instance, x: setattr(self.lblnazvanie,'text', x))
            f = open('menu.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n=n+1
            for i in range(0,n,2):
                btn = Button(text=s[i], size_hint_y=None, height=35)
                btn.bind(on_release=lambda btn: self.dd1.select(btn.text))
                self.dd1.add_widget(btn)
            f.close()

            blo2.add_widget(gl2)
            gl3 = GridLayout(cols=2, size_hint=(1, .5), row_force_default=True, row_default_height=35)
            gl3.add_widget(mainbutton)
            btn8 = Button(text='Добавить в счет',on_press = self.dobavitvschet4)

            gl3.add_widget(btn8)
            blo2.add_widget(gl3)
            th2.content = blo2
            th3 = TabbedPanelHeader(text = 'Счет')


            #счет

            bxl1 = BoxLayout(orientation = 'vertical')
            scrl1 = ScrollView(size_hint=(1, .95))
            self.gl9 = GridLayout(cols=2, size_hint = (1,1), row_force_default=True,size_hint_y=None, row_default_height=40, spacing = 1)

            self.gl9.bind(minimum_height=self.gl9.setter('height'))
            scrl1.add_widget(self.gl9)
            bxl1.add_widget(scrl1)
            bxl2 = BoxLayout(orientation = 'horizontal', size_hint=(1, .05))
            bxl2.add_widget(Label(text = 'Итог :'))
            self.txtbx4 = TextInput(text=str(self.itog4)+' руб', multiline = False, halign = 'center')
            bxl2.add_widget(self.txtbx4)
            btn = Button(text = 'Обновить', on_press = self.obnovit4)
            bxl2.add_widget(btn)
            bxl1.add_widget(bxl2)
            th3.content = bxl1
            f = open('chet4.txt','a+')
            f.close()
            f = open('chet4.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n = n + 1
            for i in range(0,n,2):
                self.gl9.add_widget(Label(text=s[i]))
                self.gl9.add_widget(Label(text=s[i+1] + ' руб'))
                if self.itogbool4:
                    self.itog4 = self.itog4 + int(s[i+1])
            f.close()
            self.itogbool4 = False
            self.txtbx4.text = str(self.itog4) + ' руб'

            self.tb4.add_widget(th1)
            self.tb4.add_widget(th2)
            self.tb4.add_widget(th3)
        if not Bool:
            self.general.add_widget(self.tb4)
            Bool = True
        else:
            self.general.remove_widget(self.general.children[0])
            self.general.add_widget(self.tb4)

    def btn5(self, instance):
        global Bool

        def on_checkbox_active_1(checkbox, value):
            f = open('cb5_1.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_2(checkbox, value):
            f = open('cb5_2.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_3(checkbox, value):
            f = open('cb5_3.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_4(checkbox, value):
            f = open('cb5_4.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_5(checkbox, value):
            f = open('cb5_5.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_6(checkbox, value):
            f = open('cb5_6.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()


        global Bool1
        if not Bool1:
            self.tb5 = TabbedPanel()
            self.tb5.do_default_tab = False

        #Заезды

            th1 = TabbedPanelHeader(text = 'Заезды')
            blo1 = BoxLayout(orientation='vertical')
            gl1 = GridLayout(cols = 1, size_hint = (1,1), row_force_default=True, row_default_height=35)
            bl0 = BoxLayout()
            bl0.add_widget(Label(text='С'))
            self.zaezdTI5_1_1 = TextInput(text='', multiline=False)
            self.zaezdTI5_1_1.bind(on_text_validate=self.zaezdTIA5_1_1)
            f = open('zaezdTI5_1_1.txt', 'a+')
            f.close()
            f = open('zaezdTI5_1_1.txt', 'r')
            a = f.read()
            self.zaezdTI5_1_1.text = a
            f.close()
            bl0.add_widget(self.zaezdTI5_1_1)
            bl0.add_widget(Label(text='по'))
            self.zaezdTI5_1_2 = TextInput(text='', multiline=False)
            self.zaezdTI5_1_2.bind(on_text_validate=self.zaezdTIA5_1_2)
            f = open('zaezdTI5_1_2.txt', 'a+')
            f.close()
            f = open('zaezdTI5_1_2.txt', 'r')
            a = f.read()
            self.zaezdTI5_1_2.text = a
            f.close()
            bl0.add_widget(self.zaezdTI5_1_2)
            bl0.add_widget(Label(text='ФИО:'))
            self.zaezdTI5_1_3 = TextInput(text='', multiline=False)
            self.zaezdTI5_1_3.bind(on_text_validate=self.zaezdTIA5_1_3)
            f = open('zaezdTI5_1_3.txt', 'a+')
            f.close()
            f = open('zaezdTI5_1_3.txt', 'r')
            a = f.read()
            self.zaezdTI5_1_3.text = a
            f.close()
            bl0.add_widget(self.zaezdTI5_1_3)
            gl1.add_widget(bl0)

            bl1 = BoxLayout()
            bl1.add_widget(Label(text='С'))
            self.zaezdTI5_2_1 = TextInput(text='', multiline=False)
            self.zaezdTI5_2_1.bind(on_text_validate=self.zaezdTIA5_2_1)
            f = open('zaezdTI5_2_1.txt', 'a+')
            f.close()
            f = open('zaezdTI5_2_1.txt', 'r')
            a = f.read()
            self.zaezdTI5_2_1.text = a
            f.close()
            bl1.add_widget(self.zaezdTI5_2_1)
            bl1.add_widget(Label(text='по'))
            self.zaezdTI5_2_2 = TextInput(text='', multiline=False)
            self.zaezdTI5_2_2.bind(on_text_validate=self.zaezdTIA5_2_2)
            f = open('zaezdTI5_2_2.txt', 'a+')
            f.close()
            f = open('zaezdTI5_2_2.txt', 'r')
            a = f.read()
            self.zaezdTI5_2_2.text = a
            f.close()
            bl1.add_widget(self.zaezdTI5_2_2)
            bl1.add_widget(Label(text='ФИО:'))
            self.zaezdTI5_2_3 = TextInput(text='', multiline=False)
            self.zaezdTI5_2_3.bind(on_text_validate=self.zaezdTIA5_2_3)
            f = open('zaezdTI5_2_3.txt', 'a+')
            f.close()
            f = open('zaezdTI5_2_3.txt', 'r')
            a = f.read()
            self.zaezdTI5_2_3.text = a
            f.close()
            bl1.add_widget(self.zaezdTI5_2_3)
            gl1.add_widget(bl1)

            bl2 = BoxLayout()
            bl2.add_widget(Label(text='С'))
            self.zaezdTI5_3_1 = TextInput(text='', multiline=False)
            self.zaezdTI5_3_1.bind(on_text_validate=self.zaezdTIA5_3_1)
            f = open('zaezdTI5_3_1.txt', 'a+')
            f.close()
            f = open('zaezdTI5_3_1.txt', 'r')
            a = f.read()
            self.zaezdTI5_3_1.text = a
            f.close()
            bl2.add_widget(self.zaezdTI5_3_1)
            bl2.add_widget(Label(text='по'))
            self.zaezdTI5_3_2 = TextInput(text='', multiline=False)
            self.zaezdTI5_3_2.bind(on_text_validate=self.zaezdTIA5_3_2)
            f = open('zaezdTI5_3_2.txt', 'a+')
            f.close()
            f = open('zaezdTI5_3_2.txt', 'r')
            a = f.read()
            self.zaezdTI5_3_2.text = a
            f.close()
            bl2.add_widget(self.zaezdTI5_3_2)
            bl2.add_widget(Label(text='ФИО:'))
            self.zaezdTI5_3_3 = TextInput(text='', multiline=False)
            self.zaezdTI5_3_3.bind(on_text_validate=self.zaezdTIA5_3_3)
            f = open('zaezdTI5_3_3.txt', 'a+')
            f.close()
            f = open('zaezdTI5_3_3.txt', 'r')
            a = f.read()
            self.zaezdTI5_3_3.text = a
            f.close()
            bl2.add_widget(self.zaezdTI5_3_3)
            gl1.add_widget(bl2)

            th1.content = gl1

            #Сведения
            th2 = TabbedPanelHeader(text = 'Сведения')
            blo2=BoxLayout(orientation = 'vertical')
            gl2 = GridLayout(cols=4, size_hint=(1, .2), row_force_default=True, row_default_height=35)

            gl2.add_widget(Label(text = 'Паспорт:'))
            f = open("pas5.txt", 'a+')
            f.close()
            f = open("pas5.txt", 'r')
            a = f.read()
            self.ti5_1 = TextInput(multiline=False)
            self.ti5_1.text = a
            self.ti5_1.bind(on_text_validate = self.ti5_1_action)
            f.close()
            gl2.add_widget(self.ti5_1)
            gl2.add_widget(Label(text='Предоплата букинг'))
            cb1 = CheckBox()
            f = open('cb5_1.txt', 'a+')
            f.close()
            f = open('cb5_1.txt','r')
            a = f.read()
            cb1.bind(active=on_checkbox_active_1)
            cb1.bind(disabled=on_checkbox_active_1)
            if a == 'true':
                cb1.trigger_action()
            f.close()
            gl2.add_widget(cb1)
            gl2.add_widget(Label(text='Предоплата:'))
            f = open('predopl5.txt', 'a+')
            f.close()
            f = open('predopl5.txt', 'r')
            a = f.read()
            self.ti5_2 = TextInput(multiline=False)
            self.ti5_2.text = a
            self.ti5_2.bind(on_text_validate=self.ti5_2_action)
            gl2.add_widget(self.ti5_2)
            f.close()
            gl2.add_widget(Label(text='Собака'))
            f = open('cb5_2.txt', 'a+')
            f.close()
            f = open('cb5_2.txt', 'r')
            a = f.read()
            cb2 = CheckBox()
            cb2.bind(active=on_checkbox_active_2)
            cb2.bind(disabled=on_checkbox_active_2)
            if a == 'true':
                cb2.trigger_action()
            f.close()
            gl2.add_widget(cb2)
            gl2.add_widget(Label(text='Ранний заезд'))
            f = open('cb5_3.txt', 'a+')
            f.close()
            f = open('cb5_3.txt', 'r')
            a = f.read()
            cb3 = CheckBox()
            cb3.bind(active=on_checkbox_active_3)
            cb3.bind(disabled=on_checkbox_active_3)
            if a == 'true':
                cb3.trigger_action()
            f.close()
            gl2.add_widget(cb3)
            gl2.add_widget(Label(text='Поздний выезд'))
            f = open('cb5_4.txt', 'a+')
            f.close()
            f = open('cb5_4.txt', 'r')
            a = f.read()
            cb4 = CheckBox()
            cb4.bind(active=on_checkbox_active_4)
            cb4.bind(disabled=on_checkbox_active_4)
            if a == 'true':
                cb4.trigger_action()
            f.close()
            gl2.add_widget(cb4)
            gl2.add_widget(Label(text='Доп. кровать'))
            f = open('cb5_5.txt', 'a+')
            f.close()
            f = open('cb5_5.txt', 'r')
            a = f.read()
            cb5 = CheckBox()
            cb5.bind(active=on_checkbox_active_5)
            cb5.bind(disabled=on_checkbox_active_5)
            if a == 'true':
                cb5.trigger_action()
            f.close()
            gl2.add_widget(cb5)
            gl2.add_widget(Label(text='Выходные'))
            f = open('cb5_6.txt', 'a+')
            f.close()
            f = open('cb5_6.txt', 'r')
            a = f.read()
            cb6 = CheckBox()
            cb6.bind(active=on_checkbox_active_6)
            cb6.bind(disabled=on_checkbox_active_6)
            if a == 'true':
                cb6.trigger_action()
            f.close()
            gl2.add_widget(cb6)

            #dropdown
            self.dd1 = DropDown()
            self.lblnazvanie = Label(text ='')
            mainbutton = Button(text='Меню')
            mainbutton.bind(on_release=self.dd1.open)
            self.dd1.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
            self.dd1.bind(on_select=lambda instance, x: setattr(self.lblnazvanie,'text', x))
            f = open('menu.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n=n+1
            for i in range(0,n,2):
                btn = Button(text=s[i], size_hint_y=None, height=35)
                btn.bind(on_release=lambda btn: self.dd1.select(btn.text))
                self.dd1.add_widget(btn)
            f.close()

            blo2.add_widget(gl2)
            gl3 = GridLayout(cols=2, size_hint=(1, .5), row_force_default=True, row_default_height=35)
            gl3.add_widget(mainbutton)
            btn8 = Button(text='Добавить в счет',on_press = self.dobavitvschet5)

            gl3.add_widget(btn8)
            blo2.add_widget(gl3)
            th2.content = blo2
            th3 = TabbedPanelHeader(text = 'Счет')


            #счет

            bxl1 = BoxLayout(orientation = 'vertical')
            scrl1 = ScrollView(size_hint=(1, .95))
            self.gl10 = GridLayout(cols=2, size_hint = (1,1), row_force_default=True,size_hint_y=None, row_default_height=40, spacing = 1)

            self.gl10.bind(minimum_height=self.gl10.setter('height'))
            scrl1.add_widget(self.gl10)
            bxl1.add_widget(scrl1)
            bxl2 = BoxLayout(orientation = 'horizontal', size_hint=(1, .05))
            bxl2.add_widget(Label(text = 'Итог :'))
            self.txtbx5 = TextInput(text=str(self.itog5)+' руб', multiline = False, halign = 'center')
            bxl2.add_widget(self.txtbx5)
            btn = Button(text = 'Обновить', on_press = self.obnovit5)
            bxl2.add_widget(btn)
            bxl1.add_widget(bxl2)
            th3.content = bxl1
            f = open('chet5.txt','a+')
            f.close()
            f = open('chet5.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n = n + 1
            for i in range(0,n,2):
                self.gl10.add_widget(Label(text=s[i]))
                self.gl10.add_widget(Label(text=s[i+1] + ' руб'))
                if self.itogbool5:
                    self.itog5 = self.itog5 + int(s[i+1])
            f.close()
            self.itogbool5 = False
            self.txtbx5.text = str(self.itog5) + ' руб'

            self.tb5.add_widget(th1)
            self.tb5.add_widget(th2)
            self.tb5.add_widget(th3)
        if not Bool:
            self.general.add_widget(self.tb5)
            Bool = True
        else:
            self.general.remove_widget(self.general.children[0])
            self.general.add_widget(self.tb5)

    def btn6(self, instance):
        global Bool

        def on_checkbox_active_1(checkbox, value):
            f = open('cb6_1.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_2(checkbox, value):
            f = open('cb6_2.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_3(checkbox, value):
            f = open('cb6_3.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_4(checkbox, value):
            f = open('cb6_4.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_5(checkbox, value):
            f = open('cb6_5.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_6(checkbox, value):
            f = open('cb6_6.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()


        global Bool1
        if not Bool1:
            self.tb6 = TabbedPanel()
            self.tb6.do_default_tab = False

        #Заезды

            th1 = TabbedPanelHeader(text = 'Заезды')
            blo1 = BoxLayout(orientation='vertical')
            gl1 = GridLayout(cols = 1, size_hint = (1,1), row_force_default=True, row_default_height=35)
            bl0 = BoxLayout()
            bl0.add_widget(Label(text='С'))
            self.zaezdTI6_1_1 = TextInput(text='', multiline=False)
            self.zaezdTI6_1_1.bind(on_text_validate=self.zaezdTIA6_1_1)
            f = open('zaezdTI6_1_1.txt', 'a+')
            f.close()
            f = open('zaezdTI6_1_1.txt', 'r')
            a = f.read()
            self.zaezdTI6_1_1.text = a
            f.close()
            bl0.add_widget(self.zaezdTI6_1_1)
            bl0.add_widget(Label(text='по'))
            self.zaezdTI6_1_2 = TextInput(text='', multiline=False)
            self.zaezdTI6_1_2.bind(on_text_validate=self.zaezdTIA6_1_2)
            f = open('zaezdTI6_1_2.txt', 'a+')
            f.close()
            f = open('zaezdTI6_1_2.txt', 'r')
            a = f.read()
            self.zaezdTI6_1_2.text = a
            f.close()
            bl0.add_widget(self.zaezdTI6_1_2)
            bl0.add_widget(Label(text='ФИО:'))
            self.zaezdTI6_1_3 = TextInput(text='', multiline=False)
            self.zaezdTI6_1_3.bind(on_text_validate=self.zaezdTIA6_1_3)
            f = open('zaezdTI6_1_3.txt', 'a+')
            f.close()
            f = open('zaezdTI6_1_3.txt', 'r')
            a = f.read()
            self.zaezdTI6_1_3.text = a
            f.close()
            bl0.add_widget(self.zaezdTI6_1_3)
            gl1.add_widget(bl0)

            bl1 = BoxLayout()
            bl1.add_widget(Label(text='С'))
            self.zaezdTI6_2_1 = TextInput(text='', multiline=False)
            self.zaezdTI6_2_1.bind(on_text_validate=self.zaezdTIA6_2_1)
            f = open('zaezdTI6_2_1.txt', 'a+')
            f.close()
            f = open('zaezdTI6_2_1.txt', 'r')
            a = f.read()
            self.zaezdTI6_2_1.text = a
            f.close()
            bl1.add_widget(self.zaezdTI6_2_1)
            bl1.add_widget(Label(text='по'))
            self.zaezdTI6_2_2 = TextInput(text='', multiline=False)
            self.zaezdTI6_2_2.bind(on_text_validate=self.zaezdTIA6_2_2)
            f = open('zaezdTI6_2_2.txt', 'a+')
            f.close()
            f = open('zaezdTI6_2_2.txt', 'r')
            a = f.read()
            self.zaezdTI6_2_2.text = a
            f.close()
            bl1.add_widget(self.zaezdTI6_2_2)
            bl1.add_widget(Label(text='ФИО:'))
            self.zaezdTI6_2_3 = TextInput(text='', multiline=False)
            self.zaezdTI6_2_3.bind(on_text_validate=self.zaezdTIA6_2_3)
            f = open('zaezdTI6_2_3.txt', 'a+')
            f.close()
            f = open('zaezdTI6_2_3.txt', 'r')
            a = f.read()
            self.zaezdTI6_2_3.text = a
            f.close()
            bl1.add_widget(self.zaezdTI6_2_3)
            gl1.add_widget(bl1)

            bl2 = BoxLayout()
            bl2.add_widget(Label(text='С'))
            self.zaezdTI6_3_1 = TextInput(text='', multiline=False)
            self.zaezdTI6_3_1.bind(on_text_validate=self.zaezdTIA6_3_1)
            f = open('zaezdTI6_3_1.txt', 'a+')
            f.close()
            f = open('zaezdTI6_3_1.txt', 'r')
            a = f.read()
            self.zaezdTI6_3_1.text = a
            f.close()
            bl2.add_widget(self.zaezdTI6_3_1)
            bl2.add_widget(Label(text='по'))
            self.zaezdTI6_3_2 = TextInput(text='', multiline=False)
            self.zaezdTI6_3_2.bind(on_text_validate=self.zaezdTIA6_3_2)
            f = open('zaezdTI6_3_2.txt', 'a+')
            f.close()
            f = open('zaezdTI6_3_2.txt', 'r')
            a = f.read()
            self.zaezdTI6_3_2.text = a
            f.close()
            bl2.add_widget(self.zaezdTI6_3_2)
            bl2.add_widget(Label(text='ФИО:'))
            self.zaezdTI6_3_3 = TextInput(text='', multiline=False)
            self.zaezdTI6_3_3.bind(on_text_validate=self.zaezdTIA6_3_3)
            f = open('zaezdTI6_3_3.txt', 'a+')
            f.close()
            f = open('zaezdTI6_3_3.txt', 'r')
            a = f.read()
            self.zaezdTI6_3_3.text = a
            f.close()
            bl2.add_widget(self.zaezdTI6_3_3)
            gl1.add_widget(bl2)

            th1.content = gl1

            #Сведения
            th2 = TabbedPanelHeader(text = 'Сведения')
            blo2=BoxLayout(orientation = 'vertical')
            gl2 = GridLayout(cols=4, size_hint=(1, .2), row_force_default=True, row_default_height=35)

            gl2.add_widget(Label(text = 'Паспорт:'))
            f = open("pas6.txt", 'a+')
            f.close()
            f = open("pas6.txt", 'r')
            a = f.read()
            self.ti6_1 = TextInput(multiline=False)
            self.ti6_1.text = a
            self.ti6_1.bind(on_text_validate = self.ti6_1_action)
            f.close()
            gl2.add_widget(self.ti6_1)
            gl2.add_widget(Label(text='Предоплата букинг'))
            cb1 = CheckBox()
            f = open('cb6_1.txt', 'a+')
            f.close()
            f = open('cb6_1.txt','r')
            a = f.read()
            cb1.bind(active=on_checkbox_active_1)
            cb1.bind(disabled=on_checkbox_active_1)
            if a == 'true':
                cb1.trigger_action()
            f.close()
            gl2.add_widget(cb1)
            gl2.add_widget(Label(text='Предоплата:'))
            f = open('predopl6.txt', 'a+')
            f.close()
            f = open('predopl6.txt', 'r')
            a = f.read()
            self.ti6_2 = TextInput(multiline=False)
            self.ti6_2.text = a
            self.ti6_2.bind(on_text_validate=self.ti6_2_action)
            gl2.add_widget(self.ti6_2)
            f.close()
            gl2.add_widget(Label(text='Собака'))
            f = open('cb6_2.txt', 'a+')
            f.close()
            f = open('cb6_2.txt', 'r')
            a = f.read()
            cb2 = CheckBox()
            cb2.bind(active=on_checkbox_active_2)
            cb2.bind(disabled=on_checkbox_active_2)
            if a == 'true':
                cb2.trigger_action()
            f.close()
            gl2.add_widget(cb2)
            gl2.add_widget(Label(text='Ранний заезд'))
            f = open('cb6_3.txt', 'a+')
            f.close()
            f = open('cb6_3.txt', 'r')
            a = f.read()
            cb3 = CheckBox()
            cb3.bind(active=on_checkbox_active_3)
            cb3.bind(disabled=on_checkbox_active_3)
            if a == 'true':
                cb3.trigger_action()
            f.close()
            gl2.add_widget(cb3)
            gl2.add_widget(Label(text='Поздний выезд'))
            f = open('cb6_4.txt', 'a+')
            f.close()
            f = open('cb6_4.txt', 'r')
            a = f.read()
            cb4 = CheckBox()
            cb4.bind(active=on_checkbox_active_4)
            cb4.bind(disabled=on_checkbox_active_4)
            if a == 'true':
                cb4.trigger_action()
            f.close()
            gl2.add_widget(cb4)
            gl2.add_widget(Label(text='Доп. кровать'))
            f = open('cb6_5.txt', 'a+')
            f.close()
            f = open('cb6_5.txt', 'r')
            a = f.read()
            cb5 = CheckBox()
            cb5.bind(active=on_checkbox_active_5)
            cb5.bind(disabled=on_checkbox_active_5)
            if a == 'true':
                cb5.trigger_action()
            f.close()
            gl2.add_widget(cb5)
            gl2.add_widget(Label(text='Выходные'))
            f = open('cb6_6.txt', 'a+')
            f.close()
            f = open('cb6_6.txt', 'r')
            a = f.read()
            cb6 = CheckBox()
            cb6.bind(active=on_checkbox_active_6)
            cb6.bind(disabled=on_checkbox_active_6)
            if a == 'true':
                cb6.trigger_action()
            f.close()
            gl2.add_widget(cb6)

            #dropdown
            self.dd1 = DropDown()
            self.lblnazvanie = Label(text ='')
            mainbutton = Button(text='Меню')
            mainbutton.bind(on_release=self.dd1.open)
            self.dd1.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
            self.dd1.bind(on_select=lambda instance, x: setattr(self.lblnazvanie,'text', x))
            f = open('menu.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n=n+1
            for i in range(0,n,2):
                btn = Button(text=s[i], size_hint_y=None, height=35)
                btn.bind(on_release=lambda btn: self.dd1.select(btn.text))
                self.dd1.add_widget(btn)
            f.close()

            blo2.add_widget(gl2)
            gl3 = GridLayout(cols=2, size_hint=(1, .5), row_force_default=True, row_default_height=35)
            gl3.add_widget(mainbutton)
            btn8 = Button(text='Добавить в счет',on_press = self.dobavitvschet6)

            gl3.add_widget(btn8)
            blo2.add_widget(gl3)
            th2.content = blo2
            th3 = TabbedPanelHeader(text = 'Счет')


            #счет

            bxl1 = BoxLayout(orientation = 'vertical')
            scrl1 = ScrollView(size_hint=(1, .95))
            self.gl11 = GridLayout(cols=2, size_hint = (1,1), row_force_default=True,size_hint_y=None, row_default_height=40, spacing = 1)

            self.gl11.bind(minimum_height=self.gl11.setter('height'))
            scrl1.add_widget(self.gl11)
            bxl1.add_widget(scrl1)
            bxl2 = BoxLayout(orientation = 'horizontal', size_hint=(1, .05))
            bxl2.add_widget(Label(text = 'Итог :'))
            self.txtbx6 = TextInput(text=str(self.itog6)+' руб', multiline = False, halign = 'center')
            bxl2.add_widget(self.txtbx6)
            btn = Button(text = 'Обновить', on_press = self.obnovit6)
            bxl2.add_widget(btn)
            bxl1.add_widget(bxl2)
            th3.content = bxl1
            f = open('chet6.txt','a+')
            f.close()
            f = open('chet6.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n = n + 1
            for i in range(0,n,2):
                self.gl11.add_widget(Label(text=s[i]))
                self.gl11.add_widget(Label(text=s[i+1] + ' руб'))
                if self.itogbool6:
                    self.itog6 = self.itog6 + int(s[i+1])
            f.close()
            self.itogbool6 = False
            self.txtbx6.text = str(self.itog6) + ' руб'

            self.tb6.add_widget(th1)
            self.tb6.add_widget(th2)
            self.tb6.add_widget(th3)
        if not Bool:
            self.general.add_widget(self.tb6)
            Bool = True
        else:
            self.general.remove_widget(self.general.children[0])
            self.general.add_widget(self.tb6)

    def btn7(self, instance):
        global Bool

        def on_checkbox_active_1(checkbox, value):
            f = open('cb7_1.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_2(checkbox, value):
            f = open('cb7_2.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_3(checkbox, value):
            f = open('cb7_3.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_4(checkbox, value):
            f = open('cb7_4.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_5(checkbox, value):
            f = open('cb7_5.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_6(checkbox, value):
            f = open('cb7_6.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()


        global Bool1
        if not Bool1:
            self.tb7 = TabbedPanel()
            self.tb7.do_default_tab = False

        #Заезды

            th1 = TabbedPanelHeader(text = 'Заезды')
            blo1 = BoxLayout(orientation='vertical')
            gl1 = GridLayout(cols = 1, size_hint = (1,1), row_force_default=True, row_default_height=35)
            bl0 = BoxLayout()
            bl0.add_widget(Label(text='С'))
            self.zaezdTI7_1_1 = TextInput(text='', multiline=False)
            self.zaezdTI7_1_1.bind(on_text_validate=self.zaezdTIA7_1_1)
            f = open('zaezdTI7_1_1.txt', 'a+')
            f.close()
            f = open('zaezdTI7_1_1.txt', 'r')
            a = f.read()
            self.zaezdTI7_1_1.text = a
            f.close()
            bl0.add_widget(self.zaezdTI7_1_1)
            bl0.add_widget(Label(text='по'))
            self.zaezdTI7_1_2 = TextInput(text='', multiline=False)
            self.zaezdTI7_1_2.bind(on_text_validate=self.zaezdTIA7_1_2)
            f = open('zaezdTI7_1_2.txt', 'a+')
            f.close()
            f = open('zaezdTI7_1_2.txt', 'r')
            a = f.read()
            self.zaezdTI7_1_2.text = a
            f.close()
            bl0.add_widget(self.zaezdTI7_1_2)
            bl0.add_widget(Label(text='ФИО:'))
            self.zaezdTI7_1_3 = TextInput(text='', multiline=False)
            self.zaezdTI7_1_3.bind(on_text_validate=self.zaezdTIA7_1_3)
            f = open('zaezdTI7_1_3.txt', 'a+')
            f.close()
            f = open('zaezdTI7_1_3.txt', 'r')
            a = f.read()
            self.zaezdTI7_1_3.text = a
            f.close()
            bl0.add_widget(self.zaezdTI7_1_3)
            gl1.add_widget(bl0)

            bl1 = BoxLayout()
            bl1.add_widget(Label(text='С'))
            self.zaezdTI7_2_1 = TextInput(text='', multiline=False)
            self.zaezdTI7_2_1.bind(on_text_validate=self.zaezdTIA7_2_1)
            f = open('zaezdTI7_2_1.txt', 'a+')
            f.close()
            f = open('zaezdTI7_2_1.txt', 'r')
            a = f.read()
            self.zaezdTI7_2_1.text = a
            f.close()
            bl1.add_widget(self.zaezdTI7_2_1)
            bl1.add_widget(Label(text='по'))
            self.zaezdTI7_2_2 = TextInput(text='', multiline=False)
            self.zaezdTI7_2_2.bind(on_text_validate=self.zaezdTIA7_2_2)
            f = open('zaezdTI7_2_2.txt', 'a+')
            f.close()
            f = open('zaezdTI7_2_2.txt', 'r')
            a = f.read()
            self.zaezdTI7_2_2.text = a
            f.close()
            bl1.add_widget(self.zaezdTI7_2_2)
            bl1.add_widget(Label(text='ФИО:'))
            self.zaezdTI7_2_3 = TextInput(text='', multiline=False)
            self.zaezdTI7_2_3.bind(on_text_validate=self.zaezdTIA7_2_3)
            f = open('zaezdTI7_2_3.txt', 'a+')
            f.close()
            f = open('zaezdTI7_2_3.txt', 'r')
            a = f.read()
            self.zaezdTI7_2_3.text = a
            f.close()
            bl1.add_widget(self.zaezdTI7_2_3)
            gl1.add_widget(bl1)

            bl2 = BoxLayout()
            bl2.add_widget(Label(text='С'))
            self.zaezdTI7_3_1 = TextInput(text='', multiline=False)
            self.zaezdTI7_3_1.bind(on_text_validate=self.zaezdTIA7_3_1)
            f = open('zaezdTI7_3_1.txt', 'a+')
            f.close()
            f = open('zaezdTI7_3_1.txt', 'r')
            a = f.read()
            self.zaezdTI7_3_1.text = a
            f.close()
            bl2.add_widget(self.zaezdTI7_3_1)
            bl2.add_widget(Label(text='по'))
            self.zaezdTI7_3_2 = TextInput(text='', multiline=False)
            self.zaezdTI7_3_2.bind(on_text_validate=self.zaezdTIA7_3_2)
            f = open('zaezdTI7_3_2.txt', 'a+')
            f.close()
            f = open('zaezdTI7_3_2.txt', 'r')
            a = f.read()
            self.zaezdTI7_3_2.text = a
            f.close()
            bl2.add_widget(self.zaezdTI7_3_2)
            bl2.add_widget(Label(text='ФИО:'))
            self.zaezdTI7_3_3 = TextInput(text='', multiline=False)
            self.zaezdTI7_3_3.bind(on_text_validate=self.zaezdTIA7_3_3)
            f = open('zaezdTI7_3_3.txt', 'a+')
            f.close()
            f = open('zaezdTI7_3_3.txt', 'r')
            a = f.read()
            self.zaezdTI7_3_3.text = a
            f.close()
            bl2.add_widget(self.zaezdTI7_3_3)
            gl1.add_widget(bl2)

            th1.content = gl1

            #Сведения
            th2 = TabbedPanelHeader(text = 'Сведения')
            blo2=BoxLayout(orientation = 'vertical')
            gl2 = GridLayout(cols=4, size_hint=(1, .2), row_force_default=True, row_default_height=35)

            gl2.add_widget(Label(text = 'Паспорт:'))
            f = open("pas7.txt", 'a+')
            f.close()
            f = open("pas7.txt", 'r')
            a = f.read()
            self.ti7_1 = TextInput(multiline=False)
            self.ti7_1.text = a
            self.ti7_1.bind(on_text_validate = self.ti7_1_action)
            f.close()
            gl2.add_widget(self.ti7_1)
            gl2.add_widget(Label(text='Предоплата букинг'))
            cb1 = CheckBox()
            f = open('cb7_1.txt', 'a+')
            f.close()
            f = open('cb7_1.txt','r')
            a = f.read()
            cb1.bind(active=on_checkbox_active_1)
            cb1.bind(disabled=on_checkbox_active_1)
            if a == 'true':
                cb1.trigger_action()
            f.close()
            gl2.add_widget(cb1)
            gl2.add_widget(Label(text='Предоплата:'))
            f = open('predopl7.txt', 'a+')
            f.close()
            f = open('predopl7.txt', 'r')
            a = f.read()
            self.ti7_2 = TextInput(multiline=False)
            self.ti7_2.text = a
            self.ti7_2.bind(on_text_validate=self.ti7_2_action)
            gl2.add_widget(self.ti7_2)
            f.close()
            gl2.add_widget(Label(text='Собака'))
            f = open('cb7_2.txt', 'a+')
            f.close()
            f = open('cb7_2.txt', 'r')
            a = f.read()
            cb2 = CheckBox()
            cb2.bind(active=on_checkbox_active_2)
            cb2.bind(disabled=on_checkbox_active_2)
            if a == 'true':
                cb2.trigger_action()
            f.close()
            gl2.add_widget(cb2)
            gl2.add_widget(Label(text='Ранний заезд'))
            f = open('cb7_3.txt', 'a+')
            f.close()
            f = open('cb7_3.txt', 'r')
            a = f.read()
            cb3 = CheckBox()
            cb3.bind(active=on_checkbox_active_3)
            cb3.bind(disabled=on_checkbox_active_3)
            if a == 'true':
                cb3.trigger_action()
            f.close()
            gl2.add_widget(cb3)
            gl2.add_widget(Label(text='Поздний выезд'))
            f = open('cb7_4.txt', 'a+')
            f.close()
            f = open('cb7_4.txt', 'r')
            a = f.read()
            cb4 = CheckBox()
            cb4.bind(active=on_checkbox_active_4)
            cb4.bind(disabled=on_checkbox_active_4)
            if a == 'true':
                cb4.trigger_action()
            f.close()
            gl2.add_widget(cb4)
            gl2.add_widget(Label(text='Доп. кровать'))
            f = open('cb7_5.txt', 'a+')
            f.close()
            f = open('cb7_5.txt', 'r')
            a = f.read()
            cb5 = CheckBox()
            cb5.bind(active=on_checkbox_active_5)
            cb5.bind(disabled=on_checkbox_active_5)
            if a == 'true':
                cb5.trigger_action()
            f.close()
            gl2.add_widget(cb5)
            gl2.add_widget(Label(text='Выходные'))
            f = open('cb7_6.txt', 'a+')
            f.close()
            f = open('cb7_6.txt', 'r')
            a = f.read()
            cb6 = CheckBox()
            cb6.bind(active=on_checkbox_active_6)
            cb6.bind(disabled=on_checkbox_active_6)
            if a == 'true':
                cb6.trigger_action()
            f.close()
            gl2.add_widget(cb6)

            #dropdown
            self.dd1 = DropDown()
            self.lblnazvanie = Label(text ='')
            mainbutton = Button(text='Меню')
            mainbutton.bind(on_release=self.dd1.open)
            self.dd1.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
            self.dd1.bind(on_select=lambda instance, x: setattr(self.lblnazvanie,'text', x))
            f = open('menu.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n=n+1
            for i in range(0,n,2):
                btn = Button(text=s[i], size_hint_y=None, height=35)
                btn.bind(on_release=lambda btn: self.dd1.select(btn.text))
                self.dd1.add_widget(btn)
            f.close()

            blo2.add_widget(gl2)
            gl3 = GridLayout(cols=2, size_hint=(1, .5), row_force_default=True, row_default_height=35)
            gl3.add_widget(mainbutton)
            btn8 = Button(text='Добавить в счет',on_press = self.dobavitvschet7)

            gl3.add_widget(btn8)
            blo2.add_widget(gl3)
            th2.content = blo2
            th3 = TabbedPanelHeader(text = 'Счет')


            #счет

            bxl1 = BoxLayout(orientation = 'vertical')
            scrl1 = ScrollView(size_hint=(1, .95))
            self.gl12 = GridLayout(cols=2, size_hint = (1,1), row_force_default=True,size_hint_y=None, row_default_height=40, spacing = 1)

            self.gl12.bind(minimum_height=self.gl12.setter('height'))
            scrl1.add_widget(self.gl12)
            bxl1.add_widget(scrl1)
            bxl2 = BoxLayout(orientation = 'horizontal', size_hint=(1, .05))
            bxl2.add_widget(Label(text = 'Итог :'))
            self.txtbx7 = TextInput(text=str(self.itog7)+' руб', multiline = False, halign = 'center')
            bxl2.add_widget(self.txtbx7)
            btn = Button(text = 'Обновить', on_press = self.obnovit7)
            bxl2.add_widget(btn)
            bxl1.add_widget(bxl2)
            th3.content = bxl1
            f = open('chet7.txt','a+')
            f.close()
            f = open('chet7.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n = n + 1
            for i in range(0,n,2):
                self.gl12.add_widget(Label(text=s[i]))
                self.gl12.add_widget(Label(text=s[i+1] + ' руб'))
                if self.itogbool7:
                    self.itog7 = self.itog7 + int(s[i+1])
            f.close()
            self.itogbool7 = False
            self.txtbx7.text = str(self.itog7) + ' руб'

            self.tb7.add_widget(th1)
            self.tb7.add_widget(th2)
            self.tb7.add_widget(th3)
        if not Bool:
            self.general.add_widget(self.tb7)
            Bool = True
        else:
            self.general.remove_widget(self.general.children[0])
            self.general.add_widget(self.tb7)

    def btn8(self, instance):
        global Bool

        def on_checkbox_active_1(checkbox, value):
            f = open('cb8_1.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_2(checkbox, value):
            f = open('cb8_2.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_3(checkbox, value):
            f = open('cb8_3.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_4(checkbox, value):
            f = open('cb8_4.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_5(checkbox, value):
            f = open('cb8_5.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_6(checkbox, value):
            f = open('cb8_6.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()


        global Bool1
        if not Bool1:
            self.tb8 = TabbedPanel()
            self.tb8.do_default_tab = False

        #Заезды

            th1 = TabbedPanelHeader(text = 'Заезды')
            blo1 = BoxLayout(orientation='vertical')
            gl1 = GridLayout(cols = 1, size_hint = (1,1), row_force_default=True, row_default_height=35)
            bl0 = BoxLayout()
            bl0.add_widget(Label(text='С'))
            self.zaezdTI8_1_1 = TextInput(text='', multiline=False)
            self.zaezdTI8_1_1.bind(on_text_validate=self.zaezdTIA8_1_1)
            f = open('zaezdTI8_1_1.txt', 'a+')
            f.close()
            f = open('zaezdTI8_1_1.txt', 'r')
            a = f.read()
            self.zaezdTI8_1_1.text = a
            f.close()
            bl0.add_widget(self.zaezdTI8_1_1)
            bl0.add_widget(Label(text='по'))
            self.zaezdTI8_1_2 = TextInput(text='', multiline=False)
            self.zaezdTI8_1_2.bind(on_text_validate=self.zaezdTIA8_1_2)
            f = open('zaezdTI8_1_2.txt', 'a+')
            f.close()
            f = open('zaezdTI8_1_2.txt', 'r')
            a = f.read()
            self.zaezdTI8_1_2.text = a
            f.close()
            bl0.add_widget(self.zaezdTI8_1_2)
            bl0.add_widget(Label(text='ФИО:'))
            self.zaezdTI8_1_3 = TextInput(text='', multiline=False)
            self.zaezdTI8_1_3.bind(on_text_validate=self.zaezdTIA8_1_3)
            f = open('zaezdTI8_1_3.txt', 'a+')
            f.close()
            f = open('zaezdTI8_1_3.txt', 'r')
            a = f.read()
            self.zaezdTI8_1_3.text = a
            f.close()
            bl0.add_widget(self.zaezdTI8_1_3)
            gl1.add_widget(bl0)

            bl1 = BoxLayout()
            bl1.add_widget(Label(text='С'))
            self.zaezdTI8_2_1 = TextInput(text='', multiline=False)
            self.zaezdTI8_2_1.bind(on_text_validate=self.zaezdTIA8_2_1)
            f = open('zaezdTI8_2_1.txt', 'a+')
            f.close()
            f = open('zaezdTI8_2_1.txt', 'r')
            a = f.read()
            self.zaezdTI8_2_1.text = a
            f.close()
            bl1.add_widget(self.zaezdTI8_2_1)
            bl1.add_widget(Label(text='по'))
            self.zaezdTI8_2_2 = TextInput(text='', multiline=False)
            self.zaezdTI8_2_2.bind(on_text_validate=self.zaezdTIA8_2_2)
            f = open('zaezdTI8_2_2.txt', 'a+')
            f.close()
            f = open('zaezdTI8_2_2.txt', 'r')
            a = f.read()
            self.zaezdTI8_2_2.text = a
            f.close()
            bl1.add_widget(self.zaezdTI8_2_2)
            bl1.add_widget(Label(text='ФИО:'))
            self.zaezdTI8_2_3 = TextInput(text='', multiline=False)
            self.zaezdTI8_2_3.bind(on_text_validate=self.zaezdTIA8_2_3)
            f = open('zaezdTI8_2_3.txt', 'a+')
            f.close()
            f = open('zaezdTI8_2_3.txt', 'r')
            a = f.read()
            self.zaezdTI8_2_3.text = a
            f.close()
            bl1.add_widget(self.zaezdTI8_2_3)
            gl1.add_widget(bl1)

            bl2 = BoxLayout()
            bl2.add_widget(Label(text='С'))
            self.zaezdTI8_3_1 = TextInput(text='', multiline=False)
            self.zaezdTI8_3_1.bind(on_text_validate=self.zaezdTIA8_3_1)
            f = open('zaezdTI8_3_1.txt', 'a+')
            f.close()
            f = open('zaezdTI8_3_1.txt', 'r')
            a = f.read()
            self.zaezdTI8_3_1.text = a
            f.close()
            bl2.add_widget(self.zaezdTI8_3_1)
            bl2.add_widget(Label(text='по'))
            self.zaezdTI8_3_2 = TextInput(text='', multiline=False)
            self.zaezdTI8_3_2.bind(on_text_validate=self.zaezdTIA8_3_2)
            f = open('zaezdTI8_3_2.txt', 'a+')
            f.close()
            f = open('zaezdTI8_3_2.txt', 'r')
            a = f.read()
            self.zaezdTI8_3_2.text = a
            f.close()
            bl2.add_widget(self.zaezdTI8_3_2)
            bl2.add_widget(Label(text='ФИО:'))
            self.zaezdTI8_3_3 = TextInput(text='', multiline=False)
            self.zaezdTI8_3_3.bind(on_text_validate=self.zaezdTIA8_3_3)
            f = open('zaezdTI8_3_3.txt', 'a+')
            f.close()
            f = open('zaezdTI8_3_3.txt', 'r')
            a = f.read()
            self.zaezdTI8_3_3.text = a
            f.close()
            bl2.add_widget(self.zaezdTI8_3_3)
            gl1.add_widget(bl2)

            th1.content = gl1

            #Сведения
            th2 = TabbedPanelHeader(text = 'Сведения')
            blo2=BoxLayout(orientation = 'vertical')
            gl2 = GridLayout(cols=4, size_hint=(1, .2), row_force_default=True, row_default_height=35)

            gl2.add_widget(Label(text = 'Паспорт:'))
            f = open("pas8.txt", 'a+')
            f.close()
            f = open("pas8.txt", 'r')
            a = f.read()
            self.ti8_1 = TextInput(multiline=False)
            self.ti8_1.text = a
            self.ti8_1.bind(on_text_validate = self.ti8_1_action)
            f.close()
            gl2.add_widget(self.ti8_1)
            gl2.add_widget(Label(text='Предоплата букинг'))
            cb1 = CheckBox()
            f = open('cb8_1.txt', 'a+')
            f.close()
            f = open('cb8_1.txt','r')
            a = f.read()
            cb1.bind(active=on_checkbox_active_1)
            cb1.bind(disabled=on_checkbox_active_1)
            if a == 'true':
                cb1.trigger_action()
            f.close()
            gl2.add_widget(cb1)
            gl2.add_widget(Label(text='Предоплата:'))
            f = open('predopl8.txt', 'a+')
            f.close()
            f = open('predopl8.txt', 'r')
            a = f.read()
            self.ti8_2 = TextInput(multiline=False)
            self.ti8_2.text = a
            self.ti8_2.bind(on_text_validate=self.ti8_2_action)
            gl2.add_widget(self.ti8_2)
            f.close()
            gl2.add_widget(Label(text='Собака'))
            f = open('cb8_2.txt', 'a+')
            f.close()
            f = open('cb8_2.txt', 'r')
            a = f.read()
            cb2 = CheckBox()
            cb2.bind(active=on_checkbox_active_2)
            cb2.bind(disabled=on_checkbox_active_2)
            if a == 'true':
                cb2.trigger_action()
            f.close()
            gl2.add_widget(cb2)
            gl2.add_widget(Label(text='Ранний заезд'))
            f = open('cb8_3.txt', 'a+')
            f.close()
            f = open('cb8_3.txt', 'r')
            a = f.read()
            cb3 = CheckBox()
            cb3.bind(active=on_checkbox_active_3)
            cb3.bind(disabled=on_checkbox_active_3)
            if a == 'true':
                cb3.trigger_action()
            f.close()
            gl2.add_widget(cb3)
            gl2.add_widget(Label(text='Поздний выезд'))
            f = open('cb8_4.txt', 'a+')
            f.close()
            f = open('cb8_4.txt', 'r')
            a = f.read()
            cb4 = CheckBox()
            cb4.bind(active=on_checkbox_active_4)
            cb4.bind(disabled=on_checkbox_active_4)
            if a == 'true':
                cb4.trigger_action()
            f.close()
            gl2.add_widget(cb4)
            gl2.add_widget(Label(text='Доп. кровать'))
            f = open('cb8_5.txt', 'a+')
            f.close()
            f = open('cb8_5.txt', 'r')
            a = f.read()
            cb5 = CheckBox()
            cb5.bind(active=on_checkbox_active_5)
            cb5.bind(disabled=on_checkbox_active_5)
            if a == 'true':
                cb5.trigger_action()
            f.close()
            gl2.add_widget(cb5)
            gl2.add_widget(Label(text='Выходные'))
            f = open('cb8_6.txt', 'a+')
            f.close()
            f = open('cb8_6.txt', 'r')
            a = f.read()
            cb6 = CheckBox()
            cb6.bind(active=on_checkbox_active_6)
            cb6.bind(disabled=on_checkbox_active_6)
            if a == 'true':
                cb6.trigger_action()
            f.close()
            gl2.add_widget(cb6)

            #dropdown
            self.dd1 = DropDown()
            self.lblnazvanie = Label(text ='')
            mainbutton = Button(text='Меню')
            mainbutton.bind(on_release=self.dd1.open)
            self.dd1.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
            self.dd1.bind(on_select=lambda instance, x: setattr(self.lblnazvanie,'text', x))
            f = open('menu.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n=n+1
            for i in range(0,n,2):
                btn = Button(text=s[i], size_hint_y=None, height=35)
                btn.bind(on_release=lambda btn: self.dd1.select(btn.text))
                self.dd1.add_widget(btn)
            f.close()

            blo2.add_widget(gl2)
            gl3 = GridLayout(cols=2, size_hint=(1, .5), row_force_default=True, row_default_height=35)
            gl3.add_widget(mainbutton)
            btn8 = Button(text='Добавить в счет',on_press = self.dobavitvschet8)

            gl3.add_widget(btn8)
            blo2.add_widget(gl3)
            th2.content = blo2
            th3 = TabbedPanelHeader(text = 'Счет')


            #счет

            bxl1 = BoxLayout(orientation = 'vertical')
            scrl1 = ScrollView(size_hint=(1, .95))
            self.gl13 = GridLayout(cols=2, size_hint = (1,1), row_force_default=True,size_hint_y=None, row_default_height=40, spacing = 1)

            self.gl13.bind(minimum_height=self.gl13.setter('height'))
            scrl1.add_widget(self.gl13)
            bxl1.add_widget(scrl1)
            bxl2 = BoxLayout(orientation = 'horizontal', size_hint=(1, .05))
            bxl2.add_widget(Label(text = 'Итог :'))
            self.txtbx8 = TextInput(text=str(self.itog8)+' руб', multiline = False, halign = 'center')
            bxl2.add_widget(self.txtbx8)
            btn = Button(text = 'Обновить', on_press = self.obnovit8)
            bxl2.add_widget(btn)
            bxl1.add_widget(bxl2)
            th3.content = bxl1
            f = open('chet8.txt','a+')
            f.close()
            f = open('chet8.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n = n + 1
            for i in range(0,n,2):
                self.gl13.add_widget(Label(text=s[i]))
                self.gl13.add_widget(Label(text=s[i+1] + ' руб'))
                if self.itogbool8:
                    self.itog8 = self.itog8 + int(s[i+1])
            f.close()
            self.itogbool8 = False
            self.txtbx8.text = str(self.itog8) + ' руб'

            self.tb8.add_widget(th1)
            self.tb8.add_widget(th2)
            self.tb8.add_widget(th3)
        if not Bool:
            self.general.add_widget(self.tb8)
            Bool = True
        else:
            self.general.remove_widget(self.general.children[0])
            self.general.add_widget(self.tb8)

    def btn9(self, instance):
        global Bool

        def on_checkbox_active_1(checkbox, value):
            f = open('cb9_1.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_2(checkbox, value):
            f = open('cb9_2.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_3(checkbox, value):
            f = open('cb9_3.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_4(checkbox, value):
            f = open('cb9_4.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_5(checkbox, value):
            f = open('cb9_5.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_6(checkbox, value):
            f = open('cb9_6.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()


        global Bool1
        if not Bool1:
            self.tb9 = TabbedPanel()
            self.tb9.do_default_tab = False

        #Заезды

            th1 = TabbedPanelHeader(text = 'Заезды')
            blo1 = BoxLayout(orientation='vertical')
            gl1 = GridLayout(cols = 1, size_hint = (1,1), row_force_default=True, row_default_height=35)
            bl0 = BoxLayout()
            bl0.add_widget(Label(text='С'))
            self.zaezdTI9_1_1 = TextInput(text='', multiline=False)
            self.zaezdTI9_1_1.bind(on_text_validate=self.zaezdTIA9_1_1)
            f = open('zaezdTI9_1_1.txt', 'a+')
            f.close()
            f = open('zaezdTI9_1_1.txt', 'r')
            a = f.read()
            self.zaezdTI9_1_1.text = a
            f.close()
            bl0.add_widget(self.zaezdTI9_1_1)
            bl0.add_widget(Label(text='по'))
            self.zaezdTI9_1_2 = TextInput(text='', multiline=False)
            self.zaezdTI9_1_2.bind(on_text_validate=self.zaezdTIA9_1_2)
            f = open('zaezdTI9_1_2.txt', 'a+')
            f.close()
            f = open('zaezdTI9_1_2.txt', 'r')
            a = f.read()
            self.zaezdTI9_1_2.text = a
            f.close()
            bl0.add_widget(self.zaezdTI9_1_2)
            bl0.add_widget(Label(text='ФИО:'))
            self.zaezdTI9_1_3 = TextInput(text='', multiline=False)
            self.zaezdTI9_1_3.bind(on_text_validate=self.zaezdTIA9_1_3)
            f = open('zaezdTI9_1_3.txt', 'a+')
            f.close()
            f = open('zaezdTI9_1_3.txt', 'r')
            a = f.read()
            self.zaezdTI9_1_3.text = a
            f.close()
            bl0.add_widget(self.zaezdTI9_1_3)
            gl1.add_widget(bl0)

            bl1 = BoxLayout()
            bl1.add_widget(Label(text='С'))
            self.zaezdTI9_2_1 = TextInput(text='', multiline=False)
            self.zaezdTI9_2_1.bind(on_text_validate=self.zaezdTIA9_2_1)
            f = open('zaezdTI9_2_1.txt', 'a+')
            f.close()
            f = open('zaezdTI9_2_1.txt', 'r')
            a = f.read()
            self.zaezdTI9_2_1.text = a
            f.close()
            bl1.add_widget(self.zaezdTI9_2_1)
            bl1.add_widget(Label(text='по'))
            self.zaezdTI9_2_2 = TextInput(text='', multiline=False)
            self.zaezdTI9_2_2.bind(on_text_validate=self.zaezdTIA9_2_2)
            f = open('zaezdTI9_2_2.txt', 'a+')
            f.close()
            f = open('zaezdTI9_2_2.txt', 'r')
            a = f.read()
            self.zaezdTI9_2_2.text = a
            f.close()
            bl1.add_widget(self.zaezdTI9_2_2)
            bl1.add_widget(Label(text='ФИО:'))
            self.zaezdTI9_2_3 = TextInput(text='', multiline=False)
            self.zaezdTI9_2_3.bind(on_text_validate=self.zaezdTIA9_2_3)
            f = open('zaezdTI9_2_3.txt', 'a+')
            f.close()
            f = open('zaezdTI9_2_3.txt', 'r')
            a = f.read()
            self.zaezdTI9_2_3.text = a
            f.close()
            bl1.add_widget(self.zaezdTI9_2_3)
            gl1.add_widget(bl1)

            bl2 = BoxLayout()
            bl2.add_widget(Label(text='С'))
            self.zaezdTI9_3_1 = TextInput(text='', multiline=False)
            self.zaezdTI9_3_1.bind(on_text_validate=self.zaezdTIA9_3_1)
            f = open('zaezdTI9_3_1.txt', 'a+')
            f.close()
            f = open('zaezdTI9_3_1.txt', 'r')
            a = f.read()
            self.zaezdTI9_3_1.text = a
            f.close()
            bl2.add_widget(self.zaezdTI9_3_1)
            bl2.add_widget(Label(text='по'))
            self.zaezdTI9_3_2 = TextInput(text='', multiline=False)
            self.zaezdTI9_3_2.bind(on_text_validate=self.zaezdTIA9_3_2)
            f = open('zaezdTI9_3_2.txt', 'a+')
            f.close()
            f = open('zaezdTI9_3_2.txt', 'r')
            a = f.read()
            self.zaezdTI9_3_2.text = a
            f.close()
            bl2.add_widget(self.zaezdTI9_3_2)
            bl2.add_widget(Label(text='ФИО:'))
            self.zaezdTI9_3_3 = TextInput(text='', multiline=False)
            self.zaezdTI9_3_3.bind(on_text_validate=self.zaezdTIA9_3_3)
            f = open('zaezdTI9_3_3.txt', 'a+')
            f.close()
            f = open('zaezdTI9_3_3.txt', 'r')
            a = f.read()
            self.zaezdTI9_3_3.text = a
            f.close()
            bl2.add_widget(self.zaezdTI9_3_3)
            gl1.add_widget(bl2)

            th1.content = gl1

            #Сведения
            th2 = TabbedPanelHeader(text = 'Сведения')
            blo2=BoxLayout(orientation = 'vertical')
            gl2 = GridLayout(cols=4, size_hint=(1, .2), row_force_default=True, row_default_height=35)

            gl2.add_widget(Label(text = 'Паспорт:'))
            f = open("pas9.txt", 'a+')
            f.close()
            f = open("pas9.txt", 'r')
            a = f.read()
            self.ti9_1 = TextInput(multiline=False)
            self.ti9_1.text = a
            self.ti9_1.bind(on_text_validate = self.ti9_1_action)
            f.close()
            gl2.add_widget(self.ti9_1)
            gl2.add_widget(Label(text='Предоплата букинг'))
            cb1 = CheckBox()
            f = open('cb9_1.txt', 'a+')
            f.close()
            f = open('cb9_1.txt','r')
            a = f.read()
            cb1.bind(active=on_checkbox_active_1)
            cb1.bind(disabled=on_checkbox_active_1)
            if a == 'true':
                cb1.trigger_action()
            f.close()
            gl2.add_widget(cb1)
            gl2.add_widget(Label(text='Предоплата:'))
            f = open('predopl9.txt', 'a+')
            f.close()
            f = open('predopl9.txt', 'r')
            a = f.read()
            self.ti9_2 = TextInput(multiline=False)
            self.ti9_2.text = a
            self.ti9_2.bind(on_text_validate=self.ti9_2_action)
            gl2.add_widget(self.ti9_2)
            f.close()
            gl2.add_widget(Label(text='Собака'))
            f = open('cb9_2.txt', 'a+')
            f.close()
            f = open('cb9_2.txt', 'r')
            a = f.read()
            cb2 = CheckBox()
            cb2.bind(active=on_checkbox_active_2)
            cb2.bind(disabled=on_checkbox_active_2)
            if a == 'true':
                cb2.trigger_action()
            f.close()
            gl2.add_widget(cb2)
            gl2.add_widget(Label(text='Ранний заезд'))
            f = open('cb9_3.txt', 'a+')
            f.close()
            f = open('cb9_3.txt', 'r')
            a = f.read()
            cb3 = CheckBox()
            cb3.bind(active=on_checkbox_active_3)
            cb3.bind(disabled=on_checkbox_active_3)
            if a == 'true':
                cb3.trigger_action()
            f.close()
            gl2.add_widget(cb3)
            gl2.add_widget(Label(text='Поздний выезд'))
            f = open('cb9_4.txt', 'a+')
            f.close()
            f = open('cb9_4.txt', 'r')
            a = f.read()
            cb4 = CheckBox()
            cb4.bind(active=on_checkbox_active_4)
            cb4.bind(disabled=on_checkbox_active_4)
            if a == 'true':
                cb4.trigger_action()
            f.close()
            gl2.add_widget(cb4)
            gl2.add_widget(Label(text='Доп. кровать'))
            f = open('cb9_5.txt', 'a+')
            f.close()
            f = open('cb9_5.txt', 'r')
            a = f.read()
            cb5 = CheckBox()
            cb5.bind(active=on_checkbox_active_5)
            cb5.bind(disabled=on_checkbox_active_5)
            if a == 'true':
                cb5.trigger_action()
            f.close()
            gl2.add_widget(cb5)
            gl2.add_widget(Label(text='Выходные'))
            f = open('cb9_6.txt', 'a+')
            f.close()
            f = open('cb9_6.txt', 'r')
            a = f.read()
            cb6 = CheckBox()
            cb6.bind(active=on_checkbox_active_6)
            cb6.bind(disabled=on_checkbox_active_6)
            if a == 'true':
                cb6.trigger_action()
            f.close()
            gl2.add_widget(cb6)

            #dropdown
            self.dd1 = DropDown()
            self.lblnazvanie = Label(text ='')
            mainbutton = Button(text='Меню')
            mainbutton.bind(on_release=self.dd1.open)
            self.dd1.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
            self.dd1.bind(on_select=lambda instance, x: setattr(self.lblnazvanie,'text', x))
            f = open('menu.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n=n+1
            for i in range(0,n,2):
                btn = Button(text=s[i], size_hint_y=None, height=35)
                btn.bind(on_release=lambda btn: self.dd1.select(btn.text))
                self.dd1.add_widget(btn)
            f.close()

            blo2.add_widget(gl2)
            gl3 = GridLayout(cols=2, size_hint=(1, .5), row_force_default=True, row_default_height=35)
            gl3.add_widget(mainbutton)
            btn8 = Button(text='Добавить в счет',on_press = self.dobavitvschet9)

            gl3.add_widget(btn8)
            blo2.add_widget(gl3)
            th2.content = blo2
            th3 = TabbedPanelHeader(text = 'Счет')


            #счет

            bxl1 = BoxLayout(orientation = 'vertical')
            scrl1 = ScrollView(size_hint=(1, .95))
            self.gl14 = GridLayout(cols=2, size_hint = (1,1), row_force_default=True,size_hint_y=None, row_default_height=40, spacing = 1)

            self.gl14.bind(minimum_height=self.gl14.setter('height'))
            scrl1.add_widget(self.gl14)
            bxl1.add_widget(scrl1)
            bxl2 = BoxLayout(orientation = 'horizontal', size_hint=(1, .05))
            bxl2.add_widget(Label(text = 'Итог :'))
            self.txtbx9 = TextInput(text=str(self.itog9)+' руб', multiline = False, halign = 'center')
            bxl2.add_widget(self.txtbx9)
            btn = Button(text = 'Обновить', on_press = self.obnovit9)
            bxl2.add_widget(btn)
            bxl1.add_widget(bxl2)
            th3.content = bxl1
            f = open('chet9.txt','a+')
            f.close()
            f = open('chet9.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n = n + 1
            for i in range(0,n,2):
                self.gl14.add_widget(Label(text=s[i]))
                self.gl14.add_widget(Label(text=s[i+1] + ' руб'))
                if self.itogbool9:
                    self.itog9 = self.itog9 + int(s[i+1])
            f.close()
            self.itogbool9 = False
            self.txtbx9.text = str(self.itog8) + ' руб'

            self.tb9.add_widget(th1)
            self.tb9.add_widget(th2)
            self.tb9.add_widget(th3)
        if not Bool:
            self.general.add_widget(self.tb9)
            Bool = True
        else:
            self.general.remove_widget(self.general.children[0])
            self.general.add_widget(self.tb9)

    def btn10(self, instance):
        global Bool

        def on_checkbox_active_1(checkbox, value):
            f = open('cb10_1.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_2(checkbox, value):
            f = open('cb10_2.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_3(checkbox, value):
            f = open('cb10_3.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_4(checkbox, value):
            f = open('cb10_4.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_5(checkbox, value):
            f = open('cb10_5.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_6(checkbox, value):
            f = open('cb10_6.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()


        global Bool1
        if not Bool1:
            self.tb10 = TabbedPanel()
            self.tb10.do_default_tab = False

        #Заезды

            th1 = TabbedPanelHeader(text = 'Заезды')
            blo1 = BoxLayout(orientation='vertical')
            gl1 = GridLayout(cols = 1, size_hint = (1,1), row_force_default=True, row_default_height=35)
            bl0 = BoxLayout()
            bl0.add_widget(Label(text='С'))
            self.zaezdTI10_1_1 = TextInput(text='', multiline=False)
            self.zaezdTI10_1_1.bind(on_text_validate=self.zaezdTIA10_1_1)
            f = open('zaezdTI10_1_1.txt', 'a+')
            f.close()
            f = open('zaezdTI10_1_1.txt', 'r')
            a = f.read()
            self.zaezdTI10_1_1.text = a
            f.close()
            bl0.add_widget(self.zaezdTI10_1_1)
            bl0.add_widget(Label(text='по'))
            self.zaezdTI10_1_2 = TextInput(text='', multiline=False)
            self.zaezdTI10_1_2.bind(on_text_validate=self.zaezdTIA10_1_2)
            f = open('zaezdTI10_1_2.txt', 'a+')
            f.close()
            f = open('zaezdTI10_1_2.txt', 'r')
            a = f.read()
            self.zaezdTI10_1_2.text = a
            f.close()
            bl0.add_widget(self.zaezdTI10_1_2)
            bl0.add_widget(Label(text='ФИО:'))
            self.zaezdTI10_1_3 = TextInput(text='', multiline=False)
            self.zaezdTI10_1_3.bind(on_text_validate=self.zaezdTIA10_1_3)
            f = open('zaezdTI10_1_3.txt', 'a+')
            f.close()
            f = open('zaezdTI10_1_3.txt', 'r')
            a = f.read()
            self.zaezdTI10_1_3.text = a
            f.close()
            bl0.add_widget(self.zaezdTI10_1_3)
            gl1.add_widget(bl0)

            bl1 = BoxLayout()
            bl1.add_widget(Label(text='С'))
            self.zaezdTI10_2_1 = TextInput(text='', multiline=False)
            self.zaezdTI10_2_1.bind(on_text_validate=self.zaezdTIA10_2_1)
            f = open('zaezdTI10_2_1.txt', 'a+')
            f.close()
            f = open('zaezdTI10_2_1.txt', 'r')
            a = f.read()
            self.zaezdTI10_2_1.text = a
            f.close()
            bl1.add_widget(self.zaezdTI10_2_1)
            bl1.add_widget(Label(text='по'))
            self.zaezdTI10_2_2 = TextInput(text='', multiline=False)
            self.zaezdTI10_2_2.bind(on_text_validate=self.zaezdTIA10_2_2)
            f = open('zaezdTI10_2_2.txt', 'a+')
            f.close()
            f = open('zaezdTI10_2_2.txt', 'r')
            a = f.read()
            self.zaezdTI10_2_2.text = a
            f.close()
            bl1.add_widget(self.zaezdTI10_2_2)
            bl1.add_widget(Label(text='ФИО:'))
            self.zaezdTI10_2_3 = TextInput(text='', multiline=False)
            self.zaezdTI10_2_3.bind(on_text_validate=self.zaezdTIA10_2_3)
            f = open('zaezdTI10_2_3.txt', 'a+')
            f.close()
            f = open('zaezdTI10_2_3.txt', 'r')
            a = f.read()
            self.zaezdTI10_2_3.text = a
            f.close()
            bl1.add_widget(self.zaezdTI10_2_3)
            gl1.add_widget(bl1)

            bl2 = BoxLayout()
            bl2.add_widget(Label(text='С'))
            self.zaezdTI10_3_1 = TextInput(text='', multiline=False)
            self.zaezdTI10_3_1.bind(on_text_validate=self.zaezdTIA10_3_1)
            f = open('zaezdTI10_3_1.txt', 'a+')
            f.close()
            f = open('zaezdTI10_3_1.txt', 'r')
            a = f.read()
            self.zaezdTI10_3_1.text = a
            f.close()
            bl2.add_widget(self.zaezdTI10_3_1)
            bl2.add_widget(Label(text='по'))
            self.zaezdTI10_3_2 = TextInput(text='', multiline=False)
            self.zaezdTI10_3_2.bind(on_text_validate=self.zaezdTIA10_3_2)
            f = open('zaezdTI10_3_2.txt', 'a+')
            f.close()
            f = open('zaezdTI10_3_2.txt', 'r')
            a = f.read()
            self.zaezdTI10_3_2.text = a
            f.close()
            bl2.add_widget(self.zaezdTI10_3_2)
            bl2.add_widget(Label(text='ФИО:'))
            self.zaezdTI10_3_3 = TextInput(text='', multiline=False)
            self.zaezdTI10_3_3.bind(on_text_validate=self.zaezdTIA10_3_3)
            f = open('zaezdTI10_3_3.txt', 'a+')
            f.close()
            f = open('zaezdTI10_3_3.txt', 'r')
            a = f.read()
            self.zaezdTI10_3_3.text = a
            f.close()
            bl2.add_widget(self.zaezdTI10_3_3)
            gl1.add_widget(bl2)

            th1.content = gl1

            #Сведения
            th2 = TabbedPanelHeader(text = 'Сведения')
            blo2=BoxLayout(orientation = 'vertical')
            gl2 = GridLayout(cols=4, size_hint=(1, .2), row_force_default=True, row_default_height=35)

            gl2.add_widget(Label(text = 'Паспорт:'))
            f = open("pas10.txt", 'a+')
            f.close()
            f = open("pas10.txt", 'r')
            a = f.read()
            self.ti10_1 = TextInput(multiline=False)
            self.ti10_1.text = a
            self.ti10_1.bind(on_text_validate = self.ti10_1_action)
            f.close()
            gl2.add_widget(self.ti10_1)
            gl2.add_widget(Label(text='Предоплата букинг'))
            cb1 = CheckBox()
            f = open('cb10_1.txt', 'a+')
            f.close()
            f = open('cb10_1.txt','r')
            a = f.read()
            cb1.bind(active=on_checkbox_active_1)
            cb1.bind(disabled=on_checkbox_active_1)
            if a == 'true':
                cb1.trigger_action()
            f.close()
            gl2.add_widget(cb1)
            gl2.add_widget(Label(text='Предоплата:'))
            f = open('predopl10.txt', 'a+')
            f.close()
            f = open('predopl10.txt', 'r')
            a = f.read()
            self.ti10_2 = TextInput(multiline=False)
            self.ti10_2.text = a
            self.ti10_2.bind(on_text_validate=self.ti10_2_action)
            gl2.add_widget(self.ti10_2)
            f.close()
            gl2.add_widget(Label(text='Собака'))
            f = open('cb10_2.txt', 'a+')
            f.close()
            f = open('cb10_2.txt', 'r')
            a = f.read()
            cb2 = CheckBox()
            cb2.bind(active=on_checkbox_active_2)
            cb2.bind(disabled=on_checkbox_active_2)
            if a == 'true':
                cb2.trigger_action()
            f.close()
            gl2.add_widget(cb2)
            gl2.add_widget(Label(text='Ранний заезд'))
            f = open('cb10_3.txt', 'a+')
            f.close()
            f = open('cb10_3.txt', 'r')
            a = f.read()
            cb3 = CheckBox()
            cb3.bind(active=on_checkbox_active_3)
            cb3.bind(disabled=on_checkbox_active_3)
            if a == 'true':
                cb3.trigger_action()
            f.close()
            gl2.add_widget(cb3)
            gl2.add_widget(Label(text='Поздний выезд'))
            f = open('cb10_4.txt', 'a+')
            f.close()
            f = open('cb10_4.txt', 'r')
            a = f.read()
            cb4 = CheckBox()
            cb4.bind(active=on_checkbox_active_4)
            cb4.bind(disabled=on_checkbox_active_4)
            if a == 'true':
                cb4.trigger_action()
            f.close()
            gl2.add_widget(cb4)
            gl2.add_widget(Label(text='Доп. кровать'))
            f = open('cb10_5.txt', 'a+')
            f.close()
            f = open('cb10_5.txt', 'r')
            a = f.read()
            cb5 = CheckBox()
            cb5.bind(active=on_checkbox_active_5)
            cb5.bind(disabled=on_checkbox_active_5)
            if a == 'true':
                cb5.trigger_action()
            f.close()
            gl2.add_widget(cb5)
            gl2.add_widget(Label(text='Выходные'))
            f = open('cb10_6.txt', 'a+')
            f.close()
            f = open('cb10_6.txt', 'r')
            a = f.read()
            cb6 = CheckBox()
            cb6.bind(active=on_checkbox_active_6)
            cb6.bind(disabled=on_checkbox_active_6)
            if a == 'true':
                cb6.trigger_action()
            f.close()
            gl2.add_widget(cb6)

            #dropdown
            self.dd1 = DropDown()
            self.lblnazvanie = Label(text ='')
            mainbutton = Button(text='Меню')
            mainbutton.bind(on_release=self.dd1.open)
            self.dd1.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
            self.dd1.bind(on_select=lambda instance, x: setattr(self.lblnazvanie,'text', x))
            f = open('menu.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n=n+1
            for i in range(0,n,2):
                btn = Button(text=s[i], size_hint_y=None, height=35)
                btn.bind(on_release=lambda btn: self.dd1.select(btn.text))
                self.dd1.add_widget(btn)
            f.close()

            blo2.add_widget(gl2)
            gl3 = GridLayout(cols=2, size_hint=(1, .5), row_force_default=True, row_default_height=35)
            gl3.add_widget(mainbutton)
            btn8 = Button(text='Добавить в счет',on_press = self.dobavitvschet10)

            gl3.add_widget(btn8)
            blo2.add_widget(gl3)
            th2.content = blo2
            th3 = TabbedPanelHeader(text = 'Счет')


            #счет

            bxl1 = BoxLayout(orientation = 'vertical')
            scrl1 = ScrollView(size_hint=(1, .95))
            self.gl15 = GridLayout(cols=2, size_hint = (1,1), row_force_default=True,size_hint_y=None, row_default_height=40, spacing = 1)

            self.gl15.bind(minimum_height=self.gl15.setter('height'))
            scrl1.add_widget(self.gl15)
            bxl1.add_widget(scrl1)
            bxl2 = BoxLayout(orientation = 'horizontal', size_hint=(1, .05))
            bxl2.add_widget(Label(text = 'Итог :'))
            self.txtbx10 = TextInput(text=str(self.itog10)+' руб', multiline = False, halign = 'center')
            bxl2.add_widget(self.txtbx10)
            btn = Button(text='Обновить', on_press=self.obnovit10)
            bxl2.add_widget(btn)
            bxl1.add_widget(bxl2)
            th3.content = bxl1
            f = open('chet10.txt', 'a+')
            f.close()
            f = open('chet10.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n = n + 1
            for i in range(0,n,2):
                self.gl15.add_widget(Label(text=s[i]))
                self.gl15.add_widget(Label(text=s[i+1] + ' руб'))
                if self.itogbool10:
                    self.itog10 = self.itog10 + int(s[i+1])
            f.close()
            self.itogbool10 = False
            self.txtbx10.text = str(self.itog10) + ' руб'

            self.tb10.add_widget(th1)
            self.tb10.add_widget(th2)
            self.tb10.add_widget(th3)
        if not Bool:
            self.general.add_widget(self.tb10)
            Bool = True
        else:
            self.general.remove_widget(self.general.children[0])
            self.general.add_widget(self.tb10)

    def btn11(self, instance):
        global Bool

        def on_checkbox_active_1(checkbox, value):
            f = open('cb11_1.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_2(checkbox, value):
            f = open('cb11_2.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_3(checkbox, value):
            f = open('cb11_3.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_4(checkbox, value):
            f = open('cb11_4.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_5(checkbox, value):
            f = open('cb11_5.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_6(checkbox, value):
            f = open('cb11_6.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()


        global Bool1
        if not Bool1:
            self.tb11 = TabbedPanel()
            self.tb11.do_default_tab = False

        #Заезды

            th1 = TabbedPanelHeader(text = 'Заезды')
            blo1 = BoxLayout(orientation='vertical')
            gl1 = GridLayout(cols = 1, size_hint = (1,1), row_force_default=True, row_default_height=35)
            bl0 = BoxLayout()
            bl0.add_widget(Label(text='С'))
            self.zaezdTI11_1_1 = TextInput(text='', multiline=False)
            self.zaezdTI11_1_1.bind(on_text_validate=self.zaezdTIA11_1_1)
            f = open('zaezdTI11_1_1.txt', 'a+')
            f.close()
            f = open('zaezdTI11_1_1.txt', 'r')
            a = f.read()
            self.zaezdTI11_1_1.text = a
            f.close()
            bl0.add_widget(self.zaezdTI11_1_1)
            bl0.add_widget(Label(text='по'))
            self.zaezdTI11_1_2 = TextInput(text='', multiline=False)
            self.zaezdTI11_1_2.bind(on_text_validate=self.zaezdTIA11_1_2)
            f = open('zaezdTI11_1_2.txt', 'a+')
            f.close()
            f = open('zaezdTI11_1_2.txt', 'r')
            a = f.read()
            self.zaezdTI11_1_2.text = a
            f.close()
            bl0.add_widget(self.zaezdTI11_1_2)
            bl0.add_widget(Label(text='ФИО:'))
            self.zaezdTI11_1_3 = TextInput(text='', multiline=False)
            self.zaezdTI11_1_3.bind(on_text_validate=self.zaezdTIA11_1_3)
            f = open('zaezdTI11_1_3.txt', 'a+')
            f.close()
            f = open('zaezdTI11_1_3.txt', 'r')
            a = f.read()
            self.zaezdTI11_1_3.text = a
            f.close()
            bl0.add_widget(self.zaezdTI11_1_3)
            gl1.add_widget(bl0)

            bl1 = BoxLayout()
            bl1.add_widget(Label(text='С'))
            self.zaezdTI11_2_1 = TextInput(text='', multiline=False)
            self.zaezdTI11_2_1.bind(on_text_validate=self.zaezdTIA11_2_1)
            f = open('zaezdTI11_2_1.txt', 'a+')
            f.close()
            f = open('zaezdTI11_2_1.txt', 'r')
            a = f.read()
            self.zaezdTI11_2_1.text = a
            f.close()
            bl1.add_widget(self.zaezdTI11_2_1)
            bl1.add_widget(Label(text='по'))
            self.zaezdTI11_2_2 = TextInput(text='', multiline=False)
            self.zaezdTI11_2_2.bind(on_text_validate=self.zaezdTIA11_2_2)
            f = open('zaezdTI11_2_2.txt', 'a+')
            f.close()
            f = open('zaezdTI11_2_2.txt', 'r')
            a = f.read()
            self.zaezdTI11_2_2.text = a
            f.close()
            bl1.add_widget(self.zaezdTI11_2_2)
            bl1.add_widget(Label(text='ФИО:'))
            self.zaezdTI11_2_3 = TextInput(text='', multiline=False)
            self.zaezdTI11_2_3.bind(on_text_validate=self.zaezdTIA11_2_3)
            f = open('zaezdTI11_2_3.txt', 'a+')
            f.close()
            f = open('zaezdTI11_2_3.txt', 'r')
            a = f.read()
            self.zaezdTI11_2_3.text = a
            f.close()
            bl1.add_widget(self.zaezdTI11_2_3)
            gl1.add_widget(bl1)

            bl2 = BoxLayout()
            bl2.add_widget(Label(text='С'))
            self.zaezdTI11_3_1 = TextInput(text='', multiline=False)
            self.zaezdTI11_3_1.bind(on_text_validate=self.zaezdTIA11_3_1)
            f = open('zaezdTI11_3_1.txt', 'a+')
            f.close()
            f = open('zaezdTI11_3_1.txt', 'r')
            a = f.read()
            self.zaezdTI11_3_1.text = a
            f.close()
            bl2.add_widget(self.zaezdTI11_3_1)
            bl2.add_widget(Label(text='по'))
            self.zaezdTI11_3_2 = TextInput(text='', multiline=False)
            self.zaezdTI11_3_2.bind(on_text_validate=self.zaezdTIA11_3_2)
            f = open('zaezdTI11_3_2.txt', 'a+')
            f.close()
            f = open('zaezdTI11_3_2.txt', 'r')
            a = f.read()
            self.zaezdTI11_3_2.text = a
            f.close()
            bl2.add_widget(self.zaezdTI11_3_2)
            bl2.add_widget(Label(text='ФИО:'))
            self.zaezdTI11_3_3 = TextInput(text='', multiline=False)
            self.zaezdTI11_3_3.bind(on_text_validate=self.zaezdTIA11_3_3)
            f = open('zaezdTI11_3_3.txt', 'a+')
            f.close()
            f = open('zaezdTI11_3_3.txt', 'r')
            a = f.read()
            self.zaezdTI11_3_3.text = a
            f.close()
            bl2.add_widget(self.zaezdTI11_3_3)
            gl1.add_widget(bl2)

            th1.content = gl1

            #Сведения
            th2 = TabbedPanelHeader(text = 'Сведения')
            blo2=BoxLayout(orientation = 'vertical')
            gl2 = GridLayout(cols=4, size_hint=(1, .2), row_force_default=True, row_default_height=35)

            gl2.add_widget(Label(text = 'Паспорт:'))
            f = open("pas11.txt", 'a+')
            f.close()
            f = open("pas11.txt", 'r')
            a = f.read()
            self.ti11_1 = TextInput(multiline=False)
            self.ti11_1.text = a
            self.ti11_1.bind(on_text_validate = self.ti11_1_action)
            f.close()
            gl2.add_widget(self.ti11_1)
            gl2.add_widget(Label(text='Предоплата букинг'))
            cb1 = CheckBox()
            f = open('cb11_1.txt', 'a+')
            f.close()
            f = open('cb11_1.txt','r')
            a = f.read()
            cb1.bind(active=on_checkbox_active_1)
            cb1.bind(disabled=on_checkbox_active_1)
            if a == 'true':
                cb1.trigger_action()
            f.close()
            gl2.add_widget(cb1)
            gl2.add_widget(Label(text='Предоплата:'))
            f = open('predopl11.txt', 'a+')
            f.close()
            f = open('predopl11.txt', 'r')
            a = f.read()
            self.ti11_2 = TextInput(multiline=False)
            self.ti11_2.text = a
            self.ti11_2.bind(on_text_validate=self.ti11_2_action)
            gl2.add_widget(self.ti11_2)
            f.close()
            gl2.add_widget(Label(text='Собака'))
            f = open('cb11_2.txt', 'a+')
            f.close()
            f = open('cb11_2.txt', 'r')
            a = f.read()
            cb2 = CheckBox()
            cb2.bind(active=on_checkbox_active_2)
            cb2.bind(disabled=on_checkbox_active_2)
            if a == 'true':
                cb2.trigger_action()
            f.close()
            gl2.add_widget(cb2)
            gl2.add_widget(Label(text='Ранний заезд'))
            f = open('cb11_3.txt', 'a+')
            f.close()
            f = open('cb11_3.txt', 'r')
            a = f.read()
            cb3 = CheckBox()
            cb3.bind(active=on_checkbox_active_3)
            cb3.bind(disabled=on_checkbox_active_3)
            if a == 'true':
                cb3.trigger_action()
            f.close()
            gl2.add_widget(cb3)
            gl2.add_widget(Label(text='Поздний выезд'))
            f = open('cb11_4.txt', 'a+')
            f.close()
            f = open('cb11_4.txt', 'r')
            a = f.read()
            cb4 = CheckBox()
            cb4.bind(active=on_checkbox_active_4)
            cb4.bind(disabled=on_checkbox_active_4)
            if a == 'true':
                cb4.trigger_action()
            f.close()
            gl2.add_widget(cb4)
            gl2.add_widget(Label(text='Доп. кровать'))
            f = open('cb11_5.txt', 'a+')
            f.close()
            f = open('cb11_5.txt', 'r')
            a = f.read()
            cb5 = CheckBox()
            cb5.bind(active=on_checkbox_active_5)
            cb5.bind(disabled=on_checkbox_active_5)
            if a == 'true':
                cb5.trigger_action()
            f.close()
            gl2.add_widget(cb5)
            gl2.add_widget(Label(text='Выходные'))
            f = open('cb11_6.txt', 'a+')
            f.close()
            f = open('cb11_6.txt', 'r')
            a = f.read()
            cb6 = CheckBox()
            cb6.bind(active=on_checkbox_active_6)
            cb6.bind(disabled=on_checkbox_active_6)
            if a == 'true':
                cb6.trigger_action()
            f.close()
            gl2.add_widget(cb6)

            #dropdown
            self.dd1 = DropDown()
            self.lblnazvanie = Label(text ='')
            mainbutton = Button(text='Меню')
            mainbutton.bind(on_release=self.dd1.open)
            self.dd1.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
            self.dd1.bind(on_select=lambda instance, x: setattr(self.lblnazvanie,'text', x))
            f = open('menu.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n=n+1
            for i in range(0,n,2):
                btn = Button(text=s[i], size_hint_y=None, height=35)
                btn.bind(on_release=lambda btn: self.dd1.select(btn.text))
                self.dd1.add_widget(btn)
            f.close()

            blo2.add_widget(gl2)
            gl3 = GridLayout(cols=2, size_hint=(1, .5), row_force_default=True, row_default_height=35)
            gl3.add_widget(mainbutton)
            btn8 = Button(text='Добавить в счет',on_press = self.dobavitvschet11)

            gl3.add_widget(btn8)
            blo2.add_widget(gl3)
            th2.content = blo2
            th3 = TabbedPanelHeader(text = 'Счет')


            #счет

            bxl1 = BoxLayout(orientation = 'vertical')
            scrl1 = ScrollView(size_hint=(1, .95))
            self.gl16 = GridLayout(cols=2, size_hint = (1,1), row_force_default=True,size_hint_y=None, row_default_height=40, spacing = 1)

            self.gl16.bind(minimum_height=self.gl16.setter('height'))
            scrl1.add_widget(self.gl16)
            bxl1.add_widget(scrl1)
            bxl2 = BoxLayout(orientation = 'horizontal', size_hint=(1, .05))
            bxl2.add_widget(Label(text = 'Итог :'))
            self.txtbx11 = TextInput(text=str(self.itog11)+' руб', multiline = False, halign = 'center')
            bxl2.add_widget(self.txtbx11)
            btn = Button(text='Обновить', on_press=self.obnovit11)
            bxl2.add_widget(btn)
            bxl1.add_widget(bxl2)
            th3.content = bxl1
            f = open('chet11.txt', 'a+')
            f.close()
            f = open('chet11.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n = n + 1
            for i in range(0,n,2):
                self.gl16.add_widget(Label(text=s[i]))
                self.gl16.add_widget(Label(text=s[i+1] + ' руб'))
                if self.itogbool11:
                    self.itog11 = self.itog11 + int(s[i+1])
            f.close()
            self.itogbool11 = False
            self.txtbx11.text = str(self.itog11) + ' руб'

            self.tb11.add_widget(th1)
            self.tb11.add_widget(th2)
            self.tb11.add_widget(th3)
        if not Bool:
            self.general.add_widget(self.tb11)
            Bool = True
        else:
            self.general.remove_widget(self.general.children[0])
            self.general.add_widget(self.tb11)

    def btn12(self, instance):
        global Bool

        def on_checkbox_active_1(checkbox, value):
            f = open('cb12_1.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_2(checkbox, value):
            f = open('cb12_2.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_3(checkbox, value):
            f = open('cb12_3.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_4(checkbox, value):
            f = open('cb12_4.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_5(checkbox, value):
            f = open('cb12_5.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_6(checkbox, value):
            f = open('cb12_6.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()


        global Bool1
        if not Bool1:
            self.tb12 = TabbedPanel()
            self.tb12.do_default_tab = False

        #Заезды

            th1 = TabbedPanelHeader(text = 'Заезды')
            blo1 = BoxLayout(orientation='vertical')
            gl1 = GridLayout(cols = 1, size_hint = (1,1), row_force_default=True, row_default_height=35)
            bl0 = BoxLayout()
            bl0.add_widget(Label(text='С'))
            self.zaezdTI12_1_1 = TextInput(text='', multiline=False)
            self.zaezdTI12_1_1.bind(on_text_validate=self.zaezdTIA12_1_1)
            f = open('zaezdTI12_1_1.txt', 'a+')
            f.close()
            f = open('zaezdTI12_1_1.txt', 'r')
            a = f.read()
            self.zaezdTI12_1_1.text = a
            f.close()
            bl0.add_widget(self.zaezdTI12_1_1)
            bl0.add_widget(Label(text='по'))
            self.zaezdTI12_1_2 = TextInput(text='', multiline=False)
            self.zaezdTI12_1_2.bind(on_text_validate=self.zaezdTIA12_1_2)
            f = open('zaezdTI12_1_2.txt', 'a+')
            f.close()
            f = open('zaezdTI12_1_2.txt', 'r')
            a = f.read()
            self.zaezdTI12_1_2.text = a
            f.close()
            bl0.add_widget(self.zaezdTI12_1_2)
            bl0.add_widget(Label(text='ФИО:'))
            self.zaezdTI12_1_3 = TextInput(text='', multiline=False)
            self.zaezdTI12_1_3.bind(on_text_validate=self.zaezdTIA12_1_3)
            f = open('zaezdTI12_1_3.txt', 'a+')
            f.close()
            f = open('zaezdTI12_1_3.txt', 'r')
            a = f.read()
            self.zaezdTI12_1_3.text = a
            f.close()
            bl0.add_widget(self.zaezdTI12_1_3)
            gl1.add_widget(bl0)

            bl1 = BoxLayout()
            bl1.add_widget(Label(text='С'))
            self.zaezdTI12_2_1 = TextInput(text='', multiline=False)
            self.zaezdTI12_2_1.bind(on_text_validate=self.zaezdTIA12_2_1)
            f = open('zaezdTI12_2_1.txt', 'a+')
            f.close()
            f = open('zaezdTI12_2_1.txt', 'r')
            a = f.read()
            self.zaezdTI12_2_1.text = a
            f.close()
            bl1.add_widget(self.zaezdTI12_2_1)
            bl1.add_widget(Label(text='по'))
            self.zaezdTI12_2_2 = TextInput(text='', multiline=False)
            self.zaezdTI12_2_2.bind(on_text_validate=self.zaezdTIA12_2_2)
            f = open('zaezdTI12_2_2.txt', 'a+')
            f.close()
            f = open('zaezdTI12_2_2.txt', 'r')
            a = f.read()
            self.zaezdTI12_2_2.text = a
            f.close()
            bl1.add_widget(self.zaezdTI12_2_2)
            bl1.add_widget(Label(text='ФИО:'))
            self.zaezdTI12_2_3 = TextInput(text='', multiline=False)
            self.zaezdTI12_2_3.bind(on_text_validate=self.zaezdTIA12_2_3)
            f = open('zaezdTI12_2_3.txt', 'a+')
            f.close()
            f = open('zaezdTI12_2_3.txt', 'r')
            a = f.read()
            self.zaezdTI12_2_3.text = a
            f.close()
            bl1.add_widget(self.zaezdTI12_2_3)
            gl1.add_widget(bl1)

            bl2 = BoxLayout()
            bl2.add_widget(Label(text='С'))
            self.zaezdTI12_3_1 = TextInput(text='', multiline=False)
            self.zaezdTI12_3_1.bind(on_text_validate=self.zaezdTIA12_3_1)
            f = open('zaezdTI12_3_1.txt', 'a+')
            f.close()
            f = open('zaezdTI12_3_1.txt', 'r')
            a = f.read()
            self.zaezdTI12_3_1.text = a
            f.close()
            bl2.add_widget(self.zaezdTI12_3_1)
            bl2.add_widget(Label(text='по'))
            self.zaezdTI12_3_2 = TextInput(text='', multiline=False)
            self.zaezdTI12_3_2.bind(on_text_validate=self.zaezdTIA12_3_2)
            f = open('zaezdTI12_3_2.txt', 'a+')
            f.close()
            f = open('zaezdTI12_3_2.txt', 'r')
            a = f.read()
            self.zaezdTI12_3_2.text = a
            f.close()
            bl2.add_widget(self.zaezdTI12_3_2)
            bl2.add_widget(Label(text='ФИО:'))
            self.zaezdTI12_3_3 = TextInput(text='', multiline=False)
            self.zaezdTI12_3_3.bind(on_text_validate=self.zaezdTIA12_3_3)
            f = open('zaezdTI12_3_3.txt', 'a+')
            f.close()
            f = open('zaezdTI12_3_3.txt', 'r')
            a = f.read()
            self.zaezdTI12_3_3.text = a
            f.close()
            bl2.add_widget(self.zaezdTI12_3_3)
            gl1.add_widget(bl2)

            th1.content = gl1

            #Сведения
            th2 = TabbedPanelHeader(text = 'Сведения')
            blo2=BoxLayout(orientation = 'vertical')
            gl2 = GridLayout(cols=4, size_hint=(1, .2), row_force_default=True, row_default_height=35)

            gl2.add_widget(Label(text = 'Паспорт:'))
            f = open("pas12.txt", 'a+')
            f.close()
            f = open("pas12.txt", 'r')
            a = f.read()
            self.ti12_1 = TextInput(multiline=False)
            self.ti12_1.text = a
            self.ti12_1.bind(on_text_validate = self.ti12_1_action)
            f.close()
            gl2.add_widget(self.ti12_1)
            gl2.add_widget(Label(text='Предоплата букинг'))
            cb1 = CheckBox()
            f = open('cb12_1.txt', 'a+')
            f.close()
            f = open('cb12_1.txt','r')
            a = f.read()
            cb1.bind(active=on_checkbox_active_1)
            cb1.bind(disabled=on_checkbox_active_1)
            if a == 'true':
                cb1.trigger_action()
            f.close()
            gl2.add_widget(cb1)
            gl2.add_widget(Label(text='Предоплата:'))
            f = open('predopl12.txt', 'a+')
            f.close()
            f = open('predopl12.txt', 'r')
            a = f.read()
            self.ti12_2 = TextInput(multiline=False)
            self.ti12_2.text = a
            self.ti12_2.bind(on_text_validate=self.ti12_2_action)
            gl2.add_widget(self.ti12_2)
            f.close()
            gl2.add_widget(Label(text='Собака'))
            f = open('cb12_2.txt', 'a+')
            f.close()
            f = open('cb12_2.txt', 'r')
            a = f.read()
            cb2 = CheckBox()
            cb2.bind(active=on_checkbox_active_2)
            cb2.bind(disabled=on_checkbox_active_2)
            if a == 'true':
                cb2.trigger_action()
            f.close()
            gl2.add_widget(cb2)
            gl2.add_widget(Label(text='Ранний заезд'))
            f = open('cb12_3.txt', 'a+')
            f.close()
            f = open('cb12_3.txt', 'r')
            a = f.read()
            cb3 = CheckBox()
            cb3.bind(active=on_checkbox_active_3)
            cb3.bind(disabled=on_checkbox_active_3)
            if a == 'true':
                cb3.trigger_action()
            f.close()
            gl2.add_widget(cb3)
            gl2.add_widget(Label(text='Поздний выезд'))
            f = open('cb12_4.txt', 'a+')
            f.close()
            f = open('cb12_4.txt', 'r')
            a = f.read()
            cb4 = CheckBox()
            cb4.bind(active=on_checkbox_active_4)
            cb4.bind(disabled=on_checkbox_active_4)
            if a == 'true':
                cb4.trigger_action()
            f.close()
            gl2.add_widget(cb4)
            gl2.add_widget(Label(text='Доп. кровать'))
            f = open('cb12_5.txt', 'a+')
            f.close()
            f = open('cb12_5.txt', 'r')
            a = f.read()
            cb5 = CheckBox()
            cb5.bind(active=on_checkbox_active_5)
            cb5.bind(disabled=on_checkbox_active_5)
            if a == 'true':
                cb5.trigger_action()
            f.close()
            gl2.add_widget(cb5)
            gl2.add_widget(Label(text='Выходные'))
            f = open('cb12_6.txt', 'a+')
            f.close()
            f = open('cb12_6.txt', 'r')
            a = f.read()
            cb6 = CheckBox()
            cb6.bind(active=on_checkbox_active_6)
            cb6.bind(disabled=on_checkbox_active_6)
            if a == 'true':
                cb6.trigger_action()
            f.close()
            gl2.add_widget(cb6)

            #dropdown
            self.dd1 = DropDown()
            self.lblnazvanie = Label(text ='')
            mainbutton = Button(text='Меню')
            mainbutton.bind(on_release=self.dd1.open)
            self.dd1.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
            self.dd1.bind(on_select=lambda instance, x: setattr(self.lblnazvanie,'text', x))
            f = open('menu.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n=n+1
            for i in range(0,n,2):
                btn = Button(text=s[i], size_hint_y=None, height=35)
                btn.bind(on_release=lambda btn: self.dd1.select(btn.text))
                self.dd1.add_widget(btn)
            f.close()

            blo2.add_widget(gl2)
            gl3 = GridLayout(cols=2, size_hint=(1, .5), row_force_default=True, row_default_height=35)
            gl3.add_widget(mainbutton)
            btn8 = Button(text='Добавить в счет',on_press = self.dobavitvschet12)

            gl3.add_widget(btn8)
            blo2.add_widget(gl3)
            th2.content = blo2
            th3 = TabbedPanelHeader(text = 'Счет')


            #счет

            bxl1 = BoxLayout(orientation = 'vertical')
            scrl1 = ScrollView(size_hint=(1, .95))
            self.gl17 = GridLayout(cols=2, size_hint = (1,1), row_force_default=True,size_hint_y=None, row_default_height=40, spacing = 1)

            self.gl17.bind(minimum_height=self.gl17.setter('height'))
            scrl1.add_widget(self.gl17)
            bxl1.add_widget(scrl1)
            bxl2 = BoxLayout(orientation = 'horizontal', size_hint=(1, .05))
            bxl2.add_widget(Label(text = 'Итог :'))
            self.txtbx12 = TextInput(text=str(self.itog12)+' руб', multiline = False, halign = 'center')
            bxl2.add_widget(self.txtbx12)
            btn = Button(text='Обновить', on_press=self.obnovit12)
            bxl2.add_widget(btn)
            bxl1.add_widget(bxl2)
            th3.content = bxl1
            f = open('chet12.txt', 'a+')
            f.close()
            f = open('chet12.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n = n + 1
            for i in range(0,n,2):
                self.gl17.add_widget(Label(text=s[i]))
                self.gl17.add_widget(Label(text=s[i+1] + ' руб'))
                if self.itogbool12:
                    self.itog12 = self.itog12 + int(s[i+1])
            f.close()
            self.itogbool12 = False
            self.txtbx12.text = str(self.itog12) + ' руб'

            self.tb12.add_widget(th1)
            self.tb12.add_widget(th2)
            self.tb12.add_widget(th3)
        if not Bool:
            self.general.add_widget(self.tb12)
            Bool = True
        else:
            self.general.remove_widget(self.general.children[0])
            self.general.add_widget(self.tb12)

    def btn13(self, instance):
        global Bool

        def on_checkbox_active_1(checkbox, value):
            f = open('cb13_1.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_2(checkbox, value):
            f = open('cb13_2.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_3(checkbox, value):
            f = open('cb13_3.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_4(checkbox, value):
            f = open('cb13_4.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_5(checkbox, value):
            f = open('cb13_5.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_6(checkbox, value):
            f = open('cb13_6.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()


        global Bool1
        if not Bool1:
            self.tb13 = TabbedPanel()
            self.tb13.do_default_tab = False

        #Заезды

            th1 = TabbedPanelHeader(text = 'Заезды')
            blo1 = BoxLayout(orientation='vertical')
            gl1 = GridLayout(cols = 1, size_hint = (1,1), row_force_default=True, row_default_height=35)
            bl0 = BoxLayout()
            bl0.add_widget(Label(text='С'))
            self.zaezdTI13_1_1 = TextInput(text='', multiline=False)
            self.zaezdTI13_1_1.bind(on_text_validate=self.zaezdTIA13_1_1)
            f = open('zaezdTI13_1_1.txt', 'a+')
            f.close()
            f = open('zaezdTI13_1_1.txt', 'r')
            a = f.read()
            self.zaezdTI13_1_1.text = a
            f.close()
            bl0.add_widget(self.zaezdTI13_1_1)
            bl0.add_widget(Label(text='по'))
            self.zaezdTI13_1_2 = TextInput(text='', multiline=False)
            self.zaezdTI13_1_2.bind(on_text_validate=self.zaezdTIA13_1_2)
            f = open('zaezdTI13_1_2.txt', 'a+')
            f.close()
            f = open('zaezdTI13_1_2.txt', 'r')
            a = f.read()
            self.zaezdTI13_1_2.text = a
            f.close()
            bl0.add_widget(self.zaezdTI13_1_2)
            bl0.add_widget(Label(text='ФИО:'))
            self.zaezdTI13_1_3 = TextInput(text='', multiline=False)
            self.zaezdTI13_1_3.bind(on_text_validate=self.zaezdTIA13_1_3)
            f = open('zaezdTI13_1_3.txt', 'a+')
            f.close()
            f = open('zaezdTI13_1_3.txt', 'r')
            a = f.read()
            self.zaezdTI13_1_3.text = a
            f.close()
            bl0.add_widget(self.zaezdTI13_1_3)
            gl1.add_widget(bl0)

            bl1 = BoxLayout()
            bl1.add_widget(Label(text='С'))
            self.zaezdTI13_2_1 = TextInput(text='', multiline=False)
            self.zaezdTI13_2_1.bind(on_text_validate=self.zaezdTIA13_2_1)
            f = open('zaezdTI13_2_1.txt', 'a+')
            f.close()
            f = open('zaezdTI13_2_1.txt', 'r')
            a = f.read()
            self.zaezdTI13_2_1.text = a
            f.close()
            bl1.add_widget(self.zaezdTI13_2_1)
            bl1.add_widget(Label(text='по'))
            self.zaezdTI13_2_2 = TextInput(text='', multiline=False)
            self.zaezdTI13_2_2.bind(on_text_validate=self.zaezdTIA13_2_2)
            f = open('zaezdTI13_2_2.txt', 'a+')
            f.close()
            f = open('zaezdTI13_2_2.txt', 'r')
            a = f.read()
            self.zaezdTI13_2_2.text = a
            f.close()
            bl1.add_widget(self.zaezdTI13_2_2)
            bl1.add_widget(Label(text='ФИО:'))
            self.zaezdTI13_2_3 = TextInput(text='', multiline=False)
            self.zaezdTI13_2_3.bind(on_text_validate=self.zaezdTIA13_2_3)
            f = open('zaezdTI13_2_3.txt', 'a+')
            f.close()
            f = open('zaezdTI13_2_3.txt', 'r')
            a = f.read()
            self.zaezdTI13_2_3.text = a
            f.close()
            bl1.add_widget(self.zaezdTI13_2_3)
            gl1.add_widget(bl1)

            bl2 = BoxLayout()
            bl2.add_widget(Label(text='С'))
            self.zaezdTI13_3_1 = TextInput(text='', multiline=False)
            self.zaezdTI13_3_1.bind(on_text_validate=self.zaezdTIA13_3_1)
            f = open('zaezdTI13_3_1.txt', 'a+')
            f.close()
            f = open('zaezdTI13_3_1.txt', 'r')
            a = f.read()
            self.zaezdTI13_3_1.text = a
            f.close()
            bl2.add_widget(self.zaezdTI13_3_1)
            bl2.add_widget(Label(text='по'))
            self.zaezdTI13_3_2 = TextInput(text='', multiline=False)
            self.zaezdTI13_3_2.bind(on_text_validate=self.zaezdTIA13_3_2)
            f = open('zaezdTI13_3_2.txt', 'a+')
            f.close()
            f = open('zaezdTI13_3_2.txt', 'r')
            a = f.read()
            self.zaezdTI13_3_2.text = a
            f.close()
            bl2.add_widget(self.zaezdTI13_3_2)
            bl2.add_widget(Label(text='ФИО:'))
            self.zaezdTI13_3_3 = TextInput(text='', multiline=False)
            self.zaezdTI13_3_3.bind(on_text_validate=self.zaezdTIA13_3_3)
            f = open('zaezdTI13_3_3.txt', 'a+')
            f.close()
            f = open('zaezdTI13_3_3.txt', 'r')
            a = f.read()
            self.zaezdTI13_3_3.text = a
            f.close()
            bl2.add_widget(self.zaezdTI13_3_3)
            gl1.add_widget(bl2)

            th1.content = gl1

            #Сведения
            th2 = TabbedPanelHeader(text = 'Сведения')
            blo2=BoxLayout(orientation = 'vertical')
            gl2 = GridLayout(cols=4, size_hint=(1, .2), row_force_default=True, row_default_height=35)

            gl2.add_widget(Label(text = 'Паспорт:'))
            f = open("pas13.txt", 'a+')
            f.close()
            f = open("pas13.txt", 'r')
            a = f.read()
            self.ti13_1 = TextInput(multiline=False)
            self.ti13_1.text = a
            self.ti13_1.bind(on_text_validate = self.ti13_1_action)
            f.close()
            gl2.add_widget(self.ti13_1)
            gl2.add_widget(Label(text='Предоплата букинг'))
            cb1 = CheckBox()
            f = open('cb13_1.txt', 'a+')
            f.close()
            f = open('cb13_1.txt','r')
            a = f.read()
            cb1.bind(active=on_checkbox_active_1)
            cb1.bind(disabled=on_checkbox_active_1)
            if a == 'true':
                cb1.trigger_action()
            f.close()
            gl2.add_widget(cb1)
            gl2.add_widget(Label(text='Предоплата:'))
            f = open('predopl13.txt', 'a+')
            f.close()
            f = open('predopl13.txt', 'r')
            a = f.read()
            self.ti13_2 = TextInput(multiline=False)
            self.ti13_2.text = a
            self.ti13_2.bind(on_text_validate=self.ti13_2_action)
            gl2.add_widget(self.ti13_2)
            f.close()
            gl2.add_widget(Label(text='Собака'))
            f = open('cb13_2.txt', 'a+')
            f.close()
            f = open('cb13_2.txt', 'r')
            a = f.read()
            cb2 = CheckBox()
            cb2.bind(active=on_checkbox_active_2)
            cb2.bind(disabled=on_checkbox_active_2)
            if a == 'true':
                cb2.trigger_action()
            f.close()
            gl2.add_widget(cb2)
            gl2.add_widget(Label(text='Ранний заезд'))
            f = open('cb13_3.txt', 'a+')
            f.close()
            f = open('cb13_3.txt', 'r')
            a = f.read()
            cb3 = CheckBox()
            cb3.bind(active=on_checkbox_active_3)
            cb3.bind(disabled=on_checkbox_active_3)
            if a == 'true':
                cb3.trigger_action()
            f.close()
            gl2.add_widget(cb3)
            gl2.add_widget(Label(text='Поздний выезд'))
            f = open('cb13_4.txt', 'a+')
            f.close()
            f = open('cb13_4.txt', 'r')
            a = f.read()
            cb4 = CheckBox()
            cb4.bind(active=on_checkbox_active_4)
            cb4.bind(disabled=on_checkbox_active_4)
            if a == 'true':
                cb4.trigger_action()
            f.close()
            gl2.add_widget(cb4)
            gl2.add_widget(Label(text='Доп. кровать'))
            f = open('cb13_5.txt', 'a+')
            f.close()
            f = open('cb13_5.txt', 'r')
            a = f.read()
            cb5 = CheckBox()
            cb5.bind(active=on_checkbox_active_5)
            cb5.bind(disabled=on_checkbox_active_5)
            if a == 'true':
                cb5.trigger_action()
            f.close()
            gl2.add_widget(cb5)
            gl2.add_widget(Label(text='Выходные'))
            f = open('cb13_6.txt', 'a+')
            f.close()
            f = open('cb13_6.txt', 'r')
            a = f.read()
            cb6 = CheckBox()
            cb6.bind(active=on_checkbox_active_6)
            cb6.bind(disabled=on_checkbox_active_6)
            if a == 'true':
                cb6.trigger_action()
            f.close()
            gl2.add_widget(cb6)

            #dropdown
            self.dd1 = DropDown()
            self.lblnazvanie = Label(text ='')
            mainbutton = Button(text='Меню')
            mainbutton.bind(on_release=self.dd1.open)
            self.dd1.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
            self.dd1.bind(on_select=lambda instance, x: setattr(self.lblnazvanie,'text', x))
            f = open('menu.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n=n+1
            for i in range(0,n,2):
                btn = Button(text=s[i], size_hint_y=None, height=35)
                btn.bind(on_release=lambda btn: self.dd1.select(btn.text))
                self.dd1.add_widget(btn)
            f.close()

            blo2.add_widget(gl2)
            gl3 = GridLayout(cols=2, size_hint=(1, .5), row_force_default=True, row_default_height=35)
            gl3.add_widget(mainbutton)
            btn8 = Button(text='Добавить в счет',on_press = self.dobavitvschet13)

            gl3.add_widget(btn8)
            blo2.add_widget(gl3)
            th2.content = blo2
            th3 = TabbedPanelHeader(text = 'Счет')


            #счет

            bxl1 = BoxLayout(orientation = 'vertical')
            scrl1 = ScrollView(size_hint=(1, .95))
            self.gl18 = GridLayout(cols=2, size_hint = (1,1), row_force_default=True,size_hint_y=None, row_default_height=40, spacing = 1)

            self.gl18.bind(minimum_height=self.gl18.setter('height'))
            scrl1.add_widget(self.gl18)
            bxl1.add_widget(scrl1)
            bxl2 = BoxLayout(orientation = 'horizontal', size_hint=(1, .05))
            bxl2.add_widget(Label(text = 'Итог :'))
            self.txtbx13 = TextInput(text=str(self.itog13)+' руб', multiline = False, halign = 'center')
            bxl2.add_widget(self.txtbx13)
            btn = Button(text='Обновить', on_press=self.obnovit13)
            bxl2.add_widget(btn)
            bxl1.add_widget(bxl2)
            th3.content = bxl1
            f = open('chet13.txt', 'a+')
            f.close()
            f = open('chet13.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n = n + 1
            for i in range(0,n,2):
                self.gl18.add_widget(Label(text=s[i]))
                self.gl18.add_widget(Label(text=s[i+1] + ' руб'))
                if self.itogbool13:
                    self.itog13 = self.itog13 + int(s[i+1])
            f.close()
            self.itogbool13 = False
            self.txtbx13.text = str(self.itog13) + ' руб'

            self.tb13.add_widget(th1)
            self.tb13.add_widget(th2)
            self.tb13.add_widget(th3)
        if not Bool:
            self.general.add_widget(self.tb13)
            Bool = True
        else:
            self.general.remove_widget(self.general.children[0])
            self.general.add_widget(self.tb13)

    def btn14(self, instance):
        global Bool

        def on_checkbox_active_1(checkbox, value):
            f = open('cb14_1.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_2(checkbox, value):
            f = open('cb14_2.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_3(checkbox, value):
            f = open('cb14_3.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_4(checkbox, value):
            f = open('cb14_4.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_5(checkbox, value):
            f = open('cb14_5.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_6(checkbox, value):
            f = open('cb14_6.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()


        global Bool1
        if not Bool1:
            self.tb14 = TabbedPanel()
            self.tb14.do_default_tab = False

        #Заезды

            th1 = TabbedPanelHeader(text = 'Заезды')
            blo1 = BoxLayout(orientation='vertical')
            gl1 = GridLayout(cols = 1, size_hint = (1,1), row_force_default=True, row_default_height=35)
            bl0 = BoxLayout()
            bl0.add_widget(Label(text='С'))
            self.zaezdTI14_1_1 = TextInput(text='', multiline=False)
            self.zaezdTI14_1_1.bind(on_text_validate=self.zaezdTIA14_1_1)
            f = open('zaezdTI14_1_1.txt', 'a+')
            f.close()
            f = open('zaezdTI14_1_1.txt', 'r')
            a = f.read()
            self.zaezdTI14_1_1.text = a
            f.close()
            bl0.add_widget(self.zaezdTI14_1_1)
            bl0.add_widget(Label(text='по'))
            self.zaezdTI14_1_2 = TextInput(text='', multiline=False)
            self.zaezdTI14_1_2.bind(on_text_validate=self.zaezdTIA14_1_2)
            f = open('zaezdTI14_1_2.txt', 'a+')
            f.close()
            f = open('zaezdTI14_1_2.txt', 'r')
            a = f.read()
            self.zaezdTI14_1_2.text = a
            f.close()
            bl0.add_widget(self.zaezdTI14_1_2)
            bl0.add_widget(Label(text='ФИО:'))
            self.zaezdTI14_1_3 = TextInput(text='', multiline=False)
            self.zaezdTI14_1_3.bind(on_text_validate=self.zaezdTIA14_1_3)
            f = open('zaezdTI14_1_3.txt', 'a+')
            f.close()
            f = open('zaezdTI14_1_3.txt', 'r')
            a = f.read()
            self.zaezdTI14_1_3.text = a
            f.close()
            bl0.add_widget(self.zaezdTI14_1_3)
            gl1.add_widget(bl0)

            bl1 = BoxLayout()
            bl1.add_widget(Label(text='С'))
            self.zaezdTI14_2_1 = TextInput(text='', multiline=False)
            self.zaezdTI14_2_1.bind(on_text_validate=self.zaezdTIA14_2_1)
            f = open('zaezdTI14_2_1.txt', 'a+')
            f.close()
            f = open('zaezdTI14_2_1.txt', 'r')
            a = f.read()
            self.zaezdTI14_2_1.text = a
            f.close()
            bl1.add_widget(self.zaezdTI14_2_1)
            bl1.add_widget(Label(text='по'))
            self.zaezdTI14_2_2 = TextInput(text='', multiline=False)
            self.zaezdTI14_2_2.bind(on_text_validate=self.zaezdTIA14_2_2)
            f = open('zaezdTI14_2_2.txt', 'a+')
            f.close()
            f = open('zaezdTI14_2_2.txt', 'r')
            a = f.read()
            self.zaezdTI14_2_2.text = a
            f.close()
            bl1.add_widget(self.zaezdTI14_2_2)
            bl1.add_widget(Label(text='ФИО:'))
            self.zaezdTI14_2_3 = TextInput(text='', multiline=False)
            self.zaezdTI14_2_3.bind(on_text_validate=self.zaezdTIA14_2_3)
            f = open('zaezdTI14_2_3.txt', 'a+')
            f.close()
            f = open('zaezdTI14_2_3.txt', 'r')
            a = f.read()
            self.zaezdTI14_2_3.text = a
            f.close()
            bl1.add_widget(self.zaezdTI14_2_3)
            gl1.add_widget(bl1)

            bl2 = BoxLayout()
            bl2.add_widget(Label(text='С'))
            self.zaezdTI14_3_1 = TextInput(text='', multiline=False)
            self.zaezdTI14_3_1.bind(on_text_validate=self.zaezdTIA14_3_1)
            f = open('zaezdTI14_3_1.txt', 'a+')
            f.close()
            f = open('zaezdTI14_3_1.txt', 'r')
            a = f.read()
            self.zaezdTI14_3_1.text = a
            f.close()
            bl2.add_widget(self.zaezdTI14_3_1)
            bl2.add_widget(Label(text='по'))
            self.zaezdTI14_3_2 = TextInput(text='', multiline=False)
            self.zaezdTI14_3_2.bind(on_text_validate=self.zaezdTIA14_3_2)
            f = open('zaezdTI14_3_2.txt', 'a+')
            f.close()
            f = open('zaezdTI14_3_2.txt', 'r')
            a = f.read()
            self.zaezdTI14_3_2.text = a
            f.close()
            bl2.add_widget(self.zaezdTI14_3_2)
            bl2.add_widget(Label(text='ФИО:'))
            self.zaezdTI14_3_3 = TextInput(text='', multiline=False)
            self.zaezdTI14_3_3.bind(on_text_validate=self.zaezdTIA14_3_3)
            f = open('zaezdTI14_3_3.txt', 'a+')
            f.close()
            f = open('zaezdTI14_3_3.txt', 'r')
            a = f.read()
            self.zaezdTI14_3_3.text = a
            f.close()
            bl2.add_widget(self.zaezdTI14_3_3)
            gl1.add_widget(bl2)

            th1.content = gl1

            #Сведения
            th2 = TabbedPanelHeader(text = 'Сведения')
            blo2=BoxLayout(orientation = 'vertical')
            gl2 = GridLayout(cols=4, size_hint=(1, .2), row_force_default=True, row_default_height=35)

            gl2.add_widget(Label(text = 'Паспорт:'))
            f = open("pas14.txt", 'a+')
            f.close()
            f = open("pas14.txt", 'r')
            a = f.read()
            self.ti14_1 = TextInput(multiline=False)
            self.ti14_1.text = a
            self.ti14_1.bind(on_text_validate = self.ti14_1_action)
            f.close()
            gl2.add_widget(self.ti14_1)
            gl2.add_widget(Label(text='Предоплата букинг'))
            cb1 = CheckBox()
            f = open('cb14_1.txt', 'a+')
            f.close()
            f = open('cb14_1.txt','r')
            a = f.read()
            cb1.bind(active=on_checkbox_active_1)
            cb1.bind(disabled=on_checkbox_active_1)
            if a == 'true':
                cb1.trigger_action()
            f.close()
            gl2.add_widget(cb1)
            gl2.add_widget(Label(text='Предоплата:'))
            f = open('predopl14.txt', 'a+')
            f.close()
            f = open('predopl14.txt', 'r')
            a = f.read()
            self.ti14_2 = TextInput(multiline=False)
            self.ti14_2.text = a
            self.ti14_2.bind(on_text_validate=self.ti14_2_action)
            gl2.add_widget(self.ti14_2)
            f.close()
            gl2.add_widget(Label(text='Собака'))
            f = open('cb14_2.txt', 'a+')
            f.close()
            f = open('cb14_2.txt', 'r')
            a = f.read()
            cb2 = CheckBox()
            cb2.bind(active=on_checkbox_active_2)
            cb2.bind(disabled=on_checkbox_active_2)
            if a == 'true':
                cb2.trigger_action()
            f.close()
            gl2.add_widget(cb2)
            gl2.add_widget(Label(text='Ранний заезд'))
            f = open('cb14_3.txt', 'a+')
            f.close()
            f = open('cb14_3.txt', 'r')
            a = f.read()
            cb3 = CheckBox()
            cb3.bind(active=on_checkbox_active_3)
            cb3.bind(disabled=on_checkbox_active_3)
            if a == 'true':
                cb3.trigger_action()
            f.close()
            gl2.add_widget(cb3)
            gl2.add_widget(Label(text='Поздний выезд'))
            f = open('cb14_4.txt', 'a+')
            f.close()
            f = open('cb14_4.txt', 'r')
            a = f.read()
            cb4 = CheckBox()
            cb4.bind(active=on_checkbox_active_4)
            cb4.bind(disabled=on_checkbox_active_4)
            if a == 'true':
                cb4.trigger_action()
            f.close()
            gl2.add_widget(cb4)
            gl2.add_widget(Label(text='Доп. кровать'))
            f = open('cb14_5.txt', 'a+')
            f.close()
            f = open('cb14_5.txt', 'r')
            a = f.read()
            cb5 = CheckBox()
            cb5.bind(active=on_checkbox_active_5)
            cb5.bind(disabled=on_checkbox_active_5)
            if a == 'true':
                cb5.trigger_action()
            f.close()
            gl2.add_widget(cb5)
            gl2.add_widget(Label(text='Выходные'))
            f = open('cb14_6.txt', 'a+')
            f.close()
            f = open('cb14_6.txt', 'r')
            a = f.read()
            cb6 = CheckBox()
            cb6.bind(active=on_checkbox_active_6)
            cb6.bind(disabled=on_checkbox_active_6)
            if a == 'true':
                cb6.trigger_action()
            f.close()
            gl2.add_widget(cb6)

            #dropdown
            self.dd1 = DropDown()
            self.lblnazvanie = Label(text ='')
            mainbutton = Button(text='Меню')
            mainbutton.bind(on_release=self.dd1.open)
            self.dd1.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
            self.dd1.bind(on_select=lambda instance, x: setattr(self.lblnazvanie,'text', x))
            f = open('menu.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n=n+1
            for i in range(0,n,2):
                btn = Button(text=s[i], size_hint_y=None, height=35)
                btn.bind(on_release=lambda btn: self.dd1.select(btn.text))
                self.dd1.add_widget(btn)
            f.close()

            blo2.add_widget(gl2)
            gl3 = GridLayout(cols=2, size_hint=(1, .5), row_force_default=True, row_default_height=35)
            gl3.add_widget(mainbutton)
            btn8 = Button(text='Добавить в счет',on_press = self.dobavitvschet14)

            gl3.add_widget(btn8)
            blo2.add_widget(gl3)
            th2.content = blo2
            th3 = TabbedPanelHeader(text = 'Счет')


            #счет

            bxl1 = BoxLayout(orientation = 'vertical')
            scrl1 = ScrollView(size_hint=(1, .95))
            self.gl19 = GridLayout(cols=2, size_hint = (1,1), row_force_default=True,size_hint_y=None, row_default_height=40, spacing = 1)

            self.gl19.bind(minimum_height=self.gl19.setter('height'))
            scrl1.add_widget(self.gl19)
            bxl1.add_widget(scrl1)
            bxl2 = BoxLayout(orientation = 'horizontal', size_hint=(1, .05))
            bxl2.add_widget(Label(text = 'Итог :'))
            self.txtbx14 = TextInput(text=str(self.itog14)+' руб', multiline = False, halign = 'center')
            bxl2.add_widget(self.txtbx14)
            btn = Button(text='Обновить', on_press=self.obnovit14)
            bxl2.add_widget(btn)
            bxl1.add_widget(bxl2)
            th3.content = bxl1
            f = open('chet14.txt', 'a+')
            f.close()
            f = open('chet14.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n = n + 1
            for i in range(0,n,2):
                self.gl19.add_widget(Label(text=s[i]))
                self.gl19.add_widget(Label(text=s[i+1] + ' руб'))
                if self.itogbool14:
                    self.itog14 = self.itog14 + int(s[i+1])
            f.close()
            self.itogbool14 = False
            self.txtbx14.text = str(self.itog14) + ' руб'

            self.tb14.add_widget(th1)
            self.tb14.add_widget(th2)
            self.tb14.add_widget(th3)
        if not Bool:
            self.general.add_widget(self.tb14)
            Bool = True
        else:
            self.general.remove_widget(self.general.children[0])
            self.general.add_widget(self.tb14)

    def btn15(self, instance):
        global Bool

        def on_checkbox_active_1(checkbox, value):
            f = open('cb15_1.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_2(checkbox, value):
            f = open('cb15_2.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_3(checkbox, value):
            f = open('cb15_3.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_4(checkbox, value):
            f = open('cb15_4.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_5(checkbox, value):
            f = open('cb15_5.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_6(checkbox, value):
            f = open('cb15_6.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()


        global Bool1
        if not Bool1:
            self.tb15 = TabbedPanel()
            self.tb15.do_default_tab = False

        #Заезды

            th1 = TabbedPanelHeader(text = 'Заезды')
            blo1 = BoxLayout(orientation='vertical')
            gl1 = GridLayout(cols = 1, size_hint = (1,1), row_force_default=True, row_default_height=35)
            bl0 = BoxLayout()
            bl0.add_widget(Label(text='С'))
            self.zaezdTI15_1_1 = TextInput(text='', multiline=False)
            self.zaezdTI15_1_1.bind(on_text_validate=self.zaezdTIA15_1_1)
            f = open('zaezdTI15_1_1.txt', 'a+')
            f.close()
            f = open('zaezdTI15_1_1.txt', 'r')
            a = f.read()
            self.zaezdTI15_1_1.text = a
            f.close()
            bl0.add_widget(self.zaezdTI15_1_1)
            bl0.add_widget(Label(text='по'))
            self.zaezdTI15_1_2 = TextInput(text='', multiline=False)
            self.zaezdTI15_1_2.bind(on_text_validate=self.zaezdTIA15_1_2)
            f = open('zaezdTI15_1_2.txt', 'a+')
            f.close()
            f = open('zaezdTI15_1_2.txt', 'r')
            a = f.read()
            self.zaezdTI15_1_2.text = a
            f.close()
            bl0.add_widget(self.zaezdTI15_1_2)
            bl0.add_widget(Label(text='ФИО:'))
            self.zaezdTI15_1_3 = TextInput(text='', multiline=False)
            self.zaezdTI15_1_3.bind(on_text_validate=self.zaezdTIA15_1_3)
            f = open('zaezdTI15_1_3.txt', 'a+')
            f.close()
            f = open('zaezdTI15_1_3.txt', 'r')
            a = f.read()
            self.zaezdTI15_1_3.text = a
            f.close()
            bl0.add_widget(self.zaezdTI15_1_3)
            gl1.add_widget(bl0)

            bl1 = BoxLayout()
            bl1.add_widget(Label(text='С'))
            self.zaezdTI15_2_1 = TextInput(text='', multiline=False)
            self.zaezdTI15_2_1.bind(on_text_validate=self.zaezdTIA15_2_1)
            f = open('zaezdTI15_2_1.txt', 'a+')
            f.close()
            f = open('zaezdTI15_2_1.txt', 'r')
            a = f.read()
            self.zaezdTI15_2_1.text = a
            f.close()
            bl1.add_widget(self.zaezdTI15_2_1)
            bl1.add_widget(Label(text='по'))
            self.zaezdTI15_2_2 = TextInput(text='', multiline=False)
            self.zaezdTI15_2_2.bind(on_text_validate=self.zaezdTIA15_2_2)
            f = open('zaezdTI15_2_2.txt', 'a+')
            f.close()
            f = open('zaezdTI15_2_2.txt', 'r')
            a = f.read()
            self.zaezdTI15_2_2.text = a
            f.close()
            bl1.add_widget(self.zaezdTI15_2_2)
            bl1.add_widget(Label(text='ФИО:'))
            self.zaezdTI15_2_3 = TextInput(text='', multiline=False)
            self.zaezdTI15_2_3.bind(on_text_validate=self.zaezdTIA15_2_3)
            f = open('zaezdTI15_2_3.txt', 'a+')
            f.close()
            f = open('zaezdTI15_2_3.txt', 'r')
            a = f.read()
            self.zaezdTI15_2_3.text = a
            f.close()
            bl1.add_widget(self.zaezdTI15_2_3)
            gl1.add_widget(bl1)

            bl2 = BoxLayout()
            bl2.add_widget(Label(text='С'))
            self.zaezdTI15_3_1 = TextInput(text='', multiline=False)
            self.zaezdTI15_3_1.bind(on_text_validate=self.zaezdTIA15_3_1)
            f = open('zaezdTI15_3_1.txt', 'a+')
            f.close()
            f = open('zaezdTI15_3_1.txt', 'r')
            a = f.read()
            self.zaezdTI15_3_1.text = a
            f.close()
            bl2.add_widget(self.zaezdTI15_3_1)
            bl2.add_widget(Label(text='по'))
            self.zaezdTI15_3_2 = TextInput(text='', multiline=False)
            self.zaezdTI15_3_2.bind(on_text_validate=self.zaezdTIA15_3_2)
            f = open('zaezdTI15_3_2.txt', 'a+')
            f.close()
            f = open('zaezdTI15_3_2.txt', 'r')
            a = f.read()
            self.zaezdTI15_3_2.text = a
            f.close()
            bl2.add_widget(self.zaezdTI15_3_2)
            bl2.add_widget(Label(text='ФИО:'))
            self.zaezdTI15_3_3 = TextInput(text='', multiline=False)
            self.zaezdTI15_3_3.bind(on_text_validate=self.zaezdTIA15_3_3)
            f = open('zaezdTI15_3_3.txt', 'a+')
            f.close()
            f = open('zaezdTI15_3_3.txt', 'r')
            a = f.read()
            self.zaezdTI15_3_3.text = a
            f.close()
            bl2.add_widget(self.zaezdTI15_3_3)
            gl1.add_widget(bl2)

            th1.content = gl1

            #Сведения
            th2 = TabbedPanelHeader(text = 'Сведения')
            blo2=BoxLayout(orientation = 'vertical')
            gl2 = GridLayout(cols=4, size_hint=(1, .2), row_force_default=True, row_default_height=35)

            gl2.add_widget(Label(text = 'Паспорт:'))
            f = open("pas15.txt", 'a+')
            f.close()
            f = open("pas15.txt", 'r')
            a = f.read()
            self.ti15_1 = TextInput(multiline=False)
            self.ti15_1.text = a
            self.ti15_1.bind(on_text_validate = self.ti15_1_action)
            f.close()
            gl2.add_widget(self.ti15_1)
            gl2.add_widget(Label(text='Предоплата букинг'))
            cb1 = CheckBox()
            f = open('cb15_1.txt', 'a+')
            f.close()
            f = open('cb15_1.txt','r')
            a = f.read()
            cb1.bind(active=on_checkbox_active_1)
            cb1.bind(disabled=on_checkbox_active_1)
            if a == 'true':
                cb1.trigger_action()
            f.close()
            gl2.add_widget(cb1)
            gl2.add_widget(Label(text='Предоплата:'))
            f = open('predopl15.txt', 'a+')
            f.close()
            f = open('predopl15.txt', 'r')
            a = f.read()
            self.ti15_2 = TextInput(multiline=False)
            self.ti15_2.text = a
            self.ti15_2.bind(on_text_validate=self.ti15_2_action)
            gl2.add_widget(self.ti15_2)
            f.close()
            gl2.add_widget(Label(text='Собака'))
            f = open('cb15_2.txt', 'a+')
            f.close()
            f = open('cb15_2.txt', 'r')
            a = f.read()
            cb2 = CheckBox()
            cb2.bind(active=on_checkbox_active_2)
            cb2.bind(disabled=on_checkbox_active_2)
            if a == 'true':
                cb2.trigger_action()
            f.close()
            gl2.add_widget(cb2)
            gl2.add_widget(Label(text='Ранний заезд'))
            f = open('cb15_3.txt', 'a+')
            f.close()
            f = open('cb15_3.txt', 'r')
            a = f.read()
            cb3 = CheckBox()
            cb3.bind(active=on_checkbox_active_3)
            cb3.bind(disabled=on_checkbox_active_3)
            if a == 'true':
                cb3.trigger_action()
            f.close()
            gl2.add_widget(cb3)
            gl2.add_widget(Label(text='Поздний выезд'))
            f = open('cb15_4.txt', 'a+')
            f.close()
            f = open('cb15_4.txt', 'r')
            a = f.read()
            cb4 = CheckBox()
            cb4.bind(active=on_checkbox_active_4)
            cb4.bind(disabled=on_checkbox_active_4)
            if a == 'true':
                cb4.trigger_action()
            f.close()
            gl2.add_widget(cb4)
            gl2.add_widget(Label(text='Доп. кровать'))
            f = open('cb15_5.txt', 'a+')
            f.close()
            f = open('cb15_5.txt', 'r')
            a = f.read()
            cb5 = CheckBox()
            cb5.bind(active=on_checkbox_active_5)
            cb5.bind(disabled=on_checkbox_active_5)
            if a == 'true':
                cb5.trigger_action()
            f.close()
            gl2.add_widget(cb5)
            gl2.add_widget(Label(text='Выходные'))
            f = open('cb15_6.txt', 'a+')
            f.close()
            f = open('cb15_6.txt', 'r')
            a = f.read()
            cb6 = CheckBox()
            cb6.bind(active=on_checkbox_active_6)
            cb6.bind(disabled=on_checkbox_active_6)
            if a == 'true':
                cb6.trigger_action()
            f.close()
            gl2.add_widget(cb6)

            #dropdown
            self.dd1 = DropDown()
            self.lblnazvanie = Label(text ='')
            mainbutton = Button(text='Меню')
            mainbutton.bind(on_release=self.dd1.open)
            self.dd1.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
            self.dd1.bind(on_select=lambda instance, x: setattr(self.lblnazvanie,'text', x))
            f = open('menu.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n=n+1
            for i in range(0,n,2):
                btn = Button(text=s[i], size_hint_y=None, height=35)
                btn.bind(on_release=lambda btn: self.dd1.select(btn.text))
                self.dd1.add_widget(btn)
            f.close()

            blo2.add_widget(gl2)
            gl3 = GridLayout(cols=2, size_hint=(1, .5), row_force_default=True, row_default_height=35)
            gl3.add_widget(mainbutton)
            btn8 = Button(text='Добавить в счет',on_press = self.dobavitvschet15)

            gl3.add_widget(btn8)
            blo2.add_widget(gl3)
            th2.content = blo2
            th3 = TabbedPanelHeader(text = 'Счет')


            #счет

            bxl1 = BoxLayout(orientation = 'vertical')
            scrl1 = ScrollView(size_hint=(1, .95))
            self.gl20 = GridLayout(cols=2, size_hint = (1,1), row_force_default=True,size_hint_y=None, row_default_height=40, spacing = 1)

            self.gl20.bind(minimum_height=self.gl20.setter('height'))
            scrl1.add_widget(self.gl20)
            bxl1.add_widget(scrl1)
            bxl2 = BoxLayout(orientation = 'horizontal', size_hint=(1, .05))
            bxl2.add_widget(Label(text = 'Итог :'))
            self.txtbx15 = TextInput(text=str(self.itog15)+' руб', multiline = False, halign = 'center')
            bxl2.add_widget(self.txtbx15)
            btn = Button(text='Обновить', on_press=self.obnovit15)
            bxl2.add_widget(btn)
            bxl1.add_widget(bxl2)
            th3.content = bxl1
            f = open('chet15.txt', 'a+')
            f.close()
            f = open('chet15.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n = n + 1
            for i in range(0,n,2):
                self.gl20.add_widget(Label(text=s[i]))
                self.gl20.add_widget(Label(text=s[i+1] + ' руб'))
                if self.itogbool15:
                    self.itog15 = self.itog15 + int(s[i+1])
            f.close()
            self.itogbool15 = False
            self.txtbx15.text = str(self.itog15) + ' руб'

            self.tb15.add_widget(th1)
            self.tb15.add_widget(th2)
            self.tb15.add_widget(th3)
        if not Bool:
            self.general.add_widget(self.tb15)
            Bool = True
        else:
            self.general.remove_widget(self.general.children[0])
            self.general.add_widget(self.tb15)

    def btn16(self, instance):
        global Bool

        def on_checkbox_active_1(checkbox, value):
            f = open('cb16_1.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_2(checkbox, value):
            f = open('cb16_2.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_3(checkbox, value):
            f = open('cb16_3.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_4(checkbox, value):
            f = open('cb16_4.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_5(checkbox, value):
            f = open('cb16_5.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()

        def on_checkbox_active_6(checkbox, value):
            f = open('cb16_6.txt', 'w+')
            if value:
                f.write('true')
            else:
                f.write('false')
            f.close()


        global Bool1
        if not Bool1:
            self.tb16 = TabbedPanel()
            self.tb16.do_default_tab = False

        #Заезды

            th1 = TabbedPanelHeader(text = 'Заезды')
            blo1 = BoxLayout(orientation='vertical')
            gl1 = GridLayout(cols = 1, size_hint = (1,1), row_force_default=True, row_default_height=35)
            bl0 = BoxLayout()
            bl0.add_widget(Label(text='С'))
            self.zaezdTI16_1_1 = TextInput(text='', multiline=False)
            self.zaezdTI16_1_1.bind(on_text_validate=self.zaezdTIA16_1_1)
            f = open('zaezdTI16_1_1.txt', 'a+')
            f.close()
            f = open('zaezdTI16_1_1.txt', 'r')
            a = f.read()
            self.zaezdTI16_1_1.text = a
            f.close()
            bl0.add_widget(self.zaezdTI16_1_1)
            bl0.add_widget(Label(text='по'))
            self.zaezdTI16_1_2 = TextInput(text='', multiline=False)
            self.zaezdTI16_1_2.bind(on_text_validate=self.zaezdTIA16_1_2)
            f = open('zaezdTI16_1_2.txt', 'a+')
            f.close()
            f = open('zaezdTI16_1_2.txt', 'r')
            a = f.read()
            self.zaezdTI16_1_2.text = a
            f.close()
            bl0.add_widget(self.zaezdTI16_1_2)
            bl0.add_widget(Label(text='ФИО:'))
            self.zaezdTI16_1_3 = TextInput(text='', multiline=False)
            self.zaezdTI16_1_3.bind(on_text_validate=self.zaezdTIA16_1_3)
            f = open('zaezdTI16_1_3.txt', 'a+')
            f.close()
            f = open('zaezdTI16_1_3.txt', 'r')
            a = f.read()
            self.zaezdTI16_1_3.text = a
            f.close()
            bl0.add_widget(self.zaezdTI16_1_3)
            gl1.add_widget(bl0)

            bl1 = BoxLayout()
            bl1.add_widget(Label(text='С'))
            self.zaezdTI16_2_1 = TextInput(text='', multiline=False)
            self.zaezdTI16_2_1.bind(on_text_validate=self.zaezdTIA16_2_1)
            f = open('zaezdTI16_2_1.txt', 'a+')
            f.close()
            f = open('zaezdTI16_2_1.txt', 'r')
            a = f.read()
            self.zaezdTI16_2_1.text = a
            f.close()
            bl1.add_widget(self.zaezdTI16_2_1)
            bl1.add_widget(Label(text='по'))
            self.zaezdTI16_2_2 = TextInput(text='', multiline=False)
            self.zaezdTI16_2_2.bind(on_text_validate=self.zaezdTIA16_2_2)
            f = open('zaezdTI16_2_2.txt', 'a+')
            f.close()
            f = open('zaezdTI16_2_2.txt', 'r')
            a = f.read()
            self.zaezdTI16_2_2.text = a
            f.close()
            bl1.add_widget(self.zaezdTI16_2_2)
            bl1.add_widget(Label(text='ФИО:'))
            self.zaezdTI16_2_3 = TextInput(text='', multiline=False)
            self.zaezdTI16_2_3.bind(on_text_validate=self.zaezdTIA16_2_3)
            f = open('zaezdTI16_2_3.txt', 'a+')
            f.close()
            f = open('zaezdTI16_2_3.txt', 'r')
            a = f.read()
            self.zaezdTI16_2_3.text = a
            f.close()
            bl1.add_widget(self.zaezdTI16_2_3)
            gl1.add_widget(bl1)

            bl2 = BoxLayout()
            bl2.add_widget(Label(text='С'))
            self.zaezdTI16_3_1 = TextInput(text='', multiline=False)
            self.zaezdTI16_3_1.bind(on_text_validate=self.zaezdTIA16_3_1)
            f = open('zaezdTI16_3_1.txt', 'a+')
            f.close()
            f = open('zaezdTI16_3_1.txt', 'r')
            a = f.read()
            self.zaezdTI16_3_1.text = a
            f.close()
            bl2.add_widget(self.zaezdTI16_3_1)
            bl2.add_widget(Label(text='по'))
            self.zaezdTI16_3_2 = TextInput(text='', multiline=False)
            self.zaezdTI16_3_2.bind(on_text_validate=self.zaezdTIA16_3_2)
            f = open('zaezdTI16_3_2.txt', 'a+')
            f.close()
            f = open('zaezdTI16_3_2.txt', 'r')
            a = f.read()
            self.zaezdTI16_3_2.text = a
            f.close()
            bl2.add_widget(self.zaezdTI16_3_2)
            bl2.add_widget(Label(text='ФИО:'))
            self.zaezdTI16_3_3 = TextInput(text='', multiline=False)
            self.zaezdTI16_3_3.bind(on_text_validate=self.zaezdTIA16_3_3)
            f = open('zaezdTI16_3_3.txt', 'a+')
            f.close()
            f = open('zaezdTI16_3_3.txt', 'r')
            a = f.read()
            self.zaezdTI16_3_3.text = a
            f.close()
            bl2.add_widget(self.zaezdTI16_3_3)
            gl1.add_widget(bl2)

            th1.content = gl1

            #Сведения
            th2 = TabbedPanelHeader(text = 'Сведения')
            blo2=BoxLayout(orientation = 'vertical')
            gl2 = GridLayout(cols=4, size_hint=(1, .2), row_force_default=True, row_default_height=35)

            gl2.add_widget(Label(text = 'Паспорт:'))
            f = open("pas16.txt", 'a+')
            f.close()
            f = open("pas16.txt", 'r')
            a = f.read()
            self.ti16_1 = TextInput(multiline=False)
            self.ti16_1.text = a
            self.ti16_1.bind(on_text_validate = self.ti16_1_action)
            f.close()
            gl2.add_widget(self.ti16_1)
            gl2.add_widget(Label(text='Предоплата букинг'))
            cb1 = CheckBox()
            f = open('cb16_1.txt', 'a+')
            f.close()
            f = open('cb16_1.txt','r')
            a = f.read()
            cb1.bind(active=on_checkbox_active_1)
            cb1.bind(disabled=on_checkbox_active_1)
            if a == 'true':
                cb1.trigger_action()
            f.close()
            gl2.add_widget(cb1)
            gl2.add_widget(Label(text='Предоплата:'))
            f = open('predopl16.txt', 'a+')
            f.close()
            f = open('predopl16.txt', 'r')
            a = f.read()
            self.ti16_2 = TextInput(multiline=False)
            self.ti16_2.text = a
            self.ti16_2.bind(on_text_validate=self.ti16_2_action)
            gl2.add_widget(self.ti16_2)
            f.close()
            gl2.add_widget(Label(text='Собака'))
            f = open('cb16_2.txt', 'a+')
            f.close()
            f = open('cb16_2.txt', 'r')
            a = f.read()
            cb2 = CheckBox()
            cb2.bind(active=on_checkbox_active_2)
            cb2.bind(disabled=on_checkbox_active_2)
            if a == 'true':
                cb2.trigger_action()
            f.close()
            gl2.add_widget(cb2)
            gl2.add_widget(Label(text='Ранний заезд'))
            f = open('cb16_3.txt', 'a+')
            f.close()
            f = open('cb16_3.txt', 'r')
            a = f.read()
            cb3 = CheckBox()
            cb3.bind(active=on_checkbox_active_3)
            cb3.bind(disabled=on_checkbox_active_3)
            if a == 'true':
                cb3.trigger_action()
            f.close()
            gl2.add_widget(cb3)
            gl2.add_widget(Label(text='Поздний выезд'))
            f = open('cb16_4.txt', 'a+')
            f.close()
            f = open('cb16_4.txt', 'r')
            a = f.read()
            cb4 = CheckBox()
            cb4.bind(active=on_checkbox_active_4)
            cb4.bind(disabled=on_checkbox_active_4)
            if a == 'true':
                cb4.trigger_action()
            f.close()
            gl2.add_widget(cb4)
            gl2.add_widget(Label(text='Доп. кровать'))
            f = open('cb16_5.txt', 'a+')
            f.close()
            f = open('cb16_5.txt', 'r')
            a = f.read()
            cb5 = CheckBox()
            cb5.bind(active=on_checkbox_active_5)
            cb5.bind(disabled=on_checkbox_active_5)
            if a == 'true':
                cb5.trigger_action()
            f.close()
            gl2.add_widget(cb5)
            gl2.add_widget(Label(text='Выходные'))
            f = open('cb16_6.txt', 'a+')
            f.close()
            f = open('cb16_6.txt', 'r')
            a = f.read()
            cb6 = CheckBox()
            cb6.bind(active=on_checkbox_active_6)
            cb6.bind(disabled=on_checkbox_active_6)
            if a == 'true':
                cb6.trigger_action()
            f.close()
            gl2.add_widget(cb6)

            #dropdown
            self.dd1 = DropDown()
            self.lblnazvanie = Label(text ='')
            mainbutton = Button(text='Меню')
            mainbutton.bind(on_release=self.dd1.open)
            self.dd1.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
            self.dd1.bind(on_select=lambda instance, x: setattr(self.lblnazvanie,'text', x))
            f = open('menu.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n=n+1
            for i in range(0,n,2):
                btn = Button(text=s[i], size_hint_y=None, height=35)
                btn.bind(on_release=lambda btn: self.dd1.select(btn.text))
                self.dd1.add_widget(btn)
            f.close()

            blo2.add_widget(gl2)
            gl3 = GridLayout(cols=2, size_hint=(1, .5), row_force_default=True, row_default_height=35)
            gl3.add_widget(mainbutton)
            btn8 = Button(text='Добавить в счет',on_press = self.dobavitvschet16)

            gl3.add_widget(btn8)
            blo2.add_widget(gl3)
            th2.content = blo2
            th3 = TabbedPanelHeader(text = 'Счет')


            #счет

            bxl1 = BoxLayout(orientation = 'vertical')
            scrl1 = ScrollView(size_hint=(1, .95))
            self.gl21 = GridLayout(cols=2, size_hint = (1,1), row_force_default=True,size_hint_y=None, row_default_height=40, spacing = 1)

            self.gl21.bind(minimum_height=self.gl21.setter('height'))
            scrl1.add_widget(self.gl21)
            bxl1.add_widget(scrl1)
            bxl2 = BoxLayout(orientation = 'horizontal', size_hint=(1, .05))
            bxl2.add_widget(Label(text = 'Итог :'))
            self.txtbx16 = TextInput(text=str(self.itog16)+' руб', multiline = False, halign = 'center')
            bxl2.add_widget(self.txtbx16)
            btn = Button(text='Обновить', on_press=self.obnovit16)
            bxl2.add_widget(btn)
            bxl1.add_widget(bxl2)
            th3.content = bxl1
            f = open('chet16.txt', 'a+')
            f.close()
            f = open('chet16.txt','r')
            a = f.read()
            s = a.split()
            n=0
            for word in s:
                n = n + 1
            for i in range(0,n,2):
                self.gl21.add_widget(Label(text=s[i]))
                self.gl21.add_widget(Label(text=s[i+1] + ' руб'))
                if self.itogbool16:
                    self.itog16 = self.itog16 + int(s[i+1])
            f.close()
            self.itogbool16 = False
            self.txtbx16.text = str(self.itog16) + ' руб'

            self.tb16.add_widget(th1)
            self.tb16.add_widget(th2)
            self.tb16.add_widget(th3)
        if not Bool:
            self.general.add_widget(self.tb16)
            Bool = True
        else:
            self.general.remove_widget(self.general.children[0])
            self.general.add_widget(self.tb16)

if __name__ == '__main__':
    app = MyApp()
    app.run()
