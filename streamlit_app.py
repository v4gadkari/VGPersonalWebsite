import streamlit as st 
import plotly.express as px
import pandas as pd



def experience():
    with st.beta_container():
            st.title('Education Director')
            st.header('Big Data Analytics Association  \n December 2020 - Present')
            st.markdown('~ Discovered the gap in understanding of data science tools and data literacy within college students')
            st.markdown('~ Facilitated the growth of club members by presenting weekly live workshops in R and Python')
            st.markdown('~ Designed a comprehensive Canvas online learning course for Data Science which targets students of various skill levels and entails Machine Learning, Data Visualization and Data Manipulation')
            st.markdown('~ Organized course structure on Canvas to accommodate for 90+ asynchronous students by providing recorded lectures and interactive notebooks in Google Colab and RStudioCloud')


            st.subheader('---------------------------------------------------------------------------------------')

            st.title('Student Research Associate')
            st.header('Big Data Analytics Association Research Teams  \n October 2020 - December 2020')
            st.markdown('~ Identified racial biases towards delivery drivers by conducting sentiment analysis on mined Reddit comments')
            st.markdown('~ Clustered comments with Latent Dirichlet Allocation and Topic Modeling in order to find relevant patterns')
            st.markdown('~ Discovered the top words within the comments were those that described skin color and race')

            st.subheader('---------------------------------------------------------------------------------------')

            st.title('Web Developer')
            st.header('See3D Inc. \n June 2020 - October 2020')
            st.markdown('~ Identified key problems in the previous website such as minimal functionality and dull user interface')
            st.markdown('~ Enhanced personal software skillset by applying HTML/CSS best practices and expanding website features with React.js')
            st.markdown('~ Improved the front-end design by developing sleek and responsive user interface components such as footers, headers, and a homepage with React.js to enhance user experience')


def projects():

    st.title('Projects')

    project_1 = st.beta_expander('Cracking the Offense\'s Code')
    project_1.subheader('Python \n Pandas, Tableau, Scikit-Learn')
    project_1.markdown('~ Awarded 2nd place at Data I/O Hackathon')
    project_1.markdown('~ Analyzed play-by-play data of various NFL teams from 2009-2018 Seasons')
    project_1.markdown('~ Conducted data analysis and predictive machine learning modeling to help defensive coordinators predict and classify an offense\'s next play')
    project_1.markdown('~ Evaluated metrics to select the most accurate model, the Gradient Boosting classifier with an accuracy of 75%')

    

    project_2 = st.beta_expander('NFL Big Data Bowl 2021')
    project_2.subheader('Python/R \n Pandas, Plotnine, Tidymodels, Stacks')
    project_2.markdown('~ Examined player tracking data and play-by-play data to predict offensive formation and quarterback drop back with 73% accuracy')
    project_2.markdown('~ Reduced data dimensionality with Principal Component Analysis')
    project_2.markdown('~ Built stacked ensemble learners with Decision Trees and K-Nearest Neighbors classifiers')

    

    project_3 = st.beta_expander('GOAT Regression Analysis')
    project_3.subheader('R \n Tidyverse, Tidymodels')
    project_3.markdown('~ Performed exploratory data analysis on career statistics for Michael Jordan, Lebron James, and Kobe Bryant')
    project_3.markdown('~ Conducted multiple regression analysis to quantify metrics such as player efficiency rating in order to help evaluate the "greatness" factor of each player ')

    

    project_4 = st.beta_expander('Brain Tumor Image Classification')
    project_4.subheader('Python \n Tensorflow')
    project_4.markdown('~ Created a Convolutional Neural Network to classify brain tumor images using Tensorflow')
    project_4.markdown('~ Utilized Keras preprocessing libraries to format data for modeling in order to experiment with various deep learning architectures')


def skills_ratings():

    st.title('Languages')
    
    st.header('Python')
    st.select_slider('Skill Level', options=[1,1.5,2,2.5,3,3.5,4,4.5,5], value=4.5, key='slider_1')

    st.header('R')
    st.select_slider('Skill Level', options=[1,1.5,2,2.5,3,3.5,4,4.5,5], value=4, key='slider_2')

    st.header('SQL')
    st.select_slider('Skill Level', options=[1,1.5,2,2.5,3,3.5,4,4.5,5], value=3, key='slider_3')



@st.cache
def pie_chart():


    skills_df = pd.DataFrame({'Skills':['Data Manipulation', 'Data Visualization', 'Data Engineering', 'Machine Learning'], 'Knowledge':[40, 20, 5, 35]})

    chart = px.pie(skills_df, values='Knowledge', names='Skills')

    return chart


def handle_click():
    links = ['https://www.linkedin.com/in/viren-gadkari-13a287191/', 'https://github.com/v4gadkari', 'https://medium.com/swlh/cracking-the-offenses-code-7565e04f54ea']
    cols1, cols2, cols3 = st.sidebar.beta_columns(3)
    linkedIn = cols1.button('LinkedIn', key='LinkedIn')
    github = cols2.button('Github', key='Github')
    medium = cols3.button('Medium', key='Medium')

    if linkedIn == True:
        st.sidebar.markdown(links[0], unsafe_allow_html=True)
    if github == True:
        st.sidebar.markdown(links[1], unsafe_allow_html=True)
    if medium == True:
        st.sidebar.markdown(links[2], unsafe_allow_html=True)


def navigation():
    option = st.sidebar.selectbox('Navigation', ['Experience', 'Projects', 'Skills'])
    if option == 'Experience':
        experience()
    elif option == 'Projects':
        projects()     
    else:
        skills_ratings()
        st.title('Data Skills')
        skills_chart = pie_chart()
        st.write(skills_chart)

        


def main():

    
    st.sidebar.title('Viren Gadkari \n The Ohio State University \'23  \n B.S. Statistics, Minor in Economics')
    navigation()
    handle_click()
    
    
    



if __name__ == '__main__':
    main()