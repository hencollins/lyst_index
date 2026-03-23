## 👠 Decoding the Lyst Index
A little bit about me — before I learned to code, I wanted to work in fashion. So, I worked on this project in February 2025 (just got to uploading it) to connect my passion for fashion with my new-found love for data science. The Lyst Index ranks the top 20 "hottest" fashion labels each quarter, so I thought it would be an entertaining way of the EDA skills I had just learng in my data sci class @ Berkeley.

### 🛠️ Tools and tech
 - `Python`
 - `pandas`
 - `BeautifulSoup` for web scraping
 - `matplotlib` for ranking visualizations
 - `Tableau` for extra visualizations (not seen in this repo)

### 🗺️ The project
For this project, I started by learning how to read HTML code and how to use the `BeautifulSoup` library in Python for web scraping. I then went through each Lyst index (from the beginning of 2018 to the end of 2024) and scraped each webpage to obtain the rankings. I then exported the respective `.csv`s and took them to Kaggle. 

There, I concatenated the `.csv`s together, cleaned the data, and made a pivot table from it. I then used `matplotlib` to plot the rankings of the top 5 brands (on average) over time. I had some pretty cool findings:

- **Prada**: was consistently in the top (they've been around awhile)
- **Gucci**: dipped at the start of 2023 due to a change in creative director (Sabato de Sarno replacing Alessandro Michele)
- **Miu Miu**: entered the Lyst after a standout Spring Summer '22 show (I remember watching the show live on YouTube during my AP Literature class senior year of high school)
- **Balenciaga**: dipped drastically near the end of 2022 due to an advertising scandal
- **Off-White**: disappeared after 2022 because of the passing of Virgil Abloh — the brand's original creative director

While I'm not focused on fashion anymore, it was fun to teach myself EDA and web scraping in this familiar context.

### 🗃️ Files
- `scrape_lyst.py` contains web scraping and dataset exporting
- `the-lyst-index-eda` contains Lyst index analysis and visualization of top 5 hottest brands
