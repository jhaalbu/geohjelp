import streamlit as st
import math

st.header('Gi forholdstall')
teller = st.number_input(label='Teller', value=1.0, step=0.1)
nemner = st.number_input(label='Nemner', value=2.0, step=0.1)
helning = math.atan(teller/nemner)
vinkel = math.degrees(helning)

st.header('Forenkla:')
st.write('Teller er 1')
st.write(f'Nemner er {round((nemner/teller), 2)}')

#st.write(f'Vinkel er {round((math.atan(teller/nemner)), 1)} radianer')
st.write(f'Vinkel er {round((math.degrees(helning)),1)} grader')

st.header('Gi vinkel')
vinkel = st.number_input(label='Vinkel', value=60, step=1)
nemner = 1/math.tan(math.radians(vinkel))

st.header('Forholdstall')
if nemner >= 1:
    st.write(f'Helling er: 1/{round(nemner,1)}')
else:
    st.write(f'Helling er: {round(1/nemner,1)}/1')
