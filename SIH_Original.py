from tkinter import *
from tkinter import messagebox
from fpdf import FPDF
from selenium import webdriver
from time import sleep
from tkinter import filedialog
import speech_recognition as sr
import os
#Recquries pyaudio
lan='en-IN'
def clear():
   c=messagebox.askquestion('Conformation','Do you Want to clear all the fields')
   if c=='yes':
      global entry3,entry0,pn_p_e,p_a_e,pn_w_e,Text1,Text2
      entry3.delete(0,END)
      entry0.delete(0,END)
      pn_p_e.delete(0,END)
      p_a_e.delete(0,END)
      pn_w_e.delete(0,END)
      Text1.delete('1.0',END)
      Text2.delete('1.0',END)
def make_changes():
   lan='en-IN'
   r=sr.Recognizer()
   mic=sr.Microphone()
   #print(sr.Microphone.list_microphone_names())
   with mic as source:
       r.adjust_for_ambient_noise(source)
       print('Listening......')
       audio = r.listen(source)
       text6=r.recognize_google(audio,language=lan)
       text6=text6.split()
       k=0
       while(k<len(text6)):
            if(k!=len(text6)-1 and ((text6[k]=='and' and text6[k+1]=='change') or text6[k]=='change' or text6[k]=='to')):
              text6.remove(text6[k])
              #print(len(text6))
              k=k-1
            k=k+1
       for k in range(len(text6)):
           if(text6[k]=='name'):
               entry3.delete(0,END)
               i=k+1
               while((i!=len(text6)) and (text6[i]!="gender" and text6[i]!="number" and text6[i]!="problem" and text6[i]!="cause" and text6[i]!="medicine" and text6[i]!='phone' and text6[i]!='age' and text6[i]!='weight')):
                 entry3.insert(END,str(text6[i])+" ")
                 i=i+1
           elif(text6[k]=="gender"):
               entry0.delete(0,END)
               entry0.insert(END,str(text6[k+1])+" ")
           elif(text6[k]=="number"):
               pn_p_e.delete(0,END)
               pn_p_e.insert(END,str(text6[k+1])+" ")
           elif (text6[k]=='age'):
               p_a_e.delete(0,END)
               p_a_e.insert(END,str(text6[k+1])+" ")
           elif(text6[k]=='weight'):
               pn_w_e.delete(0,END)
               pn_w_e.insert(END,str(text6[k+1])+" ")
           elif(text6[k]=="problem" or text6[k]=="cause"):
               Text1.delete('1.0',END)
               i=k+1
               while((i!=len(text6)) and (text6[i]!="gender" and text6[i]!="name" and text6[i]!="number" and text6[i]!="medicine" and text6[i]!='phone' and text6[i]!='age' and text6[i]!='weight')):
                 Text1.insert(END,str(text6[i])+" ")
                 i=i+1
           elif(text6[k]=="medicine" or text6[k]=='medication'):
               Text2.delete('1.0',END)
               i=k+1
               medi=[]
               while((i!=len(text6)) and (text6[i]!="gender" and text6[i]!="name" and text6[i]!="problem" and text6[i]!="cause" and text6[i]!="number" and text6[i]!='phone' and text6[i]!='age' and text6[i]!='weight')):
                 medi.append(text6[i])
                 i=i+1
               i=0
               tablets1=[]
               while len(medi)!=0:
                  for j in range(len(medi)):
                     if(medi[j]=='tablet' or medi[j]=='strips' or medi[j]=='strip' or medi[j]=='tablets' or medi[j]=='capsules' or medi[j]=='capsule'):
                       i=j
                       break
                  if i+1<len(medi) and medi[i+1]=='morning':
                     i=i+1
                  if i+1<len(medi) and medi[i+1]=='afternoon':
                     i=i+1
                  if i+1<len(medi) and medi[i+1]=='evening':
                     i=i+1
                  tablets1.append(' '.join(medi[:i+1]))
                  medi=medi[i+1:]
               list12='\n'.join(tablets1)
               Text2.insert(END,list12)
def open_pdf():
   try:
      path_pdf=entry3.get()+'.pdf'
      os.startfile(path_pdf)
   except:
      messagebox.showerror('Error','No prescription Found')
def add_sign():
   global path
   window.filename=filedialog.askopenfilename()
   path=window.filename
   print(path)
   if path!='':
      x=path[(path.rfind('/'))+1:]
      messagebox.showinfo('Information',x+' is selected')
def s_e():
   lan='en-IN'
def s_h():
   lan='hi-IN'
def s_te():
   lan='te-IN'
def s_ta():
   lan='ta-IN'
def s_mal():
   lan='ml-IN'
def s_mar():
   lan='mr-IN'
def s_g():
   lan='gu-IN'
def s_k():
   lan='kn-IN'
def s_b():
   lan='bn-IN'
def s_u():
   lan='ur-IN'
def t_e():
   pass
def t_h():
   pass
def t_te():
   pass
def t_ta():
   pass
def t_mal():
   pass
def t_mar():
   pass
def t_g():
   pass
def t_k():
   pass
def t_b():
   pass
def t_u():
   pass
def speak():
   global lan,p_name,weight,gender,age,p_no,prob,medi,name,problem,list1,entry3,entry0,pn_p_e,p_a_e,pn_w_e,Text1,Text2
   if type(p_no)==type('ram'):
       #messagebox.showinfo('Information','ex')
       c=messagebox.askquestion('Conformation','Do you Want to Create new Prescription')
       if c=='no':
           return
       else:
           sleep(0.5)
           clear()
   p_name=[]
   weight=''
   gender=''
   age=''
   p_no=[]
   prob=[]
   medi=[]
   name=''
   problem=''
   list1=''
   text=['name','Ram','age','20','gender','male','number','1234567891','weight','50','problem','headache','next','blood','cancer','medicine','trfdrs','Dolo 650']
   '''r=sr.Recognizer()
   #r.non_speaking_duration=2.5
   mic=sr.Microphone()
   #print(sr.Microphone.list_microphone_names())
   with mic as source:
       r.adjust_for_ambient_noise(source)
       print('Listening......')
       #r.non_speaking_duration=10
       try:
          audio = r.listen(source)
          #r.non_speaking_duration=1
          text=r.recognize_google(audio,language=lan)
          text=text.split()
          print(text)
       except:
          print('Please say That again')
       k=0'''
   for k in range(len(text)):
      if(text[k]=="name"):
          o=k+1
          while((o!=len(text)) and (text[o]!="gender" and text[o]!="number" and text[o]!="problem" and text[o]!="cause" and text[o]!="medicine" and text[o]!='phone' and text[o]!='age' and text[o]!='weight')):
               p_name.append(text[o])
               o=o+1
      elif(text[k]=="gender"):
               gender=text[k+1]
      elif(text[k]=="number"):
            o=k+1
            #p_no.append(text[k+1])
            while((o!=len(text)) and (text[o]!="gender" and text[o]!="name" and text[o]!="problem" and text[o]!="cause" and text[o]!="medicine" and text[o]!='phone' and text[o]!='age' and text[o]!='weight')):
               p_no.append(text[o])
               o=o+1;
      elif (text[k]=='age'):
          age=text[k+1]
      elif(text[k]=='weight'):
          weight=text[k+1]
      elif(text[k]=="problem" or text[k]=="cause"):
            o=k+1
            while((o!=len(text)) and (text[o]!="gender" and text[o]!="name" and text[o]!="number" and text[o]!="medicine" and text[o]!='phone' and text[o]!='age' and text[o]!='weight')):
               prob.append(text[o])
               o=o+1
      elif(text[k]=="medicine" or text[k]=='medication'):
            o=k+1
            while((o!=len(text)) and (text[o]!="gender" and text[o]!="name" and text[o]!="problem" and text[o]!="cause" and text[o]!="number" and text[o]!='phone' and text[o]!='age' and text[o]!='weight')):
              medi.append(text[o])
              o=o+1
   prob=list(prob)
   name=' '.join(p_name)
   p_no=''.join(p_no)
   problem=' '.join(prob)
   problem='\n'.join(problem.split(' next '))
   #medicine=' '.join(medi)
   i=0
   tablets=[]
   while len(medi)!=0:
       for j in range(len(medi)):
           if(medi[j]=='tablet' or medi[j]=='strips' or medi[j]=='strip' or medi[j]=='tablets' or medi[j]=='capsules' or medi[j]=='capsule'):
               i=j
               break
       #i=text.index('tablets')
       if i+1<len(medi) and medi[i+1]=='morning':
           i=i+1
       if i+1<len(medi) and medi[i+1]=='afternoon':
           i=i+1
       if i+1<len(medi) and medi[i+1]=='evening':
           i=i+1
       tablets.append(' '.join(medi[:i+1]))
       medi=medi[i+1:]
   list1='\n'.join(tablets)
   entry3.insert(END,name)
   entry0.insert(END,gender)
   pn_p_e.insert(END,p_no)
   p_a_e.insert(END,age)
   pn_w_e.insert(END,weight)
   Text1.insert(END,problem)
   Text2.insert(END,list1)
#text=['name','xyz','def','problem','fever','and','cold','phone','number','970','19','26783','age','18','weight','26','medicine','dolo','650','MG','4','tablets','morning','evening','saradon','5','tablets','afternoon']
#print(text)
p_name=[]
weight=''
gender=''
age=''
p_no=[]
prob=[]
medi=[]
name=''
problem=''
list1=''
'''def on_click(event):
    entry.delete(0,END)
    send_b.configure(state='active')
    entry.configure(fg='black')
    entry.unbind('<Button-1>')
def on_focus(event)
#    if entry.get()!='':
    send_b.configure(state='active')'''
'''def user_Q():
    f2=Frame(window,bg='#4dff88',borderwidth=10)
    query=entry.get()
    entry.delete(0,END)
    label=Label(f2,text=query).pack(side='right')
    f2.pack(side=TOP,fill='x')
    f3=Frame(window,borderwidth=10)
    lpic=Label(f3,image=pic).pack(side='left')
    l=Label(f3,text='How can I help you ?').pack(side='left')
    f3.pack(side=TOP,fill='x')
'''
window=Tk()
window.configure(bg='#ff8484')
window.geometry('700x650+200+2')
window.resizable(0,0)
window.title('Prescription')
def get_h():
    global window_h,d_hdw
    def display():
      global window_h,d_hdw
      d_hdw=entry1_h.get()+'$'+text_h.get('1.0',END)
      hd=open('hospital_details.txt','+w')
      hd.write(d_hdw)
      hd.close()
      window_h.destroy()
      messagebox.showinfo("Information","Details are Saved Successfully")
      '''y=open('hospital_details.txt').read()
      print(y)'''
    window_h=Toplevel()
    window_h.title("Enter hospital's details")
    f11=Frame(window_h)
    f11.configure(background='#ff8484')
    L1_h=Label(f11,bg='#ff8484',text="Hospital's Name:",font=("Ariel",14))
    L1_h.pack(side='left')
    entry1_h=Entry(f11,borderwidth=3,width=35)
    entry1_h.pack(side='left')
    f11.pack(fill='x')
    f12=Frame(window_h)
    f12.configure(background='#ff8484')
    L2_h=Label(f12,bg='#ff8484',text="             Address:",font=("Ariel",14))
    L2_h.pack(side='left')
    text_h=Text(f12,borderwidth=3,width=26,height=6)
    text_h.pack(side='left')
    f12.pack(fill='x')
    f13=Frame(window_h)
    f13.configure(background='#ff8484')
    b1_h=Button(f13,text='save',command=display)
    b1_h.pack(side='top')
    f13.pack(fill='x')
    try:
        hdw=open('hospital_details.txt').read().split('$')
        entry1_h.insert(0,hdw[0])
        text_h.insert('1.0',hdw[1])
    except FileNotFoundError:
        pass
    window_h.mainloop()
def get_d():
    global window_d
    def display(EVENT=0):
      global window_d
      x=entry1_h.get()+'$'+entry2_h.get()
      hd=open('doctor_details.txt','+w')
      hd.write(x)
      hd.close()
      window_d.destroy()
      messagebox.showinfo("Information","Details are saved Successfully")
    window_d=Toplevel()
    window_d.title("Enter doctor's details")
    f11=Frame(window_d)
    f11.config(background='#ff8484')
    L1_h=Label(f11,bg='#ff8484',text="doctor's Name:",font=("Ariel",14))
    L1_h.pack(side='left')
    entry1_h=Entry(f11,borderwidth=3,width=35)
    entry1_h.pack(side='left')
    f11.pack(fill='x')
    f12=Frame(window_d)
    f12.config(background='#ff8484')
    L2_h=Label(f12,bg='#ff8484',text="Phone number:",font=("Ariel",14))
    L2_h.pack(side='left')
    entry2_h=Entry(f12,borderwidth=3,width=35)
    entry2_h.bind('<Return>',display)
    entry2_h.pack(side='left')
    f12.pack(fill='x')
    f13=Frame(window_d)
    f13.configure(background='#ff8484')
    b1_h=Button(f13,text='save',command=display)
    b1_h.pack(side='top')
    f13.pack(fill='x')
    try:
        ddw=open('doctor_details.txt').read().split('$')
        entry1_h.insert(0,ddw[0])
        entry2_h.insert(0,ddw[1])
    except FileNotFoundError:
        pass
    window_d.mainloop()
f1=Frame(window)
f1.configure(background='#ff8484')

#L1=Label(f1,bg='#ff8484',text="Doctor's detials:",font=("Ariel",16)).pack(side='left')
#L1.pack(side='left')

#f2.configure(background='#ff8484')
b4=Button(f1,text="Reset Doctor's Details",borderwidth=4,command=get_d).pack(side='right')
wl_4=Label(f1,text="  ",bg='#ff8484').pack(side='right')
b0=Button(f1,text="Reset Hospital's Details",borderwidth=4,command=get_h).pack(side='right')
#L2=Label(f2,bg='#ff8484',text="Name:",font=("Ariel",14))
#L2.pack(side='left')
#entry1=Entry(f2,borderwidth=3,width=35)
#entry1.pack(side='left')
#L3=Label(f2,bg='#ff8484',text="Phone Number:",font=("Ariel",14)).pack(side='left')
#entry2=Entry(f2,borderwidth=3,width=20)
#entry2.insert(END,d_number)
#entry2.pack(side='left')
f1.pack(side=TOP,fill='x')
menubar=Menu(window)
set_speech=Menu(menubar,tearoff=0)
languages=['Bengali','Gujarati','Kannada','Malayalam','Marathi','Tamil','Telugu','Urdu']
set_speech.add_command(label='English',command=s_e)
set_speech.add_command(label='Hindi',command=s_h)
set_speech.add_command(label='Telugu',command=s_te)
set_speech.add_command(label='Tamil',command=s_ta)
set_speech.add_command(label='Kanada',command=s_k)
set_speech.add_command(label='Malayalam',command=s_mal)
set_speech.add_command(label='Marathi',command=s_mar)
set_speech.add_command(label='Bengali',command=s_b)
set_speech.add_command(label='Gujarati',command=s_g)
set_speech.add_command(label='Urdu',command=s_u)
menubar.add_cascade(label='Speech_language',menu=set_speech)
set_text=Menu(menubar,tearoff=0)
set_text.add_command(label='English',command=t_e)
set_text.add_command(label='Hindi',command=t_h)
set_text.add_command(label='Telugu',command=t_te)
set_text.add_command(label='Tamil',command=t_ta)
set_text.add_command(label='Kanada',command=t_k)
set_text.add_command(label='Malayalam',command=t_mal)
set_text.add_command(label='Marathi',command=t_mar)
set_text.add_command(label='Bengali',command=t_b)
set_text.add_command(label='Gujarati',command=t_g)
set_text.add_command(label='Urdu',command=t_u)
menubar.add_cascade(label='Text_language',menu=set_text)
window.config(menu=menubar)
f3=Frame(window)
f3.configure(background='#ff8484')
L4=Label(f3,bg='#ff8484',text="Enter Patient's detials:",font=("Ariel",16)).pack(side='left')
#L1.pack(side='left')
f3.pack(side=TOP,fill='x')
f4=Frame(window)
f4.configure(background='#ff8484')
L5=Label(f4,bg='#ff8484',text="Name:",font=("Ariel",14))
L5.pack(side='left')
entry3=Entry(f4,borderwidth=3,width=38)
entry3.insert(END,name)
entry3.pack(side='left')
L6=Label(f4,bg='#ff8484',text="Gender:             ",font=("Ariel",14)).pack(side='left')
entry0=Entry(f4,borderwidth=3,width=20)
entry0.insert(END,gender)
entry0.pack(side='left')
f4.pack(fill='x')
'''w_f4=Frame(window)
w_f4.config(bg='#ff8484')
w_l_f4=Label(w_f4,text=' ',bg='#ff8484').pack()
w_f4.pack(fill='x')'''
f4_1=Frame(window)
f4_1.config(bg='#ff8484')
pn_p=Label(f4_1,text='Phone Number:    ',font=("Ariel",14),bg='#ff8484').pack(side='left')
pn_p_e=Entry(f4_1,borderwidth=3,width=22)
pn_p_e.pack(side='left')
pn_p_e.insert(0,p_no)
p_a=Label(f4_1,text='      Age:            ',font=("Ariel",14),bg='#ff8484').pack(side='left')
p_a_e=Entry(f4_1,borderwidth=3,width=20)
p_a_e.pack(side='left')
p_a_e.insert(0,age)
f4_1.pack(fill='x')
f4_2=Frame(window)
f4_2.config(bg='#ff8484')
pn_w=Label(f4_2,text='Weight:                 ',font=("Ariel",14),bg='#ff8484').pack(side='left')
pn_w_e=Entry(f4_2,borderwidth=3,width=20)
pn_w_e.pack(side='left')
pn_w_e.insert(0,weight)
f4_2.pack(fill='x')
f5=Frame(window)
f5.configure(background='#ff8484')
L7=Label(f5,bg='#ff8484',text="Problem:",font=("Ariel",16)).pack(side='left')
f5.pack(fill='x')
f6=Frame(window)
f6.configure(background='#ff8484')
Text1=Text(f6,borderwidth=3,height=6,width=62)
Text1.insert(END,problem)
Text1.pack(side='left')
f6.pack(fill='x')
f7=Frame(window)
f7.configure(background='#ff8484')
L8=Label(f7,bg='#ff8484',text="Medication:",font=("Ariel",16)).pack(side='left')
f7.pack(fill='x')
f8=Frame(window)
f8.configure(background='#ff8484')
Text2=Text(f8,borderwidth=3,height=10,width=62)
Text2.insert(END,list1)
Text2.pack(side='left')
f8.pack(fill='x')
f9=Frame(window)
f9.configure(background='#ff8484')
L9=Label(f9,bg='#ff8484').pack()
f9.pack(fill='x')
f10=Frame(window)
f10.configure(background='#ff8484')
b1=Button(f10,text='START',command=speak).pack(side='left')
wl_1=Label(f10,text="  ",bg='#ff8484').pack(side='left')
b2=Button(f10,text='Edit with Speech',command=make_changes).pack(side='left')
wl_2=Label(f10,text="  ",bg='#ff8484').pack(side='left')
b3=Button(f10,text='CLEAR',command=clear).pack(side='left')
l_w=Label(f10,text='   ',bg='#ff8484').pack(side='right')
b4=Button(f10,text='Add Signature',command=add_sign)
b4.pack(side='right')
f10.pack(fill='x')
path=''
def pdf():
  if (entry3.get()=='' or entry0.get()=='' or pn_p_e.get()=='' or p_a_e.get()=='' or pn_w_e.get()=='' or Text1.get('1.0')==''or Text2.get('1.0')==''):
     messagebox.showerror('Error','Please fill all the details')
     return
  global h,d,path
  c=0
  try:
      global h,d
      d=open('doctor_details.txt').read()
      h=open('hospital_details.txt').read()
  except FileNotFoundError:
      c=1
      messagebox.showinfo('Information',"You didn't Fill either Doctor Details or Hospital Details or both. Please fill them by clicking on Reset doctor Details and Reset Hospital details")
  if c==0:
      pdf = FPDF()
      pdf.add_page()
      pdf.set_font("Arial",'B', size = 18)
      h=h.split('$')
      pdf.cell(200, 10, txt =h[0].upper(),ln = 1, align = 'C')
      pdf.set_font('Arial',size=12)
      l=h[1].split('\n')
      for i in l:
          pdf.cell(200,5, txt =i,ln =1, align = 'C')
      pdf.set_font("Arial",size=16)
      d=d.split('$')
      pdf.cell(200,10,txt="Doctor's name:  "+d[0]+'\t\t\t\t\t\t\t\t\t'+"Phone number:  "+d[1],ln=2)
          #pdf.cell(200,10,txt="Phone number:  "+x[1],ln=2)
      pdf.cell(200,10,txt="Pateint's name:  "+entry3.get()+'\t\t\t\t\t\t\t\t\t'+"Gender:  "+entry0.get(),ln=3)
          #pdf.cell(200,10,txt="Gender:  "+entry0.get(),ln=5)
      pdf.cell(200,10,txt="Patient Phone number: "+pn_p_e.get()+'\t\t\t\t\t\t\t\t\t'+"Age: "+p_a_e.get(),ln=1)
      pdf.set_font("Arial",size=16)
      probl=Text1.get('1.0',END).split('\n')
      pdf.cell(200,10,txt="PROBLEM:",ln=1)
      pdf.set_font("Arial",size=12)
      for i in range(0,len(probl)):
          pdf.cell(200,5,txt=str(i+1)+"."+probl[i],ln=1)
      pdf.cell(200,2,txt='',ln=1)
      pdf.set_font("Arial",size=16)
      pdf.cell(200,10,txt="MEDICATION:",ln=6)
      pdf.set_font("Arial",size=12)
      tablets=Text2.get('1.0',END).split('\n')
      for i in range(0,len(tablets)):
          pdf.cell(200,5,txt=str(i+1)+"."+tablets[i],ln=i+7)
      if path=='':
         messagebox.showerror('Error','Add Signature')
      else:
         pdf.image(path)
         try:
            pdf.output(entry3.get()+".pdf")
            messagebox.showinfo('Information','PDF had been saved successfully')
         except OSError:
            messagebox.showerror('Error','PDF not created Due to some error retry by typing Patient full name')
      #pdf.output(entry3.get()+".pdf")
#entry.insert(0,"Enter Your Query Here")
#entry.bind('<Button-1>',on_click)
#entry.bind('<FocusIn>',on_focus)
'''voiceicon=PhotoImage(file='microphone.png')
sendicon=PhotoImage(file='send.png')
send_b=Button(f1,image=sendicon,command=user_Q,state=DISABLED)
send_b.pack(side='left')
speech_b=Button(f1,image=voiceicon)
speech_b.pack(side='left')'''
def send_wapps():
   '''driver = webdriver.Chrome()
   driver.get('https://web.whatsapp.com/')

   name = entry3.get()
   filepath = 'D:\\'+entry3.get()+'.pdf'
   user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
   user.click()

   attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
   attachment_box.click()

   doc_box = driver.find_element_by_xpath(
       '//input[@accept="*"]')
   doc_box.send_keys(filepath)

   sleep(3)

   send_button = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
   send_button.click()'''
   print(entry3.get())
   driver = webdriver.Chrome()
   driver.get('https://web.whatsapp.com/')
   x=input()
   name =entry3.get()
   filepath =os.getcwd()+entry3.get()+'.pdf'
   print(filepath)
   #sleep(7)
   try:
      print('ok')
      sleep(2)
      user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
      user.click()
      print('c')
      #sleep(2)
      attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
      attachment_box.click()
      print('h')
      doc_box = driver.find_element_by_xpath('//input[@accept="*"]')
      print('d')
      doc_box.send_keys(filepath)
      print('harsha')
      sleep(9)
      send_button = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
      print('s')
      send_button.click()
   except:
      driver.set_window_position(0, 0)
      driver.set_window_size(0,0)
      messagebox.showerror('Error','No Contact found with given name')
f21_w=Frame(window)
f21_w.config(bg='#ff8484')
l_f21w=Label(f21_w,text=' ',bg='#ff8484').pack()
f21_w.pack(fill='x')
f21=Frame(window)
f21.configure(background='#ff8484')
b6=Button(f21,text="CREATE PDF",command=pdf)
b6.pack(side='left')
l6_1=Label(f21,text=' ',bg='#ff8484').pack(side='left')
b6_1=Button(f21,text='Open pdf',command=open_pdf)
b6_1.pack(side='left')
l6_1=Label(f21,text=' ',bg='#ff8484').pack(side='left')
b6_2=Button(f21,text='Send pdf via Whatsapp',command=send_wapps)
b6_2.pack(side='left')
f21.pack(fill='x')
window.mainloop()

