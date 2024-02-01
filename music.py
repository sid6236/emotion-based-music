import av
import cv2 
import numpy as np 
import mediapipe as mp 
from keras.models import load_model
import webbrowser
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Load models and data
model = load_model("model.h5")
label = np.load("labels.npy")
holistic = mp.solutions.holistic
hands = mp.solutions.hands
holis = holistic.Holistic()
drawing = mp.solutions.drawing_utils

# EmotionProcessor class
class EmotionProcessor:
    def __init__(self):
        pass

    def process_frame(self, frame):
        frm = frame.to_ndarray(format="bgr24")
        # Frame processing logic
        return av.VideoFrame.from_ndarray(frm, format="bgr24")

# Initialize EmotionProcessor
emotion_processor = EmotionProcessor()

# Initialize Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    dcc.Input(id='language', type='text', placeholder='Language'),
    dcc.Input(id='singer', type='text', placeholder='Singer'),
    html.Button('Recommend me songs', id='recommend-btn'),
    html.Div(id='output-div')
])

# Define callback for recommendation button click
@app.callback(
    Output('output-div', 'children'),
    [Input('recommend-btn', 'n_clicks')],
    [dash.dependencies.State('language', 'value'),
     dash.dependencies.State('singer', 'value')])
def recommend_songs(n_clicks, lang, singer):
    if n_clicks is not None:
        if not emotion:
            return "Please let me capture your emotion first"
        else:
            webbrowser.open(f"https://www.youtube.com/results?search_query={lang}+{emotion}+song+{singer}")
            np.save("emotion.npy", np.array([""]))
            return "Recommendation successful"

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
