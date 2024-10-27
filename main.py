from flask import request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, Float
from config import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/ckart/OneDrive - SSN Trust/Desktop/Flask_Python_Project/backend/instance/sqlite (5).db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class MostWicketsAllSeasons(db.Model):
    __tablename__ = 'MostWicketsAllSeasonsCombine'  

    c2 = Column(String(100), primary_key=True, nullable=False)
    c3 = Column(Integer, nullable=False)
    c4 = Column(String(100), nullable=False)
    c5 = Column(String(100), nullable=False)
    c6 = Column(String(100), nullable=False)
    c7 = Column(String(100), nullable=False)
    c9 = Column(String(100), nullable=False)
    c10 = Column(String(100), nullable=False)
    c11 = Column(String(100), nullable=False)
    c12 = Column(String(100), nullable=False)
    c13 = Column(String(100), nullable=False)

    def to_dict(self):
        return {
            'Player': self.c2,
            'Matches': self.c3,
            'Inns': self.c4,
            'Overs': self.c5,
            'Runs': self.c6,
            'Wickets': self.c7,
            'Avg': self.c9,
            'Eco': self.c10,
            'SR': self.c11,
            '4W': self.c12,
            '5W' : self.c13        
        }
    
class MostSixesAllSeasonsCombined(db.Model):
    __tablename__ = 'MostSixesInnings'  

    c2 = Column(String(100), primary_key=True, nullable=False)
    c3 = Column(String(100), nullable=False)
    c4 = Column(String(100), nullable=False)
    c5 = Column(String(100), nullable=False)
    c6 = Column(Integer, nullable=False)
    c7 = Column(Integer, nullable=False)
    c8 = Column(Float, nullable=False)
    c9 = Column(Integer, nullable=False)
    c10 = Column(Integer, nullable=False)

    def to_dict(self):
        return {
            'Player': self.c2,
            'Runs': self.c3,
            'BF': self.c4,
            'SR': self.c5,
            '4s': self.c6,
            '6s': self.c7,
            'Against': self.c8,
            'Venue': self.c9,
            'MatchDate': self.c10
        }

class MostRunsConcededPerInningsAllSeasonsCombine(db.Model):
    __tablename__ = 'MostRunsConcededPerInningsAllSeasonsCombine'  

    c2 = Column(String(100), primary_key=True, nullable=False)
    c3 = Column(Integer, nullable=False)
    c4 = Column(String(100), nullable=False)
    c5 = Column(String(100), nullable=False)
    c6 = Column(String(100), nullable=False)
    c7 = Column(String(100), nullable=False)
    c8 = Column(String(100), nullable=False)
    c9 = Column(String(100), nullable=False)

    def to_dict(self):
        return {
            'Player': self.c2,
            'Overs': self.c3,
            'Runs': self.c4,
            'Wickets': self.c5,
            'SR': self.c6,
            'Against': self.c7,
            'Venue' : self.c8,
            'Match Date': self.c9    
        }
    

class MostRunsPerOverAllSeasonsCombine(db.Model):
    __tablename__ = 'MostRunsPerOverAllSeasonsCombine'  

    c2 = Column(String(100), primary_key=True, nullable=False)
    c3 = Column(String(100), nullable=False)
    c4 = Column(String(100), nullable=False)
    c5 = Column(String(100), nullable=False)
    c6 = Column(String(100), nullable=False)
    c7 = Column(String(100), nullable=False)
    c8 = Column(String(100), nullable=False)
    c9 = Column(String(100), nullable=False)
    c10 = Column(String(100), nullable=False)

    def to_dict(self):
        return {
            'Player': self.c2,
            'Runs': self.c3,
            'BF': self.c4,
            'SR': self.c5,
            '4s': self.c6,
            '6s': self.c7,
            'Against': self.c8,
            'Venue': self.c9,
            'Match Date': self.c10 
        }

class MostRunsAllSeasonsCombine(db.Model):
    __tablename__ = 'MostRunsAllSeasonsCombine'  

    c2 = Column(String(100), primary_key=True, nullable=False)
    c3 = Column(String(100), nullable=False)
    c4 = Column(String(100), nullable=False)
    c5 = Column(String(100), nullable=False)
    c6 = Column(String(100), nullable=False)
    c7 = Column(String(100), nullable=False)
    c8 = Column(String(100), nullable=False)
    c9 = Column(String(100), nullable=False)
    c10 = Column(String(100), nullable=False)
    c11 = Column(String(100), nullable=False)
    c12 = Column(String(100), nullable=False)
    c13 = Column(String(100), nullable=False)
    c14 = Column(String(100), nullable=False)

    def to_dict(self):
        return {
            'Player': self.c2,
            'Matches': self.c3,
            'Inns': self.c4,
            'NO': self.c5,
            'Runs': self.c6,
            'HS': self.c7,
            'Avg' : self.c8,
            'BF' : self.c9,
            'SR' : self.c10,
            '100' : self.c11,
            '50' : self.c12,
            '4s' : self.c13,
            '6s' : self.c14
        }
    
class MostFoursPerInningsAllSeasonsCombine(db.Model):
    __tablename__ = 'MostFoursPerInningsAllSeasonsCombine'  

    c2 = Column(String(100), primary_key=True, nullable=False)
    c3 = Column(String(100), nullable=False)
    c4 = Column(String(100), nullable=False)
    c5 = Column(String(100), nullable=False)
    c6 = Column(Integer, nullable=False)
    c7 = Column(Integer, nullable=False)
    c8 = Column(Float, nullable=False)
    c9 = Column(Integer, nullable=False)
    c10 = Column(Integer, nullable=False)

    def to_dict(self):
        return {
            'Player': self.c2,
            'Runs': self.c3,
            'BF': self.c4,
            'SR': self.c5,
            '4s': self.c6,
            '6s': self.c7,
            'Against': self.c8,
            'Venue': self.c9,
            'MatchDate': self.c10
        }


class FastestCenturiesAllSeasonsCombine(db.Model):
    __tablename__ = 'FastestCenturiesAllSeasonsCombine'  

    c2 = Column(String(100), primary_key=True, nullable=False)
    c3 = Column(String(100), nullable=False)
    c4 = Column(String(100), nullable=False)
    c5 = Column(Integer, nullable=False)
    c6 = Column(Integer, nullable=False)
    c7 = Column(Float, nullable=False)
    c8 = Column(Integer, nullable=False)
    c9 = Column(Integer, nullable=False)

    def to_dict(self):
        return {
            'Player': self.c2,
            'Runs': self.c3,
            'BF': self.c4,
            '4s': self.c5,
            '6s': self.c6,
            'Against': self.c7,
            'Venue': self.c8,
            'MatchDate': self.c9
        }

class FastestFiftiesAllSeasonsCombine(db.Model):
    __tablename__ = 'FastestFiftiesAllSeasonsCombine'  

    c2 = Column(String(100), primary_key=True, nullable=False)
    c3 = Column(String(100), nullable=False)
    c4 = Column(String(100), nullable=False)
    c5 = Column(Integer, nullable=False)
    c6 = Column(Integer, nullable=False)
    c7 = Column(Float, nullable=False)
    c8 = Column(Integer, nullable=False)
    c9 = Column(Integer, nullable=False)

    def to_dict(self):
        return {
            'Player': self.c2,
            'Runs': self.c3,
            'BF': self.c4,
            '4s': self.c5,
            '6s': self.c6,
            'Against': self.c7,
            'Venue': self.c8,
            'MatchDate': self.c9
        }

class MostDotBallsPerInnings(db.Model):
    __tablename__ = 'MostDotBallsPerInningsAllSeasonsCombine'

    c2 = Column(String(100), primary_key=True, nullable=False)
    c3 = Column(Integer, nullable=False)
    c4 = Column(String(100), nullable=False)
    c5 = Column(String(100), nullable=False)
    c6 = Column(String(100), nullable=False)
    c7 = Column(String(100), nullable=False)
    c8 = Column(String(100), nullable=False)
    c9 = Column(String(100), nullable=False)
    c10 = Column(String(100), nullable=False)
    c11 = Column(String(100), nullable=False)

    def to_dict(self):
        return {
            'Player': self.c2,
            'Overs': self.c3,
            'Runs': self.c4,
            'Wickets': self.c5,
            'Maid': self.c6,
            'Dots' : self.c7 , 
            'SR' : self.c8 , 
            'Against': self.c9,
            'Venue' : self.c10,
            'Match Date': self.c11    
        }

class BestBowlingStrikeRatePerInningsAllSeasonsCombine(db.Model):
    __tablename__ = 'BestBowlingStrikeRatePerInningsAllSeasonsCombine'  

    c2 = Column(String(100), primary_key=True, nullable=False)
    c3 = Column(Integer, nullable=False)
    c4 = Column(String(100), nullable=False)
    c5 = Column(String(100), nullable=False)
    c6 = Column(String(100), nullable=False)
    c7 = Column(String(100), nullable=False)
    c8 = Column(String(100), nullable=False)

    def to_dict(self):
        return {
            'Player': self.c2,
            'Overs': self.c3,
            'Runs': self.c4,
            'Wickets': self.c5,
            'SR': self.c6,
            'Against': self.c7,
            'Venue' : self.c8  
        }

class BestBowlingEconomyPerInningsAllSeasonsCombine(db.Model):
    __tablename__ = 'BestBowlingEconomyPerInningsAllSeasonsCombine'  

    c2 = Column(String(100), primary_key=True, nullable=False)
    c3 = Column(String(100), nullable=False)
    c4 = Column(String(100), nullable=False)
    c5 = Column(String(100), nullable=False)
    c6 = Column(String(100), nullable=False)
    c7 = Column(String(100), nullable=False)
    c8 = Column(String(100), nullable=False)
    c9 = Column(String(100), nullable=False)
    c10 = Column(String(100), nullable=False)
    c11 = Column(String(100), nullable=False)

    def to_dict(self):
        return {
            'Player': self.c2,
            'Overs': self.c3,
            'Runs': self.c4,
            'Wickets': self.c5,
            'Dots': self.c6,
            'Economy': self.c7,
            'SR': self.c8,
            'Against': self.c9,
            'Venue': self.c10,
            'Match Date': self.c11,     
        }




@app.route("/show_most_sixes", methods=["GET"])
def get_most_sixes_data():
    most_sixes_data = MostSixesAllSeasonsCombined.query.all()
    json_data = list(map(lambda x: x.to_dict(), most_sixes_data))
    return jsonify({"most_sixes": json_data})

@app.route("/show_most_wickets", methods=["GET"])
def get_most_wickets_data():
    most_wickets_data = MostWicketsAllSeasons.query.all()
    json_data = list(map(lambda x: x.to_dict(), most_wickets_data))
    return jsonify({"most_wickets": json_data})

@app.route("/show_most_runs_conceded", methods=["GET"])
def get_most_runs_conceded_data():
    most_runs_data = MostRunsConcededPerInningsAllSeasonsCombine.query.all()
    json_data = list(map(lambda x: x.to_dict(), most_runs_data))
    return jsonify({"most_runs_conceded": json_data})

@app.route("/show_most_runs_per_over", methods=["GET"])
def get_most_runs_per_over_data():
    most_runs_per_over_data =  MostRunsPerOverAllSeasonsCombine.query.all()
    json_data = list(map(lambda x: x.to_dict(), most_runs_per_over_data))
    return jsonify({"most_runs_conceded": json_data})

@app.route("/show_most_runs", methods=["GET"])
def get_most_runs_data():
    most_runs_data =  MostRunsAllSeasonsCombine.query.all()
    json_data = list(map(lambda x: x.to_dict(), most_runs_data))
    return jsonify({"most_runs": json_data})

@app.route("/show_most_fours_per_innings", methods=["GET"])
def get_most_fours_per_innings_data():
    most_fours_per_innings_data =  MostFoursPerInningsAllSeasonsCombine.query.all()
    json_data = list(map(lambda x: x.to_dict(), most_fours_per_innings_data))
    return jsonify({"most_runs": json_data})

@app.route("/show_fastest_centuries", methods=["GET"])
def get_Fastest_Centuries_data():
    Fastest_Centuries_data = FastestCenturiesAllSeasonsCombine.query.all()
    json_data = list(map(lambda x: x.to_dict(), Fastest_Centuries_data))
    return jsonify({"Fastest_Centuries": json_data})

@app.route("/show_most_dot_balls", methods=["GET"])
def get_most_dot_balls():
    most_dot_balls = MostDotBallsPerInnings.query.all()
    json_data = list(map(lambda x: x.to_dict(), most_dot_balls))
    return jsonify({"Most_Dot_Balls": json_data})

@app.route("/show_best_bowling_strike_rate", methods=["GET"])
def get_best_bowling_strike_rate():
    best_bowling_strike_rate = BestBowlingStrikeRatePerInningsAllSeasonsCombine.query.all()
    json_data = list(map(lambda x: x.to_dict(), best_bowling_strike_rate))
    return jsonify({"Best Bowling Strike Rate": json_data})

@app.route("/show_best_bowling_economy", methods=["GET"])
def get_best_bowling_economy():
    best_bowling_economy = BestBowlingEconomyPerInningsAllSeasonsCombine.query.all()
    json_data = list(map(lambda x: x.to_dict(), best_bowling_economy))
    return jsonify({"Best Bowling Economy": json_data})

if __name__ == '__main__':
    app.run(debug=True)


    