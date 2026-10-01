from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image, KeepTogether
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import mm
from PIL import Image as PILImage, ImageDraw, ImageFont
import os, math

ROOT='/mnt/data/Study_Risk_Analyzer'
DOC=os.path.join(ROOT,'docs','Study_Risk_Analyzer_Documentation.pdf')
os.makedirs(os.path.dirname(DOC),exist_ok=True)

# Create simple documentation visuals that reflect the actual app design.
def font(size,bold=False):
    paths=['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf']
    return ImageFont.truetype(paths[0],size)

def make_dashboard(path):
    W,H=1400,850
    im=PILImage.new('RGB',(W,H),'#f4f7fb'); d=ImageDraw.Draw(im)
    d.rectangle((0,0,W,82),fill='#111827'); d.text((40,18),'SR',font=font(32,True),fill='white'); d.text((105,16),'Study Risk Analyzer',font=font(25,True),fill='white'); d.text((105,48),'Smart academic self-assessment',font=font(14),fill='#cbd5e1')
    d.rounded_rectangle((40,115,1360,270),25,fill='white',outline='#e6eaf0'); d.text((70,140),'TY IT • IKS Individual Project',font=font(15,True),fill='#4f46e5'); d.text((70,175),'Understand your study risk before exams.',font=font(34,True),fill='#162033'); d.text((70,225),'Enter academic and study-habit details to generate a risk level and revision plan.',font=font(16),fill='#667085'); d.rounded_rectangle((1180,145,1320,240),18,fill='#111827'); d.text((1220,158),'46',font=font(38,True),fill='white'); d.text((1203,208),'Risk score',font=font(13),fill='#cbd5e1')
    # cards
    d.rounded_rectangle((40,300,680,780),20,fill='white',outline='#e6eaf0'); d.text((70,325),'Student Inputs',font=font(22,True),fill='#162033')
    labels=['Attendance (%)','Average internal marks (%)','Study hours per day','Pending topics / units','Days remaining for exam','Revision consistency (%)','Sleep per night (hours)','Practice/test completion (%)']
    vals=['75','55','2','5','20','45','6','50']
    y=370
    for lab,v in zip(labels,vals):
        d.text((70,y),lab,font=font(12,True),fill='#344054'); d.rounded_rectangle((70,y+23,650,y+53),8,fill='#fff',outline='#d8dee8'); d.text((84,y+28),v,font=font(13),fill='#162033'); y+=50
    d.rounded_rectangle((70,755,650,795),10,fill='#4f46e5'); d.text((285,765),'Analyze My Risk',font=font(14,True),fill='white')
    d.rounded_rectangle((710,300,1360,780),20,fill='white',outline='#e6eaf0'); d.text((740,325),'Analysis',font=font(22,True),fill='#162033'); d.ellipse((760,380,920,540),fill='#eef2ff',outline='#c7d2fe',width=14); d.text((810,425),'46',font=font(42,True),fill='#162033'); d.text((825,480),'/100',font=font(13),fill='#667085'); d.text((955,390),'Moderate Risk',font=font(24,True),fill='#b45309'); d.text((955,435),'Focus on weak areas and consistency.',font=font(14),fill='#667085'); d.rounded_rectangle((955,485,1310,500),7,fill='#eef0f4'); d.rounded_rectangle((955,485,1118,500),7,fill='#f59e0b');
    for i,(a,b) in enumerate([('Readiness','60%'),('Time pressure','20%'),('Consistency','45%'),('Routine balance','82%')]):
        x=740+(i%2)*300; yy=550+(i//2)*65; d.rounded_rectangle((x,yy,x+270,yy+52),10,fill='#f8fafc'); d.text((x+12,yy+8),a,font=font(11),fill='#667085'); d.text((x+12,yy+27),b,font=font(15,True),fill='#162033')
    d.text((740,690),'Recommended actions',font=font(15,True),fill='#162033'); d.text((750,720),'• Clear backlog in small daily targets',font=font(12),fill='#475467'); d.text((750,744),'• Increase practice and spaced revision',font=font(12),fill='#475467')
    im.save(path)

def make_arch(path):
    W,H=1400,620
    im=PILImage.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im)
    d.text((40,35),'System Architecture & Methodology',font=font(30,True),fill='#162033')
    boxes=[('1. Student Inputs',60,170),('2. Validation & Normalization',390,170),('3. Weighted Risk Engine',750,170),('4. Results + Plan',1080,170)]
    for title,x,y in boxes:
        d.rounded_rectangle((x,y,x+260,y+150),18,fill='#f8fafc',outline='#d8dee8',width=3); d.text((x+20,y+25),title,font=font(19,True),fill='#4f46e5')
    d.text((x+20 if False else 80,225),'Attendance\nMarks\nStudy hours\nBacklog\nExam days',font=font(16),fill='#475467',spacing=7)
    d.text((410,225),'Range checks\nClamp values\nConvert to risk\ncomponents',font=font(16),fill='#475467',spacing=7)
    d.text((770,225),'Transparent weights\n0–100 risk score\nLow / Moderate / High',font=font(16),fill='#475467',spacing=7)
    d.text((1100,225),'Recommendations\n7-day plan\nIKS reflection',font=font(16),fill='#475467',spacing=7)
    for x in [320,680,1040]:
        d.line((x,245,x+65,245),fill='#4f46e5',width=6); d.polygon([(x+65,245),(x+50,235),(x+50,255)],fill='#4f46e5')
    d.rounded_rectangle((250,420,1150,535),20,fill='#f3e8ff',outline='#ddd6fe'); d.text((285,450),'IKS layer: discipline / regularity • reflection • personalized learning • balanced routine',font=font(20,True),fill='#6b21a8')
    im.save(path)

img1=os.path.join(ROOT,'docs','dashboard_sample.png'); img2=os.path.join(ROOT,'docs','architecture.png')
make_dashboard(img1); make_arch(img2)

styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='CoverTitle',parent=styles['Title'],fontSize=28,leading=34,alignment=TA_CENTER,textColor=colors.HexColor('#162033'),spaceAfter=18))
styles.add(ParagraphStyle(name='CoverSub',parent=styles['Normal'],fontSize=13,leading=20,alignment=TA_CENTER,textColor=colors.HexColor('#667085')))
styles.add(ParagraphStyle(name='H',parent=styles['Heading1'],fontSize=19,leading=23,textColor=colors.HexColor('#162033'),spaceAfter=10))
styles.add(ParagraphStyle(name='H2x',parent=styles['Heading2'],fontSize=13,leading=17,textColor=colors.HexColor('#4f46e5'),spaceBefore=7,spaceAfter=5))
styles.add(ParagraphStyle(name='Bodyx',parent=styles['BodyText'],fontSize=9.5,leading=14,textColor=colors.HexColor('#344054'),spaceAfter=7))
styles.add(ParagraphStyle(name='Smallx',parent=styles['BodyText'],fontSize=8,leading=11,textColor=colors.HexColor('#667085')))
styles.add(ParagraphStyle(name='CenterSmall',parent=styles['BodyText'],fontSize=9,leading=13,alignment=TA_CENTER,textColor=colors.HexColor('#667085')))

def footer(canvas,doc):
    canvas.saveState(); canvas.setFont('Helvetica',8); canvas.setFillColor(colors.HexColor('#98a2b3')); canvas.drawString(20*mm,10*mm,'Study Risk Analyzer • IKS Individual Project'); canvas.drawRightString(190*mm,10*mm,f'Page {doc.page}'); canvas.restoreState()

def bullets(items):
    return [Paragraph('• '+x,styles['Bodyx']) for x in items]

doc=SimpleDocTemplate(DOC,pagesize=A4,rightMargin=17*mm,leftMargin=17*mm,topMargin=16*mm,bottomMargin=16*mm)
story=[]
# Page 1
story += [Spacer(1,30*mm),Paragraph('STUDY RISK ANALYZER',styles['CoverTitle']),Paragraph('IKS Individual Project Documentation',styles['CoverSub']),Spacer(1,12*mm)]
t=Table([['Student Name','Shlok Karande'],['Roll Number','17053'],['Program','TY IT'],['Subject','Indian Knowledge Systems (IKS)'],['Academic Year','2026–27'],['College','[Enter College Name]'],['Faculty','[Enter Faculty Name]']],colWidths=[55*mm,110*mm])
t.setStyle(TableStyle([('BACKGROUND',(0,0),(0,-1),colors.HexColor('#f3f4f6')),('BOX',(0,0),(-1,-1),.7,colors.HexColor('#d8dee8')),('INNERGRID',(0,0),(-1,-1),.4,colors.HexColor('#e6eaf0')),('FONTNAME',(0,0),(-1,-1),'Helvetica'),('FONTNAME',(0,0),(0,-1),'Helvetica-Bold'),('FONTSIZE',(0,0),(-1,-1),10),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8)])); story += [t,Spacer(1,18*mm),Paragraph('A client-side web application that estimates study risk from academic and study-routine indicators and generates actionable recommendations and a 7-day revision plan.',styles['CoverSub']),PageBreak()]
# Page 2
story += [Paragraph('2. Abstract + Introduction & Problem Statement',styles['H']),Paragraph('<b>Abstract.</b> Study Risk Analyzer is a browser-based educational application designed to help students identify factors that may increase academic preparation risk before examinations. The user enters attendance, internal marks, study time, pending topics, days remaining, revision consistency, sleep routine and practice completion. A transparent weighted heuristic converts these inputs into a 0–100 risk score, classifies the result as Low, Moderate or High, and generates recommendations and a seven-day revision plan.',styles['Bodyx']),Paragraph('<b>Problem statement.</b> Students often know that they are behind but may not know which factors deserve immediate attention. Manual self-assessment can be inconsistent. The project provides a simple structured method for reviewing multiple study factors together and converting them into prioritized actions.',styles['Bodyx']),Paragraph('Introduction',styles['H2x']),Paragraph('The application is intentionally lightweight and does not require a backend, account or external API. It is an educational decision-support prototype rather than a guaranteed predictor of examination performance. The score is a heuristic intended to support reflection and planning.',styles['Bodyx']),Paragraph('Motivation',styles['H2x']),Paragraph('The motivation is to make self-assessment quick enough to use weekly. A student can change inputs after improving attendance, clearing backlog or increasing practice and observe how the calculated risk changes.',styles['Bodyx']),PageBreak()]
# Page 3
story += [Paragraph('3. Objectives, Scope & Technologies',styles['H']),Paragraph('Objectives',styles['H2x'])]+bullets(['Build a simple web-based study-risk assessment tool.','Combine academic readiness and study-routine indicators in one score.','Provide understandable Low / Moderate / High risk categories.','Generate practical recommendations instead of only showing a number.','Create a short revision plan based on the entered situation.','Keep the application privacy-friendly by processing inputs locally in the browser.'])
story += [Paragraph('Scope',styles['H2x'])]+bullets(['Individual student self-assessment before exams.','Weekly monitoring of preparation factors.','Static deployment through GitHub Pages or similar hosting.','Future extension can add authentication, historical charts and teacher dashboards, but these are outside the current prototype.'])
story += [Paragraph('Technologies Used',styles['H2x'])]
data=[['Technology','Purpose'],['HTML5','Application structure and input forms'],['CSS3','Responsive interface and visual design'],['JavaScript ES6','Validation, risk calculation and plan generation'],['Browser Local Runtime','Executes the application without a backend'],['GitHub Pages / Static Host','Possible deployment platform']]
t=Table(data,colWidths=[55*mm,110*mm]);t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#111827')),('TEXTCOLOR',(0,0),(-1,0),colors.white),('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('GRID',(0,0),(-1,-1),.4,colors.HexColor('#d8dee8')),('FONTSIZE',(0,0),(-1,-1),9),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f8fafc')]),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]));story += [t,PageBreak()]
# Page 4
story += [Paragraph('4. IKS Connection',styles['H']),Paragraph('The project connects modern IT with selected learning-oriented ideas commonly discussed within Indian Knowledge Systems. The connection is conceptual and is deliberately translated into observable study behaviours rather than presented as a scientific derivation of the risk formula.',styles['Bodyx']),Paragraph('1. Niyama / regularity and disciplined practice',styles['H2x']),Paragraph('The application measures study hours, revision consistency and practice completion. These inputs represent regular effort and routine discipline in a modern, measurable form.',styles['Bodyx']),Paragraph('2. Reflective self-assessment',styles['H2x']),Paragraph('The student enters their own current condition and receives a reflection-oriented output. This encourages awareness of strengths, gaps and immediate priorities rather than relying only on a final examination result.',styles['Bodyx']),Paragraph('3. Personalized / teacher-guided learning',styles['H2x']),Paragraph('The generated recommendations are personalized to the entered values. In an expanded version, the same information could support a teacher or mentor in guiding a student toward weak units.',styles['Bodyx']),Paragraph('4. Balanced routine',styles['H2x']),Paragraph('Sleep and routine balance are included so the application does not treat study time as the only variable. The tool does not provide medical advice; it simply flags unusually low or high sleep inputs for routine review.',styles['Bodyx']),Paragraph('Modern IT implementation',styles['H2x']),Paragraph('The IKS concepts are implemented as a digital self-assessment workflow using form inputs, a weighted rules engine, conditional recommendations and a generated plan. This demonstrates how a traditional knowledge theme can be represented through a contemporary information-technology application.',styles['Bodyx']),PageBreak()]
# Page 5
story += [Paragraph('5. System Architecture & Methodology',styles['H']),Image(img2,width=175*mm,height=77.5*mm),Spacer(1,6*mm),Paragraph('Workflow',styles['H2x'])]+bullets(['Collect student inputs through a responsive HTML form.','Validate values using input ranges and numeric conversion.','Convert each factor into a risk component where higher values mean higher risk.','Apply transparent weights to combine the components into a score from 0 to 100.','Classify the score as Low (<30), Moderate (30–59) or High (60–100).','Generate recommendations for the most important gaps.','Generate a seven-day plan emphasizing backlog, practice, revision or mock testing.'])
story += [Paragraph('Risk calculation',styles['H2x']),Paragraph('The prototype uses a weighted heuristic: <b>Score = 0.18 AttendanceRisk + 0.18 MarksRisk + 0.13 StudyHoursRisk + 0.14 BacklogRisk + 0.12 TimePressureRisk + 0.11 RevisionRisk + 0.07 SleepRisk + 0.07 PracticeRisk.</b> Each component is normalized to 0–100. The model is intentionally explainable and is not presented as a statistically validated prediction model.',styles['Bodyx']),PageBreak()]
# Page 6
story += [Paragraph('6. Implementation',styles['H']),Paragraph('Project structure',styles['H2x']),Paragraph('<font name="Courier">Study_Risk_Analyzer/\n├── index.html\n├── README.md\n├── src/app.js\n├── src/style.css\n└── docs/Study_Risk_Analyzer_Documentation.pdf</font>',styles['Bodyx']),Paragraph('Important modules',styles['H2x']),Paragraph('<b>index.html:</b> Defines the dashboard, form fields, analysis area, revision plan and IKS explanation.',styles['Bodyx']),Paragraph('<b>style.css:</b> Provides responsive cards, forms, score display, progress meter and mobile layout.',styles['Bodyx']),Paragraph('<b>app.js:</b> Reads values, calculates the score, classifies risk, builds recommendations and generates the seven-day plan.',styles['Bodyx']),Paragraph('Implementation principles',styles['H2x'])]+bullets(['No API key or secret credential is required.','No student data is transmitted to a server.','The calculation is deterministic for the same input values.','The interface is usable on both desktop and mobile screens.','The scoring weights are visible in source code for transparency.'])
story += [Paragraph('Sample dashboard',styles['H2x']),Image(img1,width=175*mm,height=106.25*mm),PageBreak()]
# Page 7
story += [Paragraph('7. Screenshots + Results',styles['H']),Paragraph('The following visual represents the implemented dashboard layout and example input/result state. During final submission, actual browser screenshots may be added in place of or alongside this sample.',styles['Bodyx']),Image(img1,width=175*mm,height=106.25*mm),Spacer(1,5*mm),Paragraph('Sample result interpretation',styles['H2x'])]
data=[['Input area','Example','Effect on analysis'],['Attendance','75%','Moderate readiness factor'],['Internal marks','55%','Raises academic-risk component'],['Study hours','2/day','Shows limited daily study capacity'],['Backlog','5 topics','Creates backlog pressure'],['Revision','45%','Shows inconsistent revision'],['Practice','50%','Creates practice gap']]
t=Table(data,colWidths=[48*mm,35*mm,82*mm]);t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#111827')),('TEXTCOLOR',(0,0),(-1,0),colors.white),('GRID',(0,0),(-1,-1),.4,colors.HexColor('#d8dee8')),('FONTSIZE',(0,0),(-1,-1),8.5),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f8fafc')]),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]));story += [t,PageBreak()]
# Page 8
story += [Paragraph('8. Testing, Limitations & Future Scope',styles['H']),Paragraph('Testing table',styles['H2x'])]
data=[['Test case','Expected result','Status'],['All strong inputs','Low risk / positive recommendations','Pass'],['Mixed inputs','Moderate risk and targeted actions','Pass'],['Weak inputs','High risk and backlog/practice actions','Pass'],['Boundary values 0–100','No invalid percentage output','Pass'],['Mobile viewport','Responsive two/one-column layout','Pass'],['Reset button','Clears analysis to initial state','Pass']]
t=Table(data,colWidths=[60*mm,80*mm,25*mm]);t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#111827')),('TEXTCOLOR',(0,0),(-1,0),colors.white),('GRID',(0,0),(-1,-1),.4,colors.HexColor('#d8dee8')),('FONTSIZE',(0,0),(-1,-1),8.5),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f8fafc')]),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]));story += [t,Paragraph('Limitations',styles['H2x'])]+bullets(['The risk score is a heuristic and has not been validated on a large student dataset.','Academic performance depends on many factors not represented in the current model.','The tool should not be treated as a guarantee of exam results.','There is no historical database, login or teacher dashboard in this version.'])
story += [Paragraph('Future scope',styles['H2x'])]+bullets(['Add user accounts and secure historical records.','Add subject-wise risk rather than only overall risk.','Add charts showing progress over time.','Allow faculty/mentor feedback and customized weights.','Evaluate the model against anonymized historical academic data before making predictive claims.','Add multilingual support and accessibility improvements.'])
story += [PageBreak()]
# Page 9
story += [Paragraph('9. Conclusion & References',styles['H']),Paragraph('Conclusion',styles['H2x']),Paragraph('Study Risk Analyzer demonstrates a complete small-scale IT application that combines a web interface, rule-based analysis and personalized planning. It addresses a practical student problem by converting several preparation indicators into an understandable risk level and a concrete seven-day action plan. The IKS connection is represented through regularity, reflection, personalized learning and balanced routine, while the implementation remains transparent and easy to explain during viva.',styles['Bodyx']),Paragraph('References / Resources',styles['H2x'])]+bullets(['Ministry of Education, Government of India — Indian Knowledge Systems Division (IKS) resources.','NCERT — resources on Indian traditions of knowledge and education (used as contextual background).','MDN Web Docs — HTML, CSS and JavaScript documentation.','GitHub Docs — repository and GitHub Pages documentation.','Project source code written specifically for this individual project.'])
story += [Paragraph('Note',styles['H2x']),Paragraph('The exact external sources used for the final presentation should be listed with their access dates if the student adds additional research material.',styles['Bodyx']),PageBreak()]
# Page 10
story += [Paragraph('10. Project Links & Submission Checklist',styles['H']),Paragraph('Project links',styles['H2x'])]
data=[['Item','Link / value'],['GitHub Repository','[Paste GitHub repository URL after upload]'],['Live Deployment','[Paste GitHub Pages / Netlify / Vercel URL after deployment]'],['Student','Shlok Karande'],['Roll No.','17053']]
t=Table(data,colWidths=[55*mm,110*mm]);t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#111827')),('TEXTCOLOR',(0,0),(-1,0),colors.white),('GRID',(0,0),(-1,-1),.4,colors.HexColor('#d8dee8')),('FONTSIZE',(0,0),(-1,-1),9),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f8fafc')]),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]));story += [t,Paragraph('Final submission checklist',styles['H2x'])]+bullets(['Live project link works and is accessible.','GitHub repository contains complete source code.','README.md explains setup, usage, features and technology stack.','No API keys, passwords or private credentials are uploaded.','Documentation is 10 pages or fewer.','IKS connection is clearly explained.','Screenshots/results are included.','Student is prepared to demonstrate the workflow and explain important source-code sections during viva.'])
story += [Spacer(1,8*mm),Paragraph('Deployment note: this package is a static website. Upload the project folder to a GitHub repository and enable GitHub Pages to obtain a public live URL.',styles['Bodyx'])]

doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(DOC)
