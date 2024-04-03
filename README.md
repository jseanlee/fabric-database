# Smart Wardrobe App ###

Mobile application that allows users to store information of their clothing on a database, and keep track of what they wear by image recognition. The app takes user entries and returns a variety of data visualizations to better understand their wardrobe. The app has trained models that help users input certain information about their clothing automatically by photo recognition, as well as provide tailored recommendations based on user preferences and color palettes. 

## Getting Started

Ensure that the proper libraries are installed to have the system running:

```python
# include libraries
import sqlite3
from sqlite3 import Error
import pandas as pd

# upgrade SQLAlchemy 
!pip install --upgrade SQLAlchemy==1.4.46
```

More information on installing API keys necessary to access trained models will be added later to this file. 
## Usage

When first using the mobile app, the user will be prompted to create an account, which will register them in the database. Once an account is made, the user can either access photos or take a picture of a piece of clothing. For now, the user will have to manually input specifications of their clothes, such as `clothing_type`, `clothing_material`, `comfortability`,`user_fit`, and `color` in a menu. When our ML model is trained, we expect to automatically identify user's pictures of clothing by type and material.

Once all user clothing data is added, the user can then create daily logs of what they wore for each day. Currently, the user has to manually select items from their existing wardrobe to add information on what they wore. We hope to use our ML model to eventually use image recognition to automatically recognize what the user wore with only a picture. 

As daily log data accumulates, data visualizations are created to help the user better visualize their wardrobe by specific characteristics. For instance, the distribution and variety of one's wardrobe can be organized by color and material. The user's daily information can also be visualized to help the user better understand their own preferences.

## Framework 

### Backend: 

Currently building in Flask under Python language. Using python, we created an SQLite database that will contain user information, clothing information, and daily log information. The app runs helper functions that run queries to easily manage database. 

#### About model: 

Currently collecting thousands of images of a variety of clothing items via web-scraping. Will need to format this data so it is formatted correctly during unsupervised learning, and label by listed specifications. Goal will be so that the image can correctly identify clothing type (shirt, jacket, pants, belt, etc.) and color(s). ML models are currently being built in PyTorch. The idea will be to have an API key connected to said model, which can be accessed to run necessary tasks. 


### Frontend: (backend higher priority)

Using React framework for frontend. 

<!-- ROADMAP -->
## Roadmap

- [x] Create Database to Store (SQLite .db for now)
  - [ ] Need to identify HOW and WHERE data is stored (locally/user-based like Firebase, or AWS)
- [ ] Create Flask Framework
- [ ] Clothing database
  - [X] Kaggle dataset (500 images)
  - [ ] Web-scraping from outlet stores, format image data by characteristics

<!-- CONTACT -->
## Contact

Sean Lee - (https://linkedin.com/in/seanleej) - jiisung21@gmail.com

Trenton vonHartitzsch - (https://linkedin.com/in/trenton-vonhartitzsch/) - trentonvonH@gmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>



