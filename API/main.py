from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
import beautifulSoup
import functional
from warnings import filterwarnings
filterwarnings("ignore")

app = Flask(__name__)
CORS(app)
api = Api(app)

class Pipe(Resource):

    def get(self):
        print(jsdata)


    def post(self):
        print("Welcome to our API!")
        jsdata = request.data
        data = beautifulSoup.get_data(jsdata)
        
        # for debugging
        # print(abc)
        # print(abc['inning'])
        if data["inning"]==1:
            prediction = functional.model1(data)
        else:
            prediction = functional.model2(data)
            
        # for debugging
        # print(prediction)
        return {
                "Team1":data['team1'],
                "Team2":data['team2'],
                "team1_probability": prediction[0][0],
               "team2_probability":prediction[0][1]}
    
api.add_resource(Pipe,"/")

if __name__ == "__main__":
    app.run(debug=True)