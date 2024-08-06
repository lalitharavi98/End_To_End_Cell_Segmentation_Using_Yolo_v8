import sys,os
from cell_segmentation.pipeline.training_pipeline import TrainPipeline
# from cell_segmentation.utils.main_utils import decodeImage, encodeImageIntoBase64
# from flask import Flask, request, jsonify, render_template,Response
# from flask_cors import CORS, cross_origin
# from cell_segmentation.constant.application import APP_HOST, APP_PORT




# app = Flask(__name__)
# CORS(app)

# class ClientApp:
#     def __init__(self):
#         self.filename = "inputImage.jpg"



# @app.route("/train")
# def trainRoute():
obj = TrainPipeline()
obj.run_pipeline()
    # return "Training Successfull!!" 