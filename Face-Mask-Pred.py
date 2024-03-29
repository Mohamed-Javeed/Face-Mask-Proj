
from fastai.vision.widgets import *
from fastai.vision.all import *

from pathlib import Path

import streamlit as st
import pathlib

temp = pathlib.WindowsPath
pathlib.WindowsPath = pathlib.PosixPath

class Predict:
    def __init__(self, filename):
        self.learn_inference = load_learner(Path()/filename)
        self.img = self.get_image_from_upload()
        st.header("Face Mask Predictor")
        st.text("By A.Mohamed Javeed, D.Naresh, M.R.Goutham")
        if self.img is not None:
            self.display_output()
            self.get_prediction()
    
    @staticmethod
    def get_image_from_upload():
        uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg', 'jpg'])
        if uploaded_file is not None:
            return PILImage.create((uploaded_file))
        return None

    def display_output(self):
        st.image(self.img.to_thumb(500,500), caption='Uploaded Image')

    def get_prediction(self):
        pred_dict = {'WithMask':' 😷', 'WithoutMask':' 😐 (Please wear one !)'}

        if st.button('Classify'):
            pred, pred_idx, probs = self.learn_inference.predict(self.img)
            st.write(f'Prediction: {pred + pred_dict[pred]}; Probability: {probs[pred_idx]:.04f}')
        else: 
            st.write(f'Click the button to classify') 

if __name__=='__main__':

    file_name='Mask-Predictor-Learner.pkl'

    predictor = Predict(file_name)
