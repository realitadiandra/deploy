import streamlit as st
    
st.divider()
st.title('Identifikator Output FTIR')
st.title('Kelompok 5 :red[PMIP]')
st.divider()

st.write('*Aplikasi yang ditujukan untuk memudahkan pengguna dalam menentukan gugus fungsi dari hasil output Instrumen Spektrofotometri Infra Merah FTIR*')
import streamlit as st
from PIL import Image

image = Image.open('ftir1.jpg')

st.image(image, caption='Spektrofotometri FTIR Carry 630')

st.write('Beberapa senyawa organik dapat menyerap radiasi pada daerah bagian tampak dan ultraviolet dari alat spektrum elektromagnetik. Hasilnya, elektron akan menghasilkan nilai yang besar dari keadaan sebelumnya melalui tingkat energi yang lebih tinggi. Di sisi lain, senyawa organik juga dapat menyerap radiasi elektromagnetik pada daerah infra merah.Jadi, molekul ini berada dalam proses pergerakan yang sangat cepat. Radiasi infra merah akan diserap oleh molekul organik dan diubah ke dalam energi rotasi pada suatu molekul dengan frekuensi kurang dari 100 cm-1 dan panjang gelombang tidak lebih dari 100 cm.')
st.header('Macam-Macam Daerah Spektrum FTIR')
st.write('*Frekuensi Gugus Fungsional*')
st.write('Daerah pada gugus fungsional ini berada pada radiasi 4000-1400 cm-1. Bagian dari gugus fungsional ini nantinya akan menghasilkan nilai absorbsi yang terjadi karena ikatan dan gugus molekul. Puncak absorbsi pada daerah spektrum ini lebih mudah dikenal karena berasal dari gugus fungsional yang khas')
st.write('*Sidik Jari (Finger print)*')
st.write('Sidik jari atau biasa disebut sebagai finger print merupakan daerah spektrum yang terletak pada 1400-4000 cm-1. Ikatan pada absorbsi di daerah ini berhubungan dengan pergerakkan molekul secara menyeluruh. Suatu atom nantinya akan saling berhubungan sehingga dapat menghasilkan ikatan ikatan yang khas untuk setiap jenis molekul yang berbeda beda,di aplikasi ini kita membuat daerah sidik jari sebagai senyawa halo.')
st.header('Prinsip Kerja FTIR')
import streamlit as st
from PIL import Image

image = Image.open('ftir2.jpg')

st.image(image, caption='prinsip kerja FTIR')

    
st.write('---')
st.write('*Kelompok 5*')
st.write('1. Diandra Realita Abdulloh  (22220452)')
st.write('2. Nasywa Shafa Feliza       (2220474)')
st.write('3. Winda Ginia Ramadhanty    (2220498)')
st.write('4. Sabilal Rusdi             (2220485)')
st.write('5. Willy Rambiansyah Maricar (2220497)')
st.write('6. Filipo Inzagi Manik       (2120419)')
st.write('---')
number = st.number_input('Bilangan gelombang FTIR (cm-1)')

if 500<=number<=690 :
    st.error ('Senyawa Halo') 
elif 550<=number<=850 :
    st.error('Senyawa Halo')
elif 695<=number<=840 :
    st.error('Alkane')
elif 885<=number<=995 :
    st.error('Alkane')
elif 1040<=number<=1049 :
    st.error('Anhydride')
elif 1030<=number<=1070 :
    st.error('Sulfoxide')
elif 1050<=number<=1086 :
    st.error('Primary Alcohol')
elif 1087<=number<=1124 :
    st.error('Secondary Alcohol')
elif 1085<number<=1150 :
    st.error('Aliphatic Ether')
elif 1124<=number<=1205 :
    st.error('Tertiary Alcohol')
elif 1163<=number<=1210 :
    st.error('Ester')
elif 1199<=number<=1225 :
    st.error('Vinyl Ether')
elif 1020<=number<=1249 :
    st.error('Amine')
elif 1200<=number<=1275 :
    st.error('Alkyl Aryl Ether')
elif 1250<=number<=1310 :
    st.error('Aromatic Ester')
elif 1266<=number<=1342 :
    st.error('Aromatic Amine')
elif 1300<=number<=1349 :
    st.error('Sulfone')
elif 1342<=number<=1350 :
    st.error('Sulfonic Acid')
elif 1334<=number<=1351 :
    st.error('Sulfonamide')
elif 1335<=number<=1372 :
    st.error('Sulfonate')
elif 1310<=number<=1390 :
    st.error('Phenol')
elif 1000<=number<=1400 :
    st.error('Fluoro Compound')
elif 1379<=number<=1410 :
    st.error('Sulfonyl Chloride')
elif 1380<=number<=1415 :
    st.error('Sulfate')
elif 1330<=number<=1420 :
    st.error('Alcohol')
elif 1379<=number<=1390 :
    st.error('Aldehyde')
elif 1380<=number<=1465 :
    st.error('Alkane')
elif 1395<=number<=1440 :
    st.error('Carboxylic Acid')
elif 1500<=number<=1550 :
    st.error('Nitro Compound')
elif 1610<=number<=1620 :
    st.error('α,β-unsaturated ketone')
elif 1566<=number<=1650 :
    st.error('Cyclic Alkene')
elif 1580<=number<=1650 :
    st.error('Amine')
elif 1600<=number<=1651 :
    st.error('Conjugated Alkene')
elif 1638<=number<=1678 :
    st.error('Alkene')
elif 1668<=number<=1679 :
    st.error('Alkene')
elif 1680<=number<=1710 :
    st.error('Conjugated Acid')
elif 1735<=number<=1750 :
    st.error('Esters')
elif number==1760 :
    st.error('Carboxylic Acid')
elif 1785<=number<=1815 :
    st.error('Acid Halide')
elif 1900<=number<=2000 :
    st.error('Allene')
elif 2120<=number<=2145 :
    st.error('Carbodiimide')
elif 2222<=number<=2260 :
    st.error('Nitrile')
elif 2695<=number<=2830 :
    st.error('Aldehyde')
elif 2850<=number<=3000 :
    st.error('Alkane')
elif 3001<=number<=3300 :
    st.error('Amina Alifatik Primer')
elif 3500<=number<=3545 :
    st.error('Amina Primer')
elif 3550<=number<=3700 :
    st.error('Alkohol')
else :
    st.success('Masukkan bilangan gelombang FTIR (cm-1)')