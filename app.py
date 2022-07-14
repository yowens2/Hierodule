import streamlit as st
import pandas as pd 
import sweetviz as sv 

from PIL import Image
from streamlit_option_menu import option_menu


### Streamlit Default Menu ###

# i like to personalise my prototypes so this is some code to hide the menu widget from your streamlit app. 
st. set_page_config(layout="wide")

hide_menu = """ <style>
#MainMenu {
    visibility:hidden;
}
layout {
   layout: wide
}
footer{
    visibility:hidden;
}
footer:after{
    content: 'Copyright @ yOwens2';
    display:block;
    position:relative;
    color:tomato;
}

</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)
#import Pyspark and start Session - need to check how this affects performance of the app

### stremalit call back ### 

def callback():
    st.session_state.button_clicked = True



# sweet visuals 
# 
def st_display_sweetviz(report_html,width=1000,height=500):
    report_file = codecs.open(report_html,'r')
    page = report_file.read()
    components.html(page,width=width,height=height,scrolling=True)    


## session state for button press 
if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

def callback():
    #button is clicked
    st.session_state.button_clicked = True



### app start ###

#structure for app menu
# 1=sidebar menu, 2=horizontal menu
struc = 2



def streamlit_menu_test(selection=1, sec_selction=2):
    if selection == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "Data Project", "Contact", "FAQ"],  # required
                #               icons=["house", "book", "envelope", "book", "alert", "heart-fill"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected


    if selection == 2:
        # 2. horizontal menu w/o custom style
        test = option_menu(
            menu_title=None,  # required
            options=["Home", "Data Projects", "FAQ", "Template",
                    "Contact", "AW Family", "Mentions"],  # required
            icons=["house", "tsunami", "question-octagon", "heart-fill", "envelope", "🐧", "👨‍👩‍👧‍👦"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal"
    )

def streamlit_menu(selection=1):
    if selection == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "Data Project", "Contact", "FAQ"],  # required
#               icons=["house", "book", "envelope", "book", "alert", "heart-fill"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected

    if selection == 2:
        # 2. horizontal menu w/o custom style
        selected = option_menu(
            menu_title=None,  # required
            options=[
                     'Information Hub',
                     "Social Board", "FAQ", "V.O.C",],  # required
            icons=["house", "tsunami", "question-octagon","heart-fill", "envelope" , "🐧", "👨‍👩‍👧‍👦", "🧤"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected

selected = streamlit_menu(selection=struc)

if selected == "Information Hub":
    st.markdown(
    "###### [![forthebadge](https://forthebadge.com/images/badges/makes-people-smile.svg)](https://forthebadge.com)") 
    st.subheader("Teamwork Makes The Dream Work")
    dm_columns = st.columns(1)

    for i in range(1,3): # number of rows in your table! = 2
    
        cols = st.columns(2) # number of columns in each row! = 2
    
    # first column of the ith row
    cols[0].subheader("Process")
    cols[0].image('Images\issue.PNG', i, use_column_width=True)
    cols[1].subheader("Insight")
    cols[0].image('Images\Process Flow.PNG', i, use_column_width=True)
    cols[1].image('Images\Insight1.PNG', i, use_column_width=True)
    cols[1].image('Images\Metad data change.PNG', i, use_column_width=True)
#    cols[1].image('row_%i_col_1.jpg' %i, use_column_width=True) 

    st.subheader("Digital hub for Data Analysis")    

    st.markdown("People colect data for data sake, so i thought i would give a go at changing the narrative. 'did it for analytics sake ' 😱🤓🤭👽🐱‍💻")

    st.write("Get in Touch to learn how you can have a light look at automation of understanding a data set for Machine Learning")
    community_mentions = st.columns(2)
    st.sidebar.title("Loving Every Drop")
    st.sidebar.subheader("My Anglian Water Family")
    st.sidebar.subheader("👪👨‍👩‍👦👨‍👩‍👧👨‍👩‍👧‍👦👨‍👩‍👦‍👦👨‍👩‍👧‍👧👨‍👨‍👦👨‍👨‍👧👨‍👨‍👧‍👦👨‍👨‍👦‍👦👨‍👨‍👧‍👧👩‍👩‍👦👩‍👩‍👧👩‍👩‍👧‍👦👩‍👩‍👦‍👦👩‍👩‍👧‍👧👩‍👦👩‍👧👩‍👧‍👦👩‍👦‍👦👩‍👧‍👧👨‍👦👨‍👧👨‍👧‍👦👨‍👦‍👦👨‍👧‍👧")
    with community_mentions[1]:
        st.sidebar.subheader("Community Shout Out 🎙")
        st.sidebar.write("A Massive thank you to the community leads and content creators, i must of gone through the majority of your sits so i could develop this so massive hats of to you all, as a fellow light house keeper. I can relate to the effort put into the amazing content youve provided")

        st.sidebar.subheader("The 6 or is it 4 Degrees of Seperation? 🤯")

        st.sidebar.video("https://www.youtube.com/watch?v=a99ry70CnRs")

        st.sidebar.subheader("Individual Shout Out 🎙")

        st.sidebar.write("They say you are an average of the 5 people you communicate with, Ive been very lucky to be to be 0.04% of these amazing minds, adopting the AW values i hope i can add to this list and when working together i get to humberly live upto the averge of the people in the room 🤜🏿🤛🤛🏻🤛🏼🤛🏽🤛🏾🤛🏿")

        addtional_data_expanders = st.sidebar.expander(
            "My Anglian Water Family - My Inspirations and Thank you 🤗 ", expanded=False)
        
        with addtional_data_expanders:
            st.markdown(
                '''Lucy Hurd \n \n  Louise Oliver \n \n  Claire Harrison \n \n Kacey Dunkley-Gates \n \n Andy Riddel \n \n Caroline Claire \n \n Fay Darbey \n \n  Graham Otter  \n \n Richard Moore \n \n Alaric Parsions \n \n Drew Piearcy \n \n Simon Murphy \n \n Fiona Smith \n \n Mike Wingell \n \n Amy Barlow \n \n Matt Edwards \n \n Chris Steele - Binnies \n \n Paul Hamilition - Binnies \n \n Chloe Ball \n \n Kim Adams \n \n Stephen Howe \n \n Karl Smith \n \n Peter Noonan \n \n Scott Ringham \n \n David Beale \n \n Reece Cooke - AMI \n \n Jaunius Urbonas - AIMI \n \n Rob Shaw - Massive Thank you for listening to me when putting the world to right,\n \n Mark Hedges - Thank you for Believing in me massive respect ♥ \n \n Philip Bradley  - My Brother From another mother, Thank you for all the coaching in understanding pain points in operations, we miss the stories starting with 'When i was on the tools 🤣, and also thank you for being present through my many berevments im sure anglian water is due a water bill with all the tears you probably had on you 😂, and thank you for showing me allyship #TEAM_PANDA \n \n

            ''', unsafe_allow_html=False)

    Data_mate_options = st.radio("What Topic are you insterested in?", {'Data Analysis', 'Data Analysis for M/L', 'Data Driven Story Product', 'Enhanced Excel'}, horizontal=True)  # type: ignore

    st.markdown(" ---")

    if Data_mate_options == "Data Analysis":
        st.markdown("# 🌍The World Of Data🌐")

        st.markdown("#### What Is Analysis?")
        video_columns = st.columns(2)
        video_columns[0].video("https://www.youtube.com/watch?v=rr-KwIjinpM")

        st.markdown("""#### There are four main type of analytics and they are as follows \n \n""") 
        st.markdown("""
            Descriptive Analysis \n \n 
            Descriptive Analysis: usually answers the question “What happened?”. This type of analysis describes or summarizes raw data into something explainable and meaningful. This is mostly used to summarize different aspects of a particular business, describe what’s going on in a particular organization and when it’s required to understand activities at an aggregate level. This relates to describing the past and is useful as it allows us to analyze past behaviors and how they could have an impact in the near future.""")
        st.markdown(
            " Exploritary Data Analysis : https://colab.research.google.com/drive/1mPjwDi_8x_JfMnvUjjM8voHgNPbeoeyD?usp=sharing")
        video_columns[1].markdown("CRISP DM Model : 👇🏻")
        video_columns[1].markdown("I. Business Understanding \n \n  1. Determine business objectives: You should first “thoroughly understand, from a business perspective, what the customer really wants to accomplish. \n \n  2. Assess situation: Determine resources availability, project requirements, assess risks and contingencies, and conduct a cost-benefit analysis. \n \n 3. Determine data mining goals: In addition to defining the business objectives, you should also define what success looks like from a technical data mining perspective. \n \n ")
        video_columns[1].markdown("4. Produce project plan: Select technologies and tools and define detailed plans for each project phase." )

        st.markdown("---")
        st.markdown("""\n \n  
            Diagnostic Analysis \n \n 
            Diagnostic Analytics: examines data to answer the question “Why did it happen?”. This is characterized by various techniques such as Drill-Down, Data Discovery, Data Mining and Correlations. These techniques allow the users to go towards deeper analysis which will result in justifying why certain activities or situations have occurred in an organization.\n \n """)
        st.markdown("---")
        st.markdown("""
            Predictive Analysis\n \n
            Predictive Analysis: answers the question “What is likely to happen?”. This method has the ability to predict what might happen in the future. Therefore, this provides organizations with actionable insights based on the data available. This is used when it’s required to know something about the future or in order to find some missing information which is essential and not available at the moment. A most commonly used technique is Data Mining Algorithms.\n \n """)
        st.markdown("---")
        st.markdown("Prescriptive Analysis \n \n  Prescriptive Analysis: answers the question “What is the best course of action?”. This method allows users to prescribe various possible actions to which as a result guides them towards a solution. This method attempts to quantify the effect of future decisions in order to advise on possible outcomes before the decisions are actually made. ")


    st.sidebar.subheader("Interesting Reads")


    st.sidebar.write(
        " Harvard Business Review | David Waller| 10 Steps to Creating a Data-Driven Culture :  https://hbr.org/2020/02/10-steps-to-creating-a-data-driven-culture")
    st.sidebar.write("IBM | IBM Garage Method : https://www.ibm.com/uk-en/garage?utm_content=SRCWW&p1=Search&p4=43700068004223875&p5=e&gclid=EAIaIQobChMI8oWWos_w-AIVBYBQBh2DnA5IEAAYASAAEgLzJvD_BwE&gclsrc=aw.ds")
    if Data_mate_options == 'Data Analysis for M/L':
        st.info("Please Refer to Sharepoint to Learn More on Data Quality: CARTIE & Information Steward")
        '''📺 : Follow a link for a video on Machine Learning and How to do it 🐱‍💻| https://www.youtube.com/watch?v=0B5eIE_1vpU'''
        ml_cols = st.columns(2)

        ml_cols[0].subheader("Automated  Exploritary Data Analysis with \n ")
        ml_cols[0].header("💻🖱 Sweet visuals 🧬🧾")
        st.markdown( "---")


        ml_cols[1].markdown("Please Use this tool to profile your data and to gain detailed inisghts")
        data_file = ml_cols[1].file_uploader("Upload CSV",type=['csv'])
        if data_file is not None:
            df = pd.read_csv(data_file)
            st.dataframe(df.head(25))
            if st.button("Generate Report"):

                # Normal Workflow
                report = sv.analyze(df)
                report.show_html()
                st_display_sweetviz("SWEETVIZ_REPORT.html")


if selected == "V.O.C":
    st.title(f"You have selected {selected}")
    st.container()
    t1, t2 = st.columns((0.07,1)) 
#   st.title(f"You have selected {selected}")
    st.sidebar.subheader("Citizen Data Engineer")
    cde = st.sidebar.expander("Pathway | Citizen Data Engineering", expanded=False)
    st.sidebar.subheader("Citizen Report Develovper Engineer")
    crd = st.sidebar.expander("Pathway | Citizen Report Developer", expanded=False)

    with cde:
        yowens2_CDE= "My Name is Yavin im an ♒ and on the way to trying tp become The Water Utilities Data Doctor 💧. _WHY_ the name 'The Data Doctor', well i was born and raised in Jamaica, Kingston 😎. Interesting Facts about Jamacia \n The National Bird is called the Doctor Bird,  While exploring my Continious Development personal journey ive always had that parental advice of joining the medical fields but to make the best of both worlds ive have been enabling myself  become _A Doctor of common Data Issues and illnesses 😷, to help data get better  , As i believe 'A JACK of All Trades, But a master of none, is always better than a master of one'_ 👨🏿‍⚕️"
        
        cde.markdown(yowens2_CDE)
        st.image('Images\yavlar.PNG', width = 150, clamp=True, use_column_width=True)

    with crd:
        ramble2= "emporium "
        
        crd.markdown(ramble2)  

    st.markdown("Hi Thank you for reviewing my Professional Review, To help Us communicate better and explore how we can increase our DATA LITERACY  for a continualy learning Data Driven Culture")


    issues_write_up =  ("Voice Of The Customer (VOC)")

    st.subheader(issues_write_up)

    testi7 = 0
    testi8 = 0
    test9= 0
    testi10 = 0

    current_issues = "" # fill in user case 

    addtional_data_expanders = st.expander("The Big Issue I Have Found.... ", expanded=False)
    with addtional_data_expanders:

        testi1 = "Big issue I have found when looking at the data is often the SAP transactions and how to convert the 'Structures' to a base table. A structure is a bunch of base tables joined together (like a view in a database). However, to convert these into their underlying base tables is really challenging. Often people in Data Architecture have been able to help and I tend to find Data Services engineers to be very helpful \n \n -Insight Developer-"

        st.markdown(testi1)

    addtional_data_expanders = st.expander("From my point of view....", expanded=False)
    with addtional_data_expanders:

        testi2 = "From my point of view its not so much getting access to data values, its more about getting hold of the data model from when something was built / changed - such as ILPM or IRIS back end \n \n -Data Architect-"
        st.markdown(testi2)

    addtional_data_expanders = st.expander("I would say there are many issues.....", expanded=False)
    with addtional_data_expanders:
        

        testi3 = "I would say there are many issues. 1 - no dictionary of data sources, 2 - no common location where data fields are explained, 3 - no curation of data (no one knows if you should trust or ignore the data) \n \n -Data Scientist-"
        st.markdown(testi3)

    addtional_data_expanders = st.expander("Find issues with data in the source system....", expanded=False)
    with addtional_data_expanders:

        testi4 = "From a data point of view, the main pinch points are, when we find issues with data in the source system i.e. SAP and it causes violation to integrity in downstream objects due to the data not being correctly managed in the source system, is who to contact to get the data corrected, it only becomes apparent to us that this data isn't being closed off in the source system as we consume it, compared to the people who are administering it \n \n -Data Engineer- " 

        st.markdown(testi4)      

    addtional_data_expanders = st.expander("needed to create 3 different reports (in different transactions)....", expanded=False)
    with addtional_data_expanders:

        testi6 = " needed to have details of WR customer reactive jobs to drive locations for sewer monitoring.  I needed at least 3 pieces of data which I then could Geo-code and use in my assessments \n \
        Location- in a Grid ref or XY \n \
        Total Cost of the job £  \n \
        Problem, Action and Impact codes \n \
        I have used SAP for this, but needed to create 3 different reports (in different transactions) as this data is not available in one report.  The reports then needed to be combined, which I would do in excel using a lookup formula. Once the data was all combined I then had to transfer it to a GIS system and geo code the jobs. Some jobs will not geocode because they are missing location data. Some are wrongly coded to a mid-point of a postcode. These jobs I would delete as they are not useable- possibly missing on some trending or repeating of issues. If data in SAP was easier to access as a self-serve, or all SAP data was available through ARC GIS, in real time, that would be great. I have access to ARC GIS, but not all the team do, so this would need to be set up. \n \n -Infrastructure Modeller"

        st.markdown(testi6) 

    last_data_expanders = st.expander("Find issues with data in the source system....", expanded=False)
    
    with last_data_expanders:


        st.markdown("example in my experience is where we have built the asset risk modelling platform on a one-time 'data drop' from our master asset data platform and simply failed to consider how you keep that risk modelling platform aligned to the master asset data as time progresses. It's the work we were doing with a collegue from COST CAPTURE, where there has been a complete failure to design the CRUD process.\n \n \ -Data Specialist-")
        
        st.markdown("---")

if selected == "FAQ": 

    st.title(f"You have selected {selected}")
    st.markdown("###### This is a 6min read according to online tools")
    st.markdown("###### By Yavin Owens - Asset Intelligence - Non-Infra Data Analyst")
    st.markdown("###### Department | Strategic Delievery & Commercial Assurance | Asset Intelligence")

    st.subheader("1. How did you come up with this product?")
    st.markdown('''At work i had noticed a word being flown around 'Data Driven, Data Managment, Data Governance, Data Quality, Big Data Analytics, Cloud Computing, Data Lakes, Data Warehouses, Curated Data i could be here all data but it wasnt clear and/or really confusing so i wanted to see if i could get my head around it all, so i guess just self improvement, i then reflected back on my journey so far story, and had a real talk with myself where i was struggling and thought if im 1 person surely im not that stupid, someone must be struggling to. So i thought of a way to document my work while enabling others to have Visual and Written Media to enable others who have faced similar... lets call it late nights, having some real CIA Special Forces, Interigation with your laptop... maybe a few tears because you realise your laptop isnt listening, but when you start reading and watching the material provided by the Analytics Academy and The Love Every Minute Training, you really start wanting to get your teath into something, and start realising yourself... Yes this maybe of value but to who, and who is your auidinanc, what is the value, and also gain some tools to engage with the "so what" question.''')
    st.subheader("2. Is this easy to use")
    st.markdown('''Feedback so far, Non Technical Data Proffesionals have found some interesting user cases to profile data, and get quick inisghts to gain quick wins, also having a drive for "Improving the way we use Technoloy", i like to hope that the user experience is fit for purpose on they user experience with this tool, but if not ive left a feedback space so i can improve it for the benefit of the many.''')
    st.subheader("3. How do i join that Analytics Academey??")
    st.markdown("My initial interest was Data Science Where 'Richard Moore'. directed me to the Analytics Community and Analytics Academy web page and even gave a cherry 🍒 on top approach 🍰. and gave me some coahcing and mentoring so im abit advict and would URGE you all that are interested in this sexy stuff, Head over to |")
    st.subheader("4. So what do i do with the Analytics Academy?")
    st.markdown("")
    st.subheader("5. What is CPD and what  does it mean for you?")
    st.write("Learn More from the Analytics Academy  https://anglianwater.sharepoint.com/sites/fcmAnalyticsCommunity/SitePages/The-Analytics-Academy.aspx?OR=Teams-HL&CT=1657613791030&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiIxNDE1LzIyMDYwNjE0ODA1IiwiSGFzRmVkZXJhdGVkVXNlciI6ZmFsc2V9")
    st.markdown("")
    st.subheader("6. Who can i get in touch with if i need help with on the Analytics Academy? 😕")
    st.markdown(" ")
    st.subheader("7. What is continious Improvement (Kaizen) 🐱‍👤")
    st.write("To learn more about Lean, have a look at this site | https://www.leanproduction.com/kaizen/ | or get in touch with Louise Oliver - Continious Improvement Manager, to talk about the Love Every Minute Trainging")
    st.markdown("")
    st.subheader("8. Dont you think this is abit excesive for a proffesional review?")
    st.markdown("Through my journey i discovered multiple ways to tell a story and do all the cool analytical stuff, but one thing it will teach you is 'Annotation is very important', because at the end of the day when we move roles, and or want to hand over some work, least we have documented the important parts, so this was a massive annotation of the output on my personal journey and how i apply a dynamic way for various user personas to almost play with data in a more pretty way.... beacause we all know spreadsheet sometimes feel like they can burn your eyes. But thats me 🐱‍💻")
         
if selected == "Social Board":
    st.markdown(
        "###### [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)")

    st.title("Social Hub")

    st.markdown("This is a list of references i used to enable the building of this product")

    st.markdown("To be able to do even cooler stuff and create value out of our data, we first need to understand we must always keep an eye out for it. We must takecare of it so we are all confident in the data we use. i hope you Enjoy the video | What is good governance? | Ben Warner | TEDxJacksonvilleSalon")

    research_reference_columns = st.columns(4)

    with research_reference_columns[0]:
        st.subheader("Data Managment")
        st.markdown("The concept of data management arose in the 1980s as technology moved from sequential processing first punched cards, then magnetic tape) to random access storage. Since it was now possible to store a discrete fact and quickly access it using random access disk technology, those suggesting that data management was more important than business process management used arguments such as 'a customer's home address is stored in 75 (or some other large number) places in our computer systems.' However, during this period, random access processing was not competitively fast, so those suggesting 'process management' was more important than 'data management' used batch processing time as their primary argument. As application software evolved into real-time, interactive usage, it became obvious that both management processes were important. If the data was not well defined, the data would be mis-used in applications. If the process wasn't well defined, it was impossible to meet user needs.")
        st.markdown(" --- ")
        st.video("https://www.youtube.com/watch?v=E6hWPDUUQ1w")
        st.markdown("###### Ben Warner | https://en.wikipedia.org/wiki/Ben_Warner")
        st.markdown(" --- ")
        st.video("https://www.youtube.com/watch?v=OqmdLcyES_Q")
        st.markdown("MINDSPRINGS PRESENTS - GREATNESS | David Marquet")
        st.markdown(" --- ")
        st.markdown("Tedx Talk | Jordan Marrow")
        st.video("https://www.youtube.com/watch?v=8ovyQZ_Z8Xs")
        st.markdown("Data Managment")
        st.video("https://www.youtube.com/watch?v=oU0RlsXunlw")

    with research_reference_columns[1]:
        st.subheader("Wellbeing, Diversity & Inclusion")
        st.markdown("Getting Lost in the code, like your in the matrix can make you lose track of time, dont forget to set an alarm so youre having regular breaks from the screen, give yourself a good shake and stay hydrated.... For some Life inpiration to listen to while your plodding away or stressed")

        st.markdown("Do the right thing - Enable yourself and others to be confident to be aware, and become an ally to help ourselves be confident that we stay proffesional even if we had our external customer(s) watching us")
        st.markdown(" --- ")
        st.video("https://www.youtube.com/watch?v=8fzGPwY40Cw")
        st.markdown(
            " 5 RULES FOR THE REST OF YOUR LIFE | Matthew McConaughey MOTIVATIONAL SPEECH")
        st.markdown(" --- ")

        st.video("https://www.youtube.com/watch?v=4K5fbQ1-zps")
        st.markdown("Social Inequalities Explained in a $100 Race | Peter D")
        st.markdown(" --- ")

        st.video("https://www.youtube.com/watch?v=u_ktRTWMX3M")
  
        st.markdown("THE MINDSET OF A CHAMPION | Arnold Schwarzenegge")
        st.markdown(" --- ")
    

    with research_reference_columns[2]:
        st.subheader("Music To Work and sip a drink  to \n 📻 💻 🐱‍💻 🎧 ☕ 🥛 ")
        st.markdown("These are a couple playlist i like to listen to when i have to conduct some analysis or develop a prototype app 🎶")
        st.markdown(" --- ")

        st.video("https://www.youtube.com/watch?v=bz5q5gl2uZA")

    with research_reference_columns[3]:

        st.subheader("Making Analysis Easier")
        st.write("Enhancing your data Journey")
        st.markdown(" --- ")
        st.markdown("Mito")
        st.video("https://www.youtube.com/watch?v=VobWi0af-Tc")
        st.markdown("Lux Library | DATA VISUALIZATION AT SINGLE TOGGLE CLICK")
        st.video("https://www.youtube.com/watch?v=m41h4mGzwwE")