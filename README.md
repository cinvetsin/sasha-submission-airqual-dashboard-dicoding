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