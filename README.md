# Air Quality Dashboard
> by Sasha Nabila Fortuna

Dashboard can be run manually thru notebook (Google Colab or Jupyter). If you run thru anaconda, you can add these for setting up the environment:
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit
```

# Run dashboard (streamlit) locally
```
!pip install streamlit -q
!wget -q -O - ipv4.icanhazip.com
!streamlit run app.py & npx localtunnel --port 8501
```
# Run deployed dashboard
You can visit this link: https://sasha-submission-airqual-dashboard.streamlit.app/

# Files needed for deployed dashboard
> [all_data.csv](cinvetsin/sasha-submission-airqual-dashboard-dicoding) for cleaned and gathered dataset
<br>
[app.py](https://github.com/cinvetsin/sasha-submission-airqual-dashboard-dicoding/blob/main/app.py) to run streamlit
<br>
[requirements.txt](https://github.com/cinvetsin/sasha-submission-airqual-dashboard-dicoding/blob/main/requirements.txt) to setup the pipeline and import the libraries