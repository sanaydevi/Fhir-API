# from flask import Flask,render_template
# from flask_restful import Api, Resource, reqparse,request
# import random
# from flask_restful import Api, Resource, reqparse
# from flask import send_from_directory
# from openpyxl import load_workbook
# import random
# from flask import send_file
#
#
# app = Flask(__name__)
# # @app.route("/",methods=['GET'])
# # def welcome():
# #     if request.method == "GET":
# #         return("Welcome to PII Masking Tool:"
# #                "Specify /id=3...to get corresoponding id"
# #                "SPecify")
#
#
# @app.route("/")
# def homePage():
#     return render_template('index.html')
#
# @app.route("/getFile",methods= ["POST"])
# def put():
#     Msg = "hi"
#     return 0
#
# @app.route('/foo', methods=['GET', 'POST'])
# def foo():
#     '''execute whatever code you want when the button gets clicked here'''
#     return "hi"
#
# @app.route('/index')
# def index():
#     path = "FileTOUpload.xlsx"
#     return send_file(path, as_attachment=True)
#     #
#     # file_name = 'document_template.xltx'
#     # wb = load_workbook('FileTOUpload.xlsx')
#     # wb.save(file_name, as_template=True)
#     #
#     # return send_from_directory(file_name, as_attachment=True)
#
#     # file_name = 'document_template.xltx'
#     # wb = load_workbook('FileTOUpload.xlsx')
#     # return wb
#     #
#     # wb.save(file_name)
#     #
#     # return send_from_directory(file_name, as_attachment=True)
#
#     # user = {'username': 'Miguel'}
#     # return render_template('index.html', title='PII', user=user)
# #file upload
# #links click display file
# #UI focus
#
# #get : dislay file content..
# #post : button user can upload a file
#
# @app.route("/getFile",methods= ["GET"])
# def startAPI(id=0):
#     ai_quotes = [
#         {
#             "id": 0,
#             "author": "Kevin Kelly",
#             "quote": "The business plans of the next 10,000 startups are easy to forecast: " +
#                      "Take X and add AI."
#         },
#         {
#             "id": 1,
#             "author": "Stephen Hawking",
#             "quote": "The development of full artificial intelligence could " +
#                      "spell the end of the human race…. " +
#                      "It would take off on its own, and re-design " +
#                      "itself at an ever increasing rate. " +
#                      "Humans, who are limited by slow biological evolution, " +
#                      "couldn't compete, and would be superseded."
#         },
#         {
#             "id": 2,
#             "author": "Claude Shannon",
#             "quote": "I visualize a time when we will be to robots what " +
#                      "dogs are to humans, " +
#                      "and I’m rooting for the machines."
#         },
#         {
#             "id": 3,
#             "author": "Elon Musk",
#             "quote": "The pace of progress in artificial intelligence " +
#                      "(I’m not referring to narrow AI) " +
#                      "is incredibly fast. Unless you have direct " +
#                      "exposure to groups like Deepmind, " +
#                      "you have no idea how fast—it is growing " +
#                      "at a pace close to exponential. " +
#                      "The risk of something seriously dangerous " +
#                      "happening is in the five-year timeframe." +
#                      "10 years at most."
#
#         },
#         {
#             "id": 4,
#             "author": "Geoffrey Hinton",
#             "quote": "I have always been convinced that the only way " +
#                      "to get artificial intelligence to work " +
#                      "is to do the computation in a way similar to the human brain. " +
#                      "That is the goal I have been pursuing. We are making progress, " +
#                      "though we still have lots to learn about " +
#                      "how the brain actually works."
#         },
#         {
#             "id": 5,
#             "author": "Pedro Domingos",
#             "quote": "People worry that computers will " +
#                      "get too smart and take over the world, " +
#                      "but the real problem is that they're too stupid " +
#                      "and they've already taken over the world."
#         },
#         {
#             "id": 6,
#             "author": "Alan Turing",
#             "quote": "It seems probable that once the machine thinking " +
#                      "method had started, it would not take long " +
#                      "to outstrip our feeble powers… " +
#                      "They would be able to converse " +
#                      "with each other to sharpen their wits. " +
#                      "At some stage therefore, we should " +
#                      "have to expect the machines to take control."
#         },
#         {
#             "id": 7,
#             "author": "Ray Kurzweil",
#             "quote": "Artificial intelligence will reach " +
#                      "human levels by around 2029. " +
#                      "Follow that out further to, say, 2045, " +
#                      "we will have multiplied the intelligence, " +
#                      "the human biological machine intelligence " +
#                      "of our civilization a billion-fold."
#         },
#         {
#             "id": 8,
#             "author": "Sebastian Thrun",
#             "quote": "Nobody phrases it this way, but I think " +
#                      "that artificial intelligence " +
#                      "is almost a humanities discipline. It's really an attempt " +
#                      "to understand human intelligence and human cognition."
#         },
#         {
#             "id": 9,
#             "author": "Andrew Ng",
#             "quote": "We're making this analogy that AI is the new electricity." +
#                      "Electricity transformed industries: agriculture, " +
#                      "transportation, communication, manufacturing."
#         }
#     ]
#
#
#     def get(id=0):
#         if id == 0:
#             return random.choice(ai_quotes), 200
#
#         for quote in ai_quotes:
#             if (quote["id"] == id):
#                 return quote, 200
#         return "Quote not found", 404
#
#     def post(id):
#         parser = reqparse.RequestParser()
#         parser.add_argument("author")
#         parser.add_argument("quote")
#         params = parser.parse_args()
#
#         for quote in ai_quotes:
#             if (id == quote["id"]):
#                 return f"Quote with id {id} already exists", 400
#
#         quote = {
#             "id": int(id),
#             "author": params["author"],
#             "quote": params["quote"]
#         }
#
#         ai_quotes.append(quote)
#         return quote, 201
#
#     def put(self, id):
#         parser = reqparse.RequestParser()
#         parser.add_argument("author")
#         parser.add_argument("quote")
#         params = parser.parse_args()
#
#         for quote in ai_quotes:
#             if (id == quote["id"]):
#                 quote["author"] = params["author"]
#                 quote["quote"] = params["quote"]
#                 return quote, 200
#
#         quote = {
#             "id": id,
#             "author": params["author"],
#             "quote": params["quote"]
#         }
#
#         ai_quotes.append(quote)
#         return quote, 201
#
#     def delete(self, id):
#         global ai_quotes
#         ai_quotes = [qoute for qoute in ai_quotes if qoute["id"] != id]
#         return f"Quote with id {id} is deleted.", 200
#
#     if request.method == 'GET':
#         return get(id)
#
#     if request.method == 'POST':
#         print("here")
#         return post(id)
#
#     # api = Api(app)
#     # print("api", api)
#     # api.add_resource(Quote, "/ai-quotes", "/ai-quotes/", "/ai-quotes/<int:id>")
#     # return api
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

""" ______________________________________________"""

# import os, uuid
# from flask import Flask, request, render_template
# from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
# from werkzeug.utils import secure_filename
#
# app = Flask(__name__)
#
# # Retrieve the connection string for use with the application. The storage
# # connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
# connect_str = 'DefaultEndpointsProtocol=https;AccountName=fhirtestingstore;AccountKey=E/bxDh1TGeGnkNT7Y2OVEzE2zmZgpkQ5t9F0suURT7f3FF0kBW4Yu+afr/q28gz9THNbm3zSwfoTeZUXW99vuQ==;EndpointSuffix=core.windows.net'
# # print(connect_str)
#
# local_path = "./uploads"
#
# @app.route('/', methods=['GET', 'POST'])
# def upload_files():
#     if request.method == 'POST':
#         file = request.files['file']
#         filename = secure_filename(file.filename)
#         file_extension = filename.rsplit('.',1)[1]
#         print(file_extension)
#         file.save(os.path.join(local_path, filename))
#
#         local_file_name = filename
#         upload_file_path = os.path.join(local_path, local_file_name)
#         try:
#             print("Azure Blob storage v12")
#             # Create the BlobServiceClient object which will be used to create a container client
#             blob_service_client = BlobServiceClient.from_connection_string(connect_str)
#
#             # Create a unique name for the container
#             container_name = "container" + str(uuid.uuid4())+file_extension
#
#             # Create the container
#             container_client = blob_service_client.create_container(container_name)
#
#             # Create a blob client using the local file name as the name for the blob
#             blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
#
#             print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)
#
#             # Upload the created file
#             with open(upload_file_path, "rb") as data:
#                 blob_client.upload_blob(data)
#
#         except Exception as ex:
#             print('Exception:')
#             print(ex)
#     return render_template('index.html')
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#

import os, uuid
from flask import Flask, request, render_template
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Retrieve the connection string for use with the application. The storage
# connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
connect_str = 'DefaultEndpointsProtocol=https;AccountName=fhirtestingstore;AccountKey=E/bxDh1TGeGnkNT7Y2OVEzE2zmZgpkQ5t9F0suURT7f3FF0kBW4Yu+afr/q28gz9THNbm3zSwfoTeZUXW99vuQ==;EndpointSuffix=core.windows.net'
# print(connect_str)

local_path = "./uploads"

@app.route('/')

def landingPage():
    return "Hi"
@app.route('/upload')
def upload_file():
    return render_template('index.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file_extension = filename.rsplit('.', 1)[1]
        print(file_extension)
        file.save(os.path.join(local_path, filename))

        local_file_name = filename
        upload_file_path = os.path.join(local_path, local_file_name)
        try:
            print("Azure Blob storage v12")
            # Create the BlobServiceClient object which will be used to create a container client
            blob_service_client = BlobServiceClient.from_connection_string(connect_str)

            # Create a unique name for the container
            container_name = "container" + str(uuid.uuid4()) + file_extension

            # Create the container
            container_client = blob_service_client.create_container(container_name)

            # Create a blob client using the local file name as the name for the blob
            blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

            print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

            # Upload the created file
            with open(upload_file_path, "rb") as data:
                blob_client.upload_blob(data)

        except Exception as ex:
            print('Exception:')
            print(ex)
    return 'file uploaded successfully'


if __name__ == '__main__':
    app.run(debug=True)