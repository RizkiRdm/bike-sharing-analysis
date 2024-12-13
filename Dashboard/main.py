import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set_theme("poster")

# helper function : weather sum function
def weather_sum_bike(df):
    weather_sum_bike = df.groupby(by="cuaca")["cnt_x"].sum().reset_index()

    # rename column 'cnt_x' to 'jumlah penyewaan'
    weather_sum_bike = weather_sum_bike.rename(columns={'cnt_x': 'jumlah_penyewaan'})

    return weather_sum_bike

# helper function : increase/deacrese rent bike function
def percent_rent_bike(df):
    
    holiday_rentals = df[df["holiday_x"] == 1]['cnt_x'].sum()
    workingday_rentals = df[df["workingday_x"] == 0]['cnt_x'].sum()
    total_rentals = df['cnt_x'].sum()
    
    if total_rentals == 0:
        return 0, 0

    # Hitung persentase penyewaan di akhir pekan
    holiday_percentage = (holiday_rentals / total_rentals) * 100

    # Hitung persentase penyewaan di hari kerja
    workingday_percentage = (workingday_rentals / total_rentals) * 100
    
    return holiday_percentage, workingday_percentage

# helper function : identify peak hours function
def peak_hours(df):
    bike_hour = df.groupby(by=["hr", "tahun_y"])["cnt_y"].sum().reset_index()
    
    # rename column 'cnt_x' to 'jumlah penyewaan'
    bike_hour = bike_hour.rename(columns={'tahun_y': 'tahun'})
    return bike_hour

# helper function : identify Tren rental bike 
def tren_rental_bike(df):
    yearly_rentals = df.groupby(by=["mnth_x", "tahun_x"]).agg({
        "cnt_x": "mean",
        "cnt_y": "sum"
    }).reset_index()

    yearly_rentals.rename(columns={
        "mnth_x" : "bulan",
        "tahun_x" : "tahun",
    }, inplace=True)

    return yearly_rentals


# define data
bike_data = pd.read_csv('bike_data.csv', parse_dates=["dteday"])

# call function
weather_sum_bike_data = weather_sum_bike(bike_data)
percent_rent_bike_data = percent_rent_bike(bike_data)
peak_hours_bike_data = peak_hours(bike_data)
tren_rental_bike_data = tren_rental_bike(bike_data)

# color palette
colors = ["#69b3a2", "#4374B3"]

# START MAKE A DASHBOARD
st.title("Data Analisis Bike Sharing")

# SECTION 1
col1, col2 = st.columns(2)

with col1:
    st.image("logo.jpg")
with col2:
    st.text("Name : Rizki Romdhoni")
    st.text("Dataset : Bike Sharing Dataset")
    st.text("Hobby : Sleep")
    st.text("ID Dicoding : rizki_romdhoni_rvM9")
    st.text("Email : rizkimvp27@gmail.com")
    
st.divider()

# SECTION 2 

st.header("Jumlah penyewaan harian berdasarkan cuaca")
fig, ax = plt.subplots(figsize=(14, 9))

sns.barplot(
x="cuaca",
y="jumlah_penyewaan",
data=weather_sum_bike_data.sort_values(by="jumlah_penyewaan", ascending=True),
ax=ax
)


# Customizing the chart
ax.set_title("Jumlah Penyewaan Sepeda Harian Berdasarkan Cuaca", fontsize=18)
ax.set_xlabel("Cuaca", fontsize=14)
ax.set_ylabel("Jumlah Penyewaan", fontsize=14)

plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

# Render chart in Streamlit
st.pyplot(fig)

# expander
with st.expander("Insights"):

    st.text(" Jumlah total penyewaan terbanyak terjadi pada cuaca cerah, diikuti dengan cuaca berawan, dan yang terkecil ada di cuaca hujan. Dengan total penyewaan sepeda dari tahun 2011 ke 2012 mencapai 50 juta lebih penyewaaan sepeda di pada saat cuaca sedang cerah")

st.divider()

# section 3

st.header("Identifikasi jam-jam puncak penyewaan sepeda")
fig, ax = plt.subplots(figsize=(14, 9))

sns.barplot(
x="hr",
y="cnt_y",
hue="tahun",
data=peak_hours_bike_data,
ax=ax,
palette=colors
)

# Customizing the chart
ax.set_title("Jumlah Penyewaan Sepeda Harian Berdasarkan Cuaca", fontsize=18)
ax.set_xlabel("Cuaca", fontsize=16)
ax.set_ylabel("Jumlah Penyewaan", fontsize=16)
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

# Render chart in Streamlit
st.pyplot(fig)

# expander
with st.expander("Insights"):

    st.write("- Dari plot tersebut bisa disimpulkan jika jumlah terbanyak orang dalam menyewa sepeda ada di jam delapan pagi sampai ke jam lima sore.\n- Baik di tahun 2011 dan tahun 2012, jam lima sore memiliki jumlah penyewaan terbesar.")
    
st.divider()

# section 4
st.header("persentase peningkatan/penurunan penyewaaan sepeda pada akhir pekan dibandingkan hari kerja")

col1, col2 = st.columns(2, gap="small")

holiday_percentage, workingday_percentage = percent_rent_bike(bike_data)

# barplot
with col1:
    st.write("### Barchart")
    percentages = [holiday_percentage, workingday_percentage]
    labels = ["Akhir pekan", "Hari kerja"]
    
    
    fig, ax = plt.subplots(figsize=(7, 8))
    
    sns.barplot(
    x=labels,
    y=percentages,
    ax=ax,
    palette=colors
    )

    # Customizing the chart
    ax.set_title("Jumlah penyewaan sepeda di hari kerja dan akhir pekan", fontsize=18)
    ax.set_xlabel("Persentase Penyewaan (%)", fontsize=16)
    ax.set_ylabel("Persentase di akhir pekan dan hari kerja", fontsize=16)

    # Render chart in Streamlit
    st.pyplot(fig)
    
# pie chart
with col2:
    st.write("### Pie chart")
    # Membuat pie chart
    fig, ax = plt.subplots(figsize=(14, 9))

    ax.pie(
    percentages,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90
    )

    # Customizing the chart
    ax.set_title("Jumlah Penyewaan Sepeda di Hari Kerja dan Akhir Pekan", fontsize=18)

    # Render chart in Streamlit
    st.pyplot(fig)
    
with st.expander("Insight"):
    st.text("Penyewaan pada akhir pekan menunjukan penurun yang cukup besar, bisa disimpulkan penyebabnya adalah karena orang pada akhir pekan lebih sedikit melakukan aktivitas, seperti berangkat kerja. Berbandingkan terbalik jika di hari kerja, orang lebih banyak melakukan aktivitas seperti berangkat kerja, pergi ke sekolah atau aktivitas lainyya.")
    
st.divider()

# SECTION 5
st.header("Tren penyewaan sepeda dari tahun 2011 ke tahun 2012")
col1, col2 = st.columns(2, gap="small")

with col1:
    fig, ax = plt.subplots(figsize=(14, 9))

    sns.lineplot(
    x="bulan",
    y="cnt_y",
    hue="tahun",
    data=tren_rental_bike_data,
    ax=ax,
    palette=colors
    )

    # Customizing the chart
    ax.set_title("Jumlah total Penyewaan Sepeda Berdasarkan Bulan dan Tahun", fontsize=22)
    ax.set_xlabel("Bulan", fontsize=16)
    ax.set_ylabel("Jumlah Penyewaan", fontsize=16)
    plt.xticks(range(1,13))
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    # Render chart in Streamlit
    st.pyplot(fig)
    
with col2:
    fig, ax = plt.subplots(figsize=(14, 9))

    sns.barplot(
    x="bulan",
    y="cnt_x",
    hue="tahun",
    data=tren_rental_bike_data,
    ax=ax,
    palette=colors
    )

    # Customizing the chart
    ax.set_title("Jumlah Penyewaan Sepeda Harian Berdasarkan Bulan dan Tahun", fontsize=22)
    ax.set_xlabel("Bulan", fontsize=16)
    ax.set_ylabel("Jumlah Penyewaan", fontsize=16)
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    # Render chart in Streamlit
    st.pyplot(fig)

with st.expander("insight"):
    st.write("- Jumlah penyewaan sepeda dari tahun 2011 sampai tahun 2012 mengalami peningkatan yang cukup besar.\n- Rata-rata jumlah penyewaan sepeda di tahun 2012 ada di angka 3.000 sampai diatas 7.000 sepeda dan terbanyak ada di bulan september (9) di tahun 2012.\n- Terdapat pola musiman yang jelas pada jumlah penyewaan sepeda. Jumlah penyewaan cenderung meningkat pada bulan-bulan tertentu seperti dari bulan maret (3) sampai bulan september (9) dan menurun pada bulan-bulan seperti bulan oktober (10) sampai bulan februari (2). Ini menunjukkan bahwa faktor cuaca, musim, atau event tertentu dapat mempengaruhi minat masyarakat untuk menyewa sepeda.")