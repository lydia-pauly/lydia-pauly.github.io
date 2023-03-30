import streamlit as st
import streamlit.components.v1 as components

c1 = st.container()
c2 = st.container()
c3 = st.container()
c4 = st.container()
c5 = st.container()

st.sidebar.markdown("# Lydia Pauly")
st.sidebar.write("📧 hey@lydiapauly.com")
st.sidebar.write('🐈‍⬛ <a href="https:www.github.com/lydia-pauly"> github.com/lydia-pauly </a>', unsafe_allow_html=True)
st.sidebar.write('📝 <a href="https:www.linkedin.com/in/lydia-pauly"> linkedin.com/lydia-pauly </a>', unsafe_allow_html=True)

c1.markdown("# Lydia Pauly")
c1.markdown("### Data Scientist, Engineer, and Analyst")
c2.write('Remote sensing 📡 ~ Machine and Deep Learning 🧠 ~ NLP ✍️ ~ Creative Tech ✨')
c3.markdown(" ")
c3.markdown(" ")
c3.markdown(" ")
with c3.container():
    col1, col2, col3, col4, col5 = st.columns(5, gap="small")
    with col3:
        st.image('data/small_walking.gif')
c3.markdown(" ")
c3.markdown(" ")
c3.markdown(" ")
c3.markdown('## Skills to write home about:')

with c3.container():
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.markdown('#### 🔎 Data analysis')
        st.write('Using **SQL**, **Pandas**, and **Numpy**, then visual dashboards with **Seaborn** \
            or in **Tableau** / **PowerBI**')
    with col2:
        st.write('#### ♾️ Statistics and modelling')
        st.write('Including linear, logistic, and decision tree regression using **SciKit-Learn**')

with c3.container():
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.markdown('#### 🧠 Machine and deep learning')
        st.write('**Tensorflow / Keras**, including neural networks with CNNs and RNNs')
    with col2:
        st.markdown('#### ⚙️ Deploying data products')
        st.write("Models trained at scale and made API-accessible with **GCP/R**, **Docker**, **FastAPI**, and **Streamlit**")

with c3.container():
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.markdown('#### 📸 Image models')
        st.write('Using generative models, such as **GANs** and **Diffusion** architecture')
    with col2:
        st.markdown('#### ✨ Creative ✨ tech')
        st.write("Soundboard generators, AI-visuals for radio, and bad horoscopes!")

c4.markdown(" ")
c4.markdown(" ")
c4.markdown(" ")
c4.markdown(" ")
c4.markdown(" ")
c4.markdown(" ")
c4.markdown('## Projects I want to talk about:')
c5.markdown('##### CALA: Coastal and Artificial Landscapes Architect <a href="/project-cala">👈</a> (go to project page)', \
    unsafe_allow_html=True)
c5.write('A custom-built Diffusion model that examines images from the SENTINEL-2 ESA Satellite, and generates \
    fictional coastlines from pure noise (along with some ChatGPT lore).')
c5.write('Try it out <a href="https:cala-website.streamlit.share">here</a>!', unsafe_allow_html=True)
c5.write('Example images:')


#components.html("<html><body><h1>Hello, World</h1></body></html>", width=200, height=200)
#st.write
