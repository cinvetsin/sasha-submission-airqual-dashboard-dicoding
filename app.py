import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='dark')

def plot_pollutant_levels(df_all, pollutants, colors):
    st.header("Pollutant Levels Analysis")
    # Calculate median pollutant levels grouped by station
    median_pollutant_levels_per_station = df_all.groupby('station')[pollutants].median()

    # Analyze the distribution of wind directions
    wind_direction_distribution = df_all['wd'].value_counts(normalize=True)

    # Analyze the median pollutant levels for different wind directions
    pollutant_levels_by_wd = df_all.groupby('wd')[pollutants].median()

    # Group data by month and hour, then calculate the median pollutant levels
    pollutant_levels_by_month_hour = df_all.groupby(['month', 'hour'])[pollutants].median()

    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    # Create main tabs for each pollutant
    tab_titles = [f'{pollutant}' for pollutant in pollutants]
    tabs = st.tabs(tab_titles)

    for i, tab in enumerate(tabs):
        with tab:
            # Sub-tabs for each analysis type
            sub_tab1, sub_tab2, sub_tab3 = st.tabs(["Levels per Station", "Levels by Wind Direction", "Levels by Month and Hour"])

            with sub_tab1:
                selected_pollutant = pollutants[i]

                # Sort median values in descending order
                sorted_median = median_pollutant_levels_per_station[selected_pollutant].sort_values(ascending=False)

                # Plotting median levels per station
                plt.figure(figsize=(10, 6))
                sorted_median.plot(kind='bar', color=colors[i])
                plt.title(f'Median {selected_pollutant} Levels per Station (Descending Order)')
                plt.xlabel('Station')
                plt.ylabel('Median Pollutant Level')
                plt.xticks(rotation=45)
                plt.tight_layout()
                st.pyplot(plt)

            with sub_tab2:
                # Plotting pollutant levels by wind direction
                pollutant_data_by_wd = pollutant_levels_by_wd[selected_pollutant]

                # Sort the data in descending order based on the median levels
                sorted_pollutant_data_by_wd = pollutant_data_by_wd.sort_values(ascending=False)

                plt.figure(figsize=(10, 6))
                sorted_pollutant_data_by_wd.plot(kind='bar', color='mediumpurple')
                plt.title(f'{selected_pollutant} Levels by Wind Direction')
                plt.xlabel('Wind Direction')
                plt.ylabel('Median Level')
                plt.xticks(rotation=45)
                plt.tight_layout()
                st.pyplot(plt)

            with sub_tab3:
                selected_month = st.selectbox("Select Month", months, key=f"month_select_{i}")
                month_number = months.index(selected_month) + 1

                # Filter data for the selected month
                monthly_data = pollutant_levels_by_month_hour.xs(month_number, level='month')[selected_pollutant]

                # Plotting
                plt.figure(figsize=(10, 6))
                monthly_data.plot(marker='o', linestyle='-', color='darkturquoise')
                plt.title(f'{selected_pollutant} Levels by Hour in {selected_month}')
                plt.xlabel('Hour of the Day')
                plt.ylabel('Median Level')
                plt.xticks(range(0, 24), range(0, 24))
                plt.grid(True)
                plt.tight_layout()

                st.pyplot(plt)

def plot_weather_pollutant_correlation(df_all, weather_variables, pollutants):
    st.header("Weather-Pollutant Correlation Analysis")
    ## Allow users to select which weather variables and pollutants to analyze
    selected_weather_variables = st.multiselect('Select Weather Variables', weather_variables, default=weather_variables)
    selected_pollutants = st.multiselect('Select Pollutants', pollutants, default=pollutants)

    if not selected_weather_variables or not selected_pollutants:
        st.warning('Please select at least one weather variable and one pollutant.')
        st.stop()

    # Calculate the correlation matrix for the selected variables
    correlation_matrix = df_all[selected_weather_variables + selected_pollutants].corr()

    # Extract the correlation values between the selected weather variables and pollutants
    correlation_weather_pollutants = correlation_matrix.loc[selected_weather_variables, selected_pollutants]

    # Plotting the correlation matrix as a heatmap
    plt.figure(figsize=(len(selected_pollutants) * 1.2, len(selected_weather_variables) * 0.8))
    sns.heatmap(correlation_weather_pollutants, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation between Weather Variables and Pollutant Levels')
    
    # Display plot in Streamlit
    st.pyplot(plt)

df_all = pd.read_csv("all_data.csv")
st.title("Air Quality Dashboard")

pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']
colors = ['skyblue', 'orange', 'green', 'red', 'violet', 'cyan']
weather_variables = ['TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']

# Sidebar description
st.sidebar.write("""
                # Air Quality Dasboard
                by Sasha Nabila Fortuna
                """)
st.sidebar.write("## Analysis Options")
st.sidebar.write("Select the analysis you want to display from the options below. You can choose to view a specific analysis or all available analyses.")
# Sidebar to choose analysis
analysis_options = ['Select Analysis', 'Pollutant Levels Analysis', 'Weather-Pollutant Correlation Analysis', 'Show All']
selected_analysis = st.sidebar.selectbox("Choose an analysis to display", options=analysis_options)

if selected_analysis == 'Pollutant Levels Analysis' or selected_analysis == 'Show All':
    plot_pollutant_levels(df_all, pollutants, colors)

if selected_analysis == 'Weather-Pollutant Correlation Analysis' or selected_analysis == 'Show All':
    plot_weather_pollutant_correlation(df_all, weather_variables, pollutants)